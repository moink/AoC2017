import asyncio
import advent_tools

class DuetComputer(advent_tools.Computer):

    operation = advent_tools.Computer.operation
    return_register = 'a'

    def __init__(self, send_to: asyncio.Queue, receive_from: asyncio.Queue):
        super().__init__()
        self.send_to = send_to
        self.receive_from = receive_from
        self.send_count = 0

    @operation('set')
    async def set_register(self, reg_num, key_or_val):
        val = self.get_key_or_val(key_or_val)
        self.registers[reg_num] = val

    def get_key_or_val(self, key_or_val):
        try:
            val = int(key_or_val)
        except ValueError:
            val = self.registers[key_or_val]
        return val

    @operation('add')
    async def add_to_register(self, reg_num, key_or_val):
        val = self.get_key_or_val(key_or_val)
        self.registers[reg_num] = self.registers[reg_num] + val

    @operation('mul')
    async def multiply_register(self, reg_num, key_or_val):
        val = self.get_key_or_val(key_or_val)
        self.registers[reg_num] = self.registers[reg_num] * val

    @operation('mod')
    async def mod_register(self, key_or_val1, key_or_val2):
        val1 = self.get_key_or_val(key_or_val1)
        val2 = self.get_key_or_val(key_or_val2)
        self.registers[key_or_val1] = val1 % val2

    @operation('jgz')
    async def jump(self, key_or_val1, key_or_val2):
        val = self.get_key_or_val(key_or_val1)
        offset = self.get_key_or_val(key_or_val2)
        if val>0:
            self.instruction_pointer = self.instruction_pointer + offset - 1

    @operation('snd')
    async def send(self, key_or_val):
        sound = self.get_key_or_val(key_or_val)
        self.send_count = self.send_count + 1
        if self.send_count > 10000:
            raise RuntimeError
        await self.send_to.put(sound)

    @operation('rcv')
    async def receive(self, reg):
        self.registers[reg] = await self.receive_from.get()
        self.receive_from.task_done()

    async def run_instruction(self, instruction):
        words = instruction.split()
        func = self.operation_map[words[0]]
        await func(self, *words[1:])

    async def run_program(self, program):
        while True:
            try:
                line = program[self.instruction_pointer]
            except IndexError:
                return self.registers[self.return_register]
            await self.run_instruction(line)
            self.instruction_pointer = self.instruction_pointer + 1

async def block_detect(queue1: asyncio.Queue, queue2: asyncio.Queue):
    while not (queue1.empty() and queue2.empty()):
        await asyncio.sleep(1)

def main():
    one_to_two = asyncio.Queue()
    two_to_one = asyncio.Queue()
    computer_one = DuetComputer(two_to_one, one_to_two)
    computer_two = DuetComputer(one_to_two, two_to_one)
    computer_one.registers['p'] = 0
    computer_two.registers['p'] = 1
    instructions = advent_tools.read_input_lines()
    loop = asyncio.get_event_loop()
    run_one = loop.create_task(computer_one.run_program(instructions))
    run_two = loop.create_task(computer_two.run_program(instructions))
    blocker = loop.create_task(block_detect(one_to_two, two_to_one))
    loop.run_until_complete(blocker)
    print(computer_two.send_count)
    run_one.cancel()
    run_two.cancel()

if __name__ == '__main__':
    main()

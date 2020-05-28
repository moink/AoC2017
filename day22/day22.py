import collections
import time

import matplotlib.pyplot as plt

import advent_tools

BOT = 2
CLEAN = 0
INFECTED = 1
FLAGGED = 2
WEAKENED = 3
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

class ComputeCluster(advent_tools.PlottingGrid):

    def __init__(self):
        super().__init__((25, 25))
        self.grid = collections.defaultdict(int)
        char_map = {'.': 0, '#': 1}
        self.read_input_file(char_map)
        # self.grid[12, 12] = BOT
        self.xpos = 12
        self.ypos = 12
        self.direction = UP

    def show(self):
        plot_grid = self.grid.copy()
        plot_grid[self.ypos, self.xpos] = BOT
        plt.clf()
        plt.imshow(plot_grid)
        plt.colorbar()
        plt.show()

    def take_part_one_step(self):
        if self.grid[self.ypos, self.xpos] == INFECTED:
            self.direction = (self.direction + 1) % 4
            self.grid[self.ypos, self.xpos] = CLEAN
            result = False
        else:
            self.direction = (self.direction - 1) % 4
            self.grid[self.ypos, self.xpos] = INFECTED
            result = True
        self.step_in_direction()
        return result

    def step_in_direction(self):
        if self.direction == UP:
            self.ypos = self.ypos - 1
        elif self.direction == DOWN:
            self.ypos = self.ypos + 1
        elif self.direction == RIGHT:
            self.xpos = self.xpos + 1
        else:
            self.xpos = self.xpos - 1

    def take_part_two_step(self):
        status = self.grid[self.ypos, self.xpos]
        result = False
        if status == INFECTED:
            self.direction = (self.direction + 1) % 4
            self.grid[self.ypos, self.xpos] = FLAGGED
        elif status == CLEAN:
            self.direction = (self.direction - 1) % 4
            self.grid[self.ypos, self.xpos] = WEAKENED
        elif status == WEAKENED:
            self.grid[self.ypos, self.xpos] = INFECTED
            result = True
        else:  # FLAGGED
            self.direction = (self.direction + 2) % 4
            self.grid[self.ypos, self.xpos] = CLEAN
        self.step_in_direction()
        return result


def run_part_1():
    grid = ComputeCluster()
    # grid.show()
    infected_steps = 0
    for _ in range(10000):
        infected_steps += grid.take_part_one_step()
        # print(grid.xpos, grid.ypos)
        # grid.draw()
    # grid.show()
    return(infected_steps)

def run_part_2():
    grid = ComputeCluster()
    infected_steps = 0
    start = time.perf_counter()
    num_steps = 10000000
    ratio = 10000000 / num_steps
    for _ in range(num_steps):
        infected_steps += grid.take_part_two_step()
    elapsed = time.perf_counter() - start
    print(elapsed)
    print(ratio * elapsed)
    return (infected_steps)


if __name__ == '__main__':
    # print(run_part_1())
    print(run_part_2()) # 2487 is too low
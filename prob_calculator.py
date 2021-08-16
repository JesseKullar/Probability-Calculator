import copy
import random


# Consider using the modules imported above.

class Hat:

    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for i in range(int(value)):
                self.contents.append(key)

    def draw(self, num_balls_drawn):
        drawn_balls = []
        if num_balls_drawn > len(self.contents):
            drawn_balls = self.contents
            return drawn_balls
        else:
            for j in range(num_balls_drawn):
                ball = random.choice(self.contents)
                drawn_balls.append(ball)
                self.contents.remove(ball)
            return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = int()
    for i in range(num_experiments):
        name = copy.deepcopy(hat)
        drawn_balls = name.draw(num_balls_drawn)
        expect = []
        for key, value in expected_balls.items():
            for j in range(value):
                expect.append(key)
        temp = copy.deepcopy(expect)
        for k in range(len(temp)):
            if temp[k] in drawn_balls:
                expect.remove(temp[k])
                drawn_balls.remove(temp[k])
        if not expect:
            M += 1
    return M/num_experiments

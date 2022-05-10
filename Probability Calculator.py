import copy
import random


class Hat:
    def __init__(self, **balls):
        self.contents = [k for k, v in balls.items() for _ in range(v)]

    def draw(self, num):
        num = min(num, len(self.contents))
        return [self.contents.pop(random.randrange(len(self.contents))) for _ in range(num)]


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    res = 0
    for _ in range(num_experiments):
        new_hat = copy.deepcopy(hat)
        balls_drawn = new_hat.draw(num_balls_drawn)
        balls_req = sum([1 for k, v in expected_balls.items() if balls_drawn.count(k) >= v])
        res += 1 if balls_req == len(expected_balls) else 0

    return res / num_experiments

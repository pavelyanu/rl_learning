# k-armed testbed
import scipy
import matplotlib
import argparse
from scipy.stats import norm

parser = argparse.ArgumentParser()
parser.add_argument('--arms', default=10, type=int)
parser.add_argument('--problems', default=2000, type=int)
parser.add_argument('--nonstationary', default=False, type=bool)
parser.add_argument('--start_equal', default=False, type=bool)
parser.add_argument('--problem_mean', default=0, type=float)
parser.add_argument('--problem_var', default=1, type=float)
parser.add_argument('--reward_var', default=1, type=float)
parser.add_argument('--nonstationary_mean', default=0, type=float)
parser.add_argument('--nonstationary_var', default=1, type=float)

class Testbed:
    def __init__(self, args: argparse.Namespace):
        self.problems = []
        self.arms = args.arms
        self.n_problems = args.problems
        self.nonstationary = args.nonstationary
        self.start_equal = args.start_equal
        self.problem_mean = args.problem_mean
        self.problem_var = args.problem_var
        self.reward_var = args.reward_var
        self.nonstationary_mean = args.nonstationary_mean
        self.nonstationary_var = args.nonstationary_var
        for _ in range(self.n_problems):
            self.problems.append(Bandit(
                self.arms,
                self.nonstationary,
                self.start_equal,
                self.problem_mean,
                self.problem_var,
                self.reward_var,
                self.nonstationary_mean,
                self.nonstationary_var,
                ))

class Bandit:
    def __init__(
            self,
            arms=10,
            nonstationary=False,
            start_equal=False,
            problem_mean=0,
            problem_var=1,
            reward_var=1,
            nonstationary_mean=0,
            nonstationary_var=0.01
            ):
        self.nonstationary = nonstationary
        self.revard_var = reward_var
        self.nonstationary_mean = nonstationary_mean
        self.nonstationary_var = nonstationary_var
        if start_equal:
            self.actions = [norm.rvs(loc=problem_mean, scale=problem_var)] * arms
        else:
            self.actions = [norm.rvs(loc=problem_mean, scale=problem_var) for _ in range(arms)]

    def apply(self, action):
        reward = norm.rvs(loc=self.actions[action - 1], scale=self.reward_var)
        if self.nonstationary:
            self.actions = [norm.rvs(loc=self.nonstationary_mean, scale=self.nonstationary_var) + x for x in self.actions]
        return reward


def main(args: argparse.Namespace):
    Testbed(args)


if __name__ == "__main__":
    args = parser.parse_args([] if "__file__" not in globals() else None)
    main:(args)

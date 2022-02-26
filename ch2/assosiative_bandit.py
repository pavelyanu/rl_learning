import random
import sys
import signal

def signal_handler(signal, frame):
    print(f'\nyour total is {total}')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

class Bandit:
    def __init__(self, left_reward, right_reward):
        self.left = left_reward
        self.right = right_reward

    def play(self, arm):
        if arm == 1 or arm == 'left' or arm == False:
            return self.left
        else:
            return self.right


bandit_a = Bandit(0.1, 0.2)
bandit_b = Bandit(0.9, 0.8)
bandit = None
total = 0

args = sys.argv
show = False
if len(args) > 1:
    if args[1] == 'show':
        show = True

while True:
    if random.randint(1, 2) == 1:
        bandit = bandit_a
        if show:
            print('you are playing A')
    else:
        bandit = bandit_b
        if show:
            print('you are playing B')
    arm = input('choose arm: ')
    try:
        arm = int(arm)
    except:
        try:
            arm = bool(arm)
        except:
            arm = arm
    reward = bandit.play(arm)
    total += reward
    print(f'your reward is {reward}')

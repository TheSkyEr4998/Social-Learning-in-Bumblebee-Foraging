import numpy as np
import random

GRID_ROWS = 3
GRID_COLS = 4


class Flower:
    def __init__(self, has_cue=False, cue_type=None, reward_prob=0.0):
        self.has_cue = has_cue
        self.cue_type = cue_type  # "social" or "non-social"
        self.reward_prob = reward_prob

    def get_reward(self):
        return random.random() < self.reward_prob


class Environment:
    def __init__(self, variance, cue_type):
        self.variance = variance
        self.cue_type = cue_type
        self.flowers = self.create_environment()

    def create_environment(self):
        flowers = []

        # ===== PAPER LOGIC =====
        # 12 flowers → 4 with cues
        for i in range(12):
            has_cue = i < 4

            if self.variance == "low":
                # No-variance → equal reward everywhere
                reward_prob = 0.5

            else:
                # High-variance → only 2 flowers rewarding
                reward_prob = 0.9 if i < 2 else 0.1

            cue = self.cue_type if has_cue else None

            flowers.append(Flower(has_cue, cue, reward_prob))

        return flowers

    def get_all_flowers(self):
        return self.flowers
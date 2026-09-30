from models import Agent
from environment import Environment
import numpy as np


class Simulation:
    def __init__(self, num_agents, variance, cue_type):
        self.env = Environment(variance, cue_type)
        self.agents = [Agent() for _ in range(num_agents)]
        self.flowers = self.env.get_all_flowers()

        self.history = []
        self.first_choices = []

    def run_step(self):
        cue_count = 0

        for agent in self.agents:
            flower, chose_cue = agent.choose(self.flowers)
            reward = flower.get_reward()

            agent.update(reward, chose_cue)

            # IMPORTANT:
            # Track landing on ANY cue flower, not just social-cue choices.
            if flower.has_cue:
                cue_count += 1

        self.history.append(cue_count / len(self.agents))

    def run(self, steps=50):
        for _ in range(steps):
            self.run_step()

        return self.history[-1]

    def run_first_choice_test(self):
        # PAPER: first landing on cue vs no-cue flower
        choices = []

        for agent in self.agents:
            flower, chose_cue = agent.choose(self.flowers)
            choices.append(1 if flower.has_cue else 0)

        return np.mean(choices)
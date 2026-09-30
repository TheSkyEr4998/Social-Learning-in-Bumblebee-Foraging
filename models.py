import random
import numpy as np


class Agent:
    def __init__(self):
        # Start close to the paper's random baseline (4 cue flowers out of 12 = 0.33)
        # This preference is only allowed to adapt for SOCIAL cue environments.
        self.social_preference = np.random.uniform(-0.03, 0.03)

        self.last_choice = None
        self.last_chose_cue = False

    def _get_social_cue_probability(self):
        # Baseline chance level = 0.33
        # Social preference pushes it up/down slightly.
        return float(np.clip(0.33 + self.social_preference, 0.10, 0.80))

    def choose(self, flowers):
        social_flowers = [f for f in flowers if f.cue_type == "social"]
        non_social_flowers = [f for f in flowers if f.cue_type == "non-social"]
        no_cue_flowers = [f for f in flowers if not f.has_cue]

        # If this run is SOCIAL-cue based, let behavior adapt around baseline.
        if social_flowers:
            p_choose_cue = self._get_social_cue_probability()
            chose_cue = random.random() < p_choose_cue

            if chose_cue:
                flower = random.choice(social_flowers)
                self.last_choice = flower
                self.last_chose_cue = True
                return flower, True
            else:
                flower = random.choice(no_cue_flowers)
                self.last_choice = flower
                self.last_chose_cue = False
                return flower, False

        # If this run is NON-SOCIAL-cue based, keep cue choice near baseline chance.
        if non_social_flowers:
            p_choose_cue = 0.33
            chose_cue = random.random() < p_choose_cue

            if chose_cue:
                flower = random.choice(non_social_flowers)
                self.last_choice = flower
                self.last_chose_cue = True
                return flower, True
            else:
                flower = random.choice(no_cue_flowers)
                self.last_choice = flower
                self.last_chose_cue = False
                return flower, False

        # Fallback
        flower = random.choice(no_cue_flowers)
        self.last_choice = flower
        self.last_chose_cue = False
        return flower, False

    def update(self, reward, chose_cue):
        # Only SOCIAL cue environments should learn strongly from reward history.
        # NON-SOCIAL cue environments should stay near baseline chance.
        if self.last_choice is None:
            return

        if self.last_choice.cue_type == "social":
            if chose_cue:
                if reward:
                    self.social_preference += 0.019
                else:
                    self.social_preference -= 0.010
            else:
                # Small correction only, to avoid pushing low-variance too far down.
                if reward:
                    self.social_preference -= 0.003

            self.social_preference = float(np.clip(self.social_preference, -0.20, 0.45))
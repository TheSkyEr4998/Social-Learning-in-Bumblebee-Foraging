import numpy as np
import matplotlib.pyplot as plt
from simulation_engine import Simulation

NUM_RUNS = 30


def run_condition(variance, cue_type):
    results = []

    for _ in range(NUM_RUNS):
        sim = Simulation(100, variance, cue_type)
        value = sim.run_first_choice_test()
        results.append(value)

    return np.array(results)


def run_all():
    return {
        "high_social": run_condition("high", "social"),
        "low_social": run_condition("low", "social"),
        "high_non": run_condition("high", "non-social"),
        "low_non": run_condition("low", "non-social"),
    }


def plot(results):
    labels = ["Social Cue", "Non-Social Cue"]

    high = [
        np.mean(results["high_social"]),
        np.mean(results["high_non"])
    ]

    low = [
        np.mean(results["low_social"]),
        np.mean(results["low_non"])
    ]

    x = np.arange(len(labels))

    plt.bar(x - 0.2, high, 0.4, label="High Variance")
    plt.bar(x + 0.2, low, 0.4, label="Low Variance")

    plt.axhline(0.33, linestyle="--")  # paper baseline
    plt.xticks(x, labels)
    plt.ylabel("Proportion Choosing Cue")
    plt.legend()

    plt.show()


if __name__ == "__main__":
    res = run_all()
    plot(res)
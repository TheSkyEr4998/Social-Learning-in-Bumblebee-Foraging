# Social Learning in Bumblebee Foraging

A Python simulation prototype exploring flower choices in environments with social and non-social cues. It includes an interactive desktop interface and a separate script for plotting first-choice proportions.

Inspired by:

> Smolla, M., Alem, S., Chittka, L., & Shultz, S. (2016). Copy-when-uncertain: bumblebees rely on social information when rewards are highly variable. *Biology Letters, 12*, 20160188.  
> https://doi.org/10.1098/rsbl.2016.0188

**Project status:** Educational prototype. This implementation is not a validated reproduction of the paper’s computational model or experimental results.

## Features

- A simulated environment containing 12 flowers, four with cues.
- Social and non-social cue conditions.
- Two reward-probability configurations labelled high and low variance.
- Agents with a simple reward-dependent social-cue preference.
- An interactive interface for selecting agent count, condition, and update interval.
- Live visualization of flower choices and the proportion of agents choosing cued flowers.
- A separate analysis script comparing initial choices across four conditions.

## Technologies

- Python
- PySide6 — desktop interface
- NumPy — numerical operations
- Matplotlib — visualization

## Project Structure

| File | Purpose |
|---|---|
| `main.py` | Starts the desktop application |
| `ui.py` | Defines the controls and visualizations |
| `controller.py` | Connects the interface to the simulation |
| `models.py` | Defines agent choices and preference updates |
| `environment.py` | Creates flowers, cues, and reward probabilities |
| `simulation_engine.py` | Runs simulation steps and first-choice tests |
| `analysis.py` | Runs repeated first-choice tests and plots averages |
| `.gitignore` | Excludes environments and generated Python files |

## Installation

Clone the repository:

```bash
git clone https://github.com/TheSkyEr4998/Social-Learning-in-Bumblebee-Foraging.git
cd Social-Learning-in-Bumblebee-Foraging
```

Create a virtual environment:

```bash
python -m venv .venv
```

On Windows PowerShell, install dependencies:

```powershell
.\.venv\Scripts\python.exe -m pip install PySide6 numpy matplotlib
```

On macOS or Linux:

```bash
.venv/bin/python -m pip install PySide6 numpy matplotlib
```

## Run the Application

On Windows:

```powershell
.\.venv\Scripts\python.exe main.py
```

On macOS or Linux:

```bash
.venv/bin/python main.py
```

In the application:

1. Select the number of agents.
2. Choose the reward condition and cue type.
3. Set the update interval in milliseconds. Smaller values produce faster updates.
4. Click **Start** to begin.
5. Click **Stop** to pause updates.

Clicking **Start** again creates a new simulation.

## Run the Analysis

On Windows:

```powershell
.\.venv\Scripts\python.exe analysis.py
```

On macOS or Linux:

```bash
.venv/bin/python analysis.py
```

The script runs 30 repetitions per condition, with 100 newly initialized agents in each repetition, and plots the average proportion choosing a cued flower.

**Interpretation:** These agents are tested without prior training. Reward conditions therefore do not influence their first choices in this script. Differences between conditions reflect random sampling and initialization, rather than a demonstrated learning effect.

## Current Model

The environment contains a 3 × 4 flower array. Four flowers carry the selected cue type.

Reward probabilities are configured as follows:

- **Low:** Every flower has a reward probability of 0.5.
- **High:** Two cued flowers have a reward probability of 0.9; all remaining flowers have a probability of 0.1.

Rewards are independent random events. The model does not represent nectar quantities, depletion, or competition between agents.

Social-cue choices depend on an agent’s adjustable preference. Non-social cue choices use a fixed probability of 0.33. These are implementation assumptions, not learning equations established by the paper.

## Relationship to the Study

The study includes two distinct components:

1. An evolutionary model involving individual and social learners, resource sharing, and replacement according to foraging success.
2. A live-bee experiment involving cue training, separate reward-distribution training, and an unrewarded first-choice test.

This prototype borrows the flower-array layout and cue categories but does not implement either component in full.

## Known Limitations

- The paper’s two training phases and separate unrewarded test are not implemented.
- Non-social cue learning is disabled by design, although the study reports learning about both cue types during initial training.
- The reward configurations change both average reward probability and its distribution.
- The current analysis tests untrained agents.
- A preference-update branch intended for uncued choices is unreachable and requires correction.
- The interface defines a custom `update()` method that should be renamed to avoid overriding Qt’s existing widget method.
- Random seeds, confidence intervals, and statistical comparisons are not implemented.
- No claim is made that the simulation reproduces the paper’s findings.

## Planned Improvements

- Implement separate cue-training, reward-training, and test phases.
- Preserve agent learning across phases.
- Document and test learning assumptions for both cue types.
- Separate reward amount from reward probability.
- Add reproducible random seeds and automated tests.
- Add uncertainty estimates and appropriate statistical analysis.

## Author

Niranjan Ghone  
GitHub: [TheSkyEr4998](https://github.com/TheSkyEr4998)
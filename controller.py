from simulation_engine import Simulation
from PySide6.QtCore import QTimer


class Controller:
    def __init__(self, ui):
        self.ui = ui
        self.sim = None
        self.timer = None

    def start(self):
        agents = self.ui.get_agents()
        variance = self.ui.get_variance()
        cue_type = self.ui.get_cue_type()
        speed_ms = self.ui.get_speed()

        self.stop()

        self.sim = Simulation(agents, variance, cue_type)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(speed_ms)

    def update(self):
        if self.sim is None:
            return

        self.sim.run_step()

        self.ui.update(
            self.sim.agents,
            self.sim.history,
            self.sim.flowers
        )

    def stop(self):
        if self.timer:
            self.timer.stop()
            self.timer = None
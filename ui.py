from PySide6.QtWidgets import *
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np


class SimulationUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Bee Simulation")

        layout = QVBoxLayout()

        self.agent_input = QSpinBox()
        self.agent_input.setMinimum(10)
        self.agent_input.setMaximum(500)
        self.agent_input.setValue(50)

        self.variance_box = QComboBox()
        self.variance_box.addItems(["high", "low"])

        self.cue_box = QComboBox()
        self.cue_box.addItems(["social", "non-social"])

        self.speed_input = QSpinBox()
        self.speed_input.setMinimum(100)
        self.speed_input.setMaximum(3000)
        self.speed_input.setSingleStep(100)
        self.speed_input.setValue(700)

        self.start_btn = QPushButton("Start")
        self.stop_btn = QPushButton("Stop")

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        layout.addWidget(QLabel("Agents"))
        layout.addWidget(self.agent_input)

        layout.addWidget(QLabel("Variance"))
        layout.addWidget(self.variance_box)

        layout.addWidget(QLabel("Cue Type"))
        layout.addWidget(self.cue_box)

        layout.addWidget(QLabel("Simulation Speed (ms)"))
        layout.addWidget(self.speed_input)

        layout.addWidget(self.start_btn)
        layout.addWidget(self.stop_btn)
        layout.addWidget(self.canvas)

        self.setLayout(layout)

    def set_controller(self, controller):
        self.controller = controller
        self.start_btn.clicked.connect(controller.start)
        self.stop_btn.clicked.connect(controller.stop)

    def get_agents(self):
        return self.agent_input.value()

    def get_variance(self):
        return self.variance_box.currentText()

    def get_cue_type(self):
        return self.cue_box.currentText()

    def get_speed(self):
        return self.speed_input.value()

    def update(self, agents, history, flowers):
        self.figure.clear()

        ax1 = self.figure.add_subplot(121)
        ax2 = self.figure.add_subplot(122)

        # Flower grid
        for i, f in enumerate(flowers):
            x = i % 4
            y = i // 4

            if f.cue_type == "social":
                color = "yellow"
            elif f.cue_type == "non-social":
                color = "lightgreen"
            else:
                color = "gray"

            ax1.scatter(x, y, color=color, s=200)

        # Bees on flowers
        for i, a in enumerate(agents):
            if a.last_choice:
                idx = flowers.index(a.last_choice)
                x = idx % 4
                y = idx // 4

                angle = (i % 6) * 0.8
                x += np.cos(angle) * 0.15
                y += np.sin(angle) * 0.15

                ax1.scatter(x, y, color="black", s=20)

        ax1.set_title("Environment")
        ax1.set_xlim(-0.2, 3.2)
        ax1.set_ylim(-0.2, 2.2)

        ax2.plot(history)
        ax2.set_title("Social Behaviour Evolution")
        ax2.set_ylim(0, 1)

        self.canvas.draw()
import sys
from PySide6.QtWidgets import QApplication
from ui import SimulationUI
from controller import Controller

app = QApplication(sys.argv)

ui = SimulationUI()
controller = Controller(ui)

ui.set_controller(controller)

ui.show()

sys.exit(app.exec())
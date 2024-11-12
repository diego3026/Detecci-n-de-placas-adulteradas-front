from PyQt6.QtWidgets import QWidget
from views.cargue_vehiculo_view import Ui_Form

class CargueVehiculoController(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.onClose)

    def onClose(self):
        self.close()

from PyQt6.QtWidgets import QMainWindow
from views.main_view import Ui_MainWindow

class MainController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_connections()

    def setup_connections(self):
        self.ui.my_button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        print("¡Botón presionado!")
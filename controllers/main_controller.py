from PyQt6.QtWidgets import QMainWindow, QSizePolicy
from views.main_view import Ui_MainWindow
from controllers.general_controller import GeneralController 

class MainController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Principal")
        self.showMaximized()
        self.ui.titulo_principal_main.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        self.ui.boton_login.clicked.connect(self.open_general_window)

    def open_general_window(self):
        self.general_window = GeneralController()
        self.close()
        self.general_window.show()

    def resizeEvent(self, event):
        self.ui.titulo_principal_main.setFixedWidth(self.width())
        self.ui.centralwidget.setFixedWidth(self.width())
        self.ui.centralwidget.setFixedHeight(self.height())
        super().resizeEvent(event)

import sys
from PyQt6.QtWidgets import QApplication
from controllers.main_controller import MainController

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_controller = MainController()
    main_controller.show()
    sys.exit(app.exec())
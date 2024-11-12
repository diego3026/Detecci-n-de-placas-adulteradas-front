from PyQt6.QtWidgets import QWidget, QListView, QVBoxLayout
from PyQt6.QtCore import QStringListModel
from views.general_view import Ui_Form
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class GeneralController(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("General")
        self.showMaximized()
        self.adjust_frame_width()

        # List View
        self.model = QStringListModel()
        self.ui.listView.setModel(self.model)
        self.ui.listView.setEditTriggers(QListView.EditTrigger.NoEditTriggers)
        self.estilo()
        self.agregar_elementos(["Elemento 1", "Elemento 2", "Elemento 3"])

        # Figura
        self.figure = Figure(figsize=(6, 6), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)
        labels = ['A', 'B', 'C', 'D']
        sizes = [25, 35, 20, 20]
        colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
        self.ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
        self.ax.axis('equal') 
        self.ax.legend(labels, loc="best")
        layout = QVBoxLayout(self.ui.frame_10)
        layout.addWidget(self.canvas)
        self.canvas.draw()

        # desconectarse
        self.ui.desconectarse.clicked.connect(self.onClose)
        
        # Imagenes
        self.ui.imagenes.clicked.connect(self.open_imagenes_window)

        #informe 
        self.ui.informes.clicked.connect(self.open_informes_window)

        # Log 
        self.ui.log.clicked.connect(self.open_log_window)
        
    def open_log_window(self):
        from controllers import LogController
        self.log_window = LogController()
        self.close()
        self.log_window.show()

    def open_informes_window(self):
        from controllers import InformesController
        self.informe_window = InformesController()
        self.close()
        self.informe_window.show()

    def onClose(self):
        from controllers import MainController
        self.main_window = MainController()
        self.close()
        self.main_window.show()

    def open_imagenes_window(self):
        from controllers import ImagenesController
        self.imagenes_window = ImagenesController()
        self.close()
        self.imagenes_window.show()

    def agregar_elementos(self, items):
        self.model.setStringList(items)

    def estilo(self):
        self.ui.desconectarse.setStyleSheet("""
            QPushButton{
                color: #000000;
                padding: 10px 0;
            }
            QPushButton:hover{
                color: #5E5ADB;
                background: #F3F4F8;
            }
        """)
        self.ui.general.setStyleSheet("""
            QPushButton{
                color: #5E5ADB;
                background: #F3F4F8;
                padding: 10px 0;
            }
            QPushButton:hover{
                color: #5E5ADB;
                background: #F3F4F8;
            }
        """)
        self.ui.informes.setStyleSheet("""
            QPushButton{
                color: #000000;
                padding: 10px 0;
            }
            QPushButton:hover{
                color: #5E5ADB;
                background: #F3F4F8;
            }
        """)
        self.ui.imagenes.setStyleSheet("""
            QPushButton{
                color: #000000;
                padding: 10px 0;
            }
            QPushButton:hover{
                color: #5E5ADB;
                background: #F3F4F8;
            }
        """)
        self.ui.log.setStyleSheet("""
            QPushButton{
                color: #000000;
                padding: 10px 0;
            }
            QPushButton:hover{
                color: #5E5ADB;
                background: #F3F4F8;
            }
        """)
        self.ui.tabWidget.setStyleSheet("""
            QTabWidget::pane { /* El contenedor de las pestañas */
                padding: 5px;
                border-top: 1px solid #8B909A;
            }
            QTabBar::tab { /* Cada pestaña */
                background: transparent;
                color: #333;
                padding: 8px 15px;
                min-width: 100px;
                font-weight: bold;
            }
            QTabBar::tab:selected { /* Pestaña seleccionada */
                background: #ffffff;
                color: #000;
                border-bottom: 2px solid #5d99c6; /* Borde inferior más grueso */
            }
            QTabBar::tab:hover { /* Efecto al pasar el mouse */
                background: #d0d0d0;
            }
        """)

        self.ui.listView.setStyleSheet("""
            QListView::item {
                color: black;
                padding: 5px 0;
            }
            QListView::item:selected {
                color: black; /* Color de fondo del elemento seleccionado */
            }
        """)

    def adjust_frame_width(self):
        width = int(self.width() / 5)
        self.ui.frame.setMaximumWidth(width)
        self.ui.frame_2.setMinimumWidth(width*4)

    def resizeEvent(self, event):
        self.adjust_frame_width()
        super().resizeEvent(event)

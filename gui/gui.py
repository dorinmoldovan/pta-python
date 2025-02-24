from PyQt6.QtWidgets import QWidget, QLineEdit, QPushButton, QTextEdit, QLabel, QComboBox
from PyQt6.QtCore import QTimer, QRect, Qt
from PyQt6.QtGui import QIntValidator, QDoubleValidator, QPalette, QColor, QPixmap

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, QColor("white"))
        self.setPalette(palette)

        self.setGeometry(500, 50, 800, 950)

        self.input1_label = QLabel("Number of plums (N):", self)
        self.input1_label.setGeometry(QRect(50, 50, 150, 30))
        
        self.input1 = QLineEdit(self)
        self.input1.setPlaceholderText("")
        self.input1.setValidator(QIntValidator())
        self.input1.setGeometry(QRect(250, 50, 120, 25))
        self.input1.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.input2_label = QLabel("Number of iterations (I):", self)
        self.input2_label.setGeometry(QRect(50, 80, 150, 30))
        
        self.input2 = QLineEdit(self)
        self.input2.setPlaceholderText("")
        self.input2.setValidator(QIntValidator())
        self.input2.setGeometry(QRect(250, 80, 120, 25))
        self.input2.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.input3_label = QLabel("Number of dimensions (D):", self)
        self.input3_label.setGeometry(QRect(50, 110, 150, 30)) 
        
        self.input3 = QLineEdit(self)
        self.input3.setPlaceholderText("")
        self.input3.setValidator(QIntValidator())
        self.input3.setGeometry(QRect(250, 110, 120, 25))
        self.input3.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.input4_label = QLabel("Fruitiness threshold (FT):", self)
        self.input4_label.setGeometry(QRect(50, 140, 150, 30))
        
        self.input4 = QLineEdit(self)
        self.input4.setPlaceholderText("")
        self.input4.setValidator(QDoubleValidator())
        self.input4.setGeometry(QRect(250, 140, 120, 25))
        self.input4.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.input5_label = QLabel("Ripeness threshold (RT):", self)
        self.input5_label.setGeometry(QRect(50, 170, 150, 30))
        
        self.input5 = QLineEdit(self)
        self.input5.setPlaceholderText("")
        self.input5.setValidator(QDoubleValidator())
        self.input5.setGeometry(QRect(250, 170, 120, 25))
        self.input5.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.input6_label = QLabel("Minimum fruitiness rate (FR_min):", self)
        self.input6_label.setGeometry(QRect(50, 200, 200, 30))
        
        self.input6 = QLineEdit(self)
        self.input6.setPlaceholderText("")
        self.input6.setValidator(QDoubleValidator())
        self.input6.setGeometry(QRect(250, 200, 120, 25))
        self.input6.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.input7_label = QLabel("Maximum fruitiness rate (FR_max):", self)
        self.input7_label.setGeometry(QRect(50, 230, 200, 30))
        
        self.input7 = QLineEdit(self)
        self.input7.setPlaceholderText("")
        self.input7.setValidator(QDoubleValidator())
        self.input7.setGeometry(QRect(250, 230, 120, 25))
        self.input7.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.input8_label = QLabel("Epsilon (eps):", self)
        self.input8_label.setGeometry(QRect(50, 260, 150, 30))
        
        self.input8 = QLineEdit(self)
        self.input8.setPlaceholderText("")
        self.input8.setValidator(QDoubleValidator())
        self.input8.setGeometry(QRect(250, 260, 120, 25))
        self.input8.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.of_label = QLabel("Objective function (OF):", self)
        self.of_label.setGeometry(QRect(50, 290, 150, 30))

        self.of_dropdown = QComboBox(self)
        self.of_dropdown.setGeometry(QRect(250, 290, 120, 25))
        self.of_dropdown.addItems([f'f{i}' for i in range(1, 8)] + [f'g{i}' for i in range(1, 8)] + [f'h{i}' for i in range(1, 11)])

        self.time_label = QLabel("Time between iterations (ms):", self)
        self.time_label.setGeometry(QRect(50, 320, 180, 30))

        self.time_dropdown = QComboBox(self)
        self.time_dropdown.setGeometry(QRect(250, 320, 120, 25))
        self.time_dropdown.addItems([f"{i}" for i in range(0, 1100, 100)])

        self.submit_button = QPushButton("Start Simulation", self)
        self.submit_button.setGeometry(QRect(50, 360, 150, 30))
        self.submit_button.clicked.connect(self.on_submit)

        self.console = QTextEdit(self)
        self.console.setReadOnly(True)
        self.console.setGeometry(QRect(50, 400, 700, 200)) 

        self.ripe_plum_image_label = QLabel(self)
        self.ripe_plum_image_label.setGeometry(QRect(50, 615, 100, 100))
        plum_pixmap = QPixmap("images/edited/ripe_plum_100.png")
        scaled_plum_pixmap = plum_pixmap.scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio)
        self.ripe_plum_image_label.setPixmap(scaled_plum_pixmap)

        self.ripe_fitness_label = QLabel("Ripe plum fitness:", self)
        self.ripe_fitness_label.setGeometry(QRect(160, 650, 110, 30))

        self.ripe_fitness_input = QLineEdit(self)
        self.ripe_fitness_input.setReadOnly(True)
        self.ripe_fitness_input.setGeometry(QRect(280, 650, 100, 25))

        self.unripe_plum_image_label = QLabel(self)
        self.unripe_plum_image_label.setGeometry(QRect(410, 615, 100, 100))
        unripe_plum_pixmap = QPixmap("images/edited/unripe_plum_100.png")
        scaled_unripe_plum_pixmap = unripe_plum_pixmap.scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio)
        self.unripe_plum_image_label.setPixmap(scaled_unripe_plum_pixmap)

        self.unripe_fitness_label = QLabel("Unripe plum fitness:", self)
        self.unripe_fitness_label.setGeometry(QRect(520, 650, 110, 30))

        self.unripe_fitness_input = QLineEdit(self)
        self.unripe_fitness_input.setReadOnly(True)
        self.unripe_fitness_input.setGeometry(QRect(650, 650, 100, 25))

        self.image_label = QLabel(self)
        self.image_label.setGeometry(QRect(400, 50, 350, 350))
        pixmap = QPixmap("images/edited/plum_tree_350.png")
        scaled_pixmap = pixmap.scaled(self.image_label.size(), Qt.AspectRatioMode.KeepAspectRatio)
        self.image_label.setPixmap(scaled_pixmap)

        self.plum_flowers_label = QLabel(self)
        self.plum_flowers_label.setGeometry(QRect(520, 700, 300, 300))
        flowers_pixmap = QPixmap("images/edited/plum_flowers_300.png")
        scaled_flowers_pixmap = flowers_pixmap.scaled(self.plum_flowers_label.size(), Qt.AspectRatioMode.KeepAspectRatio)
        self.plum_flowers_label.setPixmap(scaled_flowers_pixmap)

        self.iteration_label = QLabel("Iteration number (#):", self)
        self.iteration_label.setGeometry(QRect(50, 850, 200, 30))
        
        self.iteration = QLineEdit(self)
        self.iteration.setReadOnly(True)
        self.iteration.setPlaceholderText("")
        self.iteration.setGeometry(QRect(250, 850, 120, 25))
        self.iteration.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.gbest_label = QLabel("Global best value (GBest):", self)
        self.gbest_label.setGeometry(QRect(50, 880, 200, 30))
        
        self.gbest = QLineEdit(self)
        self.gbest.setReadOnly(True)
        self.gbest.setPlaceholderText("")
        self.gbest.setGeometry(QRect(250, 880, 120, 25))
        self.gbest.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.setWindowTitle("Plum Tree Algorithm (PTA)")
        self.setFixedSize(800, 950)
        self.show()

    def on_submit(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.display_message)
        self.timer.start(1000)

    def display_message(self):
        self.console.append("Hello World !!!")

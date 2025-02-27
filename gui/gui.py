"""
Created in 2025

@author: Dorin Moldovan

This work was created with assistance from Microsoft Copilot.
"""

from PyQt6.QtWidgets import QWidget, QLineEdit, QPushButton, QTextEdit, QLabel, QComboBox
from PyQt6.QtCore import QTimer, QRect, Qt, QRegularExpression
from PyQt6.QtGui import QIntValidator, QPalette, QColor, QPixmap, QRegularExpressionValidator

import benchmarks

class App(QWidget):
    N_DEFAULT_VALUE = "30"
    I_DEFAULT_VALUE = "1000"
    FT_DEFAULT_VALUE = "0.8"
    RT_DEFAULT_VALUE = "0.2"
    FR_MIN_VALUE = "0.5"
    FR_MAX_VALUE = "1"
    EPS_VALUE = "1.e-300"
    OF_VALUE = "f1"
    ITERATION_RATE_VALUE = "0"

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, QColor("white"))
        self.setPalette(palette)

        self.setGeometry(500, 50, 800, 950)

        double_validator = QRegularExpressionValidator(QRegularExpression(r'^(0|0\.\d+|1(\.0+)?|0(\.\d+)?([eE][+-]?\d+)?|1(\.0+)?([eE][+-]?\d+)?)$'), self)

        self.input_n_label = QLabel("Number of plums (N):", self)
        self.input_n_label.setGeometry(QRect(50, 50, 150, 30))
        
        self.input_n = QLineEdit(self)
        self.input_n.setPlaceholderText("")
        self.input_n.setValidator(QIntValidator(0, 2147483647))
        self.input_n.setText(self.N_DEFAULT_VALUE)
        self.input_n.setGeometry(QRect(250, 50, 120, 25))
        self.input_n.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.input_i_label = QLabel("Number of iterations (I):", self)
        self.input_i_label.setGeometry(QRect(50, 80, 150, 30))
        
        self.input_i = QLineEdit(self)
        self.input_i.setPlaceholderText("")
        self.input_i.setValidator(QIntValidator(0, 2147483647))
        self.input_i.setText(self.I_DEFAULT_VALUE)
        self.input_i.setGeometry(QRect(250, 80, 120, 25))
        self.input_i.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.input_ft_label = QLabel("Fruitiness threshold (FT):", self)
        self.input_ft_label.setGeometry(QRect(50, 110, 150, 30))
        
        self.input_ft = QLineEdit(self)
        self.input_ft.setPlaceholderText("")
        self.input_ft.setValidator(double_validator)
        self.input_ft.setText(self.FT_DEFAULT_VALUE)
        self.input_ft.setGeometry(QRect(250, 110, 120, 25))
        self.input_ft.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.input_rt_label = QLabel("Ripeness threshold (RT):", self)
        self.input_rt_label.setGeometry(QRect(50, 140, 150, 30))
        
        self.input_rt = QLineEdit(self)
        self.input_rt.setPlaceholderText("")
        self.input_rt.setValidator(double_validator)
        self.input_rt.setText(self.RT_DEFAULT_VALUE)
        self.input_rt.setGeometry(QRect(250, 140, 120, 25))
        self.input_rt.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.input_fr_min_label = QLabel("Minimum fruitiness rate (FR_min):", self)
        self.input_fr_min_label.setGeometry(QRect(50, 170, 200, 30))
        
        self.input_fr_min = QLineEdit(self)
        self.input_fr_min.setPlaceholderText("")
        self.input_fr_min.setValidator(double_validator)
        self.input_fr_min.setText(self.FR_MIN_VALUE)
        self.input_fr_min.setGeometry(QRect(250, 170, 120, 25))
        self.input_fr_min.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.input_fr_max_label = QLabel("Maximum fruitiness rate (FR_max):", self)
        self.input_fr_max_label.setGeometry(QRect(50, 200, 200, 30))
        
        self.input_fr_max = QLineEdit(self)
        self.input_fr_max.setPlaceholderText("")
        self.input_fr_max.setValidator(double_validator)
        self.input_fr_max.setText(self.FR_MAX_VALUE)
        self.input_fr_max.setGeometry(QRect(250, 200, 120, 25))
        self.input_fr_max.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.input_eps_label = QLabel("Epsilon (eps):", self)
        self.input_eps_label.setGeometry(QRect(50, 230, 150, 30))
        
        self.input_eps = QLineEdit(self)
        self.input_eps.setPlaceholderText("")
        self.input_eps.setValidator(double_validator)
        self.input_eps.setText(self.EPS_VALUE)
        self.input_eps.setGeometry(QRect(250, 230, 120, 25))
        self.input_eps.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.of_label = QLabel("Objective function (OF):", self)
        self.of_label.setGeometry(QRect(50, 260, 150, 30))

        self.of_dropdown = QComboBox(self)
        self.of_dropdown.setGeometry(QRect(250, 260, 120, 25))
        self.of_dropdown.addItems([f'f{i}' for i in range(1, 8)] + [f'g{i}' for i in range(1, 8)] + [f'h{i}' for i in range(1, 11)])
        self.of_dropdown.setCurrentIndex(0)

        self.time_label = QLabel("Time between iterations (ms):", self)
        self.time_label.setGeometry(QRect(50, 290, 180, 30))

        self.time_dropdown = QComboBox(self)
        self.time_dropdown.setGeometry(QRect(250, 290, 120, 25))
        self.time_dropdown.addItems([f"{i}" for i in range(0, 1100, 100)])
        self.time_dropdown.setCurrentIndex(0)

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

        self.N = None
        self.I = None
        self.iterations = 0  

        self.show()

    def on_submit(self):
        self.N = int(self.input_n.text())
        self.I = int(self.input_i.text())
        self.FT = float(self.input_ft.text())
        self.RT = float(self.input_rt.text())
        self.FR_min = float(self.input_fr_min.text())
        self.FR_max = float(self.input_fr_max.text())
        self.eps = float(self.input_eps.text())
        self.OF = self.of_dropdown.currentText()
        self.frequency = int(self.time_dropdown.currentText())
        print("N =", self.N)
        print("I =", self.I)
        print("FT =", self.FT)
        print("RT =", self.RT)
        print("FR_min =", self.FR_min)
        print("FR_max =", self.FR_max)
        print("eps =", self.eps)
        print("OF =", self.OF)
        print("frequency =", self.frequency)
        func_details = benchmarks.getFunctionDetails(self.OF)
        print(func_details[0])
        print(func_details[1])
        print(func_details[2])
        print(func_details[3])
        self.console.clear()  
        self.submit_button.setText("Reset Simulation") 
        self.submit_button.clicked.disconnect()
        self.submit_button.clicked.connect(self.on_reset) 
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_gui)
        self.timer.start(1000)

    def update_gui(self):
        if self.iterations < self.I:
            self.iterations += 1
            self.console.append(f"Iteration = {self.iterations}")
        else:
            self.timer.stop()  
            self.submit_button.setText("Reset Simulation")  
            self.submit_button.clicked.disconnect()
            self.submit_button.clicked.connect(self.on_reset) 
    
    def on_reset(self):
        self.timer.stop()
        self.console.clear() 
        self.iterations = 0  
        self.input_n.setText(self.N_DEFAULT_VALUE)  
        self.input_i.setText(self.I_DEFAULT_VALUE)
        self.input_ft.setText(self.FT_DEFAULT_VALUE)
        self.input_rt.setText(self.RT_DEFAULT_VALUE)
        self.input_fr_min.setText(self.FR_MIN_VALUE)
        self.input_fr_max.setText(self.FR_MAX_VALUE)
        self.input_eps.setText(self.EPS_VALUE)
        self.of_dropdown.setCurrentIndex(0)
        self.time_dropdown.setCurrentIndex(0)
        self.submit_button.setText("Start Simulation")  
        self.submit_button.clicked.disconnect()
        self.submit_button.clicked.connect(self.on_submit)  

"""
Created in 2025

@author: Dorin Moldovan

This work was created with assistance from Microsoft Copilot.
"""

import sys
from PyQt6.QtWidgets import QApplication
from gui.gui import App

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec())

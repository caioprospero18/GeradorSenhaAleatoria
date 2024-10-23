import Interface
import sys
from PyQt6.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    interface = Interface.Interface()
    interface.show()
    sys.exit(app.exec())




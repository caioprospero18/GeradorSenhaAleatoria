import sys
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QCheckBox, QHBoxLayout

import Senha


class Interface(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gerador de senha")
        self.resize(300,400)
        senha = Senha.Senha()

        layout = QVBoxLayout()

        label1 = QLabel("Digite o tamanho da senha que deseja gerar.")
        layout.addWidget(label1)

        entrada = QLineEdit()
        entrada.setMaxLength(3)
        entrada.setStyleSheet("background-color: white; font-size: 20px; Height: 40px;")
        layout.addWidget(entrada)

        checkbox_alfa = QCheckBox("Alfabeto")
        layout.addWidget(checkbox_alfa)
        checkbox_num = QCheckBox("Numérico")
        layout.addWidget(checkbox_num)
        checkbox_esp = QCheckBox("Caracter Especial")
        layout.addWidget(checkbox_esp)

        label_resultado = QLabel("")
        layout.addWidget(label_resultado)

        botao_layout = QHBoxLayout()
        botao_layout.addStretch()
        botao1 = QPushButton("Gerar senha", self)
        botao1.setFixedSize(120, 50)
        botao1.setStyleSheet("""
            QPushButton{
                background-color: #a1ca0d; 
                border-radius: 3px;
                border: 2px solid #a1ca0d;
                font-size: 17px;
            }
            QPushButton:hover{
                border-color: white;
                border: 2px solid white;
            }
        """)

        botao1.clicked.connect(lambda: senha.mostrar_senha(entrada, checkbox_alfa, checkbox_num, checkbox_esp, label_resultado))
        botao_layout.addWidget(botao1)
        botao_layout.addStretch()
        layout.addLayout(botao_layout)
        self.setStyleSheet("""
            QWidget {
                background-color: #16181a;
            }
            QCheckBox {
                font-size: 15px;
                color: white;
            }
            QLabel {
                font-size: 25px; 
                color:white;
            }
        """)
        self.setLayout(layout)


import string
import random
from PyQt6.QtWidgets import QMessageBox

class Senha():
    def __init__(self):
        super().__init__()
        pass

    def gerar_senha(self, tamanho, checkbox_alfa, checkbox_num, checkbox_esp):
        senha = []
        caracteres = ""
        if checkbox_alfa.isChecked():
            caracteres += string.ascii_letters
            senha.extend([
                random.choice(string.ascii_uppercase),
                random.choice(string.ascii_lowercase)])
        if checkbox_num.isChecked():
            caracteres += string.digits
            senha.append(random.choice(string.digits))
        if checkbox_esp.isChecked():
            caracteres += string.punctuation
            senha.append(random.choice(string.punctuation))

        if not caracteres:
            QMessageBox.critical(None, "Erro", "Por favor, selecione pelo menos um tipo de caractere.")
            return None

        senha.extend(random.choices(caracteres, k= tamanho - len(senha)))

        random.shuffle(senha)

        return "".join(senha)

    def definir_tamanho(self, entrada):
        entrada_valor = entrada.text()

        if entrada_valor == "":
            QMessageBox.critical(None, "Erro", "Por favor, insira um número.")
            return None
        else:
            try:
                tamanho = int(entrada_valor)
                if tamanho < 4:
                    QMessageBox.critical(None, "Erro", "Senha muito pequena, favor digitar um tamanho maior que 4.")
                    return None
                else:
                    return tamanho
            except ValueError:
                QMessageBox.critical(None, "Erro", "Por favor, insira um número.")
                return None

    def mostrar_senha(self, entrada, checkbox_alfa, checkbox_num, checkbox_esp, label_resultado):
        tamanho = self.definir_tamanho(entrada)
        if tamanho:
            senha = self.gerar_senha(tamanho, checkbox_alfa, checkbox_num, checkbox_esp)
            if senha:
                label_resultado.setText(f"Senha gerada: {senha}")
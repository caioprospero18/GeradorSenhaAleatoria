import string
import random

def gerar_senha(tamanho):
    if tamanho < 4:
        print("Senha muito pequena, favor digitar um tamanho maior.")
    else:
        senha = [
            random.choice(string.ascii_uppercase),
            random.choice(string.ascii_lowercase),
            random.choice(string.digits),
            random.choice(string.punctuation)
        ]

        caracteres = "".join([string.ascii_letters, string.digits, string.punctuation])

        senha.extend(random.choices(caracteres, k= tamanho - len(senha)))

        random.shuffle(senha)

        return "".join(senha)


def main():
    tamanho = int(input("Digite a quantidade de caracteres da sua senha: "))
    print(gerar_senha(tamanho))

if __name__ == '__main__':
    main()



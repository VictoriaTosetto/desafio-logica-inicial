class heroi:
    def __init__(self, nome, xp, nivel):
        self.nome = nome
        self.xp = xp
        self.nivel = nivel

def nome_heroi():
    while True:
        nome = input("Digite o nome do herói: ").strip().title()
        if nome.isalpha():
            return nome
        else:
            print("Nome válido apenas com letras.")

def xp_heroi():
    while True:
        try:
            xp = int(input("Digite a experiência do herói: "))
            if xp > 0:
                return xp
            else:
                print("A quantidade de experiência deve ser maior que 0.")
        except ValueError:
            print("Digite apenas números.")

def nivel_heroi(xp):
    if xp < 1000:
        return "Ferro"
    elif 1000 <= xp <= 2000:
        return "Bronze"
    elif 2001 <= xp <= 5000:
        return "Prata"
    elif 5001 <= xp <= 7000:
        return "Ouro"
    elif 7001 <= xp <= 8000:
        return "Platina"
    elif 8001 <= xp <= 9000:
        return "Ascendente"
    elif 9001 <= xp <= 10000:
        return "Imortal"
    else:
        return "Radiante"

def main():
    nome = nome_heroi()
    xp = xp_heroi()
    nivel = nivel_heroi(xp)

    print(f"O Herói de nome {nome} está no nível de {nivel}")            

main()
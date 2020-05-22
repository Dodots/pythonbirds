class Pessoa:
    def __init__(self, *filhos, nome = None, idade = 28):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    renzo = Pessoa(nome="Renzo")
    dodo = Pessoa(renzo, nome="Dodo")
    print(Pessoa.cumprimentar(dodo))
    print(id(dodo))
    print(dodo.cumprimentar())  #O jeito mais fácil de fazer.
    print(dodo.nome)
    print(dodo.idade)
    for filho in dodo.filhos:
        print(filho.nome)


class Pessoa:
    def __init__(self, nome = None, idade = 28):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa("Dodo")
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())  #O jeito mais fácil de fazer.
    print(p.nome)
    p.nome = 'Douglas'
    print(p.nome)
    print(p.idade)
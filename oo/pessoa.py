class Pessoa:

    # Criando a função
    def __init__(self, *filhos, nome = None, idade = 28):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    # Criando a função
    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    # criando uma variável da classe.
    renzo = Pessoa(nome="Renzo")

    # criando uma variável da classe.
    dodo = Pessoa(renzo, nome="Dodo")

    # chamando a função cumprimentar da calsse Pessoa passando a varíavel da classe dodo
    print(dodo.cumprimentar())
    # chamando o atributo nome
    print(dodo.nome)
    # chamando o atibuto idade
    print(dodo.idade)

    # Irá imprimir o nome de todas as variaveis do atributo filhos do dodo.
    for filho in dodo.filhos:
        print(filho.nome)

    # Estou adicionando uma variavel para o atributo sobrenome dinamicamente.
    dodo.sobrenome = "Carvalho"
    print(dodo.sobrenome)

    #Confere todos os atributos de instancia do objeto.
    print(renzo.__dict__)
    print(dodo.__dict__)

    #exclui a variavel filho dinamicamente.
    del dodo.filhos
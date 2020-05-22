class Pessoa:
    # Estou criando atributo default ou atributo de classe.
    # Atributo de classe ele não aloca um espaço na memória para cada classe. Somente quando você
    # Altera o valor.
    olhos = 2

    # Criando a função
    def __init__(self, *filhos, nome = None, idade = 28):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    # Criando a função
    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    # criando uma instancia da classe.
    renzo = Pessoa(nome="Renzo")

    # criando uma instancia da classe.
    dodo = Pessoa(renzo, nome="Dodo")


    # chamando a função cumprimentar da calsse Pessoa passando a instancia dodo
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

    # Exclui a variavel filho dinamicamente da instancia dodo e não da classe Pessoa.
    del dodo.filhos


    # Confere todos os atributos da instancia do objeto e não os atributos da classe.
    print(renzo.__dict__)

    # (somente quando altera o atributo da classe para aparecer nos atributos da instancia.)
    # Alterando a quantidade de olhos da estancia dodo.
    dodo.olhos = 1
    print(dodo.__dict__)


    # Isso não é possivel, porque nome não é um atributo da classe e sim da instancia criada.
    # print(Pessoa.nome)

    # Isso é possivel porque olhos é um atributo da classe.
    # print(Pessoa.olhos)
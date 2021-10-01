class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome = None, idade= 35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá\n{id(self)}'



if __name__ == '__main__':

    renzo = Pessoa(nome='Renzo\n')
    luciano = Pessoa(renzo,nome='Luciano\n')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filhos in luciano.filhos:
        print(filhos.nome)

    luciano.sobrenome = 'Ramalho'
    del luciano.filhos

    luciano.olhos = 1
    del luciano.olhos
    print(luciano.__dict__)
    print(renzo.__dict__)

    Pessoa.olhos = 3

    print(Pessoa.olhos)
    print(luciano.olhos)
    print(renzo.olhos)

    print(id(Pessoa.olhos), id(luciano.olhos), id(renzo.olhos))


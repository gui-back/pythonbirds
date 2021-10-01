class Pessoa:
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

    print(luciano.__dict__)
    print(renzo.__dict__)


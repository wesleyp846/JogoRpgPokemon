#01:12:40 v4
import random
class Pokemon:

    def __init__(self, especie, level=None, nome=None):
        self.especie = especie

        if level:
            self.level = level
        else:
            self.level = random.randint(1, 100)

        if nome:
            self.nome = nome
        else: self.nome = especie

    def __str__(self):
        return f'{self.nome},({self.level})'

    def atacar(self, pokemon):
        print(f'{self} atacou {pokemon}')

class PokemonEletrico(Pokemon):
    tipo = 'eletrico'
    def atacar(self, pokemon):
        print(f'{self} lançou um raio do trovão em {pokemon}')

class PokemonFogo(Pokemon):
    tipo = 'fogo'
    def atacar(self, pokemon):
        print(f'{self} lançou uma bola de fogo em {pokemon}')

class PokemonAgua(Pokemon):
    tipo = 'Agua'
    def atacar(self, pokemon):
        print(f'{self} lançou um jato de agua em {pokemon}')




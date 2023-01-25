#v4 31
import random
from Pokemon import *

NOMES = ['João', 'José', 'Maria', 'Marcelo', 'Marcio', 'Marcos', 'Silvia', 'Ana', 'Jessica'
             'Jonatan', 'Mauro', 'Fabio', 'Fabiana', 'Vanessa', 'Thais', 'Isadora', 'Diego']

POKEMONS = [PokemonFogo('Charmander'), PokemonFogo('Flareon'), PokemonFogo('Chamelion'),
            PokemonEletrico('Pikachu'), PokemonEletrico('Raichu'), PokemonAgua('Squirtle'),
            PokemonAgua('Magicarpa')]
class Pessoa:

    def __init__(self, nome=None, pokemons=[]):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

        self.pokemons = pokemons

    def __str__(self):
        return self.nome

    def mostrar_pokemons(self):
        if self.pokemons:
            print(f'Pokemons de {self}:')
            for pokemon in self.pokemons:
                print(pokemon)
        else:
            print(f'{self} Nenhum Pokemon')

class Player(Pessoa):
    tipo = 'player'

    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print(f'{self} capturou {pokemon}')



class Inimigo(Pessoa):
    tipo = 'inimigo'

    def __init__(self, nome=None, pokemons=[]):
        if not pokemons:
            for i in range(random.randint(1,6)):
                pokemons.append(random.choice(POKEMONS))
        super().__init__(nome=nome, pokemons=pokemons)


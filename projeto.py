from Node import Node
from ListaSE import ListaSE
from NodeTree import NodeTree
from BinaryTree import BinaryTree

class Filme:
    def __init__(self, titulo, genero, ano, avaliacao):
        self.titulo = titulo
        self.genero = genero
        self.ano = ano
        self.avaliacao = avaliacao

class SistemaRecomendacao:
    def __init__(self):
        self.arvore_generos = BinaryTree()
        self.lista_filmes = ListaSE()

    def adicionar_filme_lista(self, filme):
        novo_no = Node(filme)
        novo_no.next = self.lista_filmes.head
        self.lista_filmes.head = novo_no

    def adicionar_filme(self, filme):
        self.adicionar_filme_lista(filme)
        self.arvore_generos.insert(filme.genero)

    def buscar_filmes_por_genero(self, genero):
        filmes = []
        current = self.lista_filmes.head
        while current:
            filme = current.value
            if filme.genero == genero:
                filmes.append(filme)
            current = current.next
        return filmes

    def recomendar_filmes(self, genero):
        filmes_do_genero = self.buscar_filmes_por_genero(genero)
        if filmes_do_genero:
            return sorted(filmes_do_genero, key=lambda x: x.avaliacao, reverse=True)[:5]
        else:
            return []

sistema = SistemaRecomendacao()

sistema.adicionar_filme(Filme("Titanic", "Romance", 1997, 8.5))
sistema.adicionar_filme(Filme("O Senhor dos Anéis", "Fantasia", 2001, 9.2))
sistema.adicionar_filme(Filme("Pulp Fiction", "Ação", 1994, 8.8))
sistema.adicionar_filme(Filme("A Bela e a Fera", "Romance", 1991, 8.1))
sistema.adicionar_filme(Filme("O Rei Leão", "Animação", 1994, 8.5))

print([filme.titulo for filme in sistema.recomendar_filmes("Romance")])
# Output: ['Titanic', 'A Bela e a Fera']

print([filme.titulo for filme in sistema.recomendar_filmes("Ação")])
# Output: ['Pulp Fiction']
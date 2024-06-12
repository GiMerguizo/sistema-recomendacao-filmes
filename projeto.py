# imports
from Node import Node
from ListaSE import ListaSE
from NodeTree import NodeTree
from BinaryTree import BinaryTree
from Pilha import Pilha
from time import sleep
import csv

# Classe para criar a estrutura do Filme
class Filme:
    def __init__(self, titulo, genero, ano, avaliacao):
        self.titulo = titulo
        self.genero = genero
        self.ano = ano
        self.avaliacao = avaliacao
        
    def __str__(self):
        return f"{self.titulo} ({self.ano}) - Avaliação: {self.avaliacao}"

# Classe que monta a estrutura da árvore com o sitema de recomendação
class SistemaRecomendacao:
    def __init__(self):
        self.arvore_generos = BinaryTree()
        self.lista_filmes = ListaSE()
        
    def adicionar_filmes_csv(self, arquivo_csv):
        with open(arquivo_csv, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                filme = Filme(row['titulo'], row['genero'], int(row['ano']), float(row['avaliacao']))
                self.adicionar_filme(filme)

    def adicionar_filme_lista(self, filme):
        novo_no = Node(filme)
        novo_no.next = self.lista_filmes.head
        self.lista_filmes.head = novo_no

    def adicionar_filme(self, filme):
        self.adicionar_filme_lista(filme)
        self.arvore_generos.insert(filme.genero)

    def buscar_filmes(self, genero, ano_minimo=None, ano_maximo=None):
        filmes_filtrados = []
        current = self.lista_filmes.head
        while current:
            filme = current.value
            if (filme.genero == genero or genero is None) and (
                (ano_minimo is None or filme.ano >= ano_minimo) and
                (ano_maximo is None or filme.ano <= ano_maximo)
            ):
                filmes_filtrados.append(filme)
            current = current.next
        return filmes_filtrados

    def recomendar_filmes(self, genero=None, ano_minimo=None, ano_maximo=None):
        filmes_filtrados = self.buscar_filmes(genero, ano_minimo, ano_maximo)
        if filmes_filtrados:
            return sorted(filmes_filtrados, key=lambda x: x.avaliacao, reverse=True)[:5]
        else:
            return []

# Adicionando os filmes do arquivo .csv
sistema = SistemaRecomendacao()
sistema.adicionar_filmes_csv("filmes.csv")

# Fazendo a recomendação dos Filmes
while True:
    filtro = input("\nDeseja filtrar por: \n[1] Gênero e Ano \n[2] Apenas por gênero\n[3] Sair\nOpção: ")
    if filtro == '3':
        print('Programa sendo encerrado...')
        sleep(2)
        break

    generos_existentes = []
    current = sistema.lista_filmes.head
    while current:
        filme = current.value
        if filme.genero not in generos_existentes:
            generos_existentes.append(filme.genero)
        current = current.next

    if filtro == '1':
        print("\nGêneros existentes:")
        for genero in generos_existentes:
            print(f"- {genero}")
        genero = input("Digite o gênero desejado: ")
        ano_minimo_str = input("Digite o ano mínimo (opcional): ")
        ano_maximo_str = input("Digite o ano máximo (opcional): ")
        ano_minimo = int(ano_minimo_str) if ano_minimo_str else None
        ano_maximo = int(ano_maximo_str) if ano_maximo_str else None
        recomendacoes = sistema.recomendar_filmes(genero, ano_minimo, ano_maximo)
    elif filtro == '2':
        print("\nGêneros existentes:")
        for genero in generos_existentes:
            print(f"- {genero}")
        genero = input("Digite o gênero desejado: ")
        recomendacoes = sistema.recomendar_filmes(genero)
    else:
        print("Opção inválida.")
        continue

    if recomendacoes:
        print(f"\nRecomendações:")
        for filme in recomendacoes:
            print(f"\n{filme}")
    else:
        print("\nNenhum filme encontrado para os filtros especificados!.")
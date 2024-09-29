
from Modelos.avaliacao import Avaliacao
from Modelos.Cardapio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()#title garante a impressão com a inicial maiúscula
        self._categoria = categoria.upper() #upper garante a impressão e todas as letras maiúsculas
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self.nome}    |   {self.categoria}'
    
    @classmethod #Indica que o método pertence a class
    def listar_restaurantes(cls):#cls no parêntesis sempre que usar o @classmethod
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes: # .cls para informara que se trata da lista que pertence  classe Restaurante
            print (f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante._ativo}')


    #o property nos permite pegar o atributo de uma classe e mudar a forma como ele vai ser lido.
    @property
    def ativo(self):
        return 'Verdadeiro' if self._ativo else 'Falso'

    #não é um método da classe por isso não usamos o classmethod. É um metodo para os objetos
    def alternar_estado(self): 
        self._ativo = not self._ativo
   
    #O IF esta condicionando que o usuario deve escolher nota entre 0 e 5 para o codigo rodar
    def receber_avaliacao(self, cliente, nota):
        
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
    
    #o Property permite ler as informações deste metodo para cada restaurante cadastrado
    @property 
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        #sum esta somando as notas (avaliacao._nota) de cada avaliação(da lista avaliação) 
        #realizada em self._avaliacao
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        #len indica a quantidde de notas já recebidas
        quantidade_de_nota = len(self._avaliacao)

        #round é a funcao que vai ajudar a determinar que se imprima apenas uma casa decimal 
        #apos a virgula. O 1 no final informa a quantidade de digito apos a virgura
        media = round(soma_das_notas / quantidade_de_nota, 1)
        return media
    
    #isinstance retorna verdadeiro se o item que se deseja adicionar no cardapio, pertencer a classe ItemCardapio
    def adicionar_no_cardapio(self, item):
        if isinstance (item, ItemCardapio):
            self._cardapio.append(item)
    
    #O enumerate exibe o cardapio enumerato  partir do 1 (start = 1)
    #i - representa o indice do item a ser listado.
    #O Has atributo(hasattr) indica que se o item que se deseja adicionar...
    #...tiver o atributo informado, deve-se imprimir a mensagem
    @property
    def exibir_cardapio(self):
        print(f'Cardapio do restaurante {self._nome}\n')
        for i, item in enumerate (self._cardapio, start = 1):
            if hasattr(item, 'descricao'):
                mensagem_prato = f'{i}. Nome: {item._nome} | Preço: R$ {item._preco} | Descrição: {item.descricao}' 
                print(mensagem_prato)
            elif hasattr(item, 'tamanho'):
                mensagem_bebida = f'{i}. Nome: {item._nome} | Preço: R$ {item._preco} | Tamanho: {item.tamanho}' 
                print(mensagem_bebida)
            else:
                mensagem_sobremesa = f'{i}. Nome: {item._nome} | Preço: R$ {item._preco} | Descricao: {item.descricao}' 
                print(mensagem_sobremesa)







    



#Importação da classe ItemCardapio
from Modelos.Cardapio.item_cardapio import ItemCardapio

#Esta classe herdará as ações e atributos da classe item cardápio.
#O super vai permitir que se utilize as informações da classe ItemCardapio
#o self cria o objeto de um atributo exclusivo desta classe
class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self.tamanho = tamanho
    
    def __str__(self):
        return self._nome
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.08)

        
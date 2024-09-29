
#o pacote abc nos permite importar o abstractmethod para criação de metodos abstratos
from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    #Este metodo permite aplicar desconto em todos os tipos de produto das diferentes classes
    @abstractmethod
    def aplicar_desconto(self):
        pass

        
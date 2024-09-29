#arquivo principal para rodar os códigos desenvolidos na classe Restaurante.
#o From importa a classe desejada de dentro do arquivo desejado 

from Modelos.restaurante import Restaurante
from Modelos.Cardapio.bebida import Bebida
from Modelos.Cardapio.prato import Prato
from Modelos.Cardapio.sobremesa import Sobremesa

#criando os restaurantes
restaurante_praca = Restaurante('Praça', 'Gourmet')
bebida_suco = Bebida ('Suco de Melancia',  5.0, 'Grande')
bebida_suco.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(bebida_suco)


prato_paozinho = Prato ('Paozinho', 2.0, 'Francês recheado com 4 queijo, presunto e ovo.')
prato_paozinho.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(prato_paozinho)

sobremesa_pudim = Sobremesa ('Pudim', 8.0, 'Pudim de leite com cobertura de caramelo')
sobremesa_pudim.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(sobremesa_pudim)


def main():
  restaurante_praca.exibir_cardapio
  
if __name__=='__main__':
    main()  
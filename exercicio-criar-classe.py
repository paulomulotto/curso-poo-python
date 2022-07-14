"""
  Exercício da aula Como criar Classes e Objetos
  Crie uma classe chamada Automovel, com um construtor que receba:

  marca
  placa
  quantidade de portas
  quantidade pneus
  Crie três objetos diferentes para essa classe
"""

""" Solução: """

class Automovel:
    def __init__(self, marca, placa, qntdd_portas, qtdd_pneus):
        """Método construtor que recebe as informações solicitadas
        Lembre-se:
            O método __init__ é chamado quando invocamos NomeDaClasse()
            O self é necessário para atribuir as informações do objeto.
        """
        self.marca = marca
        self.placa = placa
        self.qntdd_portas = qntdd_portas
        self.qtdd_pneus = qtdd_pneus

if __name__ == "__main__":
    # Criando objetos da classe Automovel
    auto1 = Automovel("Honda", "ABC1234", 2, 4)
    auto2 = Automovel("Ford", "ABD1235", 4, 4)
    auto3 = Automovel("Ford", "ABF1236", 4, 4)

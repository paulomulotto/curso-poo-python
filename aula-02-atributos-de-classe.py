"""
Adicione na classe Automóvel criada no exercício da aula anterior (https://github.com/paulomulotto/curso-poo-python/blob/main/exercicio-criar-classe.py) 
um atributo de classe (do tipo lista) para salvar todos os automóveis criados por ela.

Altere também o método construtor (def __init__(self,...) ) para que todos os automóveis criados por essa classe sejam adicionados a essa lista.

Por fim, implemente o método __repr__(self) para que seja impresso a placa do veículo como representação do objeto.
  
"""

""" Solução: """
class Automovel:
    lista_automoveis = []
    def __init__(self, marca, placa, qntdd_portas, qtdd_pneus):
        self.marca = marca
        self.placa = placa
        self.qntdd_portas = qntdd_portas
        self.qtdd_pneus = qtdd_pneus
        Automovel.lista_automoveis.append(self)

    def __repr__(self):
        return self.placa

auto1 = Automovel("Honda", "ABC1234", 2, 4)
auto2 = Automovel("Ford", "ABD1235", 4, 4)
auto3 = Automovel("Ford", "ABF1236", 4, 4)
print(auto1)
# ABC1234

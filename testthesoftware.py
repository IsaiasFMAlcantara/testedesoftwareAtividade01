import unittest
import pytest
"""
animalnome = 'Elefante'
animalpeso = 1000
animalpata = 4
class Animal:
    def _init_(self, nome,peso=int,pata=int):
        self._nome = nome
        self.peso = peso
        self.pata = pata
    @property
    def nome(self):
        return self._nome 
    def GetCaracter(self):
        print(f"O {self.nome} - {self.pata} - {self.peso}")
    def som(self):
        print(f"O {self.nome} está trombeteando")

animal = Animal(animalnome,animalpeso,animalpata)
print(animal.nome) # passando esse metodo é possivel acessar o nome do animal através da classe
animal.som() # passando esse metodo é possivel ver o nome do animal ja que foi chamado do proprio metodo de retornar nome
animal.GetCaracter() # passando esse metodo é possivel ver as caracteristicas desse animal. nome, peso e patas
###########
###########
class TestClas(unittest.TestCase):
    def testeNome(self):
        animal = Animal(animalnome,animalpeso,animalpata)
        self.assertEqual(animal.nome, "Elefante") # para que venha ocorrer um erro é necessario que o nome de Elefante seja subistituido
    def test_som(self):
        animal = Animal(animalnome,animalpeso,animalpata)
        animal.som()
        self.assertEqual(self.testeNome, "O elefante está trombeteando")
if _name_ == "_main_":
    unittest.main()
###############################################################################################################
class Data:
    def format_date(self, date):
        month_names = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
        day = date.split('/')[0]
        month = date.split('/')[1]
        year = date.split('/')[2]
        return f'Ariquemes, {day} de {month_names[int(month) - 1]} de {year}'

    def data(self):
        date = input('Digite uma data no formato dd/mm/aaaa: ')
        formatted_date = self.format_date(date)
        print(f'{formatted_date}')
###########
###########
class TestFormatDate(unittest.TestCase):
    def test_format_date_valid_input(self):
        date = '15/08/2023'
        expected_output = 'Ariquemes, 23 de março de 2023'
        actual_output = Data().format_date(date)
        self.assertEqual(actual_output, expected_output)
    def test_format_date_invalid_input(self):
        date = '15/08/2023'
        expected_output = None
        actual_output = Data().format_date(date)
        self.assertEqual(actual_output, expected_output)

def main():
    while True:
        print('''
            1 - Datas
            2 - Unnitest
            0 - Sair
            ''')
        escolha = int(input('Escolha uma opção do menu: '))
        if escolha == 1:
            Data().data()
        elif escolha == 2:
            unittest.main()
        elif escolha == 0:
            print('t c h a u')
            break

if _name_ == '_main_':
    main()
###############################################################################################################

class Calculadora:
    def _init_(self, a=int, b=int):
        self.a = a
        self.b = b
    def soma(self):
        print(f'Adição | sua conta é: {self.a} + {self.b} = {self.a + self.b}')

    def subtracao(self):
        print(f'Subtração | sua conta é: {self.a} - {self.b} = {self.a - self.b}')

    def multiplicacao(self):
        print(f'Multiplicação | sua conta é: {self.a} * {self.b} = {self.a * self.b}')

    def divisao(self):
        if self.b == 0:
            raise ZeroDivisionError
        else:
            print(f'Divisão | sua conta é: {self.a} / {self.b} = {self.a / self.b}')
###########
###########
@pytest.mark.parametrize("a, b, esperado", [(1, 2, 3), (10, 20, 30), (10, 2, 8), (20, 10, 10)])
def test_adicionar(a, b, esperado):
    calculadora = Calculadora()
    assert calculadora.soma(a, b) == esperado
@pytest.mark.parametrize("a, b, esperado", [(10, 2, 8), (20, 10, 10)])
def test_subtrair(a, b, esperado):
    calculadora = Calculadora()
    assert calculadora.subtracao(a, b) == esperado
@pytest.mark.parametrize("a, b, esperado", [(1, 2, 2), (10, 20, 200)])
def test_multiplicar(a, b, esperado):
    calculadora = Calculadora()
    assert calculadora.multiplicacao(a, b) == esperado
@pytest.mark.parametrize("a, b, esperado", [(10, 2, 5), (20, 10, 2)])
def test_dividir(a, b, esperado):
    calculadora = Calculadora()
    assert calculadora.divisao(a, b) == esperado
@pytest.mark.parametrize("a, b", [(10, 0)])
def test_divisao_por_zero(a, b):
    with pytest.raises(ZeroDivisionError):
        calculadora = Calculadora()
        calculadora.divisao(a, b)
if _name_ == "_main_":
    pytest.main()
"""
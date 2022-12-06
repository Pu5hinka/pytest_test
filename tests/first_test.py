import pytest
from app.Calculator import Calculator

class TestCalc: #название класса тестов
    def setup(self): #предварительный метод setup в котором подключаем тестируемый объект Калькулятор
        self.calc = Calculator

    def test_multiply_calculate_correctly(self): #простой тест на проверку правильности умножения
        assert self.calc.multiply(self, 2, 2) == 4

    # def test_multiply_calculation_failed(self):
    #     assert self.calc.multiply(self, 2, 2) == 5

    def setup(self):
        self.calc = Calculator

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 10, 5) == 2

    def setup(self):
        self.calc = Calculator

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 100, 5) == 95

    def setup(self):
        self.calc = Calculator

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 11, 6) == 17
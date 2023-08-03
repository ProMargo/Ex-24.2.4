from app.Calculator import Calculator
import pytest

class TestPositive:
    def setup(self):
        self.Calculator = Calculator
    def test_successfull_addition(self):
        assert self.Calculator.adding(self, 4, 4) == 8
    def test_successfull_subtraction(self):
        assert self.Calculator.subtraction(self, 6, 1) == 5
    def test_successfull_multiplication(self):
        assert self.Calculator.multiply(self, 5, 5) == 25
    def test_successfull_division(self):
        assert self.Calculator.division(self, 100, 5) == 20

    def teardown(self):
        print('Выполнение метода Teardown')
from unittest.mock import patch

from src.pytemplate.domain.models import Operands, operands_factory
from src.pytemplate.entrypoints.cli.main import main
from src.pytemplate.service.calculator import Calculator


def test_operands_type():
    operands = Operands(2, 4)
    assert operands.first_operand == 2
    assert operands.second_operand == 4


def test_operands_factory_type():
    assert isinstance(operands_factory(1, 4), Operands)


def test_calculator_add():
    calculator = Calculator()
    assert calculator.add(operands_factory(1, 3)) == 4


def test_calculator_substract():
    calculator = Calculator()
    assert calculator.subtract(operands_factory(6, 3)) == 3


def test_calculator_divide():
    calculator = Calculator()
    assert calculator.divide(operands_factory(7, 3)) == 2


def test_calculator_mult():
    calculator = Calculator()
    assert calculator.multiply(operands_factory(4, 3)) == 12


@patch("builtins.input", return_value="12 12 add")
def test_main_add(mock_input):
    result = main()
    assert result == 24


@patch("builtins.input", return_value="12 12 divide")
def test_main_divide(mock_input):
    result = main()
    assert result == 1


@patch("builtins.input", return_value="24 12 subtract")
def test_main_subtract(mock_input):
    result = main()
    assert result == 12


@patch("builtins.input", return_value="4 12 multiply")
def test_main_multiply(mock_input):
    result = main()
    assert result == 48

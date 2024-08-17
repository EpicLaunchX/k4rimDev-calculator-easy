from src.pytemplate.domain.models import Operands, operands_factory


def test_operands_type():
    operands = Operands(2, 4)
    assert operands.first_operand == 2
    assert operands.second_operand == 4


def test_operands_factory_type():
    assert isinstance(operands_factory(1, 4), Operands)

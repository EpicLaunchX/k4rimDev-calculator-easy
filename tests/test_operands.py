from src.pytemplate.domain.models import Operands


def test_operands_type():
    operands = Operands(2, 4)
    assert operands.first_operand == 2
    assert operands.second_operand == 4

from src.pytemplate.domain.models import operands_factory
from src.pytemplate.service.calculator import Calculator


def main():
    first_operand, second_operand, action = tuple(input().split())

    operands = operands_factory(int(first_operand), int(second_operand))
    calculator = Calculator()
    if action == "add":
        return calculator.add(operands)
    elif action == "divide":
        return calculator.divide(operands)
    elif action == "subtract":
        return calculator.subtract(operands)
    elif action == "multiply":
        return calculator.multiply(operands)
    else:
        return "Wrong operation"

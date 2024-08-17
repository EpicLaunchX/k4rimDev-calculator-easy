from src.pytemplate.domain.models import operands_factory
from src.pytemplate.service.calculator import Calculator


def main():
    first_operand, second_operand, operation = tuple(input().split())

    operands = operands_factory(int(first_operand), int(second_operand))
    calculator = Calculator()
    if operation == "add":
        return calculator.add(operands)
    elif operation == "divide":
        return calculator.divide(operands)
    elif operation == "subtract":
        return calculator.subtract(operands)
    elif operation == "multiply":
        return calculator.multiply(operands)
    else:
        return "Wrong operation"

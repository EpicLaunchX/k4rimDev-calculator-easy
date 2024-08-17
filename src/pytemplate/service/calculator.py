from src.pytemplate.domain.models import operands_factory


class Calculator:
    def add(self, operand: operands_factory) -> int:
        return operand.first_operand + operand.second_operand

    def subtract(self, operand: operands_factory) -> int:
        return operand.first_operand - operand.second_operand

    def multiply(self, operand: operands_factory) -> int:
        return operand.first_operand * operand.second_operand

    def divide(self, operand: operands_factory) -> int:
        return operand.first_operand // operand.second_operand

from abc import ABCMeta, abstractmethod


class AbstractExpression(metaclass=ABCMeta):
    """
    Declare an abstract Interpret operation that is common to all nodes
    in the abstract syntax tree.
    """

    @abstractmethod
    def interpret(self):
        pass


class NonterminalExpression(AbstractExpression):
    """
    Implement an Interpret operation for nonterminal symbols in the grammar.
    """

    def __init__(self, expression):
        self._expression = expression

    def interpret(self):
        # print("NONTERMINAL")
        self._expression.interpret()


class TerminalExpression(AbstractExpression):
    """
    Implement an Interpret operation associated with terminal symbols in
    the grammar.
    """

    def interpret(self):
        pass
        # print("TERMINAL")


def main():
    abstract_syntax_tree = NonterminalExpression(TerminalExpression())
    abstract_syntax_tree.interpret()


if __name__ == "__main__":
    main()

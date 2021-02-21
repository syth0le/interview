from abc import ABCMeta, abstractmethod


class Element(metaclass=ABCMeta):
    """
    Define an Accept operation that takes a visitor as an argument.
    """

    @abstractmethod
    def accept(self, visitor):
        pass


class ConcreteElementA(Element):
    """
    Implement an Accept operation that takes a visitor as an argument.
    """

    def accept(self, visitor):
        visitor.visit_concrete_element_a(self)


class ConcreteElementB(Element):
    """
    Implement an Accept operation that takes a visitor as an argument.
    """

    def accept(self, visitor):
        visitor.visit_concrete_element_b(self)


class Visitor(metaclass=ABCMeta):
    """
    Declare a Visit operation for each class of ConcreteElement in the
    object structure. The operation's name and signature identifies the
    class that sends the Visit request to the visitor. That lets the
    visitor determine the concrete class of the element being visited.
    Then the visitor can access the element directly through its
    particular interface.
    """

    @abstractmethod
    def visit_concrete_element_a(self, concrete_element_a):
        pass

    @abstractmethod
    def visit_concrete_element_b(self, concrete_element_b):
        pass


class ConcreteVisitor1(Visitor):
    """
    Implement each operation declared by Visitor. Each operation
    implements a fragment of the algorithm defined for the corresponding
    class of object in the structure. ConcreteVisitor provides the
    context for the algorithm and stores its local state. This state
    often accumulates results during the traversal of the structure.
    """

    def visit_concrete_element_a(self, concrete_element_a):
        print('from visitor 1 to elem A ')

    def visit_concrete_element_b(self, concrete_element_b):
        print('from visitor 1 to elem B ')


class ConcreteVisitor2(Visitor):
    """
    Implement each operation declared by Visitor. Each operation
    implements a fragment of the algorithm defined for the corresponding
    class of object in the structure. ConcreteVisitor provides the
    context for the algorithm and stores its local state. This state
    often accumulates results during the traversal of the structure.
    """

    def visit_concrete_element_a(self, concrete_element_a):
        print('from visitor 2 to elem A ')

    def visit_concrete_element_b(self, concrete_element_b):
        print('from visitor 2 to elem B ')


def main():
    concrete_visitor_1 = ConcreteVisitor1()
    concrete_element_a = ConcreteElementA()
    concrete_element_a.accept(concrete_visitor_1)

    concrete_visitor_2 = ConcreteVisitor2()
    concrete_element_b = ConcreteElementB()
    concrete_element_b.accept(concrete_visitor_2)

    concrete_element_a.accept(concrete_visitor_2)
    concrete_element_b.accept(concrete_visitor_1)


if __name__ == "__main__":
    main()

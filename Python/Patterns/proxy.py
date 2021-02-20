from abc import ABC, abstractmethod


class FalseSubject(ABC):

    @abstractmethod
    def request(self):
        pass


class RealSubject(FalseSubject):

    def request(self):
        print('Its a real subject')


class Proxy(FalseSubject):

    def __init__(self, real_subject: RealSubject):
        self._real_subject = real_subject

    def request(self) -> None:
        """
                Наиболее распространёнными областями применения паттерна Заместитель
                являются ленивая загрузка, кэширование, контроль доступа, ведение
                журнала и т.д. Заместитель может выполнить одну из этих задач, а затем,
                в зависимости от результата, передать выполнение одноимённому методу в
                связанном объекте класса Реального Субъекта.
                """

        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self) -> bool:
        print("Proxy: Checking access prior to firing a real request.")
        return True

    def log_access(self) -> None:
        print("Proxy: Logging the time of request.", end="")


def client_code(subject: FalseSubject) -> None:
    """
    Клиентский код должен работать со всеми объектами (как с реальными, так и
    заместителями) через интерфейс Субъекта, чтобы поддерживать как реальные
    субъекты, так и заместителей. В реальной жизни, однако, клиенты в основном
    работают с реальными субъектами напрямую. В этом случае, для более простой
    реализации паттерна, можно расширить заместителя из класса реального
    субъекта.
    """

    # ...

    subject.request()

    # ...


if __name__ == "__main__":
    print("Client: Executing the client code with a real subject:")
    real_subject = RealSubject()
    client_code(real_subject)

    print("")

    print("Client: Executing the same client code with a proxy:")
    proxy = Proxy(real_subject)
    client_code(proxy)

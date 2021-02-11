from abc import ABC, abstractmethod


class IComputerBuilder(ABC):

    @abstractmethod
    def set_CPU(self):
        pass

    @abstractmethod
    def set_motherboard(self):
        pass

    @abstractmethod
    def set_GPU(self):
        pass

    @abstractmethod
    def set_RAM(self):
        pass


class ComputerBuilder(IComputerBuilder):

    def set_CPU(self):
        pass

    def set_motherboard(self):
        pass

    def set_GPU(self):
        pass

    def set_RAM(self):
        pass


class GamingLaptopBuilder(ComputerBuilder):

    def produce_CPU(self):
        pass

    def produce_motherboard(self):
        pass

    def produce_GPU(self):
        pass


class GamingDesktopBuilder(ComputerBuilder):

    def produce_CPU(self):
        pass

    def produce_motherboard(self):
        pass

    def produce_GPU(self):
        pass

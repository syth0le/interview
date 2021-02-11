from abc import ABC, abstractmethod


class IComputerBuilder(ABC):

    @staticmethod
    @abstractmethod
    def set_CPU(self):
        pass

    @staticmethod
    @abstractmethod
    def set_motherboard(self):
        pass

    @staticmethod
    @abstractmethod
    def set_GPU(self):
        pass

    @staticmethod
    @abstractmethod
    def set_RAM(self):
        pass


class ComputerBuilder(IComputerBuilder):

    def __init__(self):
        self.computer = Computer()

    def set_CPU(self, value):
        self.computer.cpu = value
        return self

    def set_motherboard(self, value):
        self.computer.motherboard = value
        return self

    def set_GPU(self, value):
        self.computer.gpu = value
        return self

    def set_RAM(self, value):
        self.computer.ram = value
        return self


class Computer:
    def __init__(self, cpu="Intel Core I3 8100", motherboard="H310M-R", gpu="GTX 1050TI", ram="8 GB"):
        self.cpu = cpu
        self.motherboard = motherboard
        self.gpu = gpu
        self.ram = ram

    def __str__(self):
        return f"Computer: {self.cpu} {self.motherboard} {self.gpu} {self.ram}"


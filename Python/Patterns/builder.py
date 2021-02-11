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

    @staticmethod
    @abstractmethod
    def get_result(self):
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

    def get_result(self):
        return self.computer


class Computer:
    def __init__(self, cpu="Intel Core I3 8100", motherboard="H310M-R", gpu="GTX 1050TI", ram="8 GB"):
        self.cpu = cpu
        self.motherboard = motherboard
        self.gpu = gpu
        self.ram = ram

    def __str__(self):
        return f"Computer: {self.cpu}, {self.motherboard}, {self.gpu}, {self.ram}"


class GamingLaptopDirector:

    @staticmethod
    def construct():
        return ComputerBuilder()\
            .set_CPU("Intel Core I5 4450")\
            .set_GPU("RTX 3060TI")\
            .set_motherboard("B440")\
            .set_RAM("16 GB") \
            .get_result()


class GamingDesktopDirector:

    @staticmethod
    def construct():
        return ComputerBuilder()\
            .set_CPU("Intel Core I9 10900k")\
            .set_GPU("RTX 3090TI")\
            .set_motherboard("B450")\
            .set_RAM("32 GB") \
            .get_result()


class WorkLaptopDirector:

    @staticmethod
    def construct():
        return ComputerBuilder()\
            .set_CPU("Intel Core I5 8265U")\
            .set_GPU("AMD VEGA 8")\
            .set_motherboard("B430") \
            .get_result()


def main():
    desktop = GamingDesktopDirector.construct()
    gaming_laptop = GamingLaptopDirector.construct()
    work_laptop = WorkLaptopDirector.construct()
    print(desktop)
    print(gaming_laptop)
    print(work_laptop)


if __name__ == "__main__":
    main()

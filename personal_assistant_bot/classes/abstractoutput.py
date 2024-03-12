from abc import ABC, abstractmethod

class AbstractOutput(ABC):
    @staticmethod
    @abstractmethod
    def message():
        pass
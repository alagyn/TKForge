from abc import ABC, abstractmethod


class MenuLoad(ABC):
    @abstractmethod
    def loadIntoMenu(self):
        pass

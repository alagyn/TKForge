from abc import ABC, abstractmethod


class Container(ABC):
    @abstractmethod
    def load(self, obj):
        pass

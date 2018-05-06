from abc import ABC, abstractmethod


class LinearList:
    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def size():
        pass

    @abstractmethod
    def get(self, idx):
        pass

    @abstractmethod
    def index_of(self, ele):
        pass

    @abstractmethod
    def remove(idx):
        pass

    @abstractmethod
    def add(idx, ele):
        pass

    @abstractmethod
    def __str__(self):
        pass

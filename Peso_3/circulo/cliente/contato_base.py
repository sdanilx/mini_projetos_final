from abc import ABC, abstractmethod


class ContatoBase(ABC):

    def __init__(self, id:str, email:str):
        self.id = id
        self.email = email

    @abstractmethod
    def getId(self):
        return self.id

    @abstractmethod
    def setId(self, id:str):
        self.id = id
        return self.id

    def getEmail(self):
        return self.email

    @abstractmethod
    def setEmail(self, email:str):
        self.email = email
        return self.email

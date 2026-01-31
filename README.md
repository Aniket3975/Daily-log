from abc import ABC, abstractmethod

class IUserRepository(ABC):
    @abstractmethod
    def get_by_id(self, id: int):
        pass

    @abstractmethod
    def add(self, user: User):
        pass

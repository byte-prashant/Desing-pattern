from abc import ABC, abstractmethod
class State(ABC):
    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, context) -> None:
        self._context = context

    @abstractmethod
    def change_state(self) -> None:
        pass
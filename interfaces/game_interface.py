from abc import ABC, abstractmethod


class GameABC(ABC):
    """Game interface."""

    @abstractmethod
    def play(self) -> int:
        pass

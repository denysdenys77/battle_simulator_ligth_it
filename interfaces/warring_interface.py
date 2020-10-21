from abc import ABC, abstractmethod


class WarringABC(ABC):
    """Warring interface."""

    @abstractmethod
    def attack(self) -> float:
        pass

    @abstractmethod
    def damage(self) -> float:
        pass

    @abstractmethod
    def injure(self, total_damage: float) -> bool:
        pass

    @abstractmethod
    def attack_status(self, success: bool) -> None:
        pass

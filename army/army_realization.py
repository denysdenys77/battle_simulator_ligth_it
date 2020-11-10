from army.interface import ArmyABC
from attack.interface import AttackABC
from squad.interface import SquadABC
from typing import List, Type


class Army(ArmyABC):

    def __init__(self,
                 name_number: int,
                 squads: List[SquadABC],
                 attack: Type[AttackABC]
                 ) -> None:
        super().__init__(name_number, squads)
        self._attack = attack()

    def attack(self, defending_army: ArmyABC) -> bool:
        return self._attack.attack(self, defending_army)

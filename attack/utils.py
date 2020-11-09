from army.interface import ArmyABC
from squad.interface import SquadABC


class AttackingDetails:

    def get_attacking_details(self, attacking_army):
        """Getting attacking details."""

        try:
            attacking_squad = attacking_army.squads[0]
        except IndexError as e:
            raise e

        attack_success_probability = attacking_squad.attack()
        damage = attacking_squad.damage()
        return attacking_squad, attack_success_probability, damage

    def get_defending_details(self, defending_army):
        """Getting the strongest defending squad."""
        try:
            defending_squad = sorted(defending_army.squads,
                                     key=lambda squad: squad.attack())[-1]
        except IndexError as e:
            raise e

        defend_success_probability = defending_squad.attack()
        return defending_squad, defend_success_probability

    def army_was_killed(self,
                         squad_was_killed: bool,
                         defending_army: ArmyABC,
                         defending_squad: SquadABC) -> bool:
        """Checking if defending army was killed."""
        # remove squad from army.squads if killed
        if squad_was_killed:
            defending_army.squads.remove(defending_squad)

        # check if army was killed
        if not len(defending_army.squads):
            return True  # was killed
        return False

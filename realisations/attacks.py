from interfaces.attack_interface import AttackABC
from interfaces.army_interface import ArmyABC
from interfaces.squard_interface import SquadABC
from random import choice


class OnStrongestAttack(AttackABC):

    def attack(self, attacking_army: ArmyABC, defending_army: ArmyABC) -> bool:
        """Attacking defending army, returning True if it was killed."""
        attacking_squad, attack_success_probability, damage = \
            self._get_attacking_details(attacking_army)
        defending_squad, defend_success_probability = \
            self._get_defending_details(defending_army)

        if attack_success_probability > defend_success_probability:
            squad_was_killed = defending_squad.injure(damage)
            attacking_squad.attack_status(success=True)

            return self._army_was_killed(squad_was_killed,
                                         defending_army,
                                         defending_squad)
        return False

    @staticmethod
    def _get_attacking_details(attacking_army):
        """Getting attacking details."""
        attacking_squad = attacking_army.squads[0]
        attack_success_probability = attacking_squad.attack()
        damage = attacking_squad.damage()
        return attacking_squad, attack_success_probability, damage

    @staticmethod
    def _get_defending_details(defending_army):
        """Getting the strongest defending squad."""
        defending_squad = sorted(defending_army.squads,
                                 key=lambda squad: squad.attack())[-1]
        defend_success_probability = defending_squad.attack()
        return defending_squad, defend_success_probability

    @staticmethod
    def _army_was_killed(squad_was_killed: bool,
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


class OnWeakestAttack(OnStrongestAttack):

    @staticmethod
    def _get_defending_details(defending_army):
        """Getting the weakest defending squad."""
        defending_squad = sorted(defending_army.squads,
                                 key=lambda squad: squad.attack())[0]
        defend_success_probability = defending_squad.attack()
        return defending_squad, defend_success_probability


class RandomAttack(OnStrongestAttack):

    @staticmethod
    def _get_defending_details(defending_army):
        """Getting random defending squad."""
        defending_squad = choice(defending_army.squads)
        defend_success_probability = defending_squad.attack()
        return defending_squad, defend_success_probability

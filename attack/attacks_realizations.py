from attack.interface import AttackABC
from army.interface import ArmyABC
from .utils import AttackingDetails
from random import choice


class OnStrongestAttack(AttackABC):
    attacking_details = AttackingDetails()

    def attack(self, attacking_army: ArmyABC, defending_army: ArmyABC) -> bool:
        """Attacking defending army, returning True if it was killed."""
        attacking_squad, attack_success_probability, damage = \
            self.attacking_details.get_attacking_details(attacking_army)
        defending_squad, defend_success_probability = \
            self.attacking_details.get_defending_details(defending_army)

        if attack_success_probability > defend_success_probability:
            squad_was_killed = defending_squad.injure(damage)
            attacking_squad.attack_status(success=True)

            return self.attacking_details.army_was_killed(squad_was_killed,
                                                          defending_army,
                                                          defending_squad)
        return False


class OnWeakestAttack(AttackABC):
    attacking_details = AttackingDetails()

    def attack(self, attacking_army: ArmyABC, defending_army: ArmyABC) -> bool:
        """Attacking defending army, returning True if it was killed."""
        attacking_squad, attack_success_probability, damage = \
            self.attacking_details.get_attacking_details(attacking_army)
        defending_squad, defend_success_probability = \
            self.get_defending_details(defending_army)

        if attack_success_probability > defend_success_probability:
            squad_was_killed = defending_squad.injure(damage)
            attacking_squad.attack_status(success=True)

            return self.attacking_details.army_was_killed(squad_was_killed,
                                                          defending_army,
                                                          defending_squad)
        return False

    def get_defending_details(self, defending_army):
        """Getting the weakest defending squad."""
        defending_squad = sorted(defending_army.squads,
                                 key=lambda squad: squad.attack())[0]
        defend_success_probability = defending_squad.attack()
        return defending_squad, defend_success_probability


class RandomAttack(AttackABC):
    attacking_details = AttackingDetails()

    def attack(self, attacking_army: ArmyABC, defending_army: ArmyABC) -> bool:
        """Attacking defending army, returning True if it was killed."""
        attacking_squad, attack_success_probability, damage = \
            self.attacking_details.get_attacking_details(attacking_army)
        defending_squad, defend_success_probability = \
            self.get_defending_details(defending_army)

        if attack_success_probability > defend_success_probability:
            squad_was_killed = defending_squad.injure(damage)
            attacking_squad.attack_status(success=True)

            return self.attacking_details.army_was_killed(squad_was_killed,
                                                          defending_army,
                                                          defending_squad)
        return False

    def get_defending_details(self, defending_army):
        """Getting random defending squad."""
        defending_squad = choice(defending_army.squads)
        defend_success_probability = defending_squad.attack()
        return defending_squad, defend_success_probability

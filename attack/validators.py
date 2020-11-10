from .factory import AttackFactory


class TypeOfStrategyException(Exception):
    pass


class TypeOfStrategyValidator:
    attack_factory_factory = AttackFactory()

    def validate(self, attack_strategy: str) -> str:
        """ Validate type of attack strategy. """
        if (attack_strategy not in
                self.attack_factory_factory.attack_strategies.keys()):
            raise TypeOfStrategyException
        return attack_strategy

from typing import List


class Runner:
    """A runner.

    === Attributes ===
    name: This runner's name.
    email: This runner's email address.
    speed_category: This runner's speed category.


    """
    # Attribute types
    name: str
    email: str
    speed_category: str

    def __init__(self, name: str, email: str, sc: str) -> None:
        """Initialize this runner's attributes."""
        self.name = name  # assigned to the id at name
        self.email = email
        self.speed_category = sc

    def __str__(self) -> str:
        """Return a string representing this Runner.

        >>> r1 = Runner('Gerhard', 'burger19@gmail.com', '40')
        >>> print(r1)
        Gerhard
        """
        return f'{self.name}'


class Registry:
    """A registry.

    === Attributes ===
    _runners: This race registry's list of runners.

    === Sample Usage ===
    >>> r1 = Runner('Gerhard', 'burger19@gmail.com', '40')
    >>> r2 = Runner('Tom', 'thomas32@gmail.com', '30')
    >>> r3 = Runner('Toni', 'antony6@gmail.com', '20')
    >>> r4 = Runner('Margot', 'garmot49@gmail.com', '30')
    >>> racers = [r1, r2, r3, r4]
    >>> r = Registry(racers)
    >>> r.runners_recorded('30')
    ['Tom', 'Toni', 'Margot']
    >>> r1 = Runner('Gerhard', 'burger19@gmail.com', '30')
    >>> r.update_registry(r1)
    >>> r.runners_recorded('30')
    ['Tom', 'Toni', 'Margot', 'Gerhard']
    """
    # Attribute types
    _runners: List[Runner]

    def __init__(self, runners: List[Runner]) -> None:
        """Initialize this registry's attributes."""
        self._runners = runners[:]

    def runners_recorded(self, sc: str = None) -> List[str]:
        """Return a list of runners in this race.

        If no speed category is specified, return all runners in this registry.

        >>> r1 = Runner('Gerhard', 'burger19@gmail.com', '40+')
        >>> r2 = Runner('Tom', 'thomas32@gmail.com', '30')
        >>> racers = [r1, r2]
        >>> r = Registry(racers)
        >>> r.runners_recorded()
        ['Gerhard', 'Tom']
        >>> r.runners_recorded('40+')
        ['Gerhard']
        >>> r.runners_recorded('30')
        ['Tom']
        """
        runners = []
        speed_categories = {'20': 1, '30': 2, '40': 3, '40+': 0}

        for runner in self._runners:
            if sc is not None:
                if 0 == speed_categories[runner.speed_category] and sc == '40+':
                    runners.append(runner.__str__())
                elif sc != '40+' and speed_categories[runner.speed_category] != 0:
                    if speed_categories[sc] >= speed_categories[runner.speed_category]:
                        runners.append(runner.__str__())
            elif sc is None:
                runners.append(runner.__str__())
        return runners

    def update_registry(self, runner: Runner) -> None:
        """Update the registry to include any changes made to the runner.

        >>> r1 = Runner('Toni', 'antony6@gmail.com', '20')
        >>> r2 = Runner('Tom', 'thomas32@gmail.com', '30')
        >>> racers = [r1, r2]
        >>> r = Registry(racers)
        >>> r.runners_recorded()
        ['Toni', 'Tom']
        """
        if runner not in self._runners:
            self._runners.append(runner)
        index = self._runners.index(runner)
        self._runners.pop(index)
        self._runners.insert(index, runner)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

"""
    AUTHOR:  Robin Trachsel
    VERSION: 1.0
    DATE:    04.12.2024

    DESCRIPTION: Class for a Person
"""
from dataclasses import dataclass


@dataclass
class Person:
    """
    a person playing the lottery
    """
    _givenname: str
    _password: str
    _balance: float

    @property
    def givenname(self):
        return self._givenname

    @givenname.setter
    def givenname(self, value):
        self._givenname = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        try:
            self._balance = float(value)
        except ValueError:
            self._balance = -1.0
            raise ValueError


if __name__ == '__main__':
    pass





class Timezones:
    """
        Helper class to store timezones
    """
    pass

class BankAccount:
    """
        Bank Account to ...
    """

    def __init__(self, account_number, first_name, last_name, pref_tz_offset=0, balance=0):
        self.account_number = account_number
        self._first_name = first_name
        self._last_name = last_name
        self.pref_tz_offset = pref_tz_offset
        self._balance = balance

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value.strip().title()

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value.strip().title()

    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    @property
    def balance(self):
        return self._balance

    @classmethod
    def interest_rate(cls):
        return 0.05


    def deposit(self):
        """
            deposit a transaction to the account balance
        """
        pass

    def withdraw(self):
        """
            withdraw a transaction from the account balance
        """
        pass

    def pay_interest(self):
        """
            deposit the interest based on the interest rate
        """
        pass

    def parse_confirmation_code(self):
        """
            ?
        """
        pass


b = BankAccount(140568, "Bud", "Spencer", -7, 100.00)

print(b.balance, b.interest_rate)

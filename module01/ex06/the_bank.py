class Account(object):
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        if hasattr(self, 'value'):
            self.value = 0
        Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount


class Bank(object):
    """The bank"""
    def __init__(self):
        self.account = []

    def add(self, account):
        if (type(account) is not Account):
            print('Acoount must be an `Account` object')
        else:
            self.account.append(account)

    @staticmethod
    def is_corrupted(account):
        if (len(dir(account)) % 2 == 0):
            return True
        if ('name' not in dir(account)
                or 'id' not in dir(account) or 'value' not in dir(account)):
            return True

    def transfer(self, origin, dest, amount):
        """
            @origin: int(id) or str(name) of the first account
            @dest: int(id) or str(name) of the destination account
            @amount: float(amount) amount to transfer
            @return True if success, False if an error occured
        """

        try:
            assert type(origin) is int or type(origin) is str
            assert type(dest) is int or type(dest) is str
            assert type(amount) is float
        except AssertionError as ae:
            print("Type error")
            return False
        try:
            assert amount >= 0
        except AssertionError as ae:
            print("Transfer error")
            return False

        origin_acc = None
        if (type(origin) is int):
            for account in self.account:
                if (account.id == origin):
                    origin_acc = account
                    break
        else:
            for account in self.account:
                if (account.name == origin):
                    origin_acc = account
                    break

        dest_acc = None
        if (type(dest) is int):
            for account in self.account:
                if (account.id == dest):
                    dest_acc = account
                    break
        else:
            for account in self.account:
                if (account.name == dest):
                    dest_acc = account
                    break

        if (origin_acc is None or dest_acc is None):
            print("Account not found")
            return False

        if (self.is_corrupted(origin_acc) or self.is_corrupted(dest_acc)):
            print("Account corrupted")
            return False

        if (origin_acc.value < amount):
            print("Funds insufficient")
            return False

        dest_acc.value += amount
        return True

    def fix_account(self, account):
        """
            fix the corrupted account
            @account: int(id) or str(name) of the account
            @return
            True if success, False if an error occured
        """


my_acc = Account("Aymane", addr="Kh", zip="30090")
my_acc.value = 1000.0
acc2 = Account("Jon", value=0)
bank = Bank()
bank.add(my_acc)
bank.add(acc2)
if (bank.transfer(my_acc.id, acc2.id, 100.0)):
    print("Success")

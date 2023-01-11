class Transaction:
    def __init__(self, transaction_str):
        self.transaction_str = transaction_str
        self.name, self.time, self.amount, self.city = transaction_str.split(',')
        self.time = int(self.time)
        self.amount = int(self.amount)
        self.is_valid = True
        if self.amount > 1000:
            self.is_valid = False

    def compare_with(self, transaction):
        if self.name == transaction.name and self.city != transaction.city and abs(self.time - transaction.time) <= 60:
            self.is_valid = False
            transaction.is_valid = False


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        transaction_objs = [Transaction(transaction) for transaction in transactions]
        for i in range(len(transaction_objs) - 1):
            for j in range(i + 1, len(transaction_objs)):
                transaction_objs[i].compare_with(transaction_objs[j])
        
        ret = []
        for transaction in transaction_objs:
            if not transaction.is_valid:
                ret.append(transaction.transaction_str)
        return ret
        

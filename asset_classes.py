class AssetClass:
    def __init__(self, name: str, allocated_dollars):
        self.__name = name
        self.__balance_amount = allocated_dollars

    def _get_current_balance(self):
        #print("get balance", self.__name, self.__balance_amount)
        return self.__balance_amount

    def _change_balance_absolute(self, change_value):
        self.__balance_amount = float(self.__balance_amount+change_value)
        self.__balance_amount = round(self.__balance_amount, 2) # magic number on decimal places

    def _change_balance_percentage(self, percentage):
        self.__balance_amount = float(self.__balance_amount*percentage)
        self.__balance_amount = round(self.__balance_amount, 2) # magic number on decimal places
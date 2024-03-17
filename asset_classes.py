

class AssetClass:
    def __init__(self, name: str, allocated_dollars):
        self.__name = name
        self.__balance_amount = allocated_dollars

    def _get_current_balance(self):
        #print("get balance", self.__name, self.__balance_amount)
        return self.__balance_amount

    def _add_sip_inflow(self, sip_amount: int):
        self.__balance_amount += sip_amount

    def _change_balance_percentage(self, percentage):
        self.__balance_amount = int(float(self.__balance_amount*(1+percentage))) #int bc we rounddown

    def _rebalance_to_set_value(self, rebalance_value: int):
        self.__balance_amount = rebalance_value
from asset_classes import AssetClass
class Portfolio:
    def __init__(self):
        self.__ordered_asset_classes = ['equities', 'debt', 'gold'] #warning that that the description flips debt and equity positions, but not on I/O
        self.__holdings = {}
        self.__monthly_balances = [] #suggested that when you create the monthly balances, you have element of index 0 with the allocation values
        self.__target_allocations = {}

    def _get_holdings(self):
        return self.__holdings

    def _get_target_allocations(self):
        return self.__target_allocations

    def _create_new_asset_classes(self, allocation_instructions): # comes from controller, which pulled from file reader
        self.__sum_of_allocations = 0
        for index_pos in range(len(self.__ordered_asset_classes)):
            self.__holdings[self.__ordered_asset_classes[index_pos]] = AssetClass(self.__ordered_asset_classes[index_pos] , allocation_instructions[index_pos])
            self.__sum_of_allocations += allocation_instructions[index_pos]

        for index_pos in range(len(self.__ordered_asset_classes)):
            self.__target_allocations[self.__ordered_asset_classes[index_pos]]   = allocation_instructions[index_pos]/self.__sum_of_allocations

        self._document_current_holdings()

    def _document_current_holdings(self):
        self.__current_month_holdings = []
        for asset_class_name in self.__ordered_asset_classes:
            self.__current_month_holdings.append(self.__holdings[asset_class_name]._get_current_balance())
        self.__monthly_balances.append(self.__current_month_holdings)

    def _get_monthly_balances(self):
        return self.__monthly_balances
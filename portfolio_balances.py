from asset_classes import AssetClass
class Portfolio:
    def __init__(self):
        self.__ordered_asset_classes = ['equities', 'debt', 'gold'] #warning that that the description flips debt and equity positions, but not on I/O
        self.__holdings = {}
        self.__monthly_balances = [] #suggested that when you create the monthly balances, you have element of index 0 with the allocation values
        self.__rebalance_months = ['JUNE', 'DECEMBER']
        self.__target_allocations = {}
        self.__create_calendar_indexing()  #consider having calendar creation as a new file

    def _get_holdings(self):
        return self.__holdings

    def _get_target_allocations(self):
        return self.__target_allocations

    def __create_calendar_indexing(self): # if the code gets too long in this file, you can compress it into 1 line of dictionary creation, or make calendar a new file?
        self.__calendar_indexing = {}
        self.__calendar_indexing['JANUARY'] = 1
        self.__calendar_indexing['FEBRUARY'] = 2
        self.__calendar_indexing['MARCH'] = 3
        self.__calendar_indexing['APRIL'] = 4
        self.__calendar_indexing['MAY'] = 5
        self.__calendar_indexing['JUNE'] = 6
        self.__calendar_indexing['JULY'] = 7
        self.__calendar_indexing['AUGUST'] = 8
        self.__calendar_indexing['SEPTEMBER'] = 9
        self.__calendar_indexing['OCTOBER'] = 10
        self.__calendar_indexing['NOVEMBER'] = 11
        self.__calendar_indexing['DECEMBER'] = 12

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

    def _report_specific_month(self, month: str):
        self.__monthly_figures = self.__monthly_balances[self.__calendar_indexing[month]]
        self.__stringed_monthly_balance = str(self.__monthly_figures[0])
        for subsequent_elemental in self.__monthly_figures[1:]:
            self.__stringed_monthly_balance += " " + str(subsequent_elemental)
        print(self.__stringed_monthly_balance)

    def _report_recent_rebalance(self):
        if len(self.__monthly_balances) <= 6: ## 0index for allocation, so we need indices including 0 through 6 to have a rebalance at June or later
            print("CANNOT_REBALANCE")
        else:
            self.__rebalance_index = (len(self.__monthly_balances)-1)//6 * 6
            self.__rebalance_array = self.__monthly_balances[self.__rebalance_index]
            self.__stringed_rebalance = str(self.__rebalance_array[0])
            for rebalance_element in self.__rebalance_array[1:]:
                self.__stringed_rebalance += " " + str(rebalance_element)
            print(self.__stringed_rebalance)

    """
    
    #de-activating with testing finished
    
    def _report_monthly_balances(self):
        print(self.__monthly_balances)
    
    """
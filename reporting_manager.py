class Report:
    def __init__(self, portfolio_instance):
        self.__portfolio_instance = portfolio_instance
        self.__create_calendar_indexing()
        self.__months_per_rebalance = 6
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
    def _print_month_balance(self, month_name: str):
        self.__single_month_balances = (self.__portfolio_instance._get_monthly_balances()[self.__calendar_indexing[month_name]])
        self.__stringed_single_month_balances = str(self.__single_month_balances[0])

        for subsequent_elemental in self.__single_month_balances[1:]:
            self.__stringed_single_month_balances += " " + str(subsequent_elemental)

        print(self.__stringed_single_month_balances)

    def _print_recent_rebalance(self):
        self.__index_skipping = 1
        if len(self.__portfolio_instance._get_monthly_balances()) <= self.__months_per_rebalance:  ## 0index for allocation, so we need indices including 0 through 6 to have a rebalance at June or later
            print("CANNOT_REBALANCE")
        else:
            self.__rebalance_index = (len(self.__portfolio_instance._get_monthly_balances()) - self.__index_skipping) // self.__months_per_rebalance * self.__months_per_rebalance
            self.__rebalance_array = self.__portfolio_instance._get_monthly_balances()[self.__rebalance_index]
            self.__stringed_rebalance = str(self.__rebalance_array[0])
            for rebalance_element in self.__rebalance_array[self.__index_skipping:]:
                self.__stringed_rebalance += " " + str(rebalance_element)
            print(self.__stringed_rebalance)
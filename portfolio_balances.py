from asset_classes import AssetClass
class Portfolio:
    def __init__(self):
        self.__ordered_asset_classes = ['equities', 'debt', 'gold'] #warning that that the description flips debt and equity positions, but not on I/O
        self.__holdings = {}
        self.__monthly_balances = [] #suggested that when you create the monthly balances, you have element of index 0 with the allocation values
        self.__rebalance_months = ['JUNE', 'DECEMBER']
        self.__target_allocations = {}
        self.__create_calendar_indexing()  #consider having calendar creation as a new file


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

        self._report_current_holdings()



    def _document_current_holdings(self):
        self.__current_month_holdings = []
        for asset_class_name in self.__ordered_asset_classes:
            self.__current_month_holdings.append(self.__holdings[asset_class_name]._get_current_balance())

        self.__monthly_balances.append(self.__current_month_holdings)
        #print("document extended", self.__monthly_balances)

    def _calculate_monthly_change(self, changes: list, month: str, sip_instance):
        if len(self.__monthly_balances) > 1: ##a fancy way of saying that we don't do SIP injections same month as initial allocation injection
            print("SIMP ATTMEPTS")
            for asset_class_name in self.__ordered_asset_classes:
                self.__sip_amount = sip_instance._get_SIP_inflow_by_asset_class(asset_class_name)
                self.__holdings[asset_class_name]._add_sip_inflow(self.__sip_amount)

        print("--AFTER SIP")
        self._report_current_holdings()

        self.__holdings['equities']._change_balance_percentage(changes[0]) #this could be refactored into a FOR loop running through index pos with dual purposes
        self.__holdings['debt']._change_balance_percentage(changes[1])
        self.__holdings['gold']._change_balance_percentage(changes[2])

        print("-AFTER GROWTH")
        self._report_current_holdings()


        if month in self.__rebalance_months:
            print("rebal tried")
            self.__rebalance_assets()

        print("---AFTER REBALANCE")
        self._report_current_holdings()

        self._document_current_holdings()

    def __rebalance_assets(self):
        print("rebalance starting with", self.__target_allocations)
        self.__current_total = 0
        for asset_class in self.__holdings:
            self.__current_total += self.__holdings[asset_class]._get_current_balance()
        print("current total", self.__current_total)

        for asset_class in self.__holdings:
            self.__rebalanced_value = int(self.__target_allocations[asset_class] * self.__current_total)
            self.__holdings[asset_class]._rebalance_to_set_value(self.__rebalanced_value)


    def _report_current_holdings(self):
        #print("report current holdings")
        for asset_class in self.__holdings:
            print("asset class", asset_class, self.__holdings[asset_class]._get_current_balance())

from asset_classes import AssetClass
class Portfolio:
    def __init__(self):
        self.__holdings = {}
        self.__monthly_balances = [] #suggested that when you create the monthly balances, you have element of index 0 with the allocation values
        #PLACEHOLDER FOR SETTING TARGET ALLOCATIONS, MAYBE IN A DICTIONARY? MAYBE NOT NECESSARY BECAUSE IT CAN CALCULATE ON MONTH 0????
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
        self.__holdings["debt"] = AssetClass("debt", allocation_instructions[0])
        self.__holdings["equities"] = AssetClass("equities", allocation_instructions[1])
        self.__holdings["gold"] = AssetClass("gold", allocation_instructions[2])
        #print("holdings populated", self.__holdings)

    def __document_current_holdings(self):
        self.__current_month_holdings = []

        self.__monthly_balances.append(self.__current_month_holdings)


    def _report_current_holdings(self):
        print("report current holdings")
        for asset_class in self.__holdings:
            print(asset_class, self.__holdings[asset_class]._get_current_balance())

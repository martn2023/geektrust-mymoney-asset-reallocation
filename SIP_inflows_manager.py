class SIP:
    def __init__(self, monthly_injections_amounts):  #hardcoded assumptions that it's only 3 asset classes with 3 opening balances
        self.__inflows_by_asset_class = {}
        self.__inflows_by_asset_class['equities'] = monthly_injections_amounts[0] ##careful on ordering, as description contradicts I/O order
        self.__inflows_by_asset_class['debt'] = monthly_injections_amounts[1]
        self.__inflows_by_asset_class['gold'] = monthly_injections_amounts[2]


    def _get_SIP_inflow_by_asset_class(self, asset_class_name: str):  # this is going to be summoned by controller each month
        #print(f"SIP MANAGER advises {self.__inflows_by_asset_class[asset_class_name]} injection to {asset_class_name}")
        return self.__inflows_by_asset_class[asset_class_name]
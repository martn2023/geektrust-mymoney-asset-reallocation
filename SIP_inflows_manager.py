
class SIP:
    def __init__(self, monthly_injections_amounts, portfolio_instance):  #hardcoded assumptions that it's only 3 asset classes with 3 opening balances
        self.__inflows_by_asset_class = {}
        self.__inflows_by_asset_class['equities'] = monthly_injections_amounts[0] ##careful on ordering, as description contradicts I/O order
        self.__inflows_by_asset_class['debt'] = monthly_injections_amounts[1]
        self.__inflows_by_asset_class['gold'] = monthly_injections_amounts[2]
        self.__holdings = portfolio_instance._get_holdings()
    def _perform_monthly_SIP_inflows(self, month_name: str):
        if month_name == 'JANUARY':
            return

        for asset_class_name in self.__holdings:
            self.__sip_amount = self.__inflows_by_asset_class[asset_class_name]
            self.__holdings[asset_class_name]._add_sip_inflow(self.__sip_amount)
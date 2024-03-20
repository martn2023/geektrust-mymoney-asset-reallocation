
class SIP:
    def __init__(self, monthly_injections_amounts, portfolio_instance):  #hardcoded assumptions that it's only 3 asset classes with 3 opening balances
        self.__inflows_by_asset_class = {
            'equities': monthly_injections_amounts[0], ##careful on ordering, as description contradicts I/O order
            'debt': monthly_injections_amounts[1],
            'gold': monthly_injections_amounts[2]
            }

        self.__portfolio_instance = portfolio_instance ## changed this because of ChatGPT's advice on Law of Delimiter
    def _perform_monthly_SIP_inflows(self, month_name: str):
        if month_name == 'JANUARY':
            return

        self.__portfolio_instance._factor_in_sip_inflows(self.__inflows_by_asset_class) ##feeds its field into an outside class


        """
        for asset_class_name in self.__holdings:
            self.__sip_amount = self.__inflows_by_asset_class[asset_class_name]
            self.__holdings[asset_class_name]._add_sip_inflow(self.__sip_amount)
        
        """
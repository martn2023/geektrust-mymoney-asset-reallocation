class RebalancingManager:
    def __init__(self, eligible_months: list, portfolio_instance):
        self.__portfolio_instance = portfolio_instance
        self.__rebalancing_months = eligible_months
        self.__target_allocations = portfolio_instance._get_target_allocations()
        self.__last_rebalance = []

    def _attempt_rebalance(self, month_name):
        if month_name in self.__rebalancing_months: #not checking length because fact pattern weirdly assumes 12 month max for time periods
            self.__calculate_rebalance()

        self.__portfolio_instance._document_current_holdings()

    def __calculate_rebalance(self):
        self.__current_holdings_total = 0
        self.__holdings = self.__portfolio_instance._get_holdings()

        for asset_class in self.__holdings:
            self.__current_holdings_total += self.__holdings[asset_class]._get_current_balance()

        for asset_class in self.__holdings:
            self.__rebalanced_value = int(self.__target_allocations[asset_class] * self.__current_holdings_total)
            self.__holdings[asset_class]._rebalance_to_set_value(self.__rebalanced_value)
        

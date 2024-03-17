class ChangeManager:
    def __init__(self, portfolio_instance):
        self.__holdings = portfolio_instance._get_holdings()

    def _calculate_monthly_change(self, change_instructions: list):
        print(change_instructions)
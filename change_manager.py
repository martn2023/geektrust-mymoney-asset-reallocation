class ChangeManager:
    def __init__(self, portfolio_instance):
        self.__portfolio_instance = portfolio_instance
        self.__holdings = portfolio_instance._get_holdings()

    def _calculate_monthly_change(self, change_instructions: list):
        self.__holdings['equities']._change_balance_percentage(change_instructions[0])  # this could be refactored into a FOR loop running through index pos with dual purposes
        self.__holdings['debt']._change_balance_percentage(change_instructions[1])
        self.__holdings['gold']._change_balance_percentage(change_instructions[2])

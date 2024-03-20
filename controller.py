from portfolio_balances import Portfolio
from SIP_inflows_manager import SIP
from change_manager import ChangeManager
from rebalancing_manager import RebalancingManager
from reporting_manager import Report
from constant_values import index_position_of_instruction_type, index_position_of_month_name, index_of_first_numerical_values

class Controller:
    def __init__(self):
        self.__portfolio_instance = Portfolio()
        self.__change_manager_instance = ChangeManager(self.__portfolio_instance)  # moved to initialization because it only needs a portfolio object
        self.__rebalancing_manager_instance = RebalancingManager(self.__portfolio_instance)  # moved to initialization because it only needs a portfolio object
        self.__reporting_instance = Report(self.__portfolio_instance) #moved to initialization because it only needs a portfolio object

    def _accept_instructions_instance(self, instructions_instance):
        self.__accepted_instructions = instructions_instance._get_instructions()
        self.__process_instruction()

    def __process_instruction(self):
        for instruction_line in self.__accepted_instructions:  #warning on hardcoding specific instruction words
            self.__current_instruction = instruction_line[index_position_of_instruction_type]

            if self.__current_instruction == "ALLOCATE": ##indirectly, creation of the portfolio balances instance
                self.__portfolio_instance._create_new_asset_classes(instruction_line[index_of_first_numerical_values:]) ##skipping over instruction header

            elif self.__current_instruction == "SIP": ##creation of the SIP object, which you could have done on init and then updated here
                self.__sip_instance = SIP(instruction_line[1:], self.__portfolio_instance)

            elif self.__current_instruction == "CHANGE":
                self.__sip_instance._perform_monthly_SIP_inflows(instruction_line[index_position_of_month_name])
                self.__change_manager_instance._calculate_monthly_change(instruction_line[index_of_first_numerical_values:index_position_of_month_name])
                self.__rebalancing_manager_instance._attempt_rebalance(instruction_line[index_position_of_month_name])

            elif self.__current_instruction == "BALANCE":
                self.__reporting_instance._print_month_balance(instruction_line[index_position_of_month_name])

            elif self.__current_instruction == "REBALANCE":
                self.__reporting_instance._print_recent_rebalance()
from portfolio_balances import Portfolio
from SIP_inflows_manager import SIP

class Controller:
    def __init__(self):
        pass

    def _accept_instructions_instance(self, instructions_instance):
        self.__accepted_instructions = instructions_instance._get_instructions()
        #print(self.__accepted_instructions)
        self.__process_instruction()

    def __process_instruction(self):
        for instruction_line in self.__accepted_instructions:  #warning on hardcoding specific instruction words
            self.__current_instruction = instruction_line[0]

            if self.__current_instruction == "ALLOCATE": ##indirectly, creation of the portfolio balances instance
                self.__portfolio_instance = Portfolio()
                self.__portfolio_instance._create_new_asset_classes(instruction_line[1:]) ##skipping over instruction header
                self.__portfolio_instance._document_current_holdings()


            elif self.__current_instruction == "SIP": ##creation of the SIP object
                self.__sip_instance = SIP(instruction_line[1:])

            elif self.__current_instruction == "CHANGE":
                #print("---CHANGE STARTING", instruction_line)
                self.__portfolio_instance._calculate_monthly_change(instruction_line[1:-1], instruction_line[-1], self.__sip_instance)


            elif self.__current_instruction == "BALANCE":
                self.__portfolio_instance._report_specific_month(instruction_line[-1])

            elif self.__current_instruction == "REBALANCE":
                self.__portfolio_instance._report_recent_rebalance()
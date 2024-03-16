from portfolio_balances import Portfolio
from SIP_inflows_manager import SIP

class Controller:
    def __init__(self):
        pass
        #self.__asset_class_ordering = ['debt', 'equities', 'gold'] not needed for now

    """
    def _get_asset_class_ordering(self): #optimization not needed now
        return self.__asset_class_ordering
    """

    def _accept_instructions_instance(self, instructions_instance):
        self.__accepted_instructions = instructions_instance._get_instructions()
        print(self.__accepted_instructions)
        self.__process_instruction()

    def __process_instruction(self):
        for instruction_line in self.__accepted_instructions:  #warning on hardcoding specific instruction words
            self.__current_instruction = instruction_line[0]
            print("-----current instruction", self.__current_instruction)

            if self.__current_instruction == "ALLOCATE": ##indirectly, creation of the portfolio balances instance
                self.__portfolio_instance = Portfolio()
                self.__portfolio_instance._create_new_asset_classes(instruction_line[1:]) ##skipping over instruction header
                self.__portfolio_instance._report_current_holdings()
                #self.__portfolio_instance._report_current_holdings()

            elif self.__current_instruction == "SIP": ##creation of the SIP object
                self.__sip_instance = SIP(instruction_line[1:])

            elif self.__current_instruction == "CHANGE":
                print("change", instruction_line)
                #change object advises on amounts, which feeds into classses
                #SIP manager
                #portfolio balances extends its monthly report
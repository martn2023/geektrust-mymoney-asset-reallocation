class FileReader:
    def __init__(self, file_path: str):
        self.__file_path = file_path
        self.__file = open(file_path, 'r')
        self.__data_lines = self.__file.readlines()
        self.__clean_line_breaks()

    def __clean_line_breaks(self):
        for index in range(len(self.__data_lines)-1):  #removing line breaks from every line except last
            self.__data_lines[index] = self.__data_lines[index][:-1]
        self.__split_lines()


    def __split_lines(self):
        for index in range(len(self.__data_lines)):  #removing line breaks from every line except last
            self.__data_lines[index] =  self.__data_lines[index].split(" ")
        self.__reformat_lines()

    def __reformat_lines(self):
        for index in range(len(self.__data_lines)):
            self.__input_type = self.__data_lines[index][0]
            self.__reformatted_line = self.__data_lines[index]
            if self.__input_type == "ALLOCATE":  # excluding "balance" and "rebalance" input types because they have no numbers to reformat
                for pre_correction_index in range(1,len(self.__reformatted_line)):
                    self.__reformatted_line[pre_correction_index] = int(self.__reformatted_line[pre_correction_index])

            elif self.__input_type == "SIP":
                for pre_correction_index in range(1, len(self.__reformatted_line)):
                    self.__reformatted_line[pre_correction_index] = int(self.__reformatted_line[pre_correction_index])

            elif self.__input_type == "CHANGE":
                for pre_correction_index in range(1, len(self.__reformatted_line)-1):
                    self.__reformatted_line[pre_correction_index] = self.__reformatted_line[pre_correction_index][:-1] # to clip % sign
                    self.__reformatted_line[pre_correction_index] = float(self.__reformatted_line[pre_correction_index])/100


    def _get_instructions(self):
        return self.__data_lines
from sys import argv
from input_reader import FileReader
from controller import Controller
from asset_classes import AssetClass
from constant_values import expected_number_of_arguments_input, file_input_index

def main():
    controller_instance = Controller()

    if len(argv) != expected_number_of_arguments_input:
        raise Exception("File path not entered")
    file_path = argv[file_input_index]

    instructions_instance = FileReader(file_path)

    controller_instance._accept_instructions_instance(instructions_instance)


if __name__ == "__main__":
    main()
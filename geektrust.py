from sys import argv
from input_reader import FileReader
from controller import Controller
from asset_classes import AssetClass

def main():

    controller_instance = Controller()

    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]

    instructions_instance = FileReader(file_path)

    controller_instance._accept_instructions_instance(instructions_instance)


if __name__ == "__main__":
    main()
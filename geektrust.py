from sys import argv
from input_reader import FileReader
from controller import Controller
from asset_classes import AssetClass

def main():
    print("")
    print("")
    print("")
    controller_instance = Controller()

    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]

    instructions_instance = FileReader(file_path)

    controller_instance._accept_instructions_instance(instructions_instance)

    """ THIS CODE PROVES WE CAN GROW ASSET CLASS OBJECTS AND STORE THE THEN-CURRENT VALUES IN THE PORTFOLIO BALANCE'S BALANCE SHEET
    n = 5
    new_dict = {}
    new_dict["A"] = n
    n+=7
    new_dict["B"] = n
    print(new_dict)
    """

if __name__ == "__main__":
    main()
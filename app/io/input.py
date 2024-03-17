def enter_text_console():
    """
    Function for entering text from console

    :return:
        str: Text entered by the user
    """
    return input("Enter your text here: ")


def read_file_pyt(path_to_file):
    """
    Function for reading file from given path

    :param path_to_file:
        str: Path to the file to be read
    :return:
        str: Text from file
    """
    file = open(path_to_file, 'r')
    text_from_file = file.read()
    file.close()
    return text_from_file


def read_file_pand(path_to_file):
    """
    Function for reading file from given path using pandas

    :param path_to_file:
        str: Path to the file to be read
    :return:
        str: Text from file
    """
    import pandas as pandas
    return pandas.read_csv(path_to_file)

def show_console(text):
    """
    Function to display the text in console

    :param text:
        str: Text to display
    :return:
        str: Text that was meant to be displayed
    """
    print(text)
    return text


def write_file(path_to_file, text):
    """
    Function to write the text to the file, path to which is given as a parameter

    :param path_to_file:
        str: Path to the file to write the text in
    :param text:
        DataFrame or str: Text or DataFrame to be written to the file
    :return:
        Text written in file
    """
    import pandas as pd
    if isinstance(text, pd.DataFrame):
        text = text.to_string(index=False)

    file = open(path_to_file, 'w')
    file.write(text)
    file.close()
    return text


def write_file_pand(path_to_file, text):
    """
    Function to write the text to the file using pandas

    :param path_to_file:
        str: Path to the file to write the text in
    :param text:
        DataFrame: DataFrame to be written to the flie
    :return:
        Text written in file
    """
    import pandas as pd
    text.to_csv(path_to_file, index=False)

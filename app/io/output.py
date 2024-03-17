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
        None
    """
    import pandas as pd
    if isinstance(text, pd.DataFrame):
        text = text.to_string(index=False)

    with open(path_to_file, 'w') as file:
        file.write(text)


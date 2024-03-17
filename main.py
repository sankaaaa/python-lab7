from app.io.input import enter_text_console, read_file_pyt, read_file_pand
from app.io.output import show_console, write_file


def main():
    console_text = enter_text_console()

    show_console(console_text)

    textfile = read_file_pyt("data/test1.txt")

    show_console(textfile)

    textfile_pandas = read_file_pand("data/test2.csv")

    show_console(textfile_pandas)

    write_file("data/result1.txt", console_text)
    write_file("data/result2.txt", textfile)
    write_file("data/result3.txt", textfile_pandas)


if __name__ == '__main__':
    main()

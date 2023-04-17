import textwrap
from cat_say.constants import CAT, DOWN, UP


def print_message(text: str) -> None:
    text_list = textwrap.wrap(text, 41)
    for string in text_list:
        print(f"| {string:^41} |")


def main():
    text = input('What cat should say?\n --- ')

    print(UP)
    print_message(text)
    print(DOWN)
    print(CAT)


if __name__ == "__main__":
    main()

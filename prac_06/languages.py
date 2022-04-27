from prac_06.programming_language import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(ruby)
    print(python)
    print(visual_basic)

    programming_language_list = [ruby, python, visual_basic]

    print("The dynamically typed languages are: ")
    for item in programming_language_list:
        if item.is_dynamic():
            print(item.name)


if __name__ == '__main__':
    main()

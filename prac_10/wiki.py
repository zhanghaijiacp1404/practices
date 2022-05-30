"""
A simple script to apply and test wikipedia API.
Output the webpage's title, summary, and URL based on user input webpage title.
"""
import wikipedia


def main():
    """Start program."""
    # Promote the user to enter the page title that will be searched
    title = input("Enter page title: ")
    while title != "":
        try:
            webpage = wikipedia.page(title, auto_suggest=False)
            # Display the webpage's title, summary, and URL
            print(webpage.title)
            print(webpage.summary)
            print(webpage.url)
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)
        title = input("Enter page title: ")


if __name__ == '__main__':
    main()
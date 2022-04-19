"""
Store the user's email addresses as keys, user's names as values
into a dictionary
"""
def main():
    """Start program"""
    email_to_name = {}
    user_email = input("Email: ")
    while user_email != "":
        user_name = get_name_from_email(user_email)
        confirm_name = str(input(f"Is your name {user_name}? (Y/n)"))
        if confirm_name.upper() != 'Y' and confirm_name != "":
            user_name = input("Name: ")
        email_to_name[user_email] = user_name
        user_email = input("Email: ")
    # Display the email to name dictionary
    print("")
    for key, value in email_to_name.items():
        print(f"{value} ({key})")


def get_name_from_email(email):
    """Get the user name based on user's email"""
    prefix = email.split('@')
    name_parts = prefix[0].split('.')
    name = " ".join(name_parts).title()
    return name


if __name__ == '__main__':
    main()

is_finished = False #a boolean value
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        # TODO: this line
        is_finished = True
    except ValueError:# TODO - add the exception you want to catch after except
        print("Please enter a valid integer.")
print("Valid result is:", result)
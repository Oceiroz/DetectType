

def get_input(input_message, input_type):
    while(True):
        raw_input = input(f"{input_message}\n")

        try:
            user_input = input_type(raw_input)
            break
        except ValueError:
            print("this is not a valid input")
    return user_input

while(True):
    word = get_input("please enter a string" , str)
    print(f"your data {word} is a {type(word)}\n")
    number = get_input("please enter a integer" , int)
    print(f"your data {number} is a {type(number)}\n")
    decimal = get_input("please enter a float" , float)
    print(f"your data {decimal} is a {type(decimal)}\n")
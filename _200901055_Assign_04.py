import threading
import time
input_string = ""

def input_function():
    global input_string
    try:
        input_string = input("Enter a string: ")
    except ValueError:
        input_string = ""
        print("Can't process on an empty string.")
        input_string = input("Enter a valied string: ")

def reverse_function():
    global input_string
    print()
    reverse = input_string[::-1]
    print("Reverse of input string: ", reverse)

def capitalize_function():
    global input_string
    print()
    print("Capitalizing input string: ", input_string.upper())

def shift_function():
    print()
    global input_string
    shifted_string = ""
    for letter in input_string:
        if letter == " ":
            shifted_string += " "
        shifted_string += chr(ord(letter) + 2)
    print("String after +2 character shifts: ", shifted_string)

if __name__ == "__main__":
    Input_Thread = threading.Thread(target=input_function)
    Input_Thread.start()
    Input_Thread.join()
    Reverse_Thread = threading.Thread(target=reverse_function)
    Capital_Thread = threading.Thread(target=capitalize_function)
    Shift_Thread = threading.Thread(target=shift_function)
    print("Enter 1 for reversing the string.")
    print("Enter 2 for capitalizing the string.")
    print("Enter 3 for shifting the string's charcter by +2.")
    print("Enter 4 for all at once.")
    opt = int(input("Enter the desired option: "))
    if (opt == 1):
        Reverse_Thread.start()
        Reverse_Thread.join()
    elif (opt == 2):
        Capital_Thread.start()
        Capital_Thread.join()
    elif (opt == 3):
        Shift_Thread.start()
        Shift_Thread.join()
    elif (opt == 4):
        Reverse_Thread.start()
        Reverse_Thread.join()
        Capital_Thread.start()
        Capital_Thread.join()
        Shift_Thread.start()
        Shift_Thread.join()
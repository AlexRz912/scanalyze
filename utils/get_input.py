import os

def get_input():
    os.system("cls" if os.name == "nt" else "clear")
    user_input = input()
    os.system("cls" if os.name == "nt" else "clear")
    return user_input

user_input = get_input()
start_green_charcode = "\033[92m"
end_green_charcode = "\033[0m"
print(start_green_charcode + user_input + end_green_charcode)
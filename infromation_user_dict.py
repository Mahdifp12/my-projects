from colorama.ansi import Fore
from colorama.initialise import init

info = input("What information do you want‌? ")
info = info.lower()

my_dict = {
    "name": "Mahdi",
    "age": 18
}

if info == "name":
    user_name = my_dict.pop("name", None)
    
    print(f"your information is : {user_name}")

elif info == "age":
    user_age = my_dict.pop("age", None)
    
    print(f"your information is : {user_age}")

else:
    init()
    print(Fore.RED + "Error Not found information")
from hmi import HMI
import os

def main():
    HMI.print_welcome_message()
    while True:
        user_choice = HMI.get_user_choice()
        match user_choice:
            case "P":
                HMI.print_location()
            case "C":
                HMI.copy_coordinates()
            case "E":
                os.system("cls" if os.name == "nt" else "clear")
                break
            case _:
                os.system("cls" if os.name == "nt" else "clear")
                print("Not a valid option. Try again.")
                print("")

if __name__ == "__main__":
    main()
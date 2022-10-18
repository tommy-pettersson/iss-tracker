import pyperclip
from data_manager import DataManager
import os

class HMI:

    def print_welcome_message():
        os.system("cls" if os.name == "nt" else "clear")
        print("Welcome to the ISS tracker.")
        print("What would you like to do?")
        print("")

    def get_user_choice():
        print("(P)rint current location.")
        print("(C)opy current coordinates to clipboard.")
        print("(E)xit program.")
        print("")
        user_choice = input("Select an option: ").upper()
        return user_choice
    
    def print_location():
        iss_data = DataManager.get_iss_location()
        os.system("cls" if os.name == "nt" else "clear")
        print(f"Time: {iss_data['time']}")
        print(f"Latitude: {iss_data['latitude']}")
        print(f"Longitude: {iss_data['longitude']}")
        print("")

    def copy_coordinates():
        iss_data = DataManager.get_iss_location()
        coordinates = f"{iss_data['latitude']} {iss_data['longitude']}"
        pyperclip.copy(coordinates)
        os.system("cls" if os.name == "nt" else "clear")
        print("Coordinates copied to clipboard.")
        print("")
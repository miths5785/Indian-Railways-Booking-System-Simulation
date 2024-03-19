# This Module has some Other Commonly used Functions

# Importing Required Modules

import os
import time


# Functions

def About():
    """
    About() -> Prints the About Information on the Terminal

    Parameters -> None
    """
    data = "Overview: It is a Railway Management system in which a user can book tickets, cancel reservations, check fares etc. It uses MySQL as the backend database.\n"
    print(data)
    subdata = "Book a Ticket: Users can book a ticket\nCancel a Booking: Users can cancel a booked ticket\nCheck Fares: Users can check fares before booking\nShow my Bookings: User can check their bookings\nShow Available Trains: Users can see the available trains\nClear Screen: Clears the terminal screen\nMenu: Shows the menu\nAbout: Prints the content of this file to the screen\nExit: Exit the program"
    print(subdata)

def ClearScreen():
    """
    ClearScreen() -> Clears the Terminal Screen

    Parameters -> None
    """

    print("Clearing..")
    time.sleep(3)
    os.system("cls")
    time.sleep(2)


def Menu():
    """
    Menu() -> Displays the Menu

    Parameters -> Answer (User's Choice on Displaying the Menu, by default it is set to True)
    """

    print("  WELCOME TO RAILWAY RESERVATION SYSTEM")
    print("1. Book a Ticket")
    print("2. Cancel a Booking")
    print("3. Check Fares")
    print("4. Show my Bookings")
    print("5. Show Available Trains")
    print("6. Clear Screen")
    print("7. Menu")
    print("8. About")
    print("9. Exit")
    
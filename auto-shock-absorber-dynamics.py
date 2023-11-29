"""
Automobile shock absorber dynamics
"""
import sys  # for sys.exit() - terminate program
import pickle  # for reading and writing files
import numpy as np
from matplotlib import pyplot as plt

# GLOBAL DICTIONARY -----------------------------------------------------------
records = {}


def main() -> None:
    """main function"""
    choice = main_menu()
    while choice != 5:
        if choice == 1:
            calc_choices = calc_menu()
            b = calc_choices[0]
            k = calc_choices[1]
            m = calc_choices[2]
            z = calc_choices[3]
            if z == 1:
                calc_critically_damped_system(b, k, m)
            elif z > 1:
                calc_over_damped_system(b, k, m, z)
            else:
                calc_under_damped_system(b, k, m, z)
        elif choice == 2:
            query_menu()
        elif choice == 3:
            load_file()
        elif choice == 4:
            dump_file()
        choice = main_menu()
    print("Bye")
    sys.exit(0)


# MENUS -----------------------------------------------------------------------
def main_menu() -> int:
    """displays the menu and returns the user's choice"""
    print("Automobile shock absorber dynamics")
    print("=================================")
    print("1. Calculate")
    print("2. Query")
    print("3. Upload file")
    print("4. Download file")
    print("5. Quit")
    print("=================================")
    choice  = input("Enter your choice (1..5): ", end="")

    while choice not in ["1", "2", "3", "4", "5"]:
        print(f"{choice} in not a valid choice")
        choice = input("Enter a valid choice (1..5): ", end="")

    return int(choice)


def calc_menu() -> tuple:
    """displays the calculation menu"""
    allowed = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
    print("Calculate")
    print("=========")
    print("Enter the values of the following parameters:")
    b = input("b (shock absorber): ")
    is_b_validated = False
    while not is_b_validated:
        for char in b:
            if char not in allowed:
                print("Invalid input")
                b = input("b (shock absorber): ")
            else:
                is_b_validated = True
                b = float(b)

    k = float(input("k (spring): "))
    is_k_validated = False
    while not is_k_validated:
        for char in k:
            if char not in allowed:
                print("Invalid input")
                k = input("k (spring): ")
            else:
                is_k_validated = True
                k = float(k)

    m = input("M (mass): ")
    is_m_validated = False
    while not is_m_validated:
        for char in m:
            if char not in allowed:
                print("Invalid input")
                m = input("M (mass): ")
            else:
                is_m_validated = True
                m = float(m)

    damping_coefficient = input("Damping coefficient: ")
    is_damping_coefficient_validated = False
    while not is_damping_coefficient_validated:
        for char in damping_coefficient:
            if char not in allowed:
                print("Invalid input")
                damping_coefficient = input("Damping coefficient: ")
            else:
                is_damping_coefficient_validated = True
                damping_coefficient = float(damping_coefficient)

    return (b, k, m, damping_coefficient)


def query_menu() -> None:
    """displays the query menu"""
    print("Query")
    print("=====")
    # TODO: implement


def load_file() -> None:
    """loads a file"""
    print("Upload file")
    print("===========")
    print("file must be in the same directory as this program")
    filename = input("Enter the filename: ")
    read_file(filename)


def dump_file() -> None:
    """dumps a file"""
    print("Download file")
    print("=============")

# CALCULATIONS ----------------------------------------------------------------
def calc_critically_damped_system(b: float, k: float, m: float) -> None:
    """calculates the critically damped system"""
    # TODO: implement


def calc_over_damped_system(b: float, k: float, m: float, z: float) -> None:
    """calculates the over damped system"""
    # TODO: implement

def calc_under_damped_system(b: float, k: float, m: float, z: float) -> None:
    """calculates the under damped system"""
    # TODO: implement

# PLOTTING --------------------------------------------------------------------
def plot() -> None:
    """plots the graph"""
    # TODO: implement

# I/O FUNCTIONS ---------------------------------------------------------------
def read_file(filename: str) -> None:
    """reads a file"""
    global records

    try:
        with open(filename, "rb") as file:
            records = pickle.load(file)
            print("file loaded")
    except FileNotFoundError:
        print("File not found")
        load_file()
    except Exception:
        print("Unexpected error:", sys.exc_info()[0])
        load_file()
    

def write_file() -> None:
    """writes a file"""
    # TODO: implement

# To start the program automatically
if __name__ == "__main__":
    main()

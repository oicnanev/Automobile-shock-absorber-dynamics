"""
Automobile shock absorber dynamics
"""
import sys  # for sys.exit() - terminate program
import pickle  # for reading and writing files
import math  # for math functions
import numpy as np
from matplotlib import pyplot as plt

# GLOBAL VARIABLES -----------------------------------------------------------
records = {}
number_of_records = 0


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
            t = calc_choices[4]
            if z == 1:
                x, y = calc_critically_damped_system(k, m, t)
                add_to_records(b, k, m, z, t, x, y)
                plot(x, y)
            elif z > 1:
                x, y = calc_over_damped_system(b, k, m, z, t)
                add_to_records(b, k, m, z, t, x, y)
                plot(x, y)
            else:
                Y = calc_under_damped_system(k, m, z, t)
                add_to_records(b, k, m, z, t, x, y)
                plot(x, y)
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

    k = input("k (spring): ")
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

    t = input("t (time in seconds): ")
    is_t_validated = False
    while not is_t_validated:
        for char in t:
            if char not in allowed:
                print("Invalid input")
                t = input("t (time in seconds): ")
            else:
                is_t_validated = True
                t = float(t)

    return (b, k, m, damping_coefficient, t)


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
def calc_critically_damped_system(k: float, m: float, t: float) -> tuple:
    """calculates the critically damped system
    y = 1 / Ma**2 * (1 - at - e**(-at))
    a = w = sqrt(k / m)"""
    a = math.sqrt(k / m)
    y = []
    double_time = 2 * t
    x = int(double_time / .001) # number of iterations
    for i in range(x):
        y.append(1 / (m * a**2) * (1 - a * i - math.e**(-a * i)))

    return (x, y)


def calc_over_damped_system(b: float, k: float, m: float, z: float, t: float) -> tuple:
    """calculates the over damped system
    y = 1 / Mba (1 + (1 / (a-b)) (be**-at - ae**-bt))
    a = zw + w * sqrt(z**2 - 1)
    b = zw - w * sqrt(z**2 - 1)
    w = sqrt(k / m)"""
    w = math.sqrt(k / m)
    a = z * w + w * math.sqrt(z**2 - 1)
    b = z * w - w * math.sqrt(z**2 - 1)
    y = []
    double_time = 2 * t
    x = int(double_time / .001) # number of iterations
    for i in range(x):
        y.append(1 / (m * b * a) * (1 + (1 / (a - b)) * (b * math.e**(-a * i) - a * math.e**(-b * i))))

    return (x, y)


def calc_under_damped_system(k: float, m: float, z: float, t: float) -> tuple:
    """calculates the under damped system
    y = 1 / K (1 - (1 / (sqrt(1-z**2))) e**(-zwt) sin(w sqrt(1 - z**2) t + phi)))
    phi = tan**-1 (sqrt(1 - z**2)) / z"""
    phi = math.atan(math.sqrt(1 - z**2) / z)
    w = math.sqrt(k / m)
    y = []
    double_time = 2 * t
    x = int(double_time / .001) # number of iterations
    for i in range(x):
        y.append(1 / k * (1 - (1 / (math.sqrt(1 - z**2))) * math.e**(-z * w * i) * math.sin(w * math.sqrt(1 - z**2) * i + phi)))

    return (x, y)


# PLOTTING --------------------------------------------------------------------
def plot(x: int, y: float) -> None:
    """plots the graph"""
    scale_x = np.arange(0, x, .001)
    scale_y = np.arange(0, y, .001)
    plt.plot(scale_x, scale_y, y)

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
    global records

    try:
        with open("records", "wb") as file:
            pickle.dump(records, file)
            print("file dumped")
    except Exception:
        print("Unexpected error:", sys.exc_info()[0])
        dump_file()


def add_to_records(b: float, k: float, m: float, z: float, t: float, x: int, y: float) -> None:
    """updates the records"""
    global records
    number_of_records += 1
    records[number_of_records] = (b, k, m, z, t, x, y)


# To start the program automatically
if __name__ == "__main__":
    main()

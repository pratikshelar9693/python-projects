# project Name:- Car Registration System

car_list = []

def register_car():

    reg_no = input("Enter Car Registration Number: ")
    model = input("Enter Car Model:- ")
    owner = input("Enter Owner Name:- ")
    car = {
        'Reg No': reg_no,
        'Model': model,
        'Owner': owner
    }
    car_list.append(car)
    print(" Car Registered Successfully!\n")


def show_all_cars():
    if not car_list:
        print(" No cars registered yet.\n")
        return
    print(" Registered Cars:")
    for i, car in enumerate(car_list, start=1):
        print(f"{i}. Reg No: {car['Reg No']}, Model: {car['Model']}, Owner: {car['Owner']}")
    print()


def search_by_model():
    model_search = input("Enter model name to search: ")
    found = False
    for car in car_list:
        if car['Model'].lower() == model_search.lower():
            print(f" Found - Reg No: {car['Reg No']}, Owner: {car['Owner']}")
            found = True
    if not found:
        print(" No car found with that model.\n")


def exit_system():
    print(" Exiting... Thank you for using Car Registration System.")
    exit()

def menu():
    while True:
        print("\n====== Car Registration System ======")
        print("1. Register a New Car")
        print("2. Show All Registered Cars")
        print("3. Search Car by Model")
        print("4. Exit")
        choice = input("Enter your choice (1-4):- ")

        if choice == '1':
            register_car()
        elif choice == '2':
            show_all_cars()
        elif choice == '3':
            search_by_model()
        elif choice == '4':
            exit_system()
        else:
            print(" Invalid choice. Please enter between 1 and 4.\n")


menu()




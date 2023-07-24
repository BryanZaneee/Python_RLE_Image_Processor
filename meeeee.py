from console_gfx import ConsoleGfx

# Displays the menu for the user, showcasing all the options
def display_menu():
    print("RLE Menu")
    print("--------")
    print("0. Exit")
    print("1. Load File")
    print("2. Load Test Image")
    print("3. Read RLE String")
    print("4. Read RLE Hex String")
    print("5. Read Data Hex String")
    print("6. Display Image")
    print("7. Display RLE String")
    print("8. Display Hex RLE Data")
    print("9. Display Hex Flat Data\n")


# Complete
def load_file():
    filename = input("Enter name of file to load: ").strip()
    image_data = ConsoleGfx.load_file(filename)
    print("Image data loaded.\n")
    return image_data

# ... rest of the code

# Must code all 8 methods into main()
def main():
    image_data = None
    print("Welcome to the RLE image encoder!\n")
    print("Displaying Spectrum Image:")
    ConsoleGfx.display_image(ConsoleGfx.test_rainbow)
    print("\n")
    # loops until user quits out of program
    while True:
        display_menu()
        choice = input("Select a Menu Option: ").strip()
        # Handles each option, incorporating each method into main()
        if choice == '1':
            image_data = load_file()

        # ... rest of the code

if __name__ == '__main__':
    main()

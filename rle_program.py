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
    filename = input("Enter name of file to load: ")
    image_data = ConsoleGfx.load_file(filename)
    print("Image data loaded.\n")
    return image_data


# Complete!
def load_test_image():
    image_data = ConsoleGfx.test_image
    print("Test image data loaded.\n")
    return image_data


# Need to remove leading zeros appearing in the output, conversion looks good otherwise
def to_hex_string(data):
    hex_str = ""
    for val in data:
        hex_str += format(val, 'x')
    return hex_str


# Complete!
def count_runs(rle_list):
    count = 0
    current = None
    for i in rle_list:
        if i != current:
            current = i
            count += 1
    return count


# Complete !
def encode_rle(flat_data):
    encoded_data = []  # Initialize an empty list to hold the encoded data
    current_value = flat_data[0]  # Set the current value to the first element of the input data
    count = 0  # Initialize a counter for the number of consecutive values

    # Iterate over each value in the input data
    for value in flat_data:
        # If the current value is the same as the previous value, increment the counter
        if value == current_value:
            count += 1
            # If count reaches 15, append the current count and value to encoded data,
            # start a new run plus reset the counter
            if count == 15:
                encoded_data.append(count)
                encoded_data.append(current_value)
                count = 0
        else:
            # If the current value is different from the previous value, append the previous count and value to
            # the encoded data, and update the current value and counter accordingly
            encoded_data.append(count)
            encoded_data.append(current_value)
            current_value = value
            count = 1

    # Append the final count and value to the encoded data before returning it
    encoded_data.append(count)
    encoded_data.append(current_value)

    # Return the encoded data list
    return encoded_data


# Complete!
def get_decoded_length(rle_data):
    decoded_length = 0
    for i in range(0, len(rle_data), 2):
        decoded_length += rle_data[i]
    return decoded_length


# Complete!
def decode_rle(rle_data):
    # Create an empty list to store the decoded data
    decoded_data = []

    # Iterate through the RLE data list, jumping forward by 2 each time
    for i in range(0, len(rle_data), 2):
        # Extract the run length and pixel value for the current run
        run_length = rle_data[i]
        pixel_value = rle_data[i + 1]

        # Add the pixel value to the decoded data list run_length times
        for j in range(run_length):
            decoded_data.append(pixel_value)

    # Return the decoded data list
    return decoded_data


# Complete!
def string_to_data(data_string):
    data_list = []
    # Iterate through each pair of characters in the string
    for i in range(0, len(data_string), 2):
        # Extract the pair of characters representing a hex value
        hex_val = data_string[i:i + 2]
        # Determine the count of the RLE data
        if hex_val[0].isdigit():
            count = int(hex_val[0])
        else:
            count = ord(hex_val[0]) - ord('a') + 10
        # Determine the value of the RLE data
        if hex_val[1].isdigit():
            value = int(hex_val[1])
        else:
            value = ord(hex_val[1]) - ord('a') + 10
        # Add the value to the RLE data list count number of times
        data_list.extend([value] * count)

    # Compress the RLE data
    compressed_list = []
    current_value = None
    current_count = 0
    # Iterate through each value in the RLE data list
    for value in data_list:
        # If this value is different from the previous value
        if value != current_value:
            # If there was a previous value, append its count and value to the compressed list
            if current_value is not None:
                compressed_list.append(current_count)
                compressed_list.append(current_value)
            # Start a new sequence with the current value
            current_value = value
            current_count = 1
        else:
            # If this value is the same as the previous value, increment the count
            current_count += 1
    # Append the final sequence to the compressed list
    if current_value is not None:
        compressed_list.append(current_count)
        compressed_list.append(current_value)

    # Return the compressed list of RLE data
    return compressed_list


# Seems to work correctly!
def to_rle_string(rle_data):
    result = []
    i = 0
    while i < len(rle_data):
        length = rle_data[i]
        value = rle_data[i + 1]
        # Find way to decode value into string
        result.append(f"{length:d}{value:x}")
        i += 2
    return ":".join(result)


# Seems to work okay!
def string_to_rle(rle_string):
    rle_data = []
    # Need to split data by delimiters
    for run in rle_string.split(":"):
        length = int(run[:-1])
        value = int(run[-1], 16)
        rle_data.extend([length, value])
    return rle_data


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
        choice = input("Select a Menu Option: ")
        # Handles each option, incorporating each method into main()
        if choice == '1':
            image_data = load_file()

        elif choice == "2":
            print("Test image data loaded.\n")
            image_data = ConsoleGfx.test_image

        elif choice == "3":
            rle_string = input("Enter an RLE string to be decoded: ")
            rle_data = string_to_rle(rle_string)
            image_data = decode_rle(rle_data)
            print('')

        elif choice == "4":
            rle_hex_string = input("Enter the hex string holding RLE data: ")
            rle_data = string_to_data(rle_hex_string)
            image_data = decode_rle(rle_data)

        elif choice == "5":
            flat_hex_string = input("Enter the hex string holding flat data: ")
            image_data = string_to_data(flat_hex_string)

        elif choice == "6":
            print("Displaying image...")
            ConsoleGfx.display_image(image_data)
            print('')

        elif choice == "7":
            rle_string = to_rle_string(encode_rle(image_data))
            print("RLE representation:", rle_string)

        elif choice == "8":
            rle_hex_string = to_hex_string(encode_rle(image_data))
            print("RLE hex values:", rle_hex_string)

        elif choice == "9":
            flat_hex_string = to_hex_string(image_data)
            print("Flat hexadecimal data:", flat_hex_string)
            print('')

        elif choice == '0':
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == '__main__':
    main()

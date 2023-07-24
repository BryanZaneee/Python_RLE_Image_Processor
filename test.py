import rle_program


# Test for 1. to_hex_string
print("1.Test for to_hex_string")
print("3f64")
print("Matching output:")
data = [3, 15, 6, 4]
hex_string = rle_program.to_hex_string(data)
print(f"{hex_string}\n")


# Test for 2. count_runs(flat_data)
print("2.Test for count_runs")
print("2")
print("Matching output:")
flat_data = [15, 15, 15, 4, 4, 4, 4, 4, 4]
num_runs = rle_program.count_runs(flat_data)
print(f"{num_runs}\n")


# Test for 3. encode_RLE
print("3.Test for encode RLE")
print("[2,4,15,1,15,1,5,1,1,8,1,7]")
print("Matching output:")
flat_data = [4,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,8,7]
encoded_data = rle_program.encode_rle(flat_data)
print(f"{encoded_data}\n")


#  Test for 4. get_decoded_length
print("4.Test for get_decoded_length")
print("[3, 15, 6, 4]")
print("Matching output: ")
encoded_data = [3, 15, 6, 4]
decoded_length = rle_program.get_decoded_length(encoded_data)
print(f"{decoded_length}\n")
print("Test 2")
print("[3, 15, 6, 4, 5, 424, 1, 44, 9, 4]")
encoded_data = [3, 15, 6, 4, 5, 424, 1, 44, 9, 4]
decoded_length = rle_program.get_decoded_length(encoded_data)
print(f"{decoded_length}\n")


# Test for 5. decode_RLE
print("5.Test for decode_RLE")
print(" [15, 15, 15, 4, 4, 4, 4, 4, 4]")
print("Matching output: ")
encoded_data = [3, 15, 6, 4]
decoded_length = rle_program.decode_rle(encoded_data)
print(f"{decoded_length}\n")


# Test for 6. string_to_data
print("6.Test for string_to_data")
print("[3, 15, 6, 4]")
print("Matching output: ")
data_string = "3f64"
data = rle_program.string_to_data(data_string)
print(f"{data}\n")


# Test for 7. to_rle_string
print("6.Test for to_rle_string")
print("15f:64")
print("Matching output: ")
rle_string = [15, 15, 6, 4, 15, 11, 5, 4, 6, 15, 14, 12]
result = rle_program.to_rle_string(rle_string)
print(f"{result}\n")


# Test for 8. string_to_rle
print("6.Test for string_to_rle")
print([15, 15, 6, 4])
print("Matching output: ")
rle_string = "3c:20:7d:2b:2b:8a:1b:1c"
result = rle_program.string_to_rle(rle_string)
print(f"{result}\n")
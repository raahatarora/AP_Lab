# Define the list of powers of 2
powers_of_2 = [2**i for i in range(10)]  # This generates [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

target = 2**5 
found_flag = False
index = 0

while index < len(powers_of_2) and not found_flag:
    if powers_of_2[index] == target:
        found_flag = True
    else:
        index += 1
        
if found_flag:
    print(f"The value {target} was found at index {index}.")
else:
    print(f"The value {target} was not found in the list.")

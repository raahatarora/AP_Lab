def tuple_to_succeeding_list(input_tuple):
    
    succeeding_list = []
    
    # Iterate through the tuple except for the last element
    for i in range(len(input_tuple) - 1):
        # Append the succeeding element to the list
        succeeding_list.append(input_tuple[i + 1])
    
    return succeeding_list

def main():
    # Example tuple
    example_tuple = (10, 20, 30, 40, 50)
    
    # Convert the tuple to the list of succeeding elements
    result_list = tuple_to_succeeding_list(example_tuple)
    
    # Print the result
    print(f"Original tuple: {example_tuple}")
    print(f"List of succeeding elements: {result_list}")

if __name__ == "__main__":
    main()

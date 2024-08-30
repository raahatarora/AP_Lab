from itertools import product

def sum_of_combinations(tuple_list):
    # Ensure that there is at least one tuple in the list
    if not tuple_list:
        return 0

    # Generate all possible combinations of elements from the tuples
    combinations = product(*tuple_list)
    
    # Calculate the summation of each combination
    total_sum = 0
    for combination in combinations:
        total_sum += sum(combination)
    
    return total_sum

# Example usage
tuple_list = [(1, 2), (3, 4), (5, 6)]
result = sum_of_combinations(tuple_list)
print(f"The summation of all possible combinations is: {result}")

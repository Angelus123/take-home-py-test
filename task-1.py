# Create a function that takes in two parameters, a list of numbers and a target number, and returns the two numbers in the list that add up to the target number.

def find_sum_pair(numbers, target):
  
    # Create a dictionary to store the complement of each number
    complements = {}

    # Iterate through the list of numbers
    for num in numbers:
        # Check if the complement of the current number has been seen before
        if target - num in complements:
            # If so, return the pair of numbers
            return (num, target - num)
        else:
            # Otherwise, store the complement of the current number in the dictionary
            complements[num] = target - num

    # If no pair  in the list that add up to the target number is found, return None
    return None
print(find_sum_pair([1,2,4,5,], 3))  # prints (1,2)
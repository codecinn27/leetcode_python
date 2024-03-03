def two_sum(nums, target):
    # Create a dictionary to store the indices of numbers
    num_indices = {}
    
    # Iterate through the array
    for i, num in enumerate(nums):
        # Calculate the complement (target - num)
        complement = target - num
        
        # Check if the complement exists in the dictionary
        if complement in num_indices:
            # If found, return the indices of the two numbers
            return [num_indices[complement], i]
        
        # If not found, store the index of the current number
        num_indices[num] = i
        print(f'{i} : {num}')
    
    # If no solution is found, return an empty list
    return []
# Example usage:
nums = [2, 7, 11, 15]
target = 13
print(two_sum(nums, target))

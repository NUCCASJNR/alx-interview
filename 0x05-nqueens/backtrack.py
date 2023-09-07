def generate_subsets(nums):
    def backtrack(start, path):
        # Add the current subset to the result
        subsets.append(path[:])

        # Explore all possible choices for the next element in the subset
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()  # Backtrack by removing the last element

    subsets = []
    backtrack(0, [])
    return subsets


# Example usage:
nums = [1, 2, 5, 9]
result = generate_subsets(nums)
print(result)

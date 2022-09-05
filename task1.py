def get_aspected_index(two_pair_values, target_value):
    index = None
    # indexs = []
    
    for n, values in enumerate(two_pair_values):
        if sum(values) == target_value:
            index = n
            # indexs.append(n)
        
    # return index, indexs
    return index

two_pair_values = [
    [1, 5],
    [9, -7],
    [0, 8],
    [6, 3],
    [4, 11],
    [14, 0],
    [8, 1],
    [4, 9],
]

target_value = 9
result = get_aspected_index(two_pair_values, target_value)

print(result)

# Note
# There is two index's where sum of their two pair values is
# equal to target value
# Index 3 and Index 6
# But comment in problem description described to return
# the last index which's sum is equal to target value
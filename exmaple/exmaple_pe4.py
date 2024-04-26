sequence = input("Enter a sequence of integers seperated by white space: ")
sequence = sequence.split(" ")
sequence = [int(x) for x in sequence]

temp_LICS = [sequence[0]]  # Longest Increasing Subsequence for temporary use
LICS = []  # Longest Increasing Subsequence

for element in sequence[1:]:
    if element > temp_LICS[-1]:
        temp_LICS.append(element)
    else:
        # compare the length of the current LICS with the temp_LICS
        LICS = max(LICS, temp_LICS, key=len)
        # reset the temp_LICS
        temp_LICS = [element]

# compare the length of the current LICS with the temp_LICS
LICS = max(LICS, temp_LICS, key=len)

print("Length: ", len(LICS))
print("LICS: ", LICS)

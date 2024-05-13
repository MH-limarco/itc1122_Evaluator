def print_array(array):
    print('\n'.join([' '.join(line) for line in array]))

_input = ''
shape = int(input("Enter the grid: "))
array = [['_']*shape for i in range(shape)]

print_array(array)
while _input.lower() != 'done':
    _input = input("Enter the coord: ")
    if _input != 'done':
        value = input("Enter the value: ")

        row, col = [int(i) for i in _input.split(',')][:2]
        array[row][col] = value
        print_array(array)





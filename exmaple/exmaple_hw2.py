#Problem 1‐1. Given the initial statements:
s1 = "spam"
s2 = "ni!"

#1_a
print("The Knights who say," + s2)
#1_b
print(3 * s1 + 2 * s2)
#1_c
print(s1[1])
#1_d
print(s1[1:3])
#1_e
print(s1[2] + s2[:2])
#1_f
print(s1 + s2[-1])
#1_g
print(s2[len(s2)//2])

#2_a
print(s2.upper())
#2_b
print(f"{s2+s1+s2}")
#2_c
print(f"{(s1.title()+s2.title()+' ')*3}")
#2_d
print(f"{s1[:-1]+s2[0]}")
#2_e
print(f"{s1.replace('a','')}")

#3_a
print("Looks like %s and %s for breakfast" % ("spam", "eggs") )
#3_b
print("There is %d %s %d %s" % (1, "spam", 4, "you"))
#3_c
print("Hello %s %s" % ("Suzie", "Programmer") )  #there are one "%" only, you need two
#3_d
print("%0.2f %0.2f" % (2.3, 2.3468))
#3_e
print("%7.5f %7.5f" % (2.3, 2.3468))
#3_f
print("Time left %02d:%05.2f" % (1, 37.374))
#3_g
print("%3d" % (14) ) # %d need int/float, there are str


#1-6
#4 is True
state = [None, None, None, True]
talks = ["state[0] in [False, None]",
         "state[2] in [True, None]",
         "state[3] in [True, None]",
         "state[3] in [False, None]"]

true_count = 0
for talk in talks:
    if eval(talk):
        true_count += 1
        talk = talk.split(' ')
        target = talk[0]
        bool_ = talk[2][1:-1]
        exec(f"{target} = {bool_}")
    if true_count >= len(talks)-1:
        break

state = [idx + 1  for idx, i in enumerate(state[:]) if i == True]
print(f"The true thief is {state[0]}.")

#hw2_p2
def find_perfect_numbers(end):
    perfect_numbers = []
    for num in range(1, int(end) + 1):
        divisors_sum = sum([div for div in range(1, num) if num % div == 0])
        if divisors_sum == num:
            perfect_numbers.append(num)
    print("Perfect numbers:")
    for i in perfect_numbers:
        print(i)

find_perfect_numbers(input("Input the range number: "))

#hw2_p3
def is_leap_year(year):
    """Check if a year is a leap year."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_day_of_week(year, month, day):
    """Calculate day of the week for a given date using Zeller's Congruence."""
    if month < 3:
        month += 12
        year -= 1
    q = day
    m = month
    K = year % 100
    J = year // 100
    f = q + ((13 * (m + 1)) // 5) + K + (K // 4) + (J // 4) + 5 * J
    return f % 7


def print_calendar(year, month):
    """Print the calendar for a specific month and year."""
    # Days in each month
    days_in_month = [31, 28 + is_leap_year(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Weekday of the first day of the month
    first_day_weekday = get_day_of_week(year, month, 1)

    # Adjusting the first day of the week to match the convention
    first_day_weekday = (first_day_weekday+6) % 7

    # Calendar header
    print("Sun Mon Tue Wed Thu Fri Sat")

    # Initial spacing for the first week
    print("    " * first_day_weekday, end="")

    # Printing the days
    for day in range(1, days_in_month[month - 1] + 1):
        print(f"{day:02} ", end=" ")
        first_day_weekday = (first_day_weekday + 1) % 7
        if first_day_weekday == 0:  # Start a new line after Sunday
            print()
    print()

year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))
print_calendar(year, month)

#hw2_p4
def print_triangle(side_length, cent_idx):
    """Prints a single triangle layer for the Christmas tree."""
    for i in range(2, side_length):
        print(("#" + "@" * (2 * i - 3) + "#" if i > 1 else "#").center(cent_idx,' '))
    print(("#" * (2 * side_length-1)).center(cent_idx, ' '))


def print_tree(layers, top_triangle_side, growth_layers, trunk_width, trunk_height):
    # Adjust the top triangle
    cent_idx = (top_triangle_side + (layers-1) * growth_layers) * 2

    print("#".center(cent_idx, ' '))
    print_triangle(top_triangle_side, cent_idx)

    # Generate each layer of the tree, with the side length increasing as specified
    current_side_length = top_triangle_side
    for _ in range(1, layers):
        current_side_length += growth_layers  # Increase side length for the next layer
        print_triangle(current_side_length, cent_idx)

    for _ in range(trunk_height):
        print(("|" * trunk_width).center(cent_idx, ' '))

layers = int(input("Enter the number of layers (2 to 5) = "))
top_triangle_side = int(input("Enter the side length of the top layer = "))
growth_layers = int(input("Enter the growth of each layer = "))
trunk_width = int(input("Enter the trunk width (odd number, 3 to 9) = "))
trunk_height = int(input("Enter the trunk height (odd number, 4 to 10) = "))
print_tree(layers=layers,
           top_triangle_side=top_triangle_side,growth_layers=growth_layers,
           trunk_width=trunk_width, trunk_height=trunk_height)

#hw2_p5_1
def fibonacci_sequence(n):
    fib_sequence = [0, 1]  # Initialize the sequence with the first two terms
    # Generate subsequent terms using the sum of the previous two terms
    for i in range(2, n + 1):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])

    return fib_sequence[-1]

n = int(input("Input an integer number: "))
print(f"The {n}-th Fibonacci sequence : {fibonacci_sequence(n)}")

#hw2_p5_2
def longest_palindromic_substring(s):
    if len(s) < 2:
        return s

    start = 0
    max_length = 0
    for i in range(len(s)):
        # Find longest palindrome with odd length
        left, right = i, i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > max_length:
                start = left
                max_length = right - left + 1
            left -= 1
            right += 1

        # Find longest palindrome with even length
        left, right = i, i + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > max_length:
                start = left
                max_length = right - left + 1
            left -= 1
            right += 1

    return s[start:start + max_length], max_length

st1 = input("Enter a string: ")
substring, lenght = longest_palindromic_substring(st1)
print(f"Longest palindrome substring is: {substring}")
print(f"Lenght is: {lenght}")

#hw2_p5_3
def casesar_encode(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + key) % 26 + ord('a'))
            else:
                encrypted_text += chr((ord(char) - ord('A') + key) % 26 + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

def affine_encode(text, key1, key2):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            encrypted_text += chr((((ord(char) * key1 + key2) - ord('A')) ) % 26 + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

def Message_Encryption():
    n = int(input("The number of the requested element in  Fibonacci (n) = "))
    t1 = input("Trhe first string for Palindromic detection (s1) = ")
    t2 = input("Trhe second string for Palindromic detection (s2) = ")
    encrypted = input("Trhe plaintext to be encrypted: ")

    print('----- extract key for encypt method -----')

    fibonacci_key = fibonacci_sequence(n)
    print(f"The {n}-th Fibonacci sequence number is: {fibonacci_key}")

    substring1, lenght1 = longest_palindromic_substring(t1)
    print(f"Longest palindrome substring is: {substring1}")
    print(f"Lenght is: {lenght1}")

    substring2, lenght2 = longest_palindromic_substring(t2)
    print(f"Longest palindrome substring is: {substring2}")
    print(f"Lenght is: {lenght2}")
    print('----- encryption completed -----')

    casesar_text = casesar_encode(encrypted, fibonacci_key)
    affine_text = affine_encode(casesar_text, lenght1, lenght2)
    return  affine_text
print(f"The encrypted text is: {Message_Encryption()}")











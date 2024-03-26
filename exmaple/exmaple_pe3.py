def main():
    start = True
    print('Welcome to the simple calendar program!')
    while start:
        first_ = float(input('Enter the first number: '))
        second_ = float(input('Enter the second number: '))
        operation = input('Select an arithmetic operation (+, -, *, /): ')
        try:
            print(f'Result: {eval(f"{first_} {operation} {second_}")}')

        except ZeroDivisionError:
            print('Error: Division by zero')

        continue_ = input('Do you want to perform another calculation? (yes or no): ')

        if continue_ != 'yes':
            print('Goodbye!')
            start = False

main()
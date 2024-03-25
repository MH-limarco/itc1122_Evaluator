##setting dir
discount_dir = {'Regular': [0.1, 0.15, 0.2],
                'Gold': [0.15, 0.2, 0.25]}

##input
amount = float(input("Enter the shopping amount: "))
level = input("Enter the membership level (Regular or Gold): ")

'''
test1
test2
test3
'''

"""1235
test4
test5test6

"""


##check membership level
if level not in discount_dir.keys():
    print("Invalid membership level. Please enter 'Regular' or 'Gold'.")

##if ture membership level
else:
    disount_ls = discount_dir[level]

    # check -> 3000 -> 2000 -> 1000
    if amount >= 3000:
        amount = amount * (1 - disount_ls[2])
    elif amount >= 2000:
        amount = amount * (1 - disount_ls[1])
    elif amount >= 1000:
        amount = amount * (1 - disount_ls[0])

    # print output
    print(f"{level} ${amount}")
    #print(amount)












## Input: Richter scale
Richter = float(input("Please input a Richter scale value: ")) #Please input a Richter scale value:

## energy = 10 ^((1.5 * Richter) + 4.8)
Joules = 10 ** ((1.5 * Richter) + 4.8)

## energy / (4.184 * 10 ^(9))
TNT = Joules / (4.184 * 10 ** 9)

## energy / 2930200
lunches = Joules / 2930200


## output: Richter scale
print(f"Richter scale value: {Richter}")
#print(Richter)

## output: Joules
print(f"Equivalence in Joules: {Joules:.5f}")

## output: tons of TNT
print(f"Equivalence in tons of TNT: {TNT:.5f} ")

## output: number of nutritious lunches
print(f"Equivalence in the number of nutritious lunches: {lunches:.5f}")
numbers = []                        # create a list
for number in range(1, 101):
    numbers.append(number)            # append 100 numbers to list

print("The numbers are as following: ")
print("\n")
print(numbers)
for i in range(4):
	print("\n")


def multiple_of_three(list_with_numbers):   # regular function
    multiples = []                          # create a list

    for number in list_with_numbers:
        if number % 3 == 0:                 # multiple of 3?
            multiples.append(number)        # append to list

    return multiples                        # return list


threes = multiple_of_three(numbers)         # pass numbers list into function
print(threes)
for i in range(4):
	print("\n")



def generator_multiple_of_three(list_with_numbers):         # generator
    for number in list_with_numbers:
        if number % 3 == 0:
            yield number


gen_threes = generator_multiple_of_three(numbers)
print(gen_threes)                                           # <generator object generator_multiple_of_three at >
for i in range(4):
	print("\n")


gen_threes = tuple(generator_multiple_of_three(numbers))     # cast generator to list
print(gen_threes)                                           # returns the multiples of 3 list
for i in range(4):
	print("\n")



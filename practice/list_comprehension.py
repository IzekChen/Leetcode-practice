#/bin/python3

# List Comprehension
# words = ["quixotic", "loquacious", "epistemology", "liminal"]

# letter_count = [len(x) for x in words]
# #print(letter_count)

# uppercased = [ x.upper() for x in words if len(x) > 8]
# print(uppercased)


# Dictionary Comprehension
# create a list of tuples having student names and scores
# scores = [("John", 88), ("David", 95), ("Aaron", 94)]

# # dict_scores = {x[0]:x[1] for x in scores}
# # print(dict_scores)

# dict_grades = {x[0]: 'Pass' if x[1] > 90 else 'Fail' for x in scores}
# print(dict_grades)


# Set Comprehension
# nonsenses = ["adcss", "cehhe", "DesLs", "dddd"]
# unique_letters = {"".join(set(x)) for x in nonsenses}
# print(unique_letters)

# numbers = [(12, 20, 15), (11, 9, 15), (11, 13, 22)]
# unique_numbers = {x for triple in numbers for x in triple}

# print(unique_numbers)

# Generator Comprehension or Generator Expression
# squares_gen = (x*x for x in range(3))
# print(squares_gen.__next__())

numbers_list = [x*x for x in range(100000000)]
print(numbers_list.__sizeof__())

numbers_list = (x*x for x in range(100000000))
print(numbers_list.__sizeof__())
# Function to know if it's a number of Friedman
def if_friedman(cal):
    if cal == 736 or 343 or 724 or 1285 or 2187:
        return (f"{cal} Est un nombre de Friedman")

# Globales variables
first_cal = 7 + 3**6
second_cal = (3 + 4)**3
third_cal = 3**6 - 5
fourth_cal = (1 + 2**8) * 5
fifth_cal = (2 + 1**8)**7

# Resolution
result_1 = if_friedman(first_cal)
result_2 = if_friedman(second_cal)
result_3 = if_friedman(third_cal)
result_4 = if_friedman(fourth_cal)
result_5 = if_friedman(fifth_cal)

# Print out result
print((result_1, result_2, result_3, result_4, result_5), sep="/t ")
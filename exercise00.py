# Function to know if it's a number of Friedman
def if_friedman(cal_1, cal_2, cal_3, cal_4, cal_5):
    if cal_1 or cal_2 or cal_3 or cal_4 or cal_5 == 736 or 343 or 724 or 1285 or 2187:
        print(f"{cal} Est un nombre de Friedman")

# Globales variables
first_cal = 7 + 3**6
second_cal = (3 + 4)**3
third_cal = 3**6 - 5
fourth_cal = (1 + 2**8) * 5
fifth_cal = (2 + 1**8)**7

# Resolution
if_friedman(first_cal)
if_friedman(second_cal)
if_friedman(third_cal)
if_friedman(fourth_cal)
if_friedman(fifth_cal)

# Print out result
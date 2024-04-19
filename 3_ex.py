income = float(input())
citizen_num = 0
income_sum = 0
while income != 0:
    citizen_num += 1
    income_sum += income
    income = float(input())
if income_sum/citizen_num != 0:
    print(income_sum/citizen_num)
else:
    print(0)

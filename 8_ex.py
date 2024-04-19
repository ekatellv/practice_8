str_num = '1'
sum_num = 0
num = 1
while num <= 9:
   sum_num = int(str_num) * 8 + num
   print(f'{str_num} * 8 + {num} = {sum_num}')
   num += 1
   str_num += str(num)
print()

str_num = '1'
sum_num = 0
num = 2
while num <= 10:
   sum_num = int(str_num) * 9 + num
   print(f'{str_num} * 9 + {num} = {sum_num}')
   str_num += str(num)
   num += 1
print()

str_num = '1'
sum_num = 0
while len(str_num) <= 9:
   sum_num = int(str_num) ** 2
   print(f'{str_num} * {str_num}  = {sum_num}')
   str_num += '1'
print()

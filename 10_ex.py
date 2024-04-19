N = int(input())
start_num = 2
sum_div = []
perfect_count = 0
while start_num <= N:
    for i in range(1,start_num):
        if start_num % i == 0:
            sum_div.append(i)
    if sum(sum_div) == start_num:
        print(start_num)
    start_num += 1
    sum_div.clear()

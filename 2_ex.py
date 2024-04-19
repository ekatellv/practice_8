result = int(input())
max_result = result
friends_num = 0
while result != -1:
    friends_num += 1
    if result > max_result:
        max_result = result
    result = int(input())
print(friends_num)

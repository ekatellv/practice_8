result = int(input())
max_result = result
while result != -1:
    if result > max_result:
        max_result = result
    result = int(input())
print(max_result)

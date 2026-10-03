n = int(input())
list1 = list(map(int, input().split()))

m = int(input())
list2 = list(map(int, input().split()))

result = []
used = set()

for number in list1 + list2:
    if number not in used:
        used.add(number)
        result.append(number)

print(*result)

n = int(input())
tokens = input().split()
values = []

for token in tokens:
    if token == 'True':
        values.append(1.0)
    elif token == 'False':
        values.append(0.0)
    else:
        values.append(float(token))

total = sum(values)
average = total / n
print(f'{total:g} {average:.6f}')

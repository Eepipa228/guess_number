def format_name(last, first, middle=None):
    if middle is not None:
        return f'{last} {first[0]}.{middle[0]}.'
    return f'{last} {first}'

m = int(input())
for _ in range(m):
    parts = input().split()
    if len(parts) == 3:
        last, first, middle = parts
        print(format_name(last, first, middle))
    else:
        last, first = parts
        print(format_name(last, first))


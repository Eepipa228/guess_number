s = input()
i, j = map(int, input().split())
result = s[:i] + s[i:j][::-1] + s[j:]
print(result)

n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
ans = 0

for i in range(n):
	if i + 1 <= a[i]:
		ans = i + 1
	else:
	    break

print(ans)
def euler2(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return euler2(n - 1) + euler2(n - 2)


sumeuler = 0
i = 1
while True:
    if euler2(i) < 1000000000000:
        if euler2(i) % 2 == 0:
            sumeuler += euler2(i)
        i += 1
    else:
        break
print(sumeuler)
for i in range(1, 20):
    print(euler2(i))

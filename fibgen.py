n1, n2 = 0, 1
count = 0
for i in range(101):
    while count < i:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
        nums = [i % n1 != 0 ]
        print(nums)
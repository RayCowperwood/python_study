import time

start = time.time()

for a in range(3, 150):
    a5 = a ** 5
    for b in range(a, 150):
        b5 = b ** 5
        for c in range(b, 150):
            c5 = c ** 5
            for d in range(c, 150):
                d5 = d ** 5
                sum_ = a5 + b5 + c5 + d5
                for e in range(d, 150):
                    e5 = e ** 5
                    if e5 > sum_:
                        break
                    elif e5 == sum_:
                        print(a, b, c, d, e)
end = time.time()
print(f'Время работы программы {end - start}')

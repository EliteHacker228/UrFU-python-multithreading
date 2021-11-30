import concurrent.futures
import time
from hashlib import md5
from random import choice


def generate():
    while True:
        s = "".join([choice("0123456789") for i in range(50)])
        h = md5(s.encode('utf8')).hexdigest()

        if h.endswith("00000"):
            print(s, h)
            return (s, h)


def main():
    with concurrent.futures.ProcessPoolExecutor(max_workers=60) as executor:
        futures = []
        for i in range(10):
            futures.append(executor.submit(generate))
        for future in concurrent.futures.as_completed(futures):
            print(future.result())


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print("Асинхронное исполнение с 10 воркерами заняло", end - start, "секунд")

# 2, 4, 5, 10, 100
# Вычисление на 1м ядре 10 монеток заняло 430 секунд

# Вычисление на 100 ядрах вызвало исключение - max_workers must be <= 61

# Вычисление на 60 ядрах 10 монеток заняло 143 секунды, загрузка ЦП до 100%
# Вычисление на 10 ядрах 10 монеток заняло 148 секунд, загрузка ЦП до 100%
# Вычисление на 5 ядрах 10 монеток заняло 167 секунд, загрузка ЦП до 70%
# Вычисление на 4 ядрах 10 монеток заняло 185 секнуд, загрузка ЦП до 60%
# Вычисление на 2 ядрах 10 монеток заняло 218 секнуд, загрузка ЦП до 40%

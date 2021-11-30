import concurrent
from urllib.request import Request, urlopen
from urllib.parse import unquote
import concurrent.futures
import time


def open_url(url1):
    try:
        request = Request(
            url1,
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 9.0; Win65; x64; rv:97.0) Gecko/20105107 Firefox/92.0'},
        )
        resp = urlopen(request, timeout=5)
        code = resp.code
        print(code)
        resp.close()
    except Exception as e:
        print(url1, e)


links = open('res.txt', encoding='utf8').read().split('\n')

start = time.time()

i = 0

with concurrent.futures.ThreadPoolExecutor(max_workers = 5) as executor:
    futures = []
    for url in links:
        futures.append(executor.submit(open_url, url1=url))
    for future in concurrent.futures.as_completed(futures):
        print(i)
        i += 1

end = time.time()
print("Асинхронное исполнение с 10 воркерами заняло", end - start, "секунд")

# Синхронное исполнение заняло 1101 секунд, или 18 минут
# Асинхронное исполнение с 100 воркерами заняло 39 секунд
# Асинхронное исполнение с 10 воркерами заняло 112 секунд, или 1 минуту 52 секунды
# Асинхронное исполнение с 5 воркерами заняло 196 скенд, или 3 минуты 16 секунд

# С возрастанием числа воркеров заметно увеличивалась нагрузка на сетей траффик, и немного увеличивалась нагрузка
# на ЦП

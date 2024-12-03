import time
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)


if __name__ == '__main__':
    filenames = [f'D:\\Питоним\\modules_next\\module_10\\file {number}.txt' for number in range(1, 5)]

    start = time.time()
    for filename in filenames:
        read_info(filename)
    end = time.time()
    print(f"Линейный вызов: {end - start:.4f} секунд")

    start = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    end = time.time()
    print(f"Многопроцессный вызов: {end - start:.4f} секунд")

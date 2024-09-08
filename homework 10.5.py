import time
from multiprocessing import Pool


def read_info(filename):
    with open(filename, 'r') as file:
        all_data = []
        for line in file.readlines():
            all_data.append(line)
            if not line:
                break


filenames = [f'./file {number}.txt' for number in range(1, 5)]

if __name__ == '__main__':
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    end_time = time.time()
    print(f"0:00:{end_time - start_time:.6f} (линейный)")
    start_time = time.time()
    with Pool(4) as pool:
        pool.map(read_info, filenames)
    end_time = time.time()
    print(f"0:00:{end_time - start_time:.6f} (многопроцессный)")

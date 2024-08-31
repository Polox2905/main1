import time
from threading import Thread


start_time = time.time()
def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(word_count):
            f.write('Какое-то слово № %d\n' % (i + 1))
            time.sleep(0.1)
    print("Завершилась запись в файл %s." % file_name)

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end_time = time.time()
print("Работа потоков %s." % str(round(end_time - start_time, 2)))

start_time = time.time()


threads = []
for word_count, file_name in [(10, 'example5.txt'), (30, 'example6.txt'), (200, 'example7.txt'), (100, 'example8.txt')]:
    t = Thread(target=write_words, args=(word_count, file_name))
    threads.append(t)
    t.start()


for t in threads:
    t.join()


end_time = time.time()
print("Работа потоков %s." % str(round(end_time - start_time, 2)))

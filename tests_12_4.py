import unittest
from homework_12_4 import Runner, Tournament
import logging
import os

#logging.basicConfig(filename="runner_tests.log", level=logging.DEBUG)
logging.basicConfig(filename="runner_tests.log", encoding="utf-8", filemode="w", level=logging.INFO,
                        format="%(asctime)s | %(levelname)s | %(message)s")
class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:

            runner = Runner('Alice', speed=-1)
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.INFO(f"test_walk выполнен успешно")
        except ValueError as e:
            logging.warning("Неверная скорость для Runner: %s.", e)


    def test_run(self):
        try:

            runner = Runner(123)
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.INFO(f"test_run выполнен успешно")
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner: %s.", e)


    def test_challenge(self):
        alice = Runner('Alice')
        bob = Runner('Bob')
        for _ in range(10):
            alice.walk()
            bob.run()
        self.assertNotEqual(alice.distance, bob.distance)

if not os.path.exists("runner_tests.log"):
    print("Файл `runner_tests.log` не найден. Возможно, проблемы с доступом.")
if __name__ == '__main__':

    unittest.main()
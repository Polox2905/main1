import unittest
from homework12 import Runner


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(condition=(is_frozen == True), reason='Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner = Runner('Alice')
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @unittest.skipIf(condition=(is_frozen == True), reason='Тесты в этом кейсе заморожены')
    def test_run(self):
        runner = Runner('Bob')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @unittest.skipIf(condition=(is_frozen == True), reason='Тесты в этом кейсе заморожены')
    def test_challenge(self):
        alice = Runner('Alice')
        bob = Runner('Bob')
        for _ in range(10):
            alice.walk()
            bob.run()
        self.assertNotEqual(alice.distance, bob.distance)


if __name__ == '__main__':
    unittest.main()
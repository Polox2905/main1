import unittest
from homework12 import Runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = Runner('Alice')
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner('Bob')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        alice = Runner('Alice')
        bob = Runner('Bob')
        for _ in range(10):
            alice.walk()
            bob.run()
        self.assertNotEqual(alice.distance, bob.distance)


if __name__ == '__main__':
    unittest.main()
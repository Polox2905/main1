import unittest
from homework121 import Runner, Tournament


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", speed=10)
        self.andrey = Runner("Андрей", speed=9)
        self.nick = Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)

    def test_race_between_usain_and_nick(self):
        participants = [self.usain, self.nick]
        tournament = Tournament(90, *participants)
        results = tournament.start()
        self.assertTrue(list(results.values())[0] != 'Ник')
        self.all_results['Усэйн vs Ник'] = results

    def test_race_between_andrey_and_nick(self):
        participants = [self.andrey, self.nick]
        tournament = Tournament(90, *participants)
        results = tournament.start()
        self.assertTrue(list(results.values())[0] != 'Ник')
        self.all_results['Андрей vs Ник'] = results

    def test_race_between_usain_and_andrey_and_nick(self):
        participants = [self.usain, self.andrey, self.nick]
        tournament = Tournament(90, *participants)
        results = tournament.start()
        self.assertTrue(list(results.values())[0] != 'Ник')
        self.all_results['Усэйн vs Андрей vs Ник'] = results






if __name__ == '__main__':
    unittest.main()
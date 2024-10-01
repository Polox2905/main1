import unittest
import homework121test
import homework12test

TestSuite = unittest.TestSuite()
TestSuite.addTest(unittest.TestLoader().loadTestsFromTestCase(homework121test.TournamentTest))
TestSuite.addTest(unittest.TestLoader().loadTestsFromTestCase(homework12test.RunnerTest))


runner = unittest.TextTestRunner(verbosity=2)
runner.run(TestSuite)















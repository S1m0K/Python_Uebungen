import unittest

from HandSign import HandSign


class MyTestCase(unittest.TestCase):
    scissors = HandSign("Scissors", 0)
    paper = HandSign("Paper", 1)
    rock = HandSign("Rock", 2)
    lizard = HandSign("Lizard", 3)
    spock = HandSign("Spock", 4)

    def test_play(self):
        self.assertEqual(self.scissors.play(self.paper), 1)
        self.assertEqual(self.scissors.play(self.lizard), 1)

        self.assertEqual(self.paper.play(self.rock), 1)
        self.assertEqual(self.paper.play(self.spock), 1)

        self.assertEqual(self.rock.play(self.scissors), 1)
        self.assertEqual(self.rock.play(self.lizard), 1)

        self.assertEqual(self.lizard.play(self.spock), 1)
        self.assertEqual(self.lizard.play(self.paper), 1)

        self.assertEqual(self.spock.play(self.scissors), 1)
        self.assertEqual(self.spock.play(self.rock), 1)

        self.assertEqual(self.spock.play(self.spock), 0)
        self.assertEqual(self.rock.play(self.rock), 0)
        self.assertEqual(self.paper.play(self.paper), 0)
        self.assertEqual(self.scissors.play(self.scissors), 0)
        self.assertEqual(self.lizard.play(self.lizard), 0)

        self.assertEqual(self.paper.play(self.scissors), -1)
        self.assertEqual(self.paper.play(self.lizard), -1)

        self.assertEqual(self.scissors.play(self.rock), -1)
        self.assertEqual(self.scissors.play(self.spock), -1)

        self.assertEqual(self.lizard.play(self.rock), -1)
        self.assertEqual(self.lizard.play(self.scissors), -1)

        self.assertEqual(self.spock.play(self.lizard), -1)
        self.assertEqual(self.spock.play(self.paper), -1)

        self.assertEqual(self.rock.play(self.paper), -1)
        self.assertEqual(self.rock.play(self.spock), -1)


if __name__ == '__main__':
    unittest.main()

from datavisualization import contentTaker, fileHandler, stringifyContent
import unittest
import random


def getRandomTuple():
    lengthOfData = len(contentTaker())
    index = random.randrange(lengthOfData)
    return contentTaker()[index]


class TestForVisualization(unittest.TestCase):
    def test_isList(self):
        self.assertTrue(type(contentTaker()) == list)
        self.assertFalse(type(contentTaker()) == tuple)
        self.assertFalse(type(contentTaker()) == str)

    def test_listIsEmpty(self):
        self.assertTrue(len(contentTaker()) > 0)
        self.assertFalse(len(contentTaker()) <= 0)

    def test_isElementTuple(self):
        randomTuple = getRandomTuple()
        # print(randomTuple)
        self.assertTrue(type(randomTuple) == tuple)
        self.assertFalse(type(randomTuple) == str)
        self.assertFalse(type(randomTuple) == int)

    def test_isDateString(self):
        randomTuple = getRandomTuple()
        self.assertTrue(type(randomTuple[0]) == str)
        self.assertTrue(type(randomTuple[0]) == str)
        self.assertFalse(type(randomTuple[0]) == "")
        self.assertFalse(type(randomTuple[0]) == int)
        self.assertFalse(type(randomTuple[0]) == list)
        self.assertFalse(type(randomTuple[0]) == float)

    def test_isPriceFloat(self):
        randomTuple = getRandomTuple()
        # print(randomTuple)
        self.assertTrue(type(randomTuple[1]) == float)
        self.assertTrue(type(randomTuple[1]) == float)
        self.assertFalse(type(randomTuple[1]) == int)
        self.assertFalse(type(randomTuple[1]) == str)
        self.assertFalse(type(randomTuple[1]) == list)


if __name__ == '__main__':
    unittest.main()

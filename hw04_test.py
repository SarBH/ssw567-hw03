import unittest
import hw04


class Test_hw04(unittest.TestCase):

    def testRepoCompiler(self):
        testRepoDict =  hw04.gitRepoAPI("SarBH") #use my ID as an example
        realRepoDict = {'AdvancedMazeGame': 1, 'cell-classifier': 30, 'CS583_DL': 2, 'data-science-ipython-notebooks': 30, 'E-Commerce': 8, 'learn-co-sandbox': 1, 'slp-1': 5, 'ssw567': 3, 'ssw567-hw01': 4, 'ssw567-hw04': 14, 'triangle-hw02': 8, 'university': 7, 'zaidalyafeai.github.io': 30}
        self.assertDictEqual(testRepoDict, realRepoDict)
        self.assertEqual(len(testRepoDict.values()), 13)


if __name__ == "__main__":
    print("executing unittests")
    unittest.main(exit=False)
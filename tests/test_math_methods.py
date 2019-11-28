import unittest
import calculate_price as cp
import math_methods as mm

csv_file_path = "/Users/Anne/PycharmProjects/p1-projekt/home/HOME.csv"
csv_file = cp.import_csv_file(csv_file_path)
subset = csv_file.loc[:,["Kontantpris", "Alder", "Grundareal", "Boligareal", "Liggetid"]]
subset = subset.head(11)
subset = subset.drop([9])
subset = subset.reset_index()
subset = subset.drop(columns=["index"])

kontantpris_dataframe = subset.loc[:, "Kontantpris"]
alder_dataframe = subset.loc[:, "Alder"]
grundareal_dataframe = subset.loc[:, "Grundareal"]
boligareal_dataframe = subset.loc[:, "Boligareal"]
liggetid_dataframe = subset.loc[:, "Liggetid"]

def test_haeldning():
    haeldning1 = mm.haeldning(alder_dataframe, kontantpris_dataframe)
    if -34344 == round(haeldning1):
        print("test_healdning:", True)
    else:
        print("test_healdning:", False)

test_haeldning()

class TestHaeldning(unittest.TestCase):

    def test_haeldning(self):
        haeldning1 = mm.haeldning(alder_dataframe, kontantpris_dataframe)
        self.assertEqual(-34344, round(haeldning1))

        haeldning2 = mm.haeldning(grundareal_dataframe, kontantpris_dataframe)
        self.assertEqual(-436, round(haeldning2))

        haeldning3 = mm.haeldning(boligareal_dataframe, kontantpris_dataframe)
        self.assertEqual(17131, round(haeldning3))

        haeldning4 = mm.haeldning(liggetid_dataframe, kontantpris_dataframe)
        self.assertEqual(-2767, round(haeldning4))

class TestAritmetiskMiddelvaerdi(unittest.TestCase):

    def test_middelvaerdi(self):
        self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()

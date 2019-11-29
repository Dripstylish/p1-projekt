import unittest
import math
import pandas as pd

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

class TestSlope(unittest.TestCase):

    def test_slopes(self):
        slope1 = mm.slope(alder_dataframe, kontantpris_dataframe)
        self.assertEqual(-34344, math.ceil(slope1))

        slope2 = mm.slope(grundareal_dataframe, kontantpris_dataframe)
        self.assertEqual(-436, math.ceil(slope2))

        slope3 = mm.slope(boligareal_dataframe, kontantpris_dataframe)
        self.assertEqual(17132, math.ceil(slope3))

        slope4 = mm.slope(liggetid_dataframe, kontantpris_dataframe)
        self.assertEqual(-2767, math.ceil(slope4))

class TestMean(unittest.TestCase):

    def test_find_mean_value(self):
        slope_list = [mm.slope(alder_dataframe, kontantpris_dataframe),
                  mm.slope(grundareal_dataframe, kontantpris_dataframe),
                  mm.slope(boligareal_dataframe, kontantpris_dataframe),
                  mm.slope(liggetid_dataframe, kontantpris_dataframe)]
        mean = mm.mean(slope_list)
        self.assertEqual(-5104, math.ceil(mean))

class TestStandardDeviation(unittest.TestCase):

    def test_deviations(self):
        slope_list = [mm.slope(alder_dataframe, kontantpris_dataframe),
                      mm.slope(grundareal_dataframe, kontantpris_dataframe),
                      mm.slope(boligareal_dataframe, kontantpris_dataframe),
                      mm.slope(liggetid_dataframe, kontantpris_dataframe)]

        deviation, deviantion_minus = mm.standard_deviation(slope_list)
        self.assertEqual(121, math.ceil(deviation))
        self.assertEqual(-121, math.floor(deviantion_minus))

class TestStandardisation(unittest.TestCase):

    def test_standardisation(self):
        dataframe_slopes = pd.DataFrame([mm.slope(alder_dataframe, kontantpris_dataframe),
                                        mm.slope(grundareal_dataframe, kontantpris_dataframe),
                                        mm.slope(boligareal_dataframe, kontantpris_dataframe),
                                        mm.slope(liggetid_dataframe, kontantpris_dataframe)],
                                        ["Alder", "Grundareal", "Boligareal", "Liggetid"],
                                        ["Hældninger"])
        dataframe_standardised_slopes = mm.standardisation(dataframe_slopes)
        self.assertEqual(-242, round(dataframe_standardised_slopes.at["Alder", "Hældninger"]))
        self.assertEqual(39, round(dataframe_standardised_slopes.at["Grundareal", "Hældninger"]))
        self.assertEqual(184, round(dataframe_standardised_slopes.at["Boligareal", "Hældninger"]))
        self.assertEqual(19, round(dataframe_standardised_slopes.at["Liggetid", "Hældninger"]))


if __name__ == '__main__':
    unittest.main()

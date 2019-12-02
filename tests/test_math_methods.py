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

    def test_find_slopes(self):
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

    def test_find_deviations(self):
        slope_list = [mm.slope(alder_dataframe, kontantpris_dataframe),
                      mm.slope(grundareal_dataframe, kontantpris_dataframe),
                      mm.slope(boligareal_dataframe, kontantpris_dataframe),
                      mm.slope(liggetid_dataframe, kontantpris_dataframe)]

        deviation, deviantion_minus = mm.standard_deviation(slope_list)
        self.assertEqual(121, math.ceil(deviation))
        self.assertEqual(-121, math.floor(deviantion_minus))

class TestStandardisation(unittest.TestCase):

    def test_find_standardisation_of_slope(self):
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

class TestFindMax(unittest.TestCase):

    def test_find_maximum_standardised_slope(self):
        dataframe_slopes = pd.DataFrame([mm.slope(alder_dataframe, kontantpris_dataframe),
                                         mm.slope(grundareal_dataframe, kontantpris_dataframe),
                                         mm.slope(boligareal_dataframe, kontantpris_dataframe),
                                         mm.slope(liggetid_dataframe, kontantpris_dataframe)],
                                        ["Alder", "Grundareal", "Boligareal", "Liggetid"],
                                        ["Hældninger"])
        dataframe_standardised_slopes = mm.standardisation(dataframe_slopes)
        a_max, a_max_variable = mm.find_max(dataframe_standardised_slopes)
        self.assertEqual(-242, round(a_max))
        self.assertEqual("Alder", a_max_variable)

class TestIntersection(unittest.TestCase):

    def test_find_intersection(self):
        intersection1 = mm.intersection(alder_dataframe, kontantpris_dataframe)
        self.assertEqual(3517271, round(intersection1))

        intersection2 = mm.intersection(grundareal_dataframe, kontantpris_dataframe)
        self.assertEqual(2784178, round(intersection2))

        intersection3 = mm.intersection(boligareal_dataframe, kontantpris_dataframe)
        self.assertEqual(-103905, round(intersection3))

        intersection4 = mm.intersection(liggetid_dataframe, kontantpris_dataframe)
        self.assertEqual(2649012, round(intersection4))

class TestResidual(unittest.TestCase):

    def test_find_new_y(self):
        dataframe_slopes = pd.DataFrame([mm.slope(alder_dataframe, kontantpris_dataframe),
                                         mm.slope(grundareal_dataframe, kontantpris_dataframe),
                                         mm.slope(boligareal_dataframe, kontantpris_dataframe),
                                         mm.slope(liggetid_dataframe, kontantpris_dataframe)],
                                        ["Alder", "Grundareal", "Boligareal", "Liggetid"],
                                        ["Hældninger"])
        dataframe_standardised_slopes = mm.standardisation(dataframe_slopes)

        _, a_lister = mm.residual(subset, dataframe_standardised_slopes)
        a_1 = pd.DataFrame(data=[496120, 856525, 3334427, 1944584, 3693787, 4501447, 791845, 1283702, 3693787, 2219185],
                           columns=["a_1"])

        self.assertTrue(a_1.equals(a_lister["a_1"]))

class TestStandardisationIntersection(unittest.TestCase):

    def test_find_standardisation_of_intersection(self):
        dataframe_standardised_intersections = mm.standardisation_intersection(subset,
                                                                               ['Grundareal', 'Boligareal', 'Liggetid'],
                                                                               "Alder")
        dataframe_standardised_intersections_correct = pd.DataFrame([1213.0, 532.0, -2152.0, 406.0], ["Alder", "Grundareal", "Boligareal", "Liggetid"], ["Skæringer"])
        print(dataframe_standardised_intersections_correct)
        print(dataframe_standardised_intersections.round())

        self.assertTrue(dataframe_standardised_intersections_correct.equals(dataframe_standardised_intersections.round()))

if __name__ == '__main__':
    unittest.main()

# import unittest
# import pandas as pd
# import os
# from load_csv import load

# class TestLoadCSV(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         # Create some temporary test files
#         # 1. Valid CSV
#         cls.valid_csv = "valid.csv"
#         df_valid = pd.DataFrame({
#             "Name": ["Alice", "Bob"],
#             "Age": [25, 30]
#         })
#         df_valid.to_csv(cls.valid_csv, index=False)

#         # 2. Empty CSV
#         cls.empty_csv = "empty.csv"
#         open(cls.empty_csv, "w").close()

#         # 3. Invalid CSV (bad format)
#         cls.bad_csv = "bad.csv"
#         with open(cls.bad_csv, "w") as f:
#             f.write("Name,Age\nAlice,25\nBob") # missing value in second row

#     @classmethod
#     def tearDownClass(cls):
#         # Remove temporary files
#         for f in [cls.valid_csv, cls.empty_csv, cls.bad_csv]:
#             if os.path.exists(f):
#                 os.remove(f)

#     def test_valid_csv(self):
#         df = load(self.valid_csv)
#         self.assertIsInstance(df, pd.DataFrame)
#         self.assertEqual(df.shape, (2, 2))

#     def test_file_not_found(self):
#         df = load("nonexistent.csv")
#         self.assertIsNone(df)

#     def test_empty_file(self):
#         df = load(self.empty_csv)
#         self.assertIsNone(df)

#     def test_unexpected_error(self):
#         df = load(".")
#         self.assertIsNone(df)

# if __name__ == "__main__":
#     unittest.main()

from load_csv import load
print(load("population_total.csv"))

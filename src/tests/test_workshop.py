import unittest

import numpy as np
import pandas as pd
from pandas.testing import assert_frame_equal

from src.workshop import add, multiply_by_10, impute_nans, add_is_alone_column

# add 1 + 1
class TestProcessing(unittest.TestCase):
    
    def test_add_1_and_1_should_return_2(self):
        self.assertEqual(add(1,1),2)

    def test_multiply_by_10_should_return_a_df_with_values_multiplied_by_10(self):

        # arange
        df = pd.DataFrame({
            'age': [1,2,3],
            'name': ['Bob', 'Alice', 'John']
        })
        expected_df = pd.DataFrame({
            'age': [10, 20, 30],
            'name': ['Bob', 'Alice', 'John']
        })
        assert_frame_equal(multiply_by_10(df),expected_df)
    
    def test_impute_nan_should_replace_nan_values_with_median_values(self):
        df = pd.DataFrame({
            'age': [1,np.nan,3],
            'income': [100, 300, np.nan],
            'name': ['Bob', 'Alice', np.nan]
        })
        expected_df = pd.DataFrame({
            'age': [1, 2, 3],
            'income': [100, 300, 200],
            'name': ['Bob', 'Alice', np.nan]
        })
        assert_frame_equal(impute_nans(df, columns=['age', 'income']),expected_df, check_dtype=False)

    def test_is_alone_should_create_an_isalone_column_with_value_1_if_familysize_is_1(self):
        df = pd.DataFrame({
            'FamilySize': [1,5,3],
            'name': ['Bob', 'Alice', 'John']
        })

        expected_df = pd.DataFrame({
            'FamilySize': [1,5,3],
            'name': ['Bob', 'Alice', 'John'],
            'IsAlone': [1,0,0]
        })
        assert_frame_equal(add_is_alone_column(df),expected_df)

if __name__ == '__main__':
    unittest.main()

#python -m src.tests.test_workshop
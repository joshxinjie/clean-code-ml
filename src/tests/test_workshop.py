import unittest

import pandas as pd
from pandas.testing import assert_frame_equal

from src.workshop import add, multiply_by_10

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


if __name__ == '__main__':
    unittest.main()

#python -m src.tests.test_workshop
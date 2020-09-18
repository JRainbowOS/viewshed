import numpy as np 
from pytest import param 

from viewshed.line_of_sight import LineOfSight

def test_is_in_line_of_sight_data():
    test_variables = "surface, point, expected_result"
    test_data = [
        param(
            np.zeros((3, 3), dtype=int),
            np.array([1, 1, 1]),
            True,
            id='one point above flat surface'
        ),
        param(
            np.zeros((3, 3), dtype=int),
            np.array([1, 1, -1]),
            False,
            id='one point below flat surface'
        )
    ]
    return test_variables, test_data

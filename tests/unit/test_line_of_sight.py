import pytest 

from viewshed.line_of_sight import is_in_line_of_sight
from tests.unit import test_line_of_sight_data as data

@pytest.mark.unit
class TestViewshed:

    @pytest.mark.parametrize(*data.test_is_in_line_of_sight_data())
    def test_is_in_line_of_sight(self, surface, point, expected_result):
        # Arrange

        # Act
        result = is_in_line_of_sight(surface, point)

        # Assert
        assert result == expected_result
        

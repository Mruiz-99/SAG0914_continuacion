import pytest
from src.app import allowed_file


@pytest.mark.parametrize(
    'filename, expected',
    [
        ('file.png', True),
        ('file.jpg', True),
        ('file.tiff', False),
        ('file.jpeg', True),
        ('file.gif', False),
        ('file.bmp', False),
    ]
)
def test_allowed_file(filename, expected):
    assert allowed_file(filename) == expected

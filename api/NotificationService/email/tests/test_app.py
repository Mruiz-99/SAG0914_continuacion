import pytest
from src.app import allowed_file


@pytest.mark.parametrize(
    'filename, expected',
    [
        ('file.txt', True),
        ('file.pdf', True),
        ('file.png', True),
        ('file.jpg', True),
        ('file.jpeg', True),
        ('file.gif', True),
        ('file.tiff', False),
        ('file.mp4', False),
        ('file.bmp', False),
    ]
)
def test_allowed_file(filename, expected):
    assert allowed_file(filename) == expected

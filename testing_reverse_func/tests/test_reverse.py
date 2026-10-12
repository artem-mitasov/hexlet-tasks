from pathlib import Path
from src.solution import reverse

def get_test_data_path(filename):
    return Path(__file__).parent / "test_data" / filename


def read_file(filename):
    return get_test_data_path(filename).read_text()


def test_reverse():
    before_text = read_file("before.txt")
    expected_text = read_file("after.txt")
    actual_text = reverse(before_text)

    assert actual_text == expected_text

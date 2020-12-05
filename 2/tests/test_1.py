from code.part1 import calculate1

valid_input_dict = {
        "abcdefg": [[1-3], "a"],
}

invalid_input_dict = {
        "bcddgb": [[2, 4], "z"]
}

def test_valid_input():
    assert len(calculate1(valid_input_dict)) == 1
    


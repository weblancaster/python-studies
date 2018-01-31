"""
Day 29
Getting started with unit test in python, understandin the envirnment, setup and maybe some quirks?
"""
def sum_values(val_a, val_b):
    """[Sum two values received in arguments]

    Arguments:
        val_a {[Number]}
        val_b {[Number]}

    Returns:
        [Number] -- [sum of arguments]
    """
    return val_a + val_b

def test_sum_values():
    """Small unit test for sum_values method
    """
    assert sum_values(5, 10) == 15
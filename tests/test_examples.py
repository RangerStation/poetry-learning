from poetry_learning import __version__
from poetry_learning.math import add, sub


def test_version():
    assert __version__ == "0.1.0"


def test_add__2_and_3_equals_5():
    # Given
    a = 3
    b = 2

    # When
    actual = add(a, b)

    # Then
    expected = 5
    assert actual == expected


# # Uncomment me out to see failing test.
# # Visit ./poetry_learning/math/__init__.py to fix!
# def test_sub__3_and_2_equals_1():
#     # Given
#     a = 3
#     b = 2

#     # When
#     actual = sub(a, b)

#     # Then
#     expected = 1
#     assert actual == expected

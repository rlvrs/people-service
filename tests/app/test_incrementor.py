from app.incrementor import inc


def test_inc():
    x = 1
    expected_out = x + 1
    assert inc(x) == expected_out

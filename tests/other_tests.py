import pytest
from syrupy import snapshot



@pytest.mark.parametrize(
    "a,b",(
    (1,2),
    (3,1),
    (4,2),
    (5,3),)
)
def test_smaller_than_five(snapshot, a, b):
    assert ((a+b)<5) == snapshot

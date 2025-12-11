import sys
import math
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

from app import add, sub, mult, div, log, sqr, cos, sin, sqr_root, per

def test_add():
    assert add(5, 6) == 11

def test_sub():
    assert sub(10, 6) == 4

def test_mult():
    assert mult(4, 5) == 20

def test_div():
    assert div(12, 3) == 4

def test_log():
    assert log(100) == 2

def test_square():
    assert sqr(4) == 16

def test_sin():
    assert sin(0) == 0

def test_cos():
    assert cos(math.pi) == -1

def test_percent():
    assert per (6, 10) == 60
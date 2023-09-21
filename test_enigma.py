import pytest
from main import Enigma, rotors, reverser


def test_init():
    eng = Enigma(rotors, reverser)
    assert eng.rotors


def test_set_cables():
    eng = Enigma(rotors, reverser)
    eng.set_cables("AB, CD")
    assert eng.cables["A"] == "B"
    assert eng.cables["C"] == "D"

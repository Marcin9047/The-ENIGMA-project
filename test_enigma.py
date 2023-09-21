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


def test_set_order():
    eng = Enigma(rotors, reverser)
    eng.set_order([3, 1, 2])
    assert eng.order == [3, 1, 2]


def test_shifts():
    eng = Enigma(rotors, reverser)
    eng.set_shifts([3, 1, 2])
    assert eng.shifts == [3, 1, 2]


def test_autoshift():
    eng = Enigma(rotors, reverser)
    eng.auto_shift()
    assert eng.screen_code == ["B", "A", "A"]


def test_autoshift2():
    eng = Enigma(rotors, reverser)
    eng.set_screen_code(["Z", "A", "A"])
    eng.auto_shift()
    assert eng.screen_code == ["A", "A", "A"]


def test_autoshift3():
    eng = Enigma(rotors, reverser)
    eng.set_screen_code(["Q", "A", "A"])
    eng.auto_shift()
    assert eng.screen_code == ["R", "B", "A"]

def test_autoshift4():
    eng = Enigma(rotors, reverser)
    eng.set_screen_code(["Q", "E", "A"])
    eng.auto_shift()
    assert eng.screen_code == ["R", "F", "B"]

def test_total_diff():
    eng = Enigma(rotors, reverser)
    eng.set_screen_code(["Q", "E", "A"])
    eng.set_shifts([3, 1, 2])
    assert eng.total_diff(2) == -3


def test_encrypt():
    eng = Enigma(rotors, reverser)
    eng.set_screen_code(["A", "A", "A"])
    eng.set_shifts([0, 0, 0])
    assert eng.encryption("A") == "G"
    eng.set_order([3, 1, 2])
    assert eng.encryption("A") == "L"


def test_back_encrypting():
    eng = Enigma(rotors, reverser)
    eng.set_screen_code(["A", "A", "A"])
    eng.set_shifts([0, 0, 0])
    assert eng.back_encryption("A") == "K"
    eng.set_order([3, 1, 2])
    assert eng.back_encryption("A") == "W"

def test_full_encrypting():
    eng = Enigma(rotors, reverser)
    eng.set_screen_code(["Z", "A", "A"])
    eng.set_shifts([0, 0, 0])
    eng.set_cables("AB, CD, NG")
    assert eng.full_encryption("A") == "F"
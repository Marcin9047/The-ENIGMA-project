from enigma import Enigma, rotors, reverser

eng = Enigma(rotors, reverser)
eng.set_screen_code(["C", "X", "E"])
eng.set_shifts([6, 21, 9])
eng.set_cables("AB, CD, NG SQ WO ZI KE YV RH JT")
eng.set_order([3, 1, 2])
print(eng.translate())

rotors = {
    "A": ["E", "A", "B"],
    "B": ["K", "J", "D"],
    "C": ["M", "D", "F"],
    "D": ["F", "K", "H"],
    "E": ["L", "S", "J"],
    "F": ["G", "I", "L"],
    "G": ["D", "R", "C"],
    "H": ["Q", "U", "P"],
    "I": ["V", "X", "R"],
    "J": ["Z", "B", "T"],
    "K": ["N", "L", "X"],
    "L": ["T", "H", "V"],
    "M": ["O", "W", "Z"],
    "N": ["W", "T", "N"],
    "O": ["Y", "M", "Y"],
    "P": ["H", "C", "E"],
    "Q": ["X", "Q", "I"],
    "R": ["U", "G", "W"],
    "S": ["S", "Z", "G"],
    "T": ["P", "N", "A"],
    "U": ["A", "P", "K"],
    "V": ["I", "Y", "M"],
    "W": ["B", "F", "U"],
    "X": ["R", "V", "S"],
    "Y": ["C", "O", "Q"],
    "Z": ["J", "E", "O"]
}

reverser = {
    "A": "Y",
    "B": "R",
    "C": "U",
    "D": "H",
    "E": "Q",
    "F": "S",
    "G": "L",
    "I": "P",
    "J": "X",
    "K": "N",
    "M": "O",
    "T": "Z",
    "V": "W",
}


order = [1, 2, 3]


class Enigma:
    def __init__(self, rotors, reverser):
        self.rotors = rotors
        self.reverser = reverser
        self.order = [1, 2, 3]
        self.cables = {}

    def set_cables(self, cables):
        self.cables = {}
        cables = cables.split(", ")
        for one in cables:
            self.cables[one[0]] = one[1]

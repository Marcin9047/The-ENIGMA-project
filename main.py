rotors = {
    "SHIFTS": ["R", "F", "W"],
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

alphabet = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9, "J":10, "K":11, "L":12, "M":13, "N":14, "O":15, "P":16, "Q":17, "R":18, "S":19, "T":20, "U":21, "V":22, "W":23, "X":24, "Y":25, "Z":26}

order = [1, 2, 3]


class Enigma:
    def __init__(self, rotors, reverser):
        self.rotors = rotors
        self.reverser = reverser
        self.order = [1, 2, 3]
        self.cables = {}
        self.shifts = [0, 0, 0]
        self.screen_code = ["A", "A", "A"]

    def set_cables(self, cables):
        self.cables = {}
        cables = cables.split(", ")
        for one in cables:
            self.cables[one[0]] = one[1]

    def set_order(self, order):
        self.order = order

    def set_shifts(self, shifts):
        self.shifts = shifts

    def set_screen_code(self, code):
        self.screen_code = code

    def auto_shift(self):
        for ind in range(len(self.screen_code)):
            if ind == 0 or self.screen_code[ind - 1] == self.rotors["SHIFTS"][self.order[ind - 1] - 1]:
                if self.screen_code[ind] != "Z":
                    self.screen_code[ind] = chr(ord(self.screen_code[ind]) + 1)
                else:
                    self.screen_code[ind] = "A"

    def total_diff(self, next):
        shift = self.shifts[next] - self.shifts[next - 1]
        letters = alphabet[self.screen_code[next]] - alphabet[self.screen_code[next - 1]]
        return shift + letters

    def encryption(self, char):
        for num in range(len(self.screen_code)):
            char = rotors[char][self.order[num] - 1]
            if num < len(self.screen_code) - 1:
                char = chr(ord(char) + self.total_diff(num + 1))
                if ord(char) < 65:
                    char = chr(ord(char) + 26)
                elif ord(char) > 90:
                    char = chr(ord(char) - 26)
        return char

    def back_encryption(self, char):
        for num in range(len(self.screen_code) -1, -1, -1):
            for i in rotors:
                if i != "SHIFTS" and char == rotors[i][self.order[num] - 1]:
                    char = i
                    break
            if num > 0:
                char = chr(ord(char) - self.total_diff(num))
                if ord(char) < 65:
                    char = chr(ord(char) + 26)
                elif ord(char) > 90:
                    char = chr(ord(char) - 26)
        return char

    def full_encryption(self, char):
        self.auto_shift()
        char = self.cables_encryption(char)
        char = self.encryption(char)
        if char in reverser:
            char = self.reverser[char]
        else:
            for i in reverser:
                if reverser[i] == char:
                    char = i
        char = self.back_encryption(char)
        char = self.cables_encryption(char)
        return char
    
    def cables_encryption(self, char):
        if char in self.cables:
            char = self.cables[char]
        else:
            for i in self.cables:
                if self.cables[i] == char:
                    char = i
                    break
                    char == i
                    char = i
                    break
        return char

    def translate(self):
        result = []
        text = input("Wprowadź tekst:")
        for one in text:
            if one != " ":
                result.append(self.full_encryption(one))
            else:
                result.append(" ")
        result = "".join(result)
        return result



eng = Enigma(rotors, reverser)
eng.set_screen_code(["Z", "A", "A"])
eng.set_shifts([6, 21, 9])
eng.set_cables("AB, CD, NG")
eng.set_order([3, 1, 2])
print(eng.translate())
print(eng.translate())

eng.set_screen_code(["Z", "A", "A"])
eng.set_shifts([6, 21, 9])
eng.set_cables("AB, CD, NG")
eng.set_order([3, 1, 2])
print(eng.translate())

print(eng.shifts)
print(eng.screen_code)
print(eng.translate())
print(eng.shifts)
print(eng.screen_code)
eng.set_screen_code(["Z", "A", "A"])
eng.set_shifts([6, 21, 9])
eng.set_cables("AB, CD, NG")
eng.set_order([3, 1, 2])
print(eng.translate())
print(eng.shifts)
print(eng.screen_code)





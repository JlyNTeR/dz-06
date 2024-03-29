CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u","f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

BAD_SYMBOLS = ("%", "*", " ", "-")

TRANS = {}
for c, l in zip(list(CYRILLIC_SYMBOLS), TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()

for i in BAD_SYMBOLS:
    TRANS[ord(i)] = "_"


def normalize(name: str) -> str:
    
    trans_name = name.translate(TRANS)
    return trans_name

if __name__ == "__main__":
    normalize()
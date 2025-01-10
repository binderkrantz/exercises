# Given a valid Roman numeral, convert it to an integer.

def roman_to_int(s):
    mapping = {
        'I': 1,	
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    numerals = [mapping[l] for l in s]
    numerals.append(0)
    s = 0
    while len(numerals) > 1:
        n = numerals.pop(0) 
        if n >= numerals[0]:
            s += n
        else:
            s -= n
    return s


tests = [
	('XI', 11),
	('LXIX', 69),
	('CDXX', 420),
	('MCMXCIX', 1999),
	('DCCCLXXXVIII', 888),
]
for t in tests:
    a = roman_to_int(t[0])
    assert a == t[1], a
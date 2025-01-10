# Given an array containing exactly three unique points, each represented as coordinate pairs (x, y) with no duplicates,
# determine whether these points lie on the same straight line. Return True if they do, and False otherwise.

def on_straight_line(points):
	return False

tests = [
	([(2, 1), (3, 4), (5, 6)], False),
	([(0, 0), (1, 1), (2, 2)], True),
	([(1, 1), (1, 2), (1, 3)], True),
	([(-2, 0), (0, 4), (2, 5)], False),
]

for t in tests:
	a = on_straight_line(t[0])
	assert a == t[1], (t, a)

# Given an array containing exactly three unique points, each represented as coordinate pairs (x, y) with no duplicates,
# determine whether these points lie on the same straight line. Return True if they do, and False otherwise.

def on_straight_line(points):
	a, b, c = points
	return (a[1] - b[1]) * (a[0] - c[0]) == (a[1] - c[1]) * (a[0] - b[0]) # slopes are equal
	return a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1]) == 0 # area of triangle is 0

tests = [
	([(2, 1), (3, 4), (5, 6)], False),
	([(0, 0), (1, 1), (2, 2)], True),
	([(1, 1), (1, 2), (1, 3)], True),
	([(-2, 0), (0, 4), (2, 5)], False),
]

for t in tests:
	a = on_straight_line(t[0])
	assert a == t[1], (t, a)

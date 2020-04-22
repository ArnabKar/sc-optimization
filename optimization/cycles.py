import os
import sys

sys.path.append("../")


# def scriptA(t, i1, i2, i3) :
# 	return_val = t[i1][i2][i3]["v"] * max(t[i1][i2][i3]["v"] - 1, 0) * max(t[i2][i3]["v"] - 2, 0) +\
# 				t[i1][i2][i3]["v"] * (t[i1][i3]["v"] - t[i1][i2][i3]["v"]) * max(t[i2][i3]["v"] - 1, 0) +\
# 				(t[i1][i2]["v"] - t[i1][i2][i3]["v"]) * t[i1][i2][i3]["v"] * max(t[i2][i3]["v"] - 1, 0) +\
# 				(t[i1][i2]["v"] - t[i1][i2][i3]["v"]) * (t[i1][i2]["v"] - t[i1][i2][i3]["v"]) * (t[i2][i3]["v"] - 1)
# 	return return_val

# def scriptB(t, i1, i2, i3, r, q, gamma):
# 	return_val = t[i1][i2][i3]["v"] * max(t[i1][i3]["v"] - 1, 0) * t[i2 + (r - q) * gamma][i3 + (r - q)*gamma] +\
# 				 (t[i1][i2]["v"]- t[i1][i2][i3]["v"]) * t[i1][i3] * t[i2 + (r - q) * gamma][i3 + (r - q)*gamma]
# 	return return_val

# def scriptC(t, i1, i2, i3, r, q, s, gamma):
# 	# r < q < s
# 	return_val = t[i1][i2]["v"] * t[i1 + (r - q) * gamma][i3 + (r - q) * gamma]["v"] * t[i2 + (r - s) * gamma][i3 + (r - s) * gamma]["v"]
# 	return return_val

def max_plus(a) :
	return max(a, 0)


def script_A(a, b, c,d) :
	return_val = a * max_plus(a -1) * max_plus(d -2) +\
				 a * (c - a) * max_plus(d - 1) +\
				 (b - a) * a * max_plus(d - 1) +\
				 (b - a) * (c - a) * d
	return return_val

def script_B(a, b, c, d):
	return_val = a * max_plus(d - 1) * d +\
				(b - a) * c * d
	return return_val

def script_C(a, b, c):
	# r < q < s
	return_val = a * b * c
	return return_val


def main() :
	return 0


if __name__ == '__main__':
	main()
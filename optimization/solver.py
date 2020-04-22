import os
import sys
sys.path.append("../")
from paper_hook import paper_hook

def recurse_print(t, prefix) :
	for elem in t :
		if elem == "v" :
			print("{0} = {1}".format(prefix, t["v"]))
			continue

		recurse_print(t[elem], "{0} {1}".format(prefix, elem))

def printout(t) :
	recurse_print(t, "t ")

	print("\n** \nt 0 -1 -1 = <value>, means t[0] = value")
	print("\nt 0 2 -1 = <value>, means t[0][2] = value")

def solver(m=1, gamma=3, kappa=7, L=20) :
	if m == 1 and gamma == 3:
		t = paper_hook(m=1, gamma=3, k=7,  L=L)
	else :
		t = paper_hook(m=1, gamma=3, k=7, L=L)

	printout(t)

def main():
	args = sys.argv[1:]

	if len(sys.argv) > 1 :
		m = int(args[0])
		gamma = int(args[1])
		kappa = int(args[2])
		L = int(args[3])
	else :
		m = 1
		gamma = 3
		kappa = 7
		L = 20

	solver(m, gamma, kappa, L)


if __name__ == '__main__':
	main()
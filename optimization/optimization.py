import os
import sys
sys.path.append("../")
from cycles import script_A, script_B, script_C


def finding_F(t, m, L, gamma):
	val = 0

	for k in range(1, m+2) :
		val += (L - k + 1) * F_1(t, k, m, L, gamma)

	return val

def F_1(t, k, m, L, gamma) :
	return_val = 0

	if k == 1 :
		for i1 in range(0, (m + 1) * gamma) :
			
			for i2 in range(i1+1, (m + 1) * gamma) :
				if i2 % gamma == i1 % gamma :
					continue

				for i3 in range(i2 + 1, (m + 1) * gamma) :			
					if i3 % gamma == i2 % gamma or i3 % gamma == i1 % gamma :
						continue

					# print(t[1])
					# print(t[2])
					# print(t[3])
					# print(i1)
					# print(i2)
					# print(i3)
					return_val += script_A(t[i1][i2][i3]["v"], t[i1][i2][-1]["v"], t[i1][i3][-1]["v"], t[i2][i3][-1]["v"])
	elif k == 2 :
		for i1 in range(0, (m + 1) * gamma) :
			
			for i2 in range(max(i1+1, gamma), (m + 1) * gamma) :
				if i2 % gamma == i1 % gamma :
					continue

				for i3 in range(max(i2+1, gamma), (m + 1) * gamma) :			
					if i3 % gamma == i2 % gamma or i3 % gamma == i1 % gamma :
						continue

					return_val += script_B(t[i1][i2][i3]["v"], t[i1][i2][-1]["v"], t[i1][i3][-1]["v"], t[i2 - gamma][i3 - gamma][-1]["v"])


			for i2 in range(i1+1, m * gamma) :
				if i2 % gamma == i1 % gamma :
					continue

				for i3 in range(i2+1, m * gamma) :			
					if i3 % gamma == i2 % gamma or i3 % gamma == i1 % gamma :
						continue

					return_val += script_B(t[i1][i2][i3]["v"], t[i1][i2][-1]["v"], t[i1][i3][-1]["v"], t[i2 + gamma][i3 + gamma][-1]["v"])
	else :

		for i1 in range(0, (m + 1) * gamma) :
			
			for i2 in range(max(i1+1, (k - 1) * gamma), (m + 1) * gamma) :
				if i2 % gamma == i1 % gamma :
					continue

				for i3 in range(max(i2+1, (k - 1) * gamma), (m + 1) * gamma) :			
					if i3 % gamma == i2 % gamma or i3 % gamma == i1 % gamma :
						continue

					return_val += script_B(t[i1][i2][i3]["v"], t[i1][i2][-1]["v"], t[i1][i3][-1]["v"], t[i2 + (1 - k) * gamma][i3 - (1 - k) * gamma][-1]["v"])


			for i2 in range(i1+1, (m - k + 2) * gamma) :
				if i2 % gamma == i1 % gamma :
					continue

				for i3 in range(i2+1, (m - k + 2) * gamma) :			
					if i3 % gamma == i2 % gamma or i3 % gamma == i1 % gamma :
						continue

					return_val += script_B(t[i1][i2][i3]["v"], t[i1][i2][-1]["v"], t[i1][i3][-1]["v"], t[i2 + (k - 1) * gamma][i3 + (k - 1) * gamma][-1]["v"])


		for q in range(2, k) :
			for i1 in range((q - 1) * gamma, (m + 1) * gamma) :

				for i2 in range(max(i1+1, (k - 1) * gamma), (m + 1) * gamma) :
					if i2 % gamma == i1 % gamma :
						continue

					for i3 in range(max(i2+1, (k - 1) * gamma), (m + q) * gamma) :			
						if i3 % gamma == i2 % gamma or i3 % gamma == i1 % gamma :
							continue

						return_val += script_C(t[i1][i2][-1]["v"], t[i1 + (1 - q) * gamma][i3 + (1 - q) * gamma][-1]["v"], t[i2 + (1 - k) * gamma][i3 + (1 - k)*gamma][-1]["v"])


	return return_val
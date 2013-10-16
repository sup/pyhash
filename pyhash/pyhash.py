#pyhash.py
#Charles J. Lai
#October 11, 2013

"""
======
pyhash
======
Description

--------
Contents
--------

Classes
-------

Methods
-------
"""

def fnv_1a(string, seed=0):
	"""
	Description
	"""
	#Constants
	FNV_prime = 16777619
	offset_basis = 2166136261

	#FNV-1a Hash Function
	hash = offset_basis + seed
	for char in string:
		hash = hash ^ ord(char)
 		hash = hash * FNV_prime
	return hash


def main():
	"""
	Testing application: Do something
	"""
	print fnv_1a("lol", 2)

#==============================================
#				Testing App
#==============================================
if __name__ == '__main__':
	main()
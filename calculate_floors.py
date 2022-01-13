import re
from statistics import median 
pattern = re.compile(r'^Price--amount">+[-+]?[0-9]*\.?[0-9]+')

names = [
	"GARFIELD.txt",
	"ALIEN.txt",
	"CHESHIRE.txt",
	"PINKPANTHER.txt",
    "ZOMBIE.txt",
	"CLONES.txt",
	"2017.txt",
	"2018.txt",
	"2019.txt",
	"2020.txt",
	"2021.txt"
]
filter = {
	"GARFIELD.txt": 1.1,
	"ALIEN.txt": 1.1,
	"CHESHIRE.txt": 0.75,
	"PINKPANTHER.txt": 1.0,
    "ZOMBIE.txt": 1.49,
	"CLONES.txt": 0.75,
	"2017.txt": 2.3,
	"2018.txt": 1.6,
	"2019.txt": 7.22,
	"2020.txt": 10.00,
	"2021.txt": 0.5,
    }
for n in names:
	f = open("data/"+n, "r")
	res = re.findall('Price--amount">+[-+]?[0-9]*\.?[0-9]+',f.read())
	final = []
	for s in res:
		tmp = float(s[15:])
		if tmp >= filter[n]:
			final.append(tmp)
		final_sorted = sorted(final)
		# The first value is the 'floor'
	print(n.removesuffix(".txt").capitalize(),'=', median(final_sorted))
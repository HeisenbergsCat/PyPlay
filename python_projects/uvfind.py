# _u003_v004_

def generate_pair(unum, vnum, digits):
	vdigitnum = digits - len(str(vnum))
	udigitnum = digits - len(str(unum))
	udigits = "0" * udigitnum
	vdigits = "0" * vdigitnum
	return "_u" + udigits + str(unum) + "_v" + vdigits + str(vnum) + "_"

def generate_pair_list(digits):
    pair_list = []
    i = 0
    while i <= int(str("9" * digits)):
		for u in range(0, int(str("9" * digits)) + 1 ):
			pair_list.append(generate_pair(i, u, digits))
        print "Wygenerowano par: "
    	i += 1
    return pair_list

def find_pair(test_string, digits):
	pair_list = generate_pair_list(digits)
	print "Szukalem w: " + test_string
	for i in range(0, len(pair_list)):
		test = test_string.find(pair_list[i], 0, len(test_string))
		if test != -1:
			print "Znalazlem : " + test_string[test: test + (5 + 2 * digits)]

# body

string_to_search = "sdfsd_u11_4fsdddd_usdassss_vaaaa_34__u211_v083_.jpg"


#print "".join(uv_list)
#print "ilosc par: " + len(uv_list)
print ""
find_pair(string_to_search, 3)

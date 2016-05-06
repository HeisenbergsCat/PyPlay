kod = "01000100 11111100 10011110 01110110 11110110 01011110 11000110 01110110 11110110 11010110 10101110 00000100 00110110 10000110 00101110 11001110 11110110 01011110 00000100 10011110 00100110 10100110 10010110 11010110 00000100 01110100 10100110 01010110 11110110 10110110 00000100 10100110 10010110 01110110 10000110 00101110 10011110 00001110 00000100 01110100 10011110 01110110 11110110 01011110 11000110 01011110 11001110 10010110 01110110 00100110 11110110 00001110 00000100 00110100 10011110 01001110 10000110 00101110 11001110 00000100 00110100 00110110 10000110 00101110 11001110 11110110 00000100 10100110 10010110 11001110 00000100 10101110 10010110 10110110 00100110 10100110 10010110 11001110 00000100 01011110 00000100 01110110 10100110 00100110 10100110 01010110 01000100 00000100 01011100 00101110 01110110 10010110 00010110 00000100 00110100 01110110 10010110 00001110 00000100 10011110 11101110 11110110 01001110 01100110 10011110 11000110 11110110 01001110 10100110 00101110 01011110 11000110 00000100 11110110 00101110 00000100 11110110 00110110 11001110 10000110 00010110 00000100 11101100 00011100 00101100 10110110 11010110 11110110 11110100 10110110 11110110 11000110 01110100 11001110 11001110 10100110 01001110 00001110 00100110 01001110 11110110 11101110 01110100 10000110 10110110 11100110 10010110 01110110 10100110 01011110 10011110 00011110 00000100 01110100 10000110 10010110 01110110 10100110 01011110 00100110 11110110 11101110 11110110 00001110 00000100 01110100 10000110 01000110 11110110 00101110 00000100 00100110 10100110 01011110 01001110 00001110 00000100 11110110 01001110 10100110 10010110 00001110 11110110 00100110 00000100 10010110 11010110 00100110 10000110 11100110 10000110 01011110 00000100 10100110 11101110 10010110 01011110 00100110 11101110 10000110 01001110 00001110 00000100 01110100 00110110 10000110 01110110 10000110 01000110 00000100 11010110 10000110 01110110 00100110 10100110 01010110 00000100 00110110 10011110 01000110 00000100 11110110 00101110 00000100 01110100 11110110 11101110 10000110 01001110 01000110 00000100 01110100 01011110 01001110 10000110 10010110 11000110 10011110 01001110 00001110 11001110 00000100 10100110 10010110 01000110 10100110 10010110 11000110 00000100 01011110 00000100 10011110 00110110 01011110 10100110 10010110 01110110 00000100 01110100 10010110 11010110 11001110 11101110 10000110 11010110 10100110 10010110 11000110 00000100 01010110 10000110 00101110 10010110 11101110"


def space_rem(lista):
    nospace =[]
    for i in range(0, len(lista)):
        if lista[i] != " ":
            nospace.append(lista[i])
    nospace.reverse()
    return nospace

def split_code(lista):
    kod_clean_str = "".join(space_rem(lista))
    splited_code =[]
    for i in range(0, len(kod_clean_str), 8):
        splited_code.append(kod_clean_str[i: i+8])
    return splited_code


splitted = split_code(kod)
uni_kod = []

for kod8 in splitted:
    uni_kod.append(unichr((int(kod8, 2))))

print "".join(uni_kod)

#xyzenigma.wordpress.com/lgr842
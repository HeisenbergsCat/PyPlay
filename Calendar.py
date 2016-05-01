import time

data = "11/16/1984"

def tryagain():
    try_check = raw_input("Want to try again? Y/N")
    try_check = try_check.upper()

    if try_check == "Y":
        return True
    elif try_check == "N":
        return False

if tryagain() == True:
    print "Hahaha, spoko"
else:
    print "Pussy!"

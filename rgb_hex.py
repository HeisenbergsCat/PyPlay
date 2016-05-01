"""
RGB to HEX Converter.
Marcin Stepien
05.04.2016
"""

## Tutaj pytamy uzytkownika o wartosc i ja zwracamy.
## Jak gupek wpisze zla wartos, ma jeszcze szanse (chociaz nie zasluguje)

def val_input(color, mode):
    invalid_msg = "Incorrect value!"
    error_check = False
    while error_check == False:
        print color.upper()
        out_value = int(raw_input("Input value: "))
        if mode == "1":

            if out_value > 255 or out_value < 0:
                print invalid_msg, "Try again (0-255)"
            else:
                error_check = True
                return out_value

        elif mode =="2":

            if len(str(out_value)) != 6:
                print invalid_msg, "Try again (6 hex digits)"
            else:
                error_check = True
                return out_value

## Tutaj zapisujemy do slownika wartosci RGB albo HEX uzywajac val_input.
## Tacy jestesmy zajebisci

def write_color_values(mode):

    color_values = {
        "red" : 0,
        "green" : 0,
        "blue" : 0,
        }
    hex_value = 0

    colors = color_values.keys()

    if mode == "1":
        for i in range(0, len(colors)):
            color_values[colors[i]] = val_input(colors[i], mode)
        return color_values

    elif mode == "2":
        hex_value = val_input("HEX", mode)
        return hex_value



def rgb_to_hex():

    values = write_color_values("1")
    color_sum = (values["red"] << 16 ) + (values["green"] << 8) + values["blue"]
    hexed_rgb  =  hex(color_sum)[2:].upper()

    print "Your colors in hex: ", hexed_rgb

def hex_to_rgb():

    hex_val = write_color_values("2")

    print hex_val

    two_hex_digits = 2**8

    blue = (hex_val % two_hex_digits)
    hex_val = hex_val >> 8
    green = (hex_val % two_hex_digits)
    hex_val = hex_val >> 8
    red = (hex_val % two_hex_digits)

    print "Red: %s Green: %s Blue: %s" % (red, green, blue)



## start

def main_program():

    error_check = False
    while error_check == False:

        choice = raw_input("Press 1 for RGB to HEX, press 2 for HEX to RGB: ")

        if choice == "1":
            rgb_to_hex()
            error_check = True
        elif choice == "2":
            hex_to_rgb()
            error_check = True
        elif choice =="quit":
            print "Bye!"
            error_check = True
        else:
            print "Wrong input, try again"
            my_list = range(10)

main_program()

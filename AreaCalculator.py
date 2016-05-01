"""This is an area calculator
It calculates areas"""

from math import pi
from time import sleep
from datetime import datetime
from random import randrange

# declaring global variables
now = datetime.now()
hint =  "Don't forget to include the correct units! \nExiting..."

def greeting():
  print "Area calculator on line and fully operational"
  print "%s/%s/%s %s:%s" % (now.month, now.day, now.year, now.hour, now.minute)
  print ""

def usr_choice():
  option = raw_input("Enter T for triangle, C for circle: ")
  option = option.upper()
  return option

def calculate_triangle():
  base = float(raw_input("Enter base: "))
  height = float(raw_input("Enter height: "))
  tri_area = (base*height) / 2
  baking(5)
  print "Area of your triangle: %.2f \n%s" % (tri_area, hint)


def calculate_circle():
  radius = float(raw_input("Enter radius: "))
  circ_area = pi * (radius ** 2)
  baking(5)
  print "Area of your circle: %.2f \n%s" % (circ_area, hint)

def baking(time):
  bar = ["-"] * time
  for i in range(0, len(bar)):
    sleep(randrange(1,4,1))
    bar[i] = "I"
    print "".join(bar)
  print "BAKED!"
  sleep(1)

def body():
  greeting()
  choice = usr_choice()

  if choice == "T":
    calculate_triangle()
  elif choice == "C":
    calculate_circle()
  else:
    print "Can't You type ?"

body()

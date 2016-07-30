import datetime
import random
from random import shuffle
from tkinter import *
import InputBox

s = "Result:\n"

t = datetime.datetime.now()  # get the current date/time
Y = t.strftime("%Y")  # current 4-digit year
m = t.strftime("%m")  # current month
d = t.strftime("%d")  # day of month
w = t.strftime("%w")  # day of week

# use list to create an array for month
month = ["January", "February", "March", "April",
         "May", "June", "July", "August", "September",
         "October", "November", "December"]

# use tuple to create an array for days
day = ("1st", "2nd", "3rd", "4th", "5th", "6th", "7th",
       "8th", "9th", "10th", "11th", "12th", "13th",
       "14th", "15th", "16th", "17th", "18th", "19th",
       "20th", "21st", "22nd", "23rd", "24th", "25th",
       "26th", "27th", "28th", "29th", "30th", "31st")

# use dictionary to create an associate array for weekdays
week = {"0": "Sunday", "1": "Monday", "2": "Tuesday",
        "3": "Wednesday", "4": "Thursday", "5": "Friday",
        "6": "Saturday"}
# int() does type cast
msg = "Today is " + week[w] + " the " + day[int(d)-1] + " day of " + month[int(m) - 1]\
      + ", " + Y + "."

s += msg + "\n"

# SuperLotto
z = []
for i in range(1, 48):
    z.insert(i, i)
(InputBox.ShowDialog("How many drawing(s)? "))
n = int(InputBox.GetInput())
j = 0
while j < n:
    r = ""
    shuffle(z)
    for i in range(0, 5):
        r = r + str(z[i]) + " "
    r = r + "mega: " + str(random.randint(0, 27)) + "\n"
    s += r
    j = j + 1

# Message Box Code#######

root = Tk()
root.title('Message Box')
Label(root, justify=LEFT, text=s).grid(padx=10, pady=10)

root.mainloop()


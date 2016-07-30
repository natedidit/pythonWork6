from tkinter import *

s = "Result: \n"




lsta =[ 1, 2, 3, 4, 5 ]
s += str((len(lsta), lsta.count(3))) + "\n"

lstb = lsta
s += str((lsta, lstb)) + "\n"
s += str((lsta == lstb)) + "\n"

lsta[2] = 7
s += str((lsta, lstb)) + "\n"

lstb.insert(4, 9)
s += str((lsta, lstb)) + "\n"

lsta.remove(7)
s += str((lsta, lstb)) + "\n"

lstb.pop(3)
s += str((lsta, lstb)) + "\n"

del lsta[:]
del lstb[:]

print()
tupa = ("dog", "cat", "horse", "pig", "rat", "cow")
tupb = tupa
s += str((tupa, tupb)) + "\n"
s += str((tupa == tupb)) + "\n"

tupa = None
tupb = None
dica = {"cis245": "Perl Programming",
        "cis246": "PHP Programming",
        "cis247": "Python Programming"}
s += str((dica.keys())) + "\n"
s += str((dica.values())) + "\n"
s += str((dica.items())) + "\n"
s += str(('cis247' in dica)) + "\n"
dicb = dica.copy()
s += str((dica == dicb)) + "\n"
dica.clear()
dicb.clear()
s += str(("lsta is", lsta, "lstb is", lstb)) + "\n"
s += str(("tupa is", tupa, "tupb is", tupb)) + "\n"
s += str(("dica is", dica, "dicb is", dicb)) + "\n"
s += str(("\n\nObject deleted...\n")) + "\n"
del lsta
del lstb
del tupa
del tupb
del dica
del dicb

# Message Box Code#######

root = Tk()
root.title('Message Box')
Label(root, justify=LEFT, text=s).grid(padx=10, pady=10)

root.mainloop()


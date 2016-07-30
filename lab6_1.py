import InputBox
from tkinter import *
s = "Result: \n"

lst = [1, 2, 3, 4, 5]
InputBox.ShowDialog("Enter an integer (0-4): ")
number = InputBox.GetInput()
a = "You selected", lst[int(number)], "!", "\n"

tup = ("dog", "cat", "horse", "pig", "rat", "cow")
InputBox.ShowDialog("Enter another integer (0-5): ")
animal = str(InputBox.GetInput())
b = "You picked", tup[int(animal)], "!", "\n"

dic = {"cis245": "Perl Programming", "cis246": "PHP Programming",
       "cis247": "Python Programming"}
InputBox.ShowDialog("Enter a course (e.g., cis245): ")
course = InputBox.GetInput()

c = "You selected", dic[course], "!", "\n"

# Message Box Code#######

root = Tk()
root.title('Message Box')
Label(root, justify=LEFT, text=(s, a, b, c)).grid(padx=10, pady=10)

root.mainloop()

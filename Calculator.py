from tkinter import *

fonts = ["Times new Roman", "Verdana", "Comic Sans Ms", "Arial", "Impact"]
my_font = ("Comic Sans Ms", 30, "roman")


class Main():
    def __init__(self, parent):
        self.parent = parent

        self.mText = StringVar()
        self.parent.title("Calculator")

        self.createWidgets()

    def createWidgets(self):
        Entry(self.parent, textvariable=self.mText, width=20, justify="right", font=my_font).grid(columnspan=4)

        Button(self.parent, text='Clear', height=2, width=5, font=my_font,
               command=self.reset).grid(row=1, column=0)
        Button(self.parent, text='<-Del', height=2, width=5, font=my_font,
               command=self.delete).grid(row=1, column=1)
        Button(self.parent, text='(', height=2, width=5, font=my_font,
               command=lambda: self.setText("(")).grid(row=1, column=2)
        Button(self.parent, text=')', height=2, width=5, font=my_font,
               command=lambda: self.setText(")")).grid(row=1, column=3)

        Button(self.parent, text='7', height=2, width=5, font=my_font,
               command=lambda: self.setText("7")).grid(row=2, column=0)
        Button(self.parent, text='4', height=2, width=5, font=my_font,
               command=lambda: self.setText("4")).grid(row=3, column=0)
        Button(self.parent, text='1', height=2, width=5, font=my_font,
               command=lambda: self.setText("1")).grid(row=4, column=0)
        Button(self.parent, text='0', height=2, width=5, font=my_font,
               command=lambda: self.setText("0")).grid(row=5, column=0)

        Button(self.parent, text='8', height=2, width=5, font=my_font,
               command=lambda: self.setText("8")).grid(row=2, column=1)
        Button(self.parent, text="5", height=2, width=5, font=my_font,
               command=lambda: self.setText("5")).grid(row=3, column=1)
        Button(self.parent, text="2", height=2, width=5, font=my_font,
               command=lambda: self.setText("2")).grid(row=4, column=1)
        Button(self.parent, text='.', height=2, width=5, font=my_font,
               command=lambda: self.setText(".")).grid(row=5, column=1)

        Button(self.parent, text='9', height=2, width=5, font=my_font,
               command=lambda: self.setText("9")).grid(row=2, column=2)
        Button(self.parent, text='6', height=2, width=5, font=my_font,
               command=lambda: self.setText("6")).grid(row=3, column=2)
        Button(self.parent, text='3', height=2, width=5, font=my_font,
               command=lambda: self.setText("3")).grid(row=4, column=2)
        Button(self.parent, text='=', height=2, width=5, font=my_font,
               command=self.calc).grid(row=5, column=2)

        Button(self.parent, text='÷', height=2, width=5, font=my_font,
               command=lambda: self.setText("/")).grid(row=2, column=3)
        Button(self.parent, text='×', height=2, width=5, font=my_font,
               command=lambda: self.setText("*")).grid(row=3, column=3)
        Button(self.parent, text='-', height=2, width=5, font=my_font,
               command=lambda: self.setText("-")).grid(row=4, column=3)
        Button(self.parent, text='+', height=2, width=5, font=my_font,
               command=lambda: self.setText("+")).grid(row=5, column=3)

    def delete(self):
        self.mText.set(self.mText.get()[:-1])

    def reset(self):
        self.mText.set("")

    def setText(self, text):
        curText = self.mText.get()
        if curText == "Error":
            self.mText.set(text)
        else:
            self.mText.set(curText + text)

    def calc(self):
        try:
            self.mText.set(eval(self.mText.get()))
        except:
            self.mText.set("Error")


if __name__ == '__main__':
    root = Tk()
    Main(root)
    root.mainloop()

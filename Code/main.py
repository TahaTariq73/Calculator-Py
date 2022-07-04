from tkinter import *
from btns import btns

class GUI(Tk):

    screenText = ""
    def __init__(self):
        super().__init__()

    def window(self):
        """This will make a window"""
        width = 577
        height = 455
        self.geometry(f"{width}x{height}")
        self.resizable(False, False)
        self.title("Calculator")
        self.wm_iconbitmap("icon.ico")
        self.config(background="#363636", padx=15, pady=15)

    def screen(self):
        """This will create a screen in our calculator"""
        frame1 = Frame(self, bg="#9fb096", pady=3, padx=8)
        frame1.pack(fill=BOTH, side=TOP, padx=7, pady=4)

        self.call = 0
        self.calcl = StringVar()
        self.ans = StringVar()
        self.calcl.set("000000000000")
        self.ans.set("0")

        self.sc1 = Label(frame1, textvariable=self.calcl, bg="#9fb096", font=('Sans Serif', 13, 'bold'))
        self.sc1.pack(anchor=NW, pady=5)
        self.sc2 = Label(frame1, textvariable=self.ans, bg="#9fb096", pady=7, font=('Sans Serif', 13, 'bold'))
        self.sc2.pack(anchor=SE, pady=5)

    def buttons(self):
        """This will add buttons in our calculator"""
        frame2 = Frame(self, pady=5, padx=0, background="#363636")
        frame2.pack(fill=BOTH, side=BOTTOM)

        for i in btns:
            btn = Button(frame2, text=i['txt'], command= lambda x=i['txt'], y=i['type']: self.engine(x, y),
                         font=('Sans Serif', 10, 'bold'), width=14, pady=13,
            bg=i['color'], fg="White", borderwidth=0)
            btn.grid(row=i['row'], column=i['col'], pady=7, padx=10)

    def engine(self, txt, type):
        """This will handle all the logic of calculator"""
        if type == "ope":
            self.handle_operators(txt)
        elif type == "func":
            self.handleFunctions(txt)

        self.updateScreen(txt, type)

    def updateScreen(self, txt, type):
        """This will update the screen as needed"""
        if type != "func":
            self.screenText += txt

        self.calcl.set(self.screenText)
        self.sc1.update()
        self.sc2.update()

    # For handling function according to the button
    def handle_operators(self, txt):
        try:
            numbers = self.screenText.split(self.operator)
            confirmNo = self.point(numbers[0], numbers[1])
            self.screenText = str(self.handle_calculations(confirmNo[0], self.operator, confirmNo[1]))
            self.operator = txt
            self.call = 0
            return
        except:
            self.call += 1
            self.operator = txt

    def handleFunctions(self, txt):
        if txt == "=":
            try:
                numbers = self.screenText.split(self.operator)
                confirmNo = self.point(numbers[0], numbers[1])
                self.ans.set(self.handle_calculations(confirmNo[0], self.operator, confirmNo[1]))
            except Exception as err:
                self.ans.set("Error")

        elif txt == "C":
            self.screenText = ""

        elif txt == "⌫":
            lenght = len(self.screenText)
            self.screenText = self.screenText[:(lenght-1)]

        elif txt == "Blast":
            self.destroy()

    def handle_calculations(self, num1, ope, num2):
        """This function perfom calculation and return it"""

        if ope == "x":
            return int(num1) * int(num2)
        elif ope == "+":
            return int(num1) + int(num2)
        elif ope == "-":
            return int(num1) - int(num2)
        elif ope == "÷":
            return int(num1) / int(num2)
        elif ope == "%":
            return (int(num1) / int(num2)) * 100

    def point(self, x, y):
        """This will confirm the number by checking point"""
        try:
            nx = x.split('.')
            ny = y.split('.')
            n1 = int(nx[0]) + ((int(nx[1])/10))
            n2 = int(ny[0]) + ((int(ny[1])/10))
            return [n1, n2]
        except Exception as err:
            return [x, y]

if __name__ == '__main__':
    windw = GUI()
    windw.window()
    windw.screen()
    windw.buttons()
    windw.mainloop()


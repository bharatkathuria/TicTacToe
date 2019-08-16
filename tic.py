from tkinter import *

root = Tk()
root.title("Tic Tac Toe")
player=True
status=None
count=0

class TicTacToe:
    def __init__(self,master):
        frame=Frame(master)

        menu1 = Menu(root)
        root.config(menu=menu1)

        subMenu = Menu(menu1)
        menu1.add_cascade(label="File", menu=subMenu)
        subMenu.add_command(label="New... ", command=self.refreshWindow)
        subMenu.add_separator()
        subMenu.add_command(label="Exit...", command=root.quit)

        self.B1 = Button(frame, width=10, height=5, bg="white", command= lambda: self.swapturn(self.B1))
        self.B2 = Button(frame, width=10, height=5, bg="white", command= lambda: self.swapturn(self.B2))
        self.B3 = Button(frame, width=10, height=5, bg="white", command= lambda: self.swapturn(self.B3))
        self.B4 = Button(frame, width=10, height=5, bg="white", command= lambda: self.swapturn(self.B4))
        self.B5 = Button(frame, width=10, height=5, bg="white", command= lambda: self.swapturn(self.B5))
        self.B6 = Button(frame, width=10, height=5, bg="white", command= lambda: self.swapturn(self.B6))
        self.B7 = Button(frame, width=10, height=5, bg="white", command= lambda: self.swapturn(self.B7))
        self.B8 = Button(frame, width=10, height=5, bg="white", command= lambda: self.swapturn(self.B8))
        self.B9 = Button(frame, width=10, height=5, bg="white", command= lambda: self.swapturn(self.B9))

        self.B1.grid(row=0, column=0)
        self.B2.grid(row=0, column=1)
        self.B3.grid(row=0, column=2)
        self.B4.grid(row=1, column=0)
        self.B5.grid(row=1, column=1)
        self.B6.grid(row=1, column=2)
        self.B7.grid(row=2, column=0)
        self.B8.grid(row=2, column=1)
        self.B9.grid(row=2, column=2)

        frame.pack()

    def swapturn(self,b):
        global player
        global status
        global count

        if (player):
            statusBar['text'] = "TURN:  Player 2 "
            count += 1
            player = False
            b.config(text="X", state=DISABLED, bg="yellow")
        else:
            statusBar['text'] = "TURN:  Player 1 "
            count += 1
            player = True
            b.config(text="O", state=DISABLED, bg="cyan")

        if (self.B1['text'] == self.B2['text'] == self.B3['text'] == "X" or self.B4['text'] == self.B5['text'] == self.B6['text'] == "X" or self.B7[
            'text'] ==
                self.B8['text'] == self.B9['text'] == "X" or
                self.B1['text'] == self.B4['text'] == self.B7['text'] == "X" or self.B2['text'] == self.B5['text'] == self.B8['text'] == "X" or self.B3[
                    'text'] == self.B6['text'] == self.B9['text'] == "X" or
                self.B1['text'] == self.B5['text'] == self.B9['text'] == "X" or self.B3['text'] == self.B5['text'] == self.B7['text'] == "X"):
            status = "win"
            statusBar['text'] = "Player 1 Won..."
            statusBar['bg'] = "lightgreen"
            print("player one is wiinner")

        if (self.B1['text'] == self.B2['text'] == self.B3['text'] == "O" or self.B4['text'] == self.B5['text'] == self.B6['text'] == "O" or self.B7[
            'text'] ==
                self.B8['text'] == self.B9['text'] == "O" or
                self.B1['text'] == self.B4['text'] == self.B7['text'] == "O" or self.B2['text'] == self.B5['text'] == self.B8['text'] == "O" or self.B3[
                    'text'] == self.B6['text'] == self.B9['text'] == "O" or
                self.B1['text'] == self.B5['text'] == self.B9['text'] == "O" or self.B3['text'] == self.B5['text'] == self.B7['text'] == "O"):
            print("player two is wiinner")
            statusBar['text'] = "Player 2 Won..."
            statusBar['bg'] = "lightgreen"
            status = "win"

        if (status == "win"):
            self.B1['state'] = self.B2['state'] = self.B3['state'] = self.B4['state'] = self.B5['state'] = self.B6['state'] = self.B7['state'] = self.B8[
                'state'] = self.B9['state'] = DISABLED
            return

        if (count == 9):
            print("game Draw...")
            statusBar['text'] = "Game Draw...."
            statusBar['bg']="orange"

    def refreshWindow(self):
        self.B1.config(text="", state=NORMAL, bg="white")
        self.B2.config(text="", state=NORMAL, bg="white")
        self.B3.config(text="", state=NORMAL, bg="white")
        self.B4.config(text="", state=NORMAL, bg="white")
        self.B5.config(text="", state=NORMAL, bg="white")
        self.B6.config(text="", state=NORMAL, bg="white")
        self.B7.config(text="", state=NORMAL, bg="white")
        self.B8.config(text="", state=NORMAL, bg="white")
        self.B9.config(text="", state=NORMAL, bg="white")
        global status
        global player
        global count
        player=True
        status=None
        count=0
        statusBar['text']="TURN:   Player 1"
        statusBar['bg']="white"

statusBar = Label(root, text="TURN:   Player 1", bd=1, height=5, relief=SUNKEN, anchor=W)
statusBar.pack(side=BOTTOM, fill=X)

obj = TicTacToe(root)

root.mainloop()
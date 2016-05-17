import tkinter as tk

class GUI():
    rows = 8
    columns = 8
    lightColor = '#DDB88C'
    darkColor = '#A66D4F'
    squareDim = 64

    def __init__(self, root):
        self.root = root
        canvasWidth = self.columns * self.squareDim
        canvasHeight = self.rows * self.squareDim
        self.canvas = tk.Canvas(root , height=canvasHeight,
                                width=canvasWidth, background='gray')
        self.canvas.pack(padx=8, pady=8)
        self.drawBoard()


    def drawBoard(self):
        color = self.darkColor
        for r in range(self.rows):
            color = self.lightColor if color == self.darkColor else \
                self.darkColor
            for c in range(self.columns):
                x1 = (c * self.squareDim)
                y1 = ((7 - r) * self.squareDim)
                x2 = x1 + self.squareDim
                y2 = y1 + self.squareDim
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color,
                                             tags='area')
                color = self.lightColor if color == self.darkColor else \
                    self.darkColor



root = tk.Tk()
root.title('Chess')
gui = GUI(root)
root.mainloop()


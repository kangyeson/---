import tkinter
import numPeople

class Start:
    def __init__(self, start):
        self.start = start

        # start 화면 이미지
        self.startImage = tkinter.PhotoImage(file="image/mainImage.png")
        self.startImagePlace = tkinter.Label(image=self.startImage)
        self.startImagePlace.place(x=-2, y=-2)

        # start 버튼
        self.startFont = tkinter.font.Font(size=11, weight="bold")
        self.startButton = tkinter.Button(self.start, text="시작하기", command=self.move, foreground="#9b95b7", width=10,
                                          repeatdelay=20, font=self.startFont)
        self.startButton.place(x=350, y=310)

        def move(self):
            startMove = numPeople.NumPeople(self.start)

        def play(self):
            self.start.mainloop()

if __name__ == '__main__':
    start = tkinter.Tk()
    start.title("Dutch")
    start.geometry("900x700")
    start.resizable(False,False)

    dutch = Start(start)
    dutch.play()



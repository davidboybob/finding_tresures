from tkinter import *
from PIL import ImageTk, Image

window = Tk()

window.title("Finding Tresure v1.0")
window.geometry("2048x1152+300+80")

data = {

}

styles = {
    "blue_color": "#4F92F5",
}


class Frame_main():
    # frame_main = None
    # frame_left = None

    def __init__(self, window):
        self.frame_left = Frame(window, relief="solid", bd=2)
        self.frame_left.pack(side="left", fill="both", expand=True)

        self.frame_main = Frame(window, width=1024, height=620)
        self.frame_main.pack(anchor="center", padx=15, pady=15)
        # frame_main.place(anchor='center', relx=0.5, rely=0.5)

        img = ImageTk.PhotoImage(Image.open("static/beach_bg.png"))
        label = Label(self.frame_main, image=img)
        label.image = img
        label.pack()
        
    

class Input_Data(Frame_main):
    def __init__(self, frame_left):
        self.frame_left = frame_left

    def input_label(self):
        print(self.frame_left)
        listbox = Listbox(self.frame_left, selectmode='extended')
        listbox.insert(0, "1번")
        listbox.insert(1, "2번")
        listbox.pack()


if __name__ == "__main__":
    frame = Frame_main(window)
    frame_left = frame.frame_left
    input_data = Input_Data(frame_left)
    input_data.input_label()

    window.mainloop()
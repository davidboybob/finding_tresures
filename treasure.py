from cgitb import text
from tkinter import *
from tkinter import messagebox
from turtle import width
from PIL import ImageTk, Image
import copy

window = Tk()

window.title("Finding Tresure v1.0")
window.geometry("1324x700+80+40")

photo_icon = PhotoImage(file = './static/precious_box_title_icon.png')
window.iconphoto(False, photo_icon)

WIDTH = 1224
HEIGHT = 1024

# "이름": "[미션]"
datas = {
    "박성진": [],
    "박윤영": [], 
    "이명석": [], 
    "정혜성": [], 
    "이자인": [], 
    "안정은": [], 
    "최지훈": [], 
    "이믿음": [], 
    "윤동희": [], 
    "서태규": [], 
    "한모란": []
}

styles = {
    "blue_color": "#4F92F5",
}

window.configure(bg=styles["blue_color"])

class Frame_main():
    # frame_main = None
    # frame_left = None
    def __init__(self, window):
        self.box_icon = ImageTk.PhotoImage(Image.open("./static/unboxing.png").resize((100, 50)))
        self.beach_img = ImageTk.PhotoImage(Image.open("./static/beach_bg.png").resize((1200, 680)))

        self.frame_left = Frame(window)
        self.frame_left.pack(side="left", fill="both", expand=True, padx=15, pady=15)

        self.frame_main = Frame(window)
        self.frame_main.pack(anchor="center", padx=15, pady=15)
        # frame_main.place(anchor='center', relx=0.5, rely=0.5)

        
        self.canvas = Canvas(self.frame_main, width=WIDTH, height=HEIGHT)
        self.canvas.pack()
        self.canvas.background = self.beach_img
        self.canvas.create_image(0, 0, anchor=NW, image=self.beach_img)
        # self.canvas.create_image(0, 0,image=self.box_icon)

        # self.label = Label(self.frame_main, image=img, width=1280, height=1049)
        # self.label.image = img
        # self.label.pack()        


    def close_box(self, index):
        print("close")
        self.canvas.delete(str(index))

    
    def open_box(self, x, y, index):
        
        # if self.box_switch == True:
        #     print()

        #     self.canvas.destroy()
        # elif self.box_switch == False:
        #     print(self.canvas.create_text(x, y, text="Open the box.", tags=index))
        #     box_switch = True
        # print("open")
        self.canvas.create_text(x, y, text="Open_box", tags=index)
        # print(self.canvas.tag_raise(index))
        # print(self.canvas.tag_lower(index))
        # self.canvas.bind("<B3-Motion>", self.close_box(index))    
        


    def main(self):
        total_count = 36
        self.box_switch = False
        for idx in range(total_count):
            place_x = idx % 6 * 180
            place_y = idx // 6 * 110
            secret_box = Button(self.frame_main, 
                                text = str(idx+1), 
                                image=self.box_icon, 
                                compound=BOTTOM, 
                                command=lambda idx_str=str(idx+1), place_x=place_x, place_y=place_y: self.open_box(place_x, place_y, idx_str))
            secret_box.place(x=(place_x+15), y=(place_y+15))
        # secret_box_canvas = self.canvas.create_window(10, 10, window=secret_box)


class Input_Data(Frame_main):
    def __init__(self, frame_left):
        self.frame_left = frame_left


    def set_member(self):
        self.join_member = Listbox(self.frame_left, selectmode='extended', height=11, selectforeground='white')

        for idx, data in enumerate(datas.items()):
            # print(idx, data[0])
            self.join_member.insert(idx, data[0])

        self.join_member.pack(fill="both", padx=15, pady=15)


    def input_label(self):
        label = Label(self.frame_left, text="참가자 목록")
        label.pack(anchor="w", padx=15)
        
        self.set_member()

    def entry_data(self):
        self.content = StringVar()
        self.entry = Entry(self.frame_left, textvariable=self.content)
        self.entry.pack(fill="both", padx=15, pady=15)


    def add_item(self, event=1):
        if self.content.get() != "":
            self.join_member.insert(END, self.content.get())
            self.content.set("")


    def delete_selected(self):
        try:
            # print(self.join_member.curselection()[-1])
            # selected_value = self.join_member.get(self.join_member.curselection())
            selected_index = self.join_member.curselection()[0]
            self.join_member.delete(self.join_member.curselection()[0], self.join_member.curselection()[-1])
            self.join_member.select_set(selected_index)
            # self.join_member.activate(selected_index - 1)

        except Exception as err:
            print(err)
            pass

    def reset_member(self):
        self.join_member.delete(0, END)
        for idx, data in enumerate(datas.items()):
            self.join_member.insert(idx, data[0])



    def buttons(self):
        self.frame_member_button = Frame(self.frame_left)
        self.frame_member_button.pack()

        add_button = Button(self.frame_member_button, text="추가", command=self.add_item)
        delete_button = Button(self.frame_member_button, text="삭제", command=self.delete_selected)
        reset_button = Button(self.frame_member_button, text="초기화", command=self.reset_member)

        add_button.grid(row=0, column=0, padx=5)
        delete_button.grid(row=0, column=1, padx=5)
        reset_button.grid(row=0, column=2, padx=5)




if __name__ == "__main__":
    frame = Frame_main(window)
    frame.main()

    frame_left = frame.frame_left

    input_data = Input_Data(frame_left)
    input_data.input_label()
    input_data.entry_data()
    input_data.buttons()

    window.mainloop()
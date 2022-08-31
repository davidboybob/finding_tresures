from cgitb import text
from tkinter import *
from tkinter import messagebox
from turtle import width
from PIL import ImageTk, Image
import copy

window = Tk()

window.title("Finding Tresure v1.0")
window.geometry("1400x750+40+20")

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
    def __init__(self, window, msg):
        self.beach_img = ImageTk.PhotoImage(Image.open("./static/beach_bg.png").resize((1100, 680)))
        self.box_icon = ImageTk.PhotoImage(Image.open("./static/unboxing.png").resize((100, 50)))
        self.bang_icon = ImageTk.PhotoImage(Image.open("./static/Bang.png").resize((100, 50)))

        self.frame_left = Frame(window, width=300, height=500)
        self.frame_left.pack(side="left", fill="both", padx=15, pady=15)
        self.frame_left.propagate(0)

        self.frame_main = Frame(window, width=1100, height=680)
        self.frame_main.pack(anchor="center", padx=15, pady=15)
        self.frame_main.propagate(0)
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


    def append_log(self, msg):
        pass


    def open_box(self, x, y, index):
        self.button_lists[index].configure(image = self.bang_icon)
        self.append_log("박스를 선택했습니다.")
        # Logs.append_log("%s 박스를 선택했습니다." %(index+1))
        

    def main(self):
        total_count = 36
        self.box_switch = False
        self.button_lists = []

        for idx in range(total_count):
            place_x = idx % 6 * 180
            place_y = idx // 6 * 110
            secret_box = Button(self.frame_main,
                                text = str(idx+1),
                                image=self.box_icon,
                                compound=BOTTOM,
                                command=lambda index=idx, place_x=place_x, place_y=place_y: self.open_box(place_x, place_y, index))
            self.button_lists.append(secret_box)
            # print(secret_box)
            # secret_box.place(x=(place_x+15), y=(place_y+15))
            # self.open_box_label.place(x=place_x+15, y=place_y + 15)
        # secret_box_canvas = self.canvas.create_window(10, 10, window=secret_box)
        
        for idx, button in enumerate(self.button_lists):
            place_x = idx % 6 * 180
            place_y = idx // 6 * 110
            button.place(x=(place_x+15), y=(place_y+15))


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
            self.join_member.see(END)


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


class Logs(Frame_main):
    def __init__(self, frame_left):
        self.frame_left = frame_left
        self.msg = Frame_main()


    def set_logs_list_box(self):
        self.logs_box = Listbox(self.frame_left, width=250)
        self.logs_box.pack(fill="both", padx=15, pady=15)


    def append_log(self):
        self.logs_box.insert(END, self.msg)
        self.logs_box.update()
        self.logs_box.see(END)
    

if __name__ == "__main__":
    frame = Frame_main(window)
    frame.main()

    frame_left = frame.frame_left

    input_data = Input_Data(frame_left)
    input_data.input_label()
    input_data.entry_data()
    input_data.buttons()

    logs = Logs(frame_left)
    logs.set_logs_list_box()
    # logs.append_log("testset")

    window.mainloop()
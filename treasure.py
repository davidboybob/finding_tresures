from tkinter import *
from PIL import ImageTk, Image
import random
import os

window = Tk()

window.title("Finding Tresure v1.0")
window.geometry("1400x750+40+20")

photo_icon = PhotoImage(file = './static/precious_box_title_icon.png')
window.iconphoto(False, photo_icon)

WIDTH = 1224
HEIGHT = 1024

# "이름": "[미션]"
members = {
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

number_of_box = 36

treasures = {
    "key1": "지각 초기화",
    "key2": "결석 초기화",
    "key3": "지각/결석 초기화",
    "mission1": "엄마에게 사랑한다고 이야기하기.",
    "mission2": "아빠에게 사랑한다고 이야기하기.",
    "mission3": "+1 선행하기",
    "mission4": "기부하기"
}

styles = {
    "blue_color": "#4F92F5",
}

window.configure(bg=styles["blue_color"])

class Frame_main():
    def __init__(self, window):
        self.button_counts = 0
        self.button_lists = []

        self.beach_img = ImageTk.PhotoImage(Image.open("./static/beach_bg.png").resize((1100, 680)))
        self.box_icon = ImageTk.PhotoImage(Image.open("./static/unboxing.png").resize((100, 50)))
        self.bang_icon = ImageTk.PhotoImage(Image.open("./static/Bang.png").resize((100, 50)))
        self.jackpot_icon = ImageTk.PhotoImage(Image.open("./static/jackpot.png").resize((100, 50)))
        self.shovel_icon = ImageTk.PhotoImage(Image.open("./static/shovel.png").resize((100, 50)))

        self.frame_left = Frame(window, width=300, height=500)
        self.frame_left.pack(side="left", fill="both", padx=15, pady=15)
        self.frame_left.propagate(0)

        self.frame_main = Frame(window, width=1100, height=680)
        self.frame_main.pack(anchor="center", padx=15, pady=15)
        self.frame_main.propagate(0)

        self.canvas = Canvas(self.frame_main, width=WIDTH, height=HEIGHT)
        self.canvas.pack()
        self.canvas.background = self.beach_img
        self.canvas.create_image(0, 0, anchor=NW, image=self.beach_img)
        # self.canvas.create_image(0, 0,image=self.box_icon)

        # self.label = Label(self.frame_main, image=img, width=1280, height=1049)
        # self.label.image = img
        # self.label.pack() 
         
        input_data = Input_Member(self.frame_left)
        input_data.input_label()
        self.join_member = input_data.set_member()
        input_data.entry_data()
        input_data.set_buttons()      


    def shuffle_treasures(self):
        treasures_lists = list(treasures.keys())
        random.shuffle(treasures_lists)        
        self.treasures_lists = treasures_lists

        random_numbers = list(range(1, number_of_box))
        random.shuffle(random_numbers)
        self.random_numbers =  random_numbers[:len(treasures_lists)]

        return [self.treasures_lists, self.random_numbers]


    def set_logs_list_box(self):
        self.logs_box = Listbox(self.frame_left, width=250, height=20)
        self.logs_box.pack(fill="both", padx=15, pady=15)


    def append_log(self, msg):
        self.logs_box.insert(END, msg)
        self.logs_box.update()
        self.logs_box.see(END)


    def close_box(self, index):
        # self.canvas.delete(str(index))
        pass


    def open_box(self, x, y, index):
        members_size = self.join_member.size()
        now_select_person = self.button_counts % members_size
        # print(self.join_member.curselection())
        self.join_member.selection_clear(0, END)
        now_person_name = self.join_member.get(now_select_person)
        self.button_counts += 1
        next_select_person = self.button_counts % members_size
        

        if (index + 1) in self.random_numbers:
            index_of_box = self.random_numbers.index(index + 1)
            # print(index_of_box)

            key_of_treasure = self.treasures_lists[index_of_box]
            value_text = treasures[key_of_treasure]

            if  key_of_treasure.find("key") != -1:
                self.button_lists[index].configure(image = self.jackpot_icon)
                self.append_log(f"{index + 1}번 박스를 선택했습니다." )
                self.append_log(f"{now_person_name}님 축하드립니다. 보물을 찾으셨습니다." )
                self.append_log(f" ♪（*＾-＾*） || {value_text}" )
                self.append_log(f"" )
                members[now_person_name].append(value_text)

            elif  key_of_treasure.find("mission") != -1:
                self.button_lists[index].configure(image = self.shovel_icon)
                self.append_log(f"{index + 1}번 박스를 선택했습니다." )
                self.append_log(f"{now_person_name}님 축하드립니다. 미션을 찾으셨습니다." )
                self.append_log(f"♥ {value_text} ♥" )
                self.append_log(f"" )
                members[now_person_name].append(value_text)

        else:
            self.button_lists[index].configure(image = self.bang_icon)
            self.append_log(f"{index + 1}번 박스를 선택했습니다." )
            self.append_log(f"{now_person_name}님 꽝입니다. ㅜㅜ" )
            self.append_log(f"" )
            
        # print(self.join_member.size())
        # print(type(self.join_member.size()))
        self.join_member.selection_set(next_select_person)

        print(members)


    def main(self):
        total_count = number_of_box
        self.box_switch = False

        for idx in range(total_count):
            place_x = idx % 6 * 180
            place_y = idx // 6 * 110
            secret_box = Button(self.frame_main,
                                text = str(idx+1),
                                image=self.box_icon,
                                compound=BOTTOM,
                                state = DISABLED,
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

        return self.button_lists


class Input_Member(Frame_main):
    def __init__(self, frame_left):
        self.frame_left = frame_left


    def set_member(self):
        self.join_member = Listbox(self.frame_left, selectmode='extended', height=11, selectforeground='white')

        for idx, data in enumerate(members.items()):
            # print(idx, data[0])
            self.join_member.insert(idx, data[0])

        self.join_member.pack(fill="both", padx=15, pady=15)

        self.join_member.select_set(0)

        return self.join_member


    def input_label(self):
        label = Label(self.frame_left, text="참가자 목록")
        label.pack(anchor="w", padx=15)
        
        # self.set_member()


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
        for idx, data in enumerate(members.items()):
            self.join_member.insert(idx, data[0])


    def set_buttons(self):
        self.frame_member_button = Frame(self.frame_left)
        self.frame_member_button.pack()

        add_button = Button(self.frame_member_button, text="추가", command=self.add_item)
        delete_button = Button(self.frame_member_button, text="삭제", command=self.delete_selected)
        reset_button = Button(self.frame_member_button, text="초기화", command=self.reset_member)

        add_button.grid(row=0, column=0, padx=5)
        delete_button.grid(row=0, column=1, padx=5)
        reset_button.grid(row=0, column=2, padx=5)
    

class Game_buttons(Frame_main):
    def __init__(self, frame_left, button_lists):
        self.frame_left = frame_left
        self.frame_game_button = Frame(self.frame_left, width=200)
        self.frame_game_button.pack()
        # self.frame_game_button.propagate(0)

        self.button_lists = button_lists


    def starting_games(self):
        self.start_button.configure(state = DISABLED)
        # self.start_button['state'] = DISABLED

        for button in self.button_lists:
            button.configure(state = NORMAL)

    def exit_games(self):
        window.quit()


    def save_win_members(self):
        win_logs = list(members.items())
        file_path = os.path.dirname(os.path.abspath(__file__))

        with open('./당첨 기록.txt', 'w', encoding="utf-8") as f:
            for items in win_logs:
                if len(items[1]) > 0:
                    f.writelines(f"{items[0]}: {', '.join(items[1])} \n")
            # f.writelines("test")


    def set_buttons(self):
        self.start_button = Button(self.frame_game_button, text="게임 시작", command=self.starting_games)
        self.exit_button = Button(self.frame_game_button, text="게임 종료", command=self.exit_games)
        self.save_button = Button(self.frame_game_button, text="당첨 저장", command=self.save_win_members)

        self.save_button.grid(row=0, column=0, padx=30)
        self.start_button.grid(row=0, column=1, padx=5)
        self.exit_button.grid(row=0, column=2, padx=5)


if __name__ == "__main__":
    frame = Frame_main(window)
    frame.shuffle_treasures()
    button_lists = frame.main()

    frame_left = frame.frame_left

    # input_data = Input_Member(frame_left)
    # input_data.input_label()
    # input_data.entry_data()
    # input_data.set_buttons()

    frame.set_logs_list_box()

    game_buttons = Game_buttons(frame_left, button_lists)
    game_buttons.set_buttons()

    window.mainloop()
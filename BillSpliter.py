import tkinter
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("1440x1024")
app.resizable(False, False)
app.title('Button')

# background frame
frame_1 = customtkinter.CTkFrame(master=app,
                                 width=1440,
                                 height=1024,
                                 corner_radius=10,
                                 fg_color='#C5E4E7')

frame_1.place(x=0, y=0)

# white background frame
frame_2 = customtkinter.CTkFrame(
    width=920,
    height=481,
    corner_radius=25,
    fg_color='#FFFFFF',
    bg_color='#C5E4E7'
)
frame_2.place(x=260, y=271)

# greem frame on right handside
frame_3 = customtkinter.CTkFrame(
    width=413,
    height=417,
    corner_radius=15,
    fg_color='#00474B',
    bg_color='#FFFFFF'
)
frame_3.place(x=735, y=303)


def button_function_1():
    entry_1.delete(0, 'end')
    entry_2.delete(0, 'end')
    entry_3.delete(0, 'end')
    entry_4.delete(0, 'end')
    entry_5.delete(0, 'end')


def button_function_2():
    entry_1.delete(0, 'end')
    entry_1.insert(0, 5)


def button_function_3():
    entry_1.delete(0, 'end')
    entry_1.insert(0, 10)


def button_function_4():
    entry_1.delete(0, 'end')
    entry_1.insert(0, 15)


def button_function_5():
    entry_1.delete(0, 'end')
    entry_1.insert(0, 25)


def button_function_6():
    entry_1.delete(0, 'end')
    entry_1.insert(0, 50)


def submit(e):
    tip = float(entry_1.get())
    bill = float(entry_2.get())
    numb_of_ppl = int(entry_3.get())
    tip_amount = round((bill * tip / 100) / numb_of_ppl, 2)
    calculation = round((bill + (bill * tip / 100)) / numb_of_ppl, 2)
    test_tip = f'${tip_amount}'
    test_calculation = f'${calculation}'
    entry_4.insert(0, test_tip)
    entry_5.insert(0, test_calculation)


font_size = 36

app.bind('<Return>', submit)

# buttons
button_1 = customtkinter.CTkButton(master=app, text="Reset", text_font=('Space Mono', 20, 'bold'),
                                   command=button_function_1, corner_radius=5,
                                   text_color='black', hover_color='#71C9CE', fg_color='#0D686D', bg_color='#00474B',
                                   width=333, height=48)

button_2 = customtkinter.CTkButton(master=app, text="5%", text_font=('Space Mono', 24, 'bold'),
                                   command=button_function_2, corner_radius=5,
                                   text_color='white', hover_color='#71C9CE', fg_color='#00474B', width=117, height=48)

button_3 = customtkinter.CTkButton(master=app, text="10%", text_font=('Space Mono', 24, 'bold'),
                                   command=button_function_3, corner_radius=5,
                                   text_color='white', hover_color='#71C9CE', fg_color='#00474B', width=117, height=48)

button_4 = customtkinter.CTkButton(master=app, text="15%", text_font=('Space Mono', 24, 'bold'),
                                   command=button_function_4, corner_radius=5,
                                   text_color='white', hover_color='#71C9CE', fg_color='#00474B', width=117, height=48)

button_5 = customtkinter.CTkButton(master=app, text="25%", text_font=('Space Mono', 24, 'bold'),
                                   command=button_function_5, corner_radius=5,
                                   text_color='white', hover_color='#71C9CE', fg_color='#00474B', width=117, height=48)

button_6 = customtkinter.CTkButton(master=app, text="50%", text_font=('Space Mono', 24, 'bold'),
                                   command=button_function_6, corner_radius=5,
                                   text_color='white', hover_color='#71C9CE', fg_color='#00474B', width=117, height=48)

# entry inputs

entry_1 = customtkinter.CTkEntry(master=app, placeholder_text="Custom", text_font=('Space Mono', 20, 'bold'),
                                 corner_radius=5, fg_color="#F3F9FA", bg_color='white',
                                 text_color="#547878", width=117, height=55, justify="right", border_width=0)

entry_2 = customtkinter.CTkEntry(master=app, placeholder_text=0, text_font=('Space Mono', 24, 'bold'),
                                 corner_radius=5, fg_color="#F3F9FA", bg_color='white',
                                 text_color="#547878", width=379, height=48, justify="right", border_width=0)

entry_3 = customtkinter.CTkEntry(master=app, placeholder_text=0, text_font=('Space Mono', 24, 'bold'),
                                 corner_radius=5, fg_color="#F3F9FA", bg_color='white',
                                 text_color="#547878", width=379, height=48, justify="right", border_width=0)

entry_4 = customtkinter.CTkEntry(master=app, placeholder_text="$0.00", text_font=('Space Mono', 32, 'bold'),
                                 corner_radius=5, border_width=0, fg_color="#00474B", bg_color="#00474B",
                                 text_color="#26C2AE", placeholder_text_color='#26C2AE', width=215, height=71,
                                 justify="right")

entry_5 = customtkinter.CTkEntry(master=app, placeholder_text="$0.00", text_font=('Space Mono', 32, 'bold'),
                                 corner_radius=5, border_width=0, fg_color="#00474B", bg_color="#00474B",
                                 text_color="#26C2AE", placeholder_text_color='#26C2AE', width=215, height=71,
                                 justify="right")

# text lables
label_1 = customtkinter.CTkLabel(master=app, text="Total", text_font=('Space Mono', 16, 'bold'),
                                 fg_color="#00474B", text_color='white'
                                 )
label_2 = customtkinter.CTkLabel(master=app, text="/ person", text_font=('Space Mono', 13, 'bold'),
                                 fg_color="#00474B", text_color='#7F9D9F'
                                 )

label_3 = customtkinter.CTkLabel(master=app, text="Tip Amount", text_font=('Space Mono', 16, 'bold'),
                                 fg_color="#00474B", text_color='white'
                                 )

label_4 = customtkinter.CTkLabel(master=app, text="/ person", text_font=('Space Mono', 13, 'bold'),
                                 fg_color="#00474B", text_color='#7F9D9F'
                                 )

label_5 = customtkinter.CTkLabel(master=app, text="Bill", text_font=('Space Mono', 16, 'bold'),
                                 fg_color="white", width=40,
                                 height=24, text_color='#5E7A7D'
                                 )

label_6 = customtkinter.CTkLabel(master=app, text="Select Tip %", text_font=('Space Mono', 16, 'bold'),
                                 fg_color="white", width=40,
                                 height=24, text_color='#5E7A7D'
                                 )

label_7 = customtkinter.CTkLabel(master=app, text="Number of People", text_font=('Space Mono', 16, 'bold'),
                                 fg_color="white", width=40,
                                 height=24, text_color='#5E7A7D'
                                 )

label_8 = customtkinter.CTkLabel(master=app, text="S P L I", text_font=('Space Mono', 26, 'bold'),
                                 fg_color="#C5E4E7", width=40,
                                 height=44, text_color='#3D6666'
                                 )

label_9 = customtkinter.CTkLabel(master=app, text="T T E R", text_font=('Space Mono', 26, 'bold'),
                                 fg_color="#C5E4E7", width=40,
                                 height=44, text_color='#3D6666'
                                 )

label_10 = customtkinter.CTkLabel(master=app, text="For calculation press 'Enter' ",
                                  text_font=('Space Mono', 16, 'bold'),
                                  fg_color="#C5E4E7", width=40,
                                  height=44, text_color='#3D6666'
                                  )
#
# label_11 = customtkinter.CTkLabel(master=app, text="$", text_font=('Space Mono', 32, 'bold'),
#                                     width=40, height=24, fg_color="#00474B", bg_color="#00474B",
#                                     text_color="#26C2AE"
#                                )
#
# label_12 = customtkinter.CTkLabel(master=app, text="$", text_font=('Space Mono', 32, 'bold'),
#                                     width=40, height=24, fg_color="#00474B", bg_color="#00474B",
#                                     text_color="#26C2AE"
#                                )


# button place
button_1.place(x=940, y=657, anchor=tkinter.CENTER)
button_2.place(x=347, y=488, anchor=tkinter.CENTER)
button_3.place(x=481, y=488, anchor=tkinter.CENTER)
button_4.place(x=615, y=488, anchor=tkinter.CENTER)
button_5.place(x=347, y=553, anchor=tkinter.CENTER)
button_6.place(x=481, y=553, anchor=tkinter.CENTER)

# entry place
entry_1.place(x=615, y=553, anchor=tkinter.CENTER)
entry_2.place(x=478, y=377, anchor=tkinter.CENTER)
entry_3.place(x=478, y=687, anchor=tkinter.CENTER)
entry_4.place(x=1010, y=375, anchor=tkinter.CENTER)
entry_5.place(x=1010, y=508, anchor=tkinter.CENTER)

label_1.place(x=805, y=495, anchor=tkinter.CENTER)
label_2.place(x=810, y=525, anchor=tkinter.CENTER)
label_3.place(x=835, y=361, anchor=tkinter.CENTER)
label_4.place(x=810, y=391, anchor=tkinter.CENTER)
label_5.place(x=315, y=330, anchor=tkinter.CENTER)
label_6.place(x=368, y=440, anchor=tkinter.CENTER)
label_7.place(x=395, y=645, anchor=tkinter.CENTER)
label_8.place(x=720, y=145, anchor=tkinter.CENTER)
label_9.place(x=720, y=190, anchor=tkinter.CENTER)
label_10.place(x=720, y=990, anchor=tkinter.CENTER)
# label_11.place(x=940, y=378, anchor=tkinter.CENTER)
# label_12.place(x=940, y=510, anchor=tkinter.CENTER)


app.mainloop()

from tkinter import *
import tkinter.font as font


def con():
    temp_celsius = celsius_value.get()

    if(temp_celsius.replace('.','',1).isdigit()):
        error_msg.grid_forget()
        temp_fahrenheit = (float(temp_celsius) * 9/5) + 32
        output_fahrenheit.config(text = 'Temperature in Fahrenheit : ' + str(temp_fahrenheit))
    else:
        error_msg.grid(row=1, column=1)


def clear():
    celsius_value.delete(0,END)

root = Tk()
root.title("Celsius to Fahrenheit Converter")

root.configure(background='black')

description = Label(text = 'Celsius To Fahrenheit', fg = "black")
description.pack()

frame = Frame(root,bg="black")
frame.pack(pady = 20)


message_one = Label(frame, text = 'Enter Temperature in Celsius : ')
message_one.grid(row = 0, column = 0)

celsius_value = Entry(frame)
celsius_value.grid(row = 0, column = 1)


error_msg = Label(frame, text = 'Please enter valid number.', fg = 'red')


output_fahrenheit = Label(frame, font = font.Font(size = 12))
output_fahrenheit.grid(row = 2, column = 0, columnspan = 2, pady = 10)


submit_btn = Button(frame, text = 'Convert', width = 30, fg = "black", bg = "#D93E1D", bd = 0, padx = 20, pady = 10, command = con)
submit_btn.grid(row = 3, column = 0, columnspan = 2, pady = 10)
clear_btn = Button(frame, text = 'Clear', width = 30, fg = "black", bg = "red", bd = 0, padx = 20, pady = 10, command = clear)
clear_btn.grid(row = 4, column = 0, columnspan = 2, pady = 10)

root.geometry('500x250')
root.mainloop()

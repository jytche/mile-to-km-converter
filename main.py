from tkinter import *


def button_clicked():
    new_text = float(entry.get()) * 1.609344
    km_converted.config(text=new_text)


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=10, pady=10)

entry = Entry(width=5)
entry.insert(END, string="0")
print(entry.get())
entry.grid(column=1,row=0)

miles_label = Label(text="Miles", font=("Arial", 12, "bold"))
miles_label.grid(column=2, row=0)

km_converted = Label(text="0", font=("Arial", 12, "bold"))
km_converted.grid(column=1, row=1)

equal_label = Label(text="is equal to", font=("Arial", 12, "bold"))
equal_label.grid(column=0, row=1)

km_label = Label(text="Km", font=("Arial", 12, "bold"))
km_label.grid(column=2, row=1)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()

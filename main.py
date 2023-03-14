from tkinter import *

def miles_to_km():
  miles = float(miles_input.get())
  km = miles * 1.609
  calculation_label.config(text=f"{km}")

##How to use padding and grid to maniuplate GUI properties

window = Tk()
window.title("Miles to Kilometers Conversion Tool")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#Entry
miles_input = Entry(width=5)
miles_input.grid(column=2, row=0)
print(miles_input.get())

#Miles Label
miles_label = Label(text="Miles", font=("Arial", 12))
miles_label.config(text="Miles")
miles_label.grid(column=3, row=0)

#Is equal to Label

equal_to_label = Label(text="Is Equal to", font=("Arial", 12))
equal_to_label.config(text="Is Equal to")
equal_to_label.grid(column=0, row=1)

#Calculation Output Label

calculation_label = Label(text="0", font=("Arial", 12))
calculation_label.config(text="0")
calculation_label.grid(column=2, row=1)

#Kilometer Label
km_label = Label(text="Km", font=("Arial", 12))
km_label.config(text="Km")
km_label.grid(column=3, row=1)

#Button
  
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=2, row=2)

window.mainloop()

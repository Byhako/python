from tkinter import Tk, ttk, Label, Button, BOTTOM, X, TOP

window = Tk()
window.geometry('500x500') # anchura x altura

window.configure(bg='beige')

window.title('Aplicación')

# METODO PACK
# Label(window, text='Mi primer ventana', font=("Tahoma", 25, 'bold'), background='beige').pack()

# Label(
#   window,
#   text='Texto 20',
#   font=("Tahoma", 20),
#   cursor="dotbox",
#   fg='white',
#   background='blue'
# ).pack(side=TOP)

# Label(
#   window,
#   text='Texto 18',
#   font=("Tahoma", 18,),
#   fg='white',
#   background='green'
# ).pack(side=TOP)

# Label(
#   window,
#   text='Texto 16',
#   font=("Tahoma", 16,),
#   fg='white',
#   background='red'
# ).pack(side=TOP)

# Button(
#   window,
#   text='Salir',
#   fg='white',
#   background='black',
#   font=("Tahoma", 16,),
#   command=quit
# ).pack(side=BOTTOM, fill=X)


# METODO GRID

# Label(
#   frame1,
#   text='Grid 0 0',
#   font=("Tahoma", 16,),
#   fg='brown',
#   background='yellow'
# ).grid(column=0, row=0)

# Label(
#   frame1,
#   text='Grid 0 1',
#   font=("Tahoma", 16,),
#   fg='brown',
#   background='yellow'
# ).grid(column=0, row=1)

# Label(
#   frame1,
#   text='Grid 0 2',
#   font=("Tahoma", 16,),
#   fg='brown',
#   background='yellow'
# ).grid(column=0, row=2)



Label(
  window,
  text='Hola bebe',
  font=("Tahoma", 16,),
  fg='brown',
  background='yellow'
).place(x=150, y=20, width=200, height=50)

window.mainloop()
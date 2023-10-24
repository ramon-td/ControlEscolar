import tkinter as tk
from tkinter import messagebox, ttk

#-----------------------------------SETUP INICIAL-----------------------------------
main =tk.Tk()
main.title("Control Escolar")
main.config(width=700, height=400)


#-----------------------------------DEFINICIÓN DE PESTAÑAS-----------------------------------
#- - - - - - - - - - - - - - - - - - MAIN - - - - - - - - - - - - - - - - - - 
pestanas =ttk.Notebook(main)
pestanas.grid(row=0)
#- - - - - - - - - - - - - - - - - - LOGIN - - - - - - - - - - - - - - - - - - 
pestana_login = ttk.Frame(pestanas)
pestanas.add(pestana_login, text="Sesión")
pestanas.tab(0, state="normal")
#- - - - - - - - - - - - - - - - - - USUARIOS - - - - - - - - - - - - - - - - - - 
pestana_login = ttk.Frame(pestanas)
pestanas.add(pestana_login, text="Usuarios")
pestanas.tab(1, state="disabled")
#- - - - - - - - - - - - - - - - - - ALUMNOS - - - - - - - - - - - - - - - - - - 
pestana_login = ttk.Frame(pestanas)
pestanas.add(pestana_login, text="Alumnos")
pestanas.tab(2, state="disabled")
#- - - - - - - - - - - - - - - - - - MAESTROS - - - - - - - - - - - - - - - - - - 
pestana_login = ttk.Frame(pestanas)
pestanas.add(pestana_login, text="Maestros")
pestanas.tab(3, state="disabled")
#- - - - - - - - - - - - - - - - - - MATERIAS - - - - - - - - - - - - - - - - - - 
pestana_login = ttk.Frame(pestanas)
pestanas.add(pestana_login, text="Materias")
pestanas.tab(4, state="disabled")
#- - - - - - - - - - - - - - - - - - GRUPOS - - - - - - - - - - - - - - - - - - 
pestana_login = ttk.Frame(pestanas)
pestanas.add(pestana_login, text="Grupos")
pestanas.tab(5, state="disabled")
#- - - - - - - - - - - - - - - - - - HORARIO - - - - - - - - - - - - - - - - - - 
pestana_login = ttk.Frame(pestanas)
pestanas.add(pestana_login, text="Horario")
pestanas.tab(6, state="disabled")
#- - - - - - - - - - - - - - - - - - SALON - - - - - - - - - - - - - - - - - - 
pestana_login = ttk.Frame(pestanas)
pestanas.add(pestana_login, text="Salón")
pestanas.tab(7, state="disabled")
#- - - - - - - - - - - - - - - - - - CARRERA - - - - - - - - - - - - - - - - - - 
pestana_login = ttk.Frame(pestanas)
pestanas.add(pestana_login, text="Carrera")
pestanas.tab(8, state="disabled")
#- - - - - - - - - - - - - - - - - - PLANEACIÓN - - - - - - - - - - - - - - - - - - 
pestana_login = ttk.Frame(pestanas)
pestanas.add(pestana_login, text="Planeación")
pestanas.tab(9, state="disabled")




main.mainloop()
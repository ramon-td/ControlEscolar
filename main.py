import tkinter as tk

from tkinter import messagebox, ttk
from controlObjetos import Usuarios

#=============================================SETUP INICIAL=============================================
main =tk.Tk()
main.title("Control Escolar")
main.config(width=900, height=400)
#========================================================================================================

#=========================================DEFINICIÓN DE PESTAÑAS=========================================
#--------------------------------------------------MAIN--------------------------------------------------
pestanas =ttk.Notebook(main)
pestanas.grid(row=0)
#--------------------------------------------------LOGIN-------------------------------------------------
pestana_login = ttk.Frame(pestanas)
pestanas.add(pestana_login, text="Sesión")
pestanas.tab(0, state="normal")

#- - - - - - - - - - - - - - - - - - - - - - - Entries y etiquetas - - - - - - - - - - - - - - - - - - - -
username_label = tk.Label(pestana_login, text="Username: ")
username_entry = tk.Entry(pestana_login)
password_label = tk.Label(pestana_login, text="Password: ")
password_entry = tk.Entry(pestana_login, show="•")

#- - - - - - - - - - - - - - - - - - - - - - - - - - Botones - - - - - - - - - - - - - - - - - - - - - - -
login_button = tk.Button(pestana_login, text="Login", command=lambda:login())
login_button.configure(width=10)
#- - - - - - - - - - - - - - - - - - - - - - - - - - Posiciones - - - - - - - - - - - - - - - - - - - - - - -
username_label.grid(column=1, row=1, padx=10, pady=15)
password_label.grid(column=1, row=2, padx=10, pady=15)
username_entry.grid(column=2, row=1, padx=10, pady=15)
password_entry.grid(column=2, row=2, padx=10, pady=15)
login_button.grid(column=1, columnspan=2, row=4, padx=10, pady=15)

#------------------------------------------------------USUARIOS ----------------------------------------------
pestana_usuarios = ttk.Frame(pestanas)
pestanas.add(pestana_usuarios, text="Usuarios")
pestanas.tab(1, state="normal")
#- - - - - - - - - - - - - - - - - - - - - - - - - Entries y etiquetas - - - - - - - - - - - - - - - - - - - - - 
user_code_label = tk.Label(pestana_usuarios, text="Ingrese codigo de usuario: ")
user_id_label = tk.Label(pestana_usuarios, text="ID:")
user_nombre_label = tk.Label(pestana_usuarios, text="Nombre: ")
user_apellidoP_label = tk.Label(pestana_usuarios, text="Apellido Paterno: ")
user_apellidoM_label = tk.Label(pestana_usuarios, text="Apellido Materno: ")
user_email_label = tk.Label(pestana_usuarios, text="Email: ")
user_username_label = tk.Label(pestana_usuarios, text="Nombre de usuario: ")
user_password_label = tk.Label(pestana_usuarios, text="Password: ")
user_perfil_label = tk.Label(pestana_usuarios, text="Perfil: ")
user_code_entry = tk.Entry(pestana_usuarios)
user_id_entry = tk.Entry(pestana_usuarios, state="disabled")
user_nombre_entry = tk.Entry(pestana_usuarios, state="disabled")
user_apellidoP_entry = tk.Entry(pestana_usuarios, state="disabled")
user_apellidoM_entry = tk.Entry(pestana_usuarios, state="disabled")
user_email_entry = tk.Entry(pestana_usuarios, state="disabled")
user_username_entry = tk.Entry(pestana_usuarios, state="disabled")
user_password_entry = tk.Entry(pestana_usuarios, state="disabled", show="•")
user_perfil_selection = tk.StringVar(main)
user_perfil_options = ("Administrador", "Maestro", "Alumno")
user_perfil_optionMenu = tk.OptionMenu(pestana_usuarios, user_perfil_selection, *user_perfil_options)
user_perfil_optionMenu.configure(state="disabled")

#- - - - - - - - - - - - - - - - - - - - - - - - - - - Botones - - - - - - - - - - - - - - - - - - - - - - - - 
user_buscar_btn = tk.Button(pestana_usuarios, text="Buscar", command=lambda:buscarUsuarios())
user_buscar_btn.configure(width=10)
user_nuevo_btn = tk.Button(pestana_usuarios, text="Nuevo")
user_nuevo_btn.configure(width=10)
user_guardar_btn = tk.Button(pestana_usuarios, text="Guardar")
user_guardar_btn.configure(width=10, state="disabled")
user_cancelar_btn = tk.Button(pestana_usuarios, text="Cancelar")
user_cancelar_btn.configure(width=10, state="disabled")
user_editar_btn = tk.Button(pestana_usuarios, text="Editar", command=lambda:editarUsuario())
user_editar_btn.configure(width=10, state="disabled")
user_baja_btn = tk.Button(pestana_usuarios, text="Baja")
user_baja_btn.configure(width=10, state="disabled")

#- - - - - - - - - - - - - - - - - - - - - - - - - - - Posiciones - - - - - - - - - - - - - - - - - - - - - - - - 
user_code_label.grid(column=1, columnspan=2, row=0, padx=10, pady=10, sticky=tk.E)
user_id_label.grid(column=0, columnspan=1, row=1, padx=10, pady=10, sticky=tk.E)
user_nombre_label.grid(column=0, columnspan=1, row=2, padx=10, pady=10, sticky=tk.E)
user_apellidoP_label.grid(column=0, columnspan=1, row=3, padx=10, pady=10, sticky=tk.E)
user_apellidoM_label.grid(column=0, columnspan=1, row=4, padx=10, pady=10, sticky=tk.E)
user_email_label.grid(column=0, columnspan=1, row=5, padx=10, pady=10, sticky=tk.E)
user_username_label.grid(column=2, columnspan=2, row=1, padx=10, pady=10, sticky=tk.E)
user_password_label.grid(column=3, columnspan=1, row=2, padx=10, pady=10, sticky=tk.E)
user_perfil_label.grid(column=3, columnspan=1, row=3, padx=10, pady=10, sticky=tk.E)
user_code_entry.grid(column=3, columnspan=2, row=0, padx=10, pady=10, sticky=tk.W)
user_code_entry.configure(width=30)
user_id_entry.grid(column=1, columnspan=1, row=1, padx=10, pady=10, sticky=tk.W)
user_id_entry.configure(width=15)
user_nombre_entry.grid(column=1, columnspan=2, row=2, padx=10, pady=10, sticky=tk.W)
user_nombre_entry.configure(width=30)
user_apellidoP_entry.grid(column=1, columnspan=2, row=3, padx=10, pady=10, sticky=tk.W)
user_apellidoP_entry.configure(width=30)
user_apellidoM_entry.grid(column=1, columnspan=2, row=4, padx=10, pady=10, sticky=tk.W)
user_apellidoM_entry.configure(width=30)
user_email_entry.grid(column=1, columnspan=2, row=5, padx=10, pady=10, sticky=tk.W)
user_email_entry.configure(width=30)
user_username_entry.grid(column=4, columnspan=2, row=1, padx=10, pady=10, sticky=tk.W)
user_username_entry.configure(width=30)
user_password_entry.grid(column=4, columnspan=2, row=2, padx=10, pady=10, sticky=tk.W)
user_password_entry.configure(width=30)
user_perfil_optionMenu.grid(column=4, columnspan=1, row=3, padx=10, pady=10, sticky=tk.E)
user_perfil_optionMenu.configure(width=8)
user_buscar_btn.grid(column=5, columnspan=1, row=0, padx=10, pady=10, sticky=tk.E)
user_nuevo_btn.grid(column=1, columnspan=1, row=6, padx=10, pady=10, sticky=tk.E)
user_guardar_btn.grid(column=2, columnspan=1, row=6, padx=10, pady=10, sticky=tk.E)
user_cancelar_btn.grid(column=3, columnspan=1, row=6, padx=10, pady=10, sticky=tk.E)
user_editar_btn.grid(column=4, columnspan=1, row=6, padx=10, pady=10, sticky=tk.E)
user_baja_btn.grid(column=5, columnspan=1, row=6, padx=10, pady=10, sticky=tk.E)

#-------------------------------------------------------ALUMNOS ----------------------------------------------------
pestana_alumnos = ttk.Frame(pestanas)
pestanas.add(pestana_alumnos, text="Alumnos")
pestanas.tab(2, state="normal")

#- - - - - - - - - - - - - - - - - - - - - - - Entryes y etiquetas - - - - - - - - - - - - - - - - - - - -
alumno_code_label = tk.Label(pestana_alumnos, text="Ingrese codigo de usuario: ")
alumno_id_label = tk.Label(pestana_alumnos, text="ID:")
alumno_nombre_label = tk.Label(pestana_alumnos, text="Nombre: ")
alumno_apellidoP_label = tk.Label(pestana_alumnos, text="Apellido Paterno: ")
alumno_apellidoM_label = tk.Label(pestana_alumnos, text="Apellido Materno: ")
alumno_email_label = tk.Label(pestana_alumnos, text="Email: ")
alumno_estado_label = tk.Label(pestana_alumnos, text="Estado: ")
alumno_fechanac_label = tk.Label(pestana_alumnos, text="Fecha de Nacimiento: ")
alumno_carrera_label = tk.Label(pestana_alumnos, text="Carrera: ")
alumno_materia_label = tk.Label(pestana_alumnos, text="Materia: ")
alumno_code_entry = tk.Entry(pestana_alumnos)
alumno_id_entry = tk.Entry(pestana_alumnos, state="disabled")
alumno_nombre_entry = tk.Entry(pestana_alumnos, state="disabled")
alumno_apellidoP_entry = tk.Entry(pestana_alumnos, state="disabled")
alumno_apellidoM_entry = tk.Entry(pestana_alumnos, state="disabled")
alumno_email_entry = tk.Entry(pestana_alumnos, state="disabled")
alumno_username_entry = tk.Entry(pestana_alumnos, state="disabled")
alumno_password_entry = tk.Entry(pestana_alumnos, state="disabled", show="•")
alumno_carrera_selection = tk.StringVar(main)
alumno_carrera_options = ("Administrador", "Maestro", "Alumno")
alumno_carrera_optionMenu = tk.OptionMenu(pestana_alumnos, alumno_carrera_selection, *alumno_carrera_options)
alumno_carrera_optionMenu.configure(state="normal")
alumno_materia_selection = tk.StringVar(main)
alumno_materia_options = ("Administrador", "Maestro", "Alumno")
alumno_materia_optionMenu = tk.OptionMenu(pestana_alumnos, alumno_materia_selection, *alumno_materia_options)
alumno_materia_optionMenu.configure(state="normal")

#- - - - - - - - - - - - - - - - - - - - - - - - - - Botones - - - - - - - - - - - - - - - - - - - - - - -
alumno_buscar_btn = tk.Button(pestana_alumnos, text="Buscar")
alumno_buscar_btn.configure(width=10)
alumno_nuevo_btn = tk.Button(pestana_alumnos, text="Nuevo")
alumno_nuevo_btn.configure(width=10)
alumno_guardar_btn = tk.Button(pestana_alumnos, text="Guardar")
alumno_guardar_btn.configure(width=10, state="disabled")
alumno_cancelar_btn = tk.Button(pestana_alumnos, text="Cancelar")
alumno_cancelar_btn.configure(width=10, state="disabled")
alumno_editar_btn = tk.Button(pestana_alumnos, text="Editar")
alumno_editar_btn.configure(width=10, state="disabled")
alumno_baja_btn = tk.Button(pestana_alumnos, text="Baja")
alumno_baja_btn.configure(width=10, state="disabled")
#- - - - - - - - - - - - - - - - - - - - - - - - - - Posiciones - - - - - - - - - - - - - - - - - - - - - - -

alumno_code_label.grid(column=1, columnspan=2, row=0, padx=10, pady=10, sticky=tk.E)
alumno_id_label.grid(column=0, columnspan=1, row=1, padx=10, pady=10, sticky=tk.E)
alumno_nombre_label.grid(column=0, columnspan=1, row=2, padx=10, pady=10, sticky=tk.E)
alumno_apellidoP_label.grid(column=0, columnspan=1, row=3, padx=10, pady=10, sticky=tk.E)
alumno_apellidoM_label.grid(column=0, columnspan=1, row=4, padx=10, pady=10, sticky=tk.E)
alumno_email_label.grid(column=0, columnspan=1, row=5, padx=10, pady=10, sticky=tk.E)
alumno_estado_label.grid(column=2, columnspan=2, row=1, padx=10, pady=10, sticky=tk.E)
alumno_carrera_label.grid(column=3, columnspan=1, row=2, padx=10, pady=10, sticky=tk.E)
alumno_materia_label.grid(column=3, columnspan=1, row=3, padx=10, pady=10, sticky=tk.E)
alumno_code_entry.grid(column=3, columnspan=2, row=0, padx=10, pady=10, sticky=tk.W)
alumno_code_entry.configure(width=30)
alumno_id_entry.grid(column=1, columnspan=1, row=1, padx=10, pady=10, sticky=tk.W)
alumno_id_entry.configure(width=15)
alumno_nombre_entry.grid(column=1, columnspan=2, row=2, padx=10, pady=10, sticky=tk.W)
alumno_nombre_entry.configure(width=30)
alumno_apellidoP_entry.grid(column=1, columnspan=2, row=3, padx=10, pady=10, sticky=tk.W)
alumno_apellidoP_entry.configure(width=30)
alumno_apellidoM_entry.grid(column=1, columnspan=2, row=4, padx=10, pady=10, sticky=tk.W)
alumno_apellidoM_entry.configure(width=30)
alumno_email_entry.grid(column=1, columnspan=2, row=5, padx=10, pady=10, sticky=tk.W)
alumno_email_entry.configure(width=30)
alumno_username_entry.grid(column=4, columnspan=2, row=1, padx=10, pady=10, sticky=tk.W)
alumno_username_entry.configure(width=30)
alumno_password_entry.grid(column=4, columnspan=2, row=2, padx=10, pady=10, sticky=tk.W)
alumno_password_entry.configure(width=30)
alumno_carrera_optionMenu.grid(column=4, columnspan=1, row=3, padx=10, pady=10, sticky=tk.E)
alumno_carrera_optionMenu.configure(width=8)
alumno_buscar_btn.grid(column=5, columnspan=1, row=0, padx=10, pady=10, sticky=tk.E)
alumno_nuevo_btn.grid(column=1, columnspan=1, row=6, padx=10, pady=10, sticky=tk.E)
alumno_guardar_btn.grid(column=2, columnspan=1, row=6, padx=10, pady=10, sticky=tk.E)
alumno_cancelar_btn.grid(column=3, columnspan=1, row=6, padx=10, pady=10, sticky=tk.E)
alumno_editar_btn.grid(column=4, columnspan=1, row=6, padx=10, pady=10, sticky=tk.E)
alumno_baja_btn.grid(column=5, columnspan=1, row=6, padx=10, pady=10, sticky=tk.E)

#-------------------------------------------------------MAESTROS ---------------------------------------------------
pestana_maestros = ttk.Frame(pestanas)
pestanas.add(pestana_maestros, text="Maestros")
pestanas.tab(3, state="normal")

#- - - - - - - - - - - - - - - - - - - - - - - Entries y etiquetas - - - - - - - - - - - - - - - - - - - -
maestro_code_label = tk.Label(pestana_maestros, text="Ingrese codigo de maestro: ")
maestro_id_label = tk.Label(pestana_maestros, text="ID:")
maestro_nombre_label = tk.Label(pestana_maestros, text="Nombre: ")
maestro_apellidoP_label = tk.Label(pestana_maestros, text="Apellido Paterno: ")
maestro_apellidoM_label = tk.Label(pestana_maestros, text="Apellido Materno: ")
maestro_email_label = tk.Label(pestana_maestros, text="Email: ")
maestro_fechanac_label = tk.Label(pestana_maestros, text="Fecha de Nacimiento: ")
maestro_carrera_label = tk.Label(pestana_maestros, text="Carrera: ")
maestro_materia_label = tk.Label(pestana_maestros, text="Materia: ")
maestro_code_entry = tk.Entry(pestana_maestros)
maestro_id_entry = tk.Entry(pestana_maestros, state="disabled")
maestro_nombre_entry = tk.Entry(pestana_maestros, state="disabled")
maestro_apellidoP_entry = tk.Entry(pestana_maestros, state="disabled")
maestro_apellidoM_entry = tk.Entry(pestana_maestros, state="disabled")
maestro_email_entry = tk.Entry(pestana_maestros, state="disabled")
maestro_username_entry = tk.Entry(pestana_maestros, state="disabled")
maestro_password_entry = tk.Entry(pestana_maestros, state="disabled", show="•")
maestro_carrera_selection = tk.StringVar(main)
maestro_carrera_options = ("Administrador", "Maestro", "Alumno")
maestro_carrera_optionMenu = tk.OptionMenu(pestana_maestros, maestro_carrera_selection, *maestro_carrera_options)
maestro_carrera_optionMenu.configure(state="normal")
maestro_materia_selection = tk.StringVar(main)
maestro_materia_options = ("Administrador", "Maestro", "Alumno")
maestro_materia_optionMenu = tk.OptionMenu(pestana_maestros, maestro_materia_selection, *maestro_materia_options)
maestro_materia_optionMenu.configure(state="normal")

#- - - - - - - - - - - - - - - - - - - - - - - - - - Botones - - - - - - - - - - - - - - - - - - - - - - -
maestro_buscar_btn = tk.Button(pestana_maestros, text="Buscar")
maestro_buscar_btn.configure(width=10)
maestro_nuevo_btn = tk.Button(pestana_maestros, text="Nuevo")
maestro_nuevo_btn.configure(width=10)
maestro_guardar_btn = tk.Button(pestana_maestros, text="Guardar")
maestro_guardar_btn.configure(width=10, state="disabled")
maestro_cancelar_btn = tk.Button(pestana_maestros, text="Cancelar")
maestro_cancelar_btn.configure(width=10, state="disabled")
maestro_editar_btn = tk.Button(pestana_maestros, text="Editar")
maestro_editar_btn.configure(width=10, state="disabled")
maestro_baja_btn = tk.Button(pestana_maestros, text="Baja")
maestro_baja_btn.configure(width=10, state="disabled")
#- - - - - - - - - - - - - - - - - - - - - - - - - - Posiciones - - - - - - - - - - - - - - - - - - - - - - -
maestro_code_label.grid(column=1, columnspan=2, row=0, padx=10, pady=10, sticky=tk.E)
maestro_id_label.grid(column=0, columnspan=1, row=1, padx=10, pady=10, sticky=tk.E)
maestro_nombre_label.grid(column=0, columnspan=1, row=2, padx=10, pady=10, sticky=tk.E)
maestro_apellidoP_label.grid(column=0, columnspan=1, row=3, padx=10, pady=10, sticky=tk.E)
maestro_apellidoM_label.grid(column=0, columnspan=1, row=4, padx=10, pady=10, sticky=tk.E)
maestro_email_label.grid(column=0, columnspan=1, row=5, padx=10, pady=10, sticky=tk.E)
maestro_carrera_label.grid(column=3, columnspan=1, row=2, padx=10, pady=10, sticky=tk.E)
maestro_materia_label.grid(column=3, columnspan=1, row=3, padx=10, pady=10, sticky=tk.E)
maestro_code_entry.grid(column=3, columnspan=2, row=0, padx=10, pady=10, sticky=tk.W)
maestro_code_entry.configure(width=30)
maestro_id_entry.grid(column=1, columnspan=1, row=1, padx=10, pady=10, sticky=tk.W)
maestro_id_entry.configure(width=15)
maestro_nombre_entry.grid(column=1, columnspan=2, row=2, padx=10, pady=10, sticky=tk.W)
maestro_nombre_entry.configure(width=30)
maestro_apellidoP_entry.grid(column=1, columnspan=2, row=3, padx=10, pady=10, sticky=tk.W)
maestro_apellidoP_entry.configure(width=30)
maestro_apellidoM_entry.grid(column=1, columnspan=2, row=4, padx=10, pady=10, sticky=tk.W)
maestro_apellidoM_entry.configure(width=30)
maestro_email_entry.grid(column=1, columnspan=2, row=5, padx=10, pady=10, sticky=tk.W)
maestro_email_entry.configure(width=30)
maestro_username_entry.grid(column=4, columnspan=2, row=1, padx=10, pady=10, sticky=tk.W)
maestro_username_entry.configure(width=30)
maestro_password_entry.grid(column=4, columnspan=2, row=2, padx=10, pady=10, sticky=tk.W)
maestro_password_entry.configure(width=30)
maestro_carrera_optionMenu.grid(column=4, columnspan=1, row=3, padx=10, pady=10, sticky=tk.E)
maestro_carrera_optionMenu.configure(width=8)
maestro_buscar_btn.grid(column=5, columnspan=1, row=0, padx=10, pady=10, sticky=tk.E)
maestro_nuevo_btn.grid(column=1, columnspan=1, row=6, padx=10, pady=10, sticky=tk.E)
maestro_guardar_btn.grid(column=2, columnspan=1, row=6, padx=10, pady=10, sticky=tk.E)
maestro_cancelar_btn.grid(column=3, columnspan=1, row=6, padx=10, pady=10, sticky=tk.E)
maestro_editar_btn.grid(column=4, columnspan=1, row=6, padx=10, pady=10, sticky=tk.E)
maestro_baja_btn.grid(column=5, columnspan=1, row=6, padx=10, pady=10, sticky=tk.E)

#-------------------------------------------------------MATERIAS ---------------------------------------------------
pestana_materias = ttk.Frame(pestanas)
pestanas.add(pestana_materias, text="Materias")
pestanas.tab(4, state="normal")
#- - - - - - - - - - - - - - - - - - - - - - - Entries y etiquetas - - - - - - - - - - - - - - - - - - - -
materia_code_label = tk.Label(pestana_materias, text="Ingrese codigo de usuario: ")
materia_id_label = tk.Label(pestana_materias, text="ID:")
materia_asignatura_label = tk.Label(pestana_materias, text="Asignatura: ")
materia_creditos_label = tk.Label(pestana_materias, text="Creditos: ")
materia_semestre_label = tk.Label(pestana_materias, text="Semestre: ")
materia_carrera_label = tk.Label(pestana_materias, text="Carrera: ")
materia_materia_label = tk.Label(pestana_materias, text="Materia: ")
materia_code_entry = tk.Entry(pestana_materias)
materia_id_entry = tk.Entry(pestana_materias, state="disabled")
materia_nombre_entry = tk.Entry(pestana_materias, state="disabled")
materia_apellidoP_entry = tk.Entry(pestana_materias, state="disabled")
materia_apellidoM_entry = tk.Entry(pestana_materias, state="disabled")
materia_email_entry = tk.Entry(pestana_materias, state="disabled")
materia_username_entry = tk.Entry(pestana_materias, state="disabled")
materia_password_entry = tk.Entry(pestana_materias, state="disabled", show="•")
materia_carrera_selection = tk.StringVar(main)
materia_carrera_options = ("Administrador", "Materia", "Alumno")
materia_carrera_optionMenu = tk.OptionMenu(pestana_materias, materia_carrera_selection, *materia_carrera_options)
materia_carrera_optionMenu.configure(state="normal")
materia_materia_selection = tk.StringVar(main)
materia_materia_options = ("Administrador", "Materia", "Alumno")
materia_materia_optionMenu = tk.OptionMenu(pestana_materias, materia_materia_selection, *materia_materia_options)
materia_materia_optionMenu.configure(state="normal")
#- - - - - - - - - - - - - - - - - - - - - - - - - - Botones - - - - - - - - - - - - - - - - - - - - - - -
materia_buscar_btn = tk.Button(pestana_materias, text="Buscar")
materia_buscar_btn.configure(width=10)
materia_nuevo_btn = tk.Button(pestana_materias, text="Nuevo")
materia_nuevo_btn.configure(width=10)
materia_guardar_btn = tk.Button(pestana_materias, text="Guardar")
materia_guardar_btn.configure(width=10, state="disabled")
materia_cancelar_btn = tk.Button(pestana_materias, text="Cancelar")
materia_cancelar_btn.configure(width=10, state="disabled")
materia_editar_btn = tk.Button(pestana_materias, text="Editar")
materia_editar_btn.configure(width=10, state="disabled")
materia_baja_btn = tk.Button(pestana_materias, text="Baja")
materia_baja_btn.configure(width=10, state="disabled")
#- - - - - - - - - - - - - - - - - - - - - - - - - - Posiciones - - - - - - - - - - - - - - - - - - - - - - -

materia_code_label.grid(column=1, columnspan=2, row=0, padx=10, pady=10, sticky=tk.E)
materia_id_label.grid(column=0, columnspan=1, row=1, padx=10, pady=10, sticky=tk.E)
materia_asignatura_label.grid(column=0, columnspan=1, row=2, padx=10, pady=10, sticky=tk.E)
materia_creditos_label.grid(column=0, columnspan=1, row=3, padx=10, pady=10, sticky=tk.E)
materia_semestre_label.grid(column=0, columnspan=1, row=4, padx=10, pady=10, sticky=tk.E)
materia_carrera_label.grid(column=3, columnspan=1, row=2, padx=10, pady=10, sticky=tk.E)
materia_materia_label.grid(column=3, columnspan=1, row=3, padx=10, pady=10, sticky=tk.E)
materia_code_entry.grid(column=3, columnspan=2, row=0, padx=10, pady=10, sticky=tk.W)
materia_code_entry.configure(width=30)
materia_id_entry.grid(column=1, columnspan=1, row=1, padx=10, pady=10, sticky=tk.W)
materia_id_entry.configure(width=15)
materia_nombre_entry.grid(column=1, columnspan=2, row=2, padx=10, pady=10, sticky=tk.W)
materia_nombre_entry.configure(width=30)
materia_apellidoP_entry.grid(column=1, columnspan=2, row=3, padx=10, pady=10, sticky=tk.W)
materia_apellidoP_entry.configure(width=30)
materia_apellidoM_entry.grid(column=1, columnspan=2, row=4, padx=10, pady=10, sticky=tk.W)
materia_apellidoM_entry.configure(width=30)
materia_email_entry.grid(column=1, columnspan=2, row=5, padx=10, pady=10, sticky=tk.W)
materia_email_entry.configure(width=30)
materia_username_entry.grid(column=4, columnspan=2, row=1, padx=10, pady=10, sticky=tk.W)
materia_username_entry.configure(width=30)
materia_password_entry.grid(column=4, columnspan=2, row=2, padx=10, pady=10, sticky=tk.W)
materia_password_entry.configure(width=30)
materia_carrera_optionMenu.grid(column=4, columnspan=1, row=3, padx=10, pady=10, sticky=tk.E)
materia_carrera_optionMenu.configure(width=8)
materia_buscar_btn.grid(column=5, columnspan=1, row=0, padx=10, pady=10, sticky=tk.E)
materia_nuevo_btn.grid(column=1, columnspan=1, row=6, padx=10, pady=10, sticky=tk.E)
materia_guardar_btn.grid(column=2, columnspan=1, row=6, padx=10, pady=10, sticky=tk.E)
materia_cancelar_btn.grid(column=3, columnspan=1, row=6, padx=10, pady=10, sticky=tk.E)
materia_editar_btn.grid(column=4, columnspan=1, row=6, padx=10, pady=10, sticky=tk.E)
materia_baja_btn.grid(column=5, columnspan=1, row=6, padx=10, pady=10, sticky=tk.E)

#--------------------------------------------------------GRUPOS ----------------------------------------------------
pestana_grupos = ttk.Frame(pestanas)
pestanas.add(pestana_grupos, text="Grupos")
pestanas.tab(5, state="normal")
#- - - - - - - - - - - - - - - - - - - - - - - Entries y etiquetas - - - - - - - - - - - - - - - - - - - -

grupo_code_label = tk.Label(pestana_grupos, text="Ingrese codigo de usuario: ")
grupo_id_label = tk.Label(pestana_grupos, text="ID:")
grupo_nombre_label = tk.Label(pestana_grupos, text="Nombre: ")
grupo_apellidoP_label = tk.Label(pestana_grupos, text="Apellido Paterno: ")
grupo_apellidoM_label = tk.Label(pestana_grupos, text="Apellido Materno: ")
grupo_email_label = tk.Label(pestana_grupos, text="Email: ")
grupo_estado_label = tk.Label(pestana_grupos, text="Estado: ")
grupo_fechanac_label = tk.Label(pestana_grupos, text="Fecha de Nacimiento: ")
grupo_carrera_label = tk.Label(pestana_grupos, text="Carrera: ")
grupo_materia_label = tk.Label(pestana_grupos, text="Materia: ")
grupo_code_entry = tk.Entry(pestana_grupos)
grupo_id_entry = tk.Entry(pestana_grupos, state="disabled")
grupo_nombre_entry = tk.Entry(pestana_grupos, state="disabled")
grupo_apellidoP_entry = tk.Entry(pestana_grupos, state="disabled")
grupo_apellidoM_entry = tk.Entry(pestana_grupos, state="disabled")
grupo_email_entry = tk.Entry(pestana_grupos, state="disabled")
grupo_username_entry = tk.Entry(pestana_grupos, state="disabled")
grupo_password_entry = tk.Entry(pestana_grupos, state="disabled", show="•")
grupo_carrera_selection = tk.StringVar(main)
grupo_carrera_options = ("Administrador", "Grupo", "Alumno")
grupo_carrera_optionMenu = tk.OptionMenu(pestana_grupos, grupo_carrera_selection, *grupo_carrera_options)
grupo_carrera_optionMenu.configure(state="normal")
grupo_materia_selection = tk.StringVar(main)
grupo_materia_options = ("Administrador", "Grupo", "Alumno")
grupo_materia_optionMenu = tk.OptionMenu(pestana_grupos, grupo_materia_selection, *grupo_materia_options)
grupo_materia_optionMenu.configure(state="normal")



#- - - - - - - - - - - - - - - - - - - - - - - - - - Botones - - - - - - - - - - - - - - - - - - - - - - -
grupo_buscar_btn = tk.Button(pestana_grupos, text="Buscar")
grupo_buscar_btn.configure(width=10)
grupo_nuevo_btn = tk.Button(pestana_grupos, text="Nuevo")
grupo_nuevo_btn.configure(width=10)
grupo_guardar_btn = tk.Button(pestana_grupos, text="Guardar")
grupo_guardar_btn.configure(width=10, state="disabled")
grupo_cancelar_btn = tk.Button(pestana_grupos, text="Cancelar")
grupo_cancelar_btn.configure(width=10, state="disabled")
grupo_editar_btn = tk.Button(pestana_grupos, text="Editar")
grupo_editar_btn.configure(width=10, state="disabled")
grupo_baja_btn = tk.Button(pestana_grupos, text="Baja")
grupo_baja_btn.configure(width=10, state="disabled")
#- - - - - - - - - - - - - - - - - - - - - - - - - - Posiciones - - - - - - - - - - - - - - - - - - - - - - -
grupo_code_label.grid(column=1, columnspan=2, row=0, padx=10, pady=10, sticky=tk.E)
grupo_id_label.grid(column=0, columnspan=1, row=1, padx=10, pady=10, sticky=tk.E)
grupo_nombre_label.grid(column=0, columnspan=1, row=2, padx=10, pady=10, sticky=tk.E)
grupo_apellidoP_label.grid(column=0, columnspan=1, row=3, padx=10, pady=10, sticky=tk.E)
grupo_apellidoM_label.grid(column=0, columnspan=1, row=4, padx=10, pady=10, sticky=tk.E)
grupo_email_label.grid(column=0, columnspan=1, row=5, padx=10, pady=10, sticky=tk.E)
grupo_estado_label.grid(column=2, columnspan=2, row=1, padx=10, pady=10, sticky=tk.E)
grupo_carrera_label.grid(column=3, columnspan=1, row=2, padx=10, pady=10, sticky=tk.E)
grupo_materia_label.grid(column=3, columnspan=1, row=3, padx=10, pady=10, sticky=tk.E)
grupo_code_entry.grid(column=3, columnspan=2, row=0, padx=10, pady=10, sticky=tk.W)
grupo_code_entry.configure(width=30)
grupo_id_entry.grid(column=1, columnspan=1, row=1, padx=10, pady=10, sticky=tk.W)
grupo_id_entry.configure(width=15)
grupo_nombre_entry.grid(column=1, columnspan=2, row=2, padx=10, pady=10, sticky=tk.W)
grupo_nombre_entry.configure(width=30)
grupo_apellidoP_entry.grid(column=1, columnspan=2, row=3, padx=10, pady=10, sticky=tk.W)
grupo_apellidoP_entry.configure(width=30)
grupo_apellidoM_entry.grid(column=1, columnspan=2, row=4, padx=10, pady=10, sticky=tk.W)
grupo_apellidoM_entry.configure(width=30)
grupo_email_entry.grid(column=1, columnspan=2, row=5, padx=10, pady=10, sticky=tk.W)
grupo_email_entry.configure(width=30)
grupo_username_entry.grid(column=4, columnspan=2, row=1, padx=10, pady=10, sticky=tk.W)
grupo_username_entry.configure(width=30)
grupo_password_entry.grid(column=4, columnspan=2, row=2, padx=10, pady=10, sticky=tk.W)
grupo_password_entry.configure(width=30)
grupo_carrera_optionMenu.grid(column=4, columnspan=1, row=3, padx=10, pady=10, sticky=tk.E)
grupo_carrera_optionMenu.configure(width=8)
grupo_buscar_btn.grid(column=5, columnspan=1, row=0, padx=10, pady=10, sticky=tk.E)
grupo_nuevo_btn.grid(column=1, columnspan=1, row=6, padx=10, pady=10, sticky=tk.E)
grupo_guardar_btn.grid(column=2, columnspan=1, row=6, padx=10, pady=10, sticky=tk.E)
grupo_cancelar_btn.grid(column=3, columnspan=1, row=6, padx=10, pady=10, sticky=tk.E)
grupo_editar_btn.grid(column=4, columnspan=1, row=6, padx=10, pady=10, sticky=tk.E)
grupo_baja_btn.grid(column=5, columnspan=1, row=6, padx=10, pady=10, sticky=tk.E)
#--------------------------------------------------------HORARIO ---------------------------------------------------
pestana_horario = ttk.Frame(pestanas)
pestanas.add(pestana_horario, text="Horario")
pestanas.tab(6, state="disabled")
#- - - - - - - - - - - - - - - - - - - - - - - Entries y etiquetas - - - - - - - - - - - - - - - - - - - -


#- - - - - - - - - - - - - - - - - - - - - - - - - - Botones - - - - - - - - - - - - - - - - - - - - - - -

#- - - - - - - - - - - - - - - - - - - - - - - - - - Posiciones - - - - - - - - - - - - - - - - - - - - - - -


#---------------------------------------------------------SALON ----------------------------------------------------
pestana_salon = ttk.Frame(pestanas)
pestanas.add(pestana_salon, text="Salón")
pestanas.tab(7, state="disabled")
#- - - - - - - - - - - - - - - - - - - - - - - Entries y etiquetas - - - - - - - - - - - - - - - - - - - -


#- - - - - - - - - - - - - - - - - - - - - - - - - - Botones - - - - - - - - - - - - - - - - - - - - - - -

#- - - - - - - - - - - - - - - - - - - - - - - - - - Posiciones - - - - - - - - - - - - - - - - - - - - - - -


#--------------------------------------------------------CARRERA ---------------------------------------------------
pestana_carrera = ttk.Frame(pestanas)
pestanas.add(pestana_carrera, text="Carrera")
pestanas.tab(8, state="disabled")
#-------------------------------------------------------PLANEACIÓN -------------------------------------------------
pestana_planeacion = ttk.Frame(pestanas)
pestanas.add(pestana_planeacion, text="Planeación")
pestanas.tab(9, state="disabled")
#==============================================================================================================

#=======================================================AJUSTES DE POSICION====================================
test_label = tk.Label(pestana_usuarios, text="")
test_label.grid(column=6, row=6, sticky=tk.NSEW)
test_label.configure(width=18)
pestana_usuarios.columnconfigure(0, weight=1)
pestana_usuarios.columnconfigure(6, weight=1)
pestana_login.columnconfigure(0, weight=1)
pestana_login.columnconfigure(3, weight=1)
pestana_login.rowconfigure(0, weight=1)
pestana_login.rowconfigure(5, weight=1)
#===============================================================================================================

#======================================================FUNCIONES================================================
#----------------------------------------------Funcionamiento general-------------------------------------------
def dormirPestanas(code): #Se introduce un binario que indica que pestañas dormir y cuáles mantener despiertas
    for x in range(0, len(code)):
        if code[x] == '0':
            pestanas.tab(x, state="disable")
        else:
            pestanas.tab(x, state="normal")

def validarCampoNoVacio(lista): #Se usa cuando hay que verificar qun campo no se quede vacío
    for x in lista:
        if x.get() == "":
            messagebox.showerror(title="Campo vacío", message="El campo " + str(x) + " no puede estar vacío")
            return False
    return True

def bloquearCampos(accion, listaCampos):  #Accion es un booleano, si es true se van a bloquear los campos listados en ListaCampos, si es false se van a desbloquear
    for campo in listaCampos:
        if accion:
            campo.configure(state="disabled")
        if not accion:
            campo.configure(state="normal")
            
def llenarCampos(listaCampos, listaDatos, diccionario):
    for campo, dato in zip(listaCampos, listaDatos):
        campo.configure(state="normal")
        campo.delete(0, tk.END)
        campo.insert(0, diccionario.get(dato))
        campo.configure(state="disabled")


#-----------------------------------------------------Login----------------------------------------------------
def login():
    listaUsuarios = Usuarios()
    listaUsuarios = listaUsuarios.listarUsuarios()
    listaCampos = {username_entry, password_entry}
    if validarCampoNoVacio(listaCampos):
        for x in range(len(listaUsuarios)):
            if username_entry.get() == listaUsuarios[x].get("usuario"):
                if password_entry.get() == listaUsuarios[x].get("password"):
                    if listaUsuarios[x].get("perfil") == "Admin":
                        dormirPestanas("1111111111")
                    elif listaUsuarios[x].get("perfil") == "Maestro":
                        dormirPestanas("1101000000")
                    elif listaUsuarios[x].get("perfil") == "Alumno":
                        dormirPestanas("1110000000")
                    messagebox.showinfo(title="Bienvenido!", message="Bienvenido " + username_entry.get() + "!")
                    pestanas.select(pestana_usuarios)
                    clearLogin()
                    return 0
                else:
                    messagebox.showerror(title="Credenciales erróneas", message="Ha introducido una contraseña inválida")
                    return 0
        messagebox.showerror(title="Credenciales erróneas", message="No se encontró el nombre de usuario")

def clearLogin():
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
#--------------------------------------------------------------------------------------------------------------
#----------------------------------------------------Usuarios--------------------------------------------------
def buscarUsuarios():
    listaUsuarios = Usuarios()
    listaUsuarios = listaUsuarios.listarUsuarios()
    listaCampos = {user_code_entry}
    if validarCampoNoVacio(listaCampos):
        for x in range(len(listaUsuarios)):
            if user_code_entry.get() == str(listaUsuarios[x].get("idusuario")):
                user_editar_btn.configure(state="normal")
                listaCampos = ( user_id_entry, 
                                user_nombre_entry, 
                                user_apellidoP_entry, 
                                user_apellidoM_entry, 
                                user_email_entry, 
                                user_username_entry, 
                                user_password_entry)
                listaDatos = ("idusuario", "nombre", "ap", "am", "usuario", "usuario", "password")
                llenarCampos(listaCampos, listaDatos, listaUsuarios[x])
                return 0
        messagebox.showerror(title="No se encuentra", message= "No se encontró el código")

def editarUsuario():
    listaCampos = {user_code_entry, 
                    user_nombre_entry, 
                    user_apellidoP_entry, 
                    user_apellidoM_entry, 
                    user_email_entry, 
                    user_username_entry, 
                    user_password_entry}
    listaCamposBloquear = {user_editar_btn,
                           user_nuevo_btn,
                           user_buscar_btn,
                           user_code_entry}
    listaOtros = {user_editar_btn,
                  user_baja_btn,
                  user_perfil_optionMenu,
                  user_cancelar_btn,
                  user_guardar_btn}
    bloquearCampos(False, listaCampos)
    bloquearCampos(False, listaOtros)
    bloquearCampos(True, listaCamposBloquear)


#--------------------------------------------------------------------------------------------------------------
#===============================================================================================================

dormirPestanas("1100000000")
pestanas.select(pestana_usuarios)

main.mainloop()
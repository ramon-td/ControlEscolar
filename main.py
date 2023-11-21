import tkinter as tk

from tkinter import messagebox, ttk
from controlObjetos import Conexion

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
user_perfil_selection = tk.StringVar(value="Alumno")
user_perfil_options = ("Admin", "Maestro", "Alumno")
user_perfil_optionMenu = tk.OptionMenu(pestana_usuarios, user_perfil_selection, *user_perfil_options)
user_perfil_optionMenu.configure(state="disabled")

#- - - - - - - - - - - - - - - - - - - - - - - - - - - Botones - - - - - - - - - - - - - - - - - - - - - - - - 
user_buscar_btn = tk.Button(pestana_usuarios, text="Buscar", command=lambda:buscarUsuarios())
user_buscar_btn.configure(width=10)
user_nuevo_btn = tk.Button(pestana_usuarios, text="Nuevo", command=lambda:nuevoUsuario())
user_nuevo_btn.configure(width=10)
user_guardar_btn = tk.Button(pestana_usuarios, text="Guardar", command=lambda:guardarUsuario())
user_guardar_btn.configure(width=10, state="disabled")
user_cancelar_btn = tk.Button(pestana_usuarios, text="Cancelar", command=lambda:cancelarUsuario())
user_cancelar_btn.configure(width=10, state="disabled")
user_editar_btn = tk.Button(pestana_usuarios, text="Editar", command=lambda:editarUsuario())
user_editar_btn.configure(width=10, state="disabled")
user_baja_btn = tk.Button(pestana_usuarios, text="Baja", command=lambda:bajaUsuario())
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
alumno_code_label = tk.Label(pestana_alumnos, text="Ingrese codigo de alumno: ")
alumno_id_label = tk.Label(pestana_alumnos, text="ID:")
alumno_nombre_label = tk.Label(pestana_alumnos, text="Nombre: ")
alumno_apellidoP_label = tk.Label(pestana_alumnos, text="Apellido Paterno: ")
alumno_apellidoM_label = tk.Label(pestana_alumnos, text="Apellido Materno: ")
alumno_email_label = tk.Label(pestana_alumnos, text="Email: ")
alumno_estado_label = tk.Label(pestana_alumnos, text="Estado: ")
alumno_fechanac_label = tk.Label(pestana_alumnos, text="Fech. de Nac.: ")
alumno_carrera_label = tk.Label(pestana_alumnos, text="Carrera: ")
alumno_materia_label = tk.Label(pestana_alumnos, text="Materia: ")
alumno_code_entry = tk.Entry(pestana_alumnos)
alumno_id_entry = tk.Entry(pestana_alumnos, state="disabled")
alumno_nombre_entry = tk.Entry(pestana_alumnos, state="disabled")
alumno_apellidoP_entry = tk.Entry(pestana_alumnos, state="disabled")
alumno_apellidoM_entry = tk.Entry(pestana_alumnos, state="disabled")
alumno_email_entry = tk.Entry(pestana_alumnos, state="disabled")
alumno_estado_selection = tk.StringVar(value="Jalisco")
alumno_estado_options = ("Aguascalientes", "Colima", "Jalisco", "Nayarit")
alumno_estado_optionMenu = tk.OptionMenu(pestana_alumnos, alumno_estado_selection, *alumno_estado_options)
alumno_fechanac_entry = tk.Entry(pestana_alumnos, state="disabled", show="•")
alumno_carrera_selection = tk.StringVar(main)
alumno_carrera_options = ("Administrador", "Maestro", "Alumno", "TEST")
alumno_carrera_optionMenu = tk.OptionMenu(pestana_alumnos, alumno_carrera_selection, *alumno_carrera_options)
alumno_carrera_optionMenu.configure(state="normal")
alumno_materia_selection = tk.StringVar(main)
alumno_materia_options = ("Administrador", "Maestro", "Alumno", "MATEMATICAS")
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
alumno_fechanac_label.grid(column=2, columnspan=2, row=2, padx=10, pady=10, sticky=tk.E)
alumno_carrera_label.grid(column=3, columnspan=1, row=3, padx=10, pady=10, sticky=tk.E)
alumno_materia_label.grid(column=3, columnspan=1, row=4, padx=10, pady=10, sticky=tk.E)
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
alumno_estado_optionMenu.grid(column=4, columnspan=2, row=1, padx=10, pady=10, sticky=tk.W)
alumno_estado_optionMenu.configure(width=20)
alumno_fechanac_entry.grid(column=4, columnspan=2, row=2, padx=10, pady=10, sticky=tk.W)
alumno_fechanac_entry.configure(width=30)
alumno_carrera_optionMenu.grid(column=4, columnspan=2, row=3, padx=10, pady=10, sticky=tk.W)
alumno_carrera_optionMenu.configure(width=20)
alumno_materia_optionMenu.grid(column=4, columnspan=2, row=4, padx=10, pady=10, sticky=tk.W)
alumno_materia_optionMenu.configure(width=20)
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
maestro_carrera_label = tk.Label(pestana_maestros, text="Carrera: ")
maestro_materia_label = tk.Label(pestana_maestros, text="Materia: ")
maestro_grado_label = tk.Label(pestana_maestros, text="Grado Estudios: ")
maestro_code_entry = tk.Entry(pestana_maestros)
maestro_id_entry = tk.Entry(pestana_maestros, state="disabled")
maestro_nombre_entry = tk.Entry(pestana_maestros, state="disabled")
maestro_apellidoP_entry = tk.Entry(pestana_maestros, state="disabled")
maestro_apellidoM_entry = tk.Entry(pestana_maestros, state="disabled")
maestro_email_entry = tk.Entry(pestana_maestros, state="disabled")
maestro_username_entry = tk.Entry(pestana_maestros, state="disabled")
maestro_password_entry = tk.Entry(pestana_maestros, state="disabled", show="•")
maestro_carrera_selection = tk.StringVar(main)
maestro_carrera_options = ("CARRERAS", "1KM", "5KM")
maestro_carrera_optionMenu = tk.OptionMenu(pestana_maestros, maestro_carrera_selection, *maestro_carrera_options)
maestro_carrera_optionMenu.configure(state="normal")
maestro_materia_selection = tk.StringVar(main)
maestro_materia_options = ("MATERIAS", "ESPAÑOL", "MATEMATICAS")
maestro_materia_optionMenu = tk.OptionMenu(pestana_maestros, maestro_materia_selection, *maestro_materia_options)
maestro_materia_optionMenu.configure(state="normal")
maestro_grado_selection = tk.StringVar(main)
maestro_grado_options = ("1RO", "2DO", "3RO", "4TO", "5TO", "6TO", "7MO", "8VO")
maestro_grado_optionMenu = tk.OptionMenu(pestana_maestros, maestro_grado_selection, *maestro_grado_options)
maestro_grado_optionMenu.configure(state="normal")

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
maestro_grado_label.grid(column=3, columnspan=1, row=5, padx=10, pady=10, sticky=tk.E)
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
maestro_carrera_optionMenu.grid(column=4, columnspan=2, row=2, padx=10, pady=10, sticky=tk.W)
maestro_carrera_optionMenu.configure(width=16)
maestro_materia_optionMenu.grid(column=4, columnspan=2, row=3, padx=10, pady=10, sticky=tk.W)
maestro_materia_optionMenu.configure(width=16)
maestro_grado_optionMenu.grid(column=4, columnspan=2, row=5, padx=10, pady=10, sticky=tk.W)
maestro_grado_optionMenu.configure(width=16)
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
materia_code_label = tk.Label(pestana_materias, text="Ingrese codigo de materia: ")
materia_id_label = tk.Label(pestana_materias, text="ID:")
materia_asignatura_label = tk.Label(pestana_materias, text="Asignatura: ")
materia_creditos_label = tk.Label(pestana_materias, text="Creditos: ")
materia_semestre_label = tk.Label(pestana_materias, text="Semestre: ")
materia_carrera_label = tk.Label(pestana_materias, text="Carrera: ")
materia_code_entry = tk.Entry(pestana_materias)
materia_id_entry = tk.Entry(pestana_materias, state="disabled")
materia_asignatura_entry = tk.Entry(pestana_materias, state="disabled")
materia_creditos_entry = tk.Entry(pestana_materias, state="disabled")
materia_semestre_entry = tk.Entry(pestana_materias, state="disabled")
materia_carrera_selection = tk.StringVar(main)
materia_carrera_options = ("TEST", "TEST2", "TEST#")
materia_carrera_optionMenu = tk.OptionMenu(pestana_materias, materia_carrera_selection, *materia_carrera_options)
materia_carrera_optionMenu.configure(state="normal")

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
materia_code_entry.grid(column=3, columnspan=2, row=0, padx=10, pady=10, sticky=tk.W)
materia_code_entry.configure(width=30)
materia_id_entry.grid(column=1, columnspan=1, row=1, padx=10, pady=10, sticky=tk.W)
materia_id_entry.configure(width=15)
materia_asignatura_entry.grid(column=1, columnspan=2, row=2, padx=10, pady=10, sticky=tk.W)
materia_asignatura_entry.configure(width=30)
materia_creditos_entry.grid(column=1, columnspan=2, row=3, padx=10, pady=10, sticky=tk.W)
materia_creditos_entry.configure(width=30)
materia_semestre_entry.grid(column=1, columnspan=2, row=4, padx=10, pady=10, sticky=tk.W)
materia_semestre_entry.configure(width=30)
materia_carrera_optionMenu.grid(column=4, columnspan=2, row=2, padx=10, pady=10, sticky=tk.W)
materia_carrera_optionMenu.configure(width=20)
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

grupo_code_label = tk.Label(pestana_grupos, text="Ingrese codigo de grupo: ")
grupo_id_label = tk.Label(pestana_grupos, text="ID:")
grupo_nombre_label = tk.Label(pestana_grupos, text="Nombre de Grupo: ")
grupo_fecha_label = tk.Label(pestana_grupos, text="Fecha: ")
grupo_carrera_label = tk.Label(pestana_grupos, text="Carrera: ")
grupo_materia_label = tk.Label(pestana_grupos, text="Materia: ")
grupo_maestro_label = tk.Label(pestana_grupos, text="Maestro: ")
grupo_salon_label = tk.Label(pestana_grupos, text="Salon: ")
grupo_horario_label = tk.Label(pestana_grupos, text="Horario: ")
grupo_semestre_label = tk.Label(pestana_grupos, text="Semestre: ")
grupo_alumnos_label = tk.Label(pestana_grupos, text="Numero de alumnos: ")
grupo_code_entry = tk.Entry(pestana_grupos, state="disabled")
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
grupo_fecha_label.grid(column=0, columnspan=1, row=3, padx=10, pady=10, sticky=tk.E)
grupo_carrera_label.grid(column=0, columnspan=1, row=4, padx=10, pady=10, sticky=tk.W)
grupo_materia_label.grid(column=0, columnspan=1, row=5, padx=10, pady=10, sticky=tk.E)
grupo_maestro_label.grid(column=2, columnspan=2, row=1, padx=10, pady=10, sticky=tk.E)
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
pestanas.tab(6, state="normal")
#- - - - - - - - - - - - - - - - - - - - - - - Entries y etiquetas - - - - - - - - - - - - - - - - - - - -
horario_code_label = tk.Label(pestana_horario, text="Ingrese codigo de grupo: ")
horario_id_label = tk.Label(pestana_horario, text="ID:")
horario_turno_label = tk.Label(pestana_horario, text="Turno: ")
horario_hora_label = tk.Label(pestana_horario, text="Hora: ")
horario_code_entry = tk.Entry(pestana_horario)
horario_id_entry = tk.Entry(pestana_horario, state="disabled")
horario_turno_selection = tk.StringVar(main)
horario_turno_options = ("Turno", "Turno2", "Turno#")
horario_turno_optionMenu = tk.OptionMenu(pestana_horario, horario_turno_selection, *horario_turno_options)
horario_turno_optionMenu.configure(state="normal")
horario_hora_selection = tk.StringVar(main)
horario_hora_options = ("HORA", "HORA2", "HORA#")
horario_hora_optionMenu = tk.OptionMenu(pestana_horario, horario_hora_selection, *horario_hora_options)
horario_hora_optionMenu.configure(state="normal")

#- - - - - - - - - - - - - - - - - - - - - - - - - - Botones - - - - - - - - - - - - - - - - - - - - - - -
horario_buscar_btn = tk.Button(pestana_horario, text="Buscar")
horario_buscar_btn.configure(width=10)
horario_nuevo_btn = tk.Button(pestana_horario, text="Nuevo")
horario_nuevo_btn.configure(width=10)
horario_guardar_btn = tk.Button(pestana_horario, text="Guardar")
horario_guardar_btn.configure(width=10, state="disabled")
horario_cancelar_btn = tk.Button(pestana_horario, text="Cancelar")
horario_cancelar_btn.configure(width=10, state="disabled")
horario_editar_btn = tk.Button(pestana_horario, text="Editar")
horario_editar_btn.configure(width=10, state="disabled")
horario_baja_btn = tk.Button(pestana_horario, text="Baja")
horario_baja_btn.configure(width=10, state="disabled")
#- - - - - - - - - - - - - - - - - - - - - - - - - - Posiciones - - - - - - - - - - - - - - - - - - - - - - -
horario_code_label.grid(column=1, columnspan=2, row=1, padx=10, pady=10, sticky=tk.E)
horario_id_label.grid(column=1, columnspan=1, row=2, padx=10, pady=10, sticky=tk.E)
horario_turno_label.grid(column=1, columnspan=1, row=3, padx=10, pady=10, sticky=tk.E)
horario_hora_label.grid(column=1, columnspan=1, row=4, padx=10, pady=10, sticky=tk.E)
horario_code_entry.configure(width=30)
horario_code_entry.grid(column=3, columnspan=2, row=1, padx=10, pady=10, sticky=tk.W)
horario_id_entry.configure(width=15)
horario_id_entry.grid(column=2, columnspan=2, row=2, padx=10, pady=10, sticky=tk.W)
horario_turno_optionMenu.configure(width=15)
horario_turno_optionMenu.grid(column=2, columnspan=2, row=3, padx=10, pady=10, sticky=tk.W)
horario_hora_optionMenu.configure(width=15)
horario_hora_optionMenu.grid(column=2, columnspan=2, row=4, padx=10, pady=10, sticky=tk.W)

horario_buscar_btn.grid(column=5, columnspan=1, row=1, padx=10, pady=10, sticky=tk.E)
horario_nuevo_btn.grid(column=1, columnspan=1, row=6, padx=10, pady=10, sticky=tk.E)
horario_guardar_btn.grid(column=2, columnspan=1, row=6, padx=10, pady=10, sticky=tk.E)
horario_cancelar_btn.grid(column=3, columnspan=1, row=6, padx=10, pady=10, sticky=tk.E)
horario_editar_btn.grid(column=4, columnspan=1, row=6, padx=10, pady=10, sticky=tk.E)
horario_baja_btn.grid(column=5, columnspan=1, row=6, padx=10, pady=10, sticky=tk.E)

#---------------------------------------------------------SALON ----------------------------------------------------
pestana_salon = ttk.Frame(pestanas)
pestanas.add(pestana_salon, text="Salón")
pestanas.tab(7, state="normal")
#- - - - - - - - - - - - - - - - - - - - - - - Entries y etiquetas - - - - - - - - - - - - - - - - - - - -
salon_code_label = tk.Label(pestana_salon, text="Ingrese codigo de salón: ")
salon_id_label = tk.Label(pestana_salon, text="ID:")
salon_salon_label = tk.Label(pestana_salon, text="Nombre Salon: ")
salon_edificio_label = tk.Label(pestana_salon, text="Edificio: ")
salon_code_entry = tk.Entry(pestana_salon)
salon_salon_entry = tk.Entry(pestana_salon)
salon_id_entry = tk.Entry(pestana_salon, state="disabled")

salon_edificio_selection = tk.StringVar(main)
salon_edificio_options = ("edificio", "edificio2", "edificio#")
salon_edificio_optionMenu = tk.OptionMenu(pestana_salon, salon_edificio_selection, *salon_edificio_options)
salon_edificio_optionMenu.configure(state="normal")

#- - - - - - - - - - - - - - - - - - - - - - - - - - Botones - - - - - - - - - - - - - - - - - - - - - - -

salon_buscar_btn = tk.Button(pestana_salon, text="Buscar")
salon_buscar_btn.configure(width=10)
salon_nuevo_btn = tk.Button(pestana_salon, text="Nuevo")
salon_nuevo_btn.configure(width=10)
salon_guardar_btn = tk.Button(pestana_salon, text="Guardar")
salon_guardar_btn.configure(width=10, state="disabled")
salon_cancelar_btn = tk.Button(pestana_salon, text="Cancelar")
salon_cancelar_btn.configure(width=10, state="disabled")
salon_editar_btn = tk.Button(pestana_salon, text="Editar")
salon_editar_btn.configure(width=10, state="disabled")
salon_baja_btn = tk.Button(pestana_salon, text="Baja")
salon_baja_btn.configure(width=10, state="disabled")
#- - - - - - - - - - - - - - - - - - - - - - - - - - Posiciones - - - - - - - - - - - - - - - - - - - - - - -
salon_code_label.grid(column=1, columnspan=2, row=0, padx=10, pady=10, sticky=tk.E)
salon_id_label.grid(column=1, columnspan=1, row=1, padx=10, pady=10, sticky=tk.E)
salon_salon_label.grid(column=1, columnspan=1, row=2, padx=10, pady=10, sticky=tk.E)
salon_code_entry.grid(column=3, columnspan=2, row=0, padx=10, pady=10, sticky=tk.W)
salon_code_entry.configure(width=30)
salon_salon_entry.grid(column=2, columnspan=2, row=2, padx=10, pady=10, sticky=tk.W)
salon_salon_entry.configure(width=30)
salon_id_entry.grid(column=2, columnspan=2, row=1, padx=10, pady=10, sticky=tk.W)
salon_id_entry.configure(width=15)

salon_edificio_label.grid(column=1, columnspan=1, row=3, padx=10, pady=10, sticky=tk.E)
salon_edificio_optionMenu.grid(column=2, columnspan=1, row=3, padx=10, pady=10, sticky=tk.E)
salon_edificio_optionMenu.configure(width=8)



salon_buscar_btn.grid(column=5, columnspan=1, row=0, padx=10, pady=10, sticky=tk.E)
salon_nuevo_btn.grid(column=1, columnspan=1, row=6, padx=10, pady=10, sticky=tk.E)
salon_guardar_btn.grid(column=2, columnspan=1, row=6, padx=10, pady=10, sticky=tk.E)
salon_cancelar_btn.grid(column=3, columnspan=1, row=6, padx=10, pady=10, sticky=tk.E)
salon_editar_btn.grid(column=4, columnspan=1, row=6, padx=10, pady=10, sticky=tk.E)
salon_baja_btn.grid(column=5, columnspan=1, row=6, padx=10, pady=10, sticky=tk.E)

#--------------------------------------------------------CARRERA ---------------------------------------------------
pestana_carrera = ttk.Frame(pestanas)
pestanas.add(pestana_carrera, text="Carrera")
pestanas.tab(8, state="normal")
#- - - - - - - - - - - - - - - - - - - - - - - Entries y etiquetas - - - - - - - - - - - - - - - - - - - -
carrera_code_label = tk.Label(pestana_carrera, text="Ingrese codigo de carrera: ")
carrera_id_label = tk.Label(pestana_carrera, text="ID:")
carrera_nombre_label = tk.Label(pestana_carrera, text="Nombre de Carrera: ")
carrera_semestres_label = tk.Label(pestana_carrera, text="Numero de Semestres: ")
carrera_materia_label = tk.Label(pestana_carrera, text="Materia: ")
carrera_code_entry = tk.Entry(pestana_carrera)
carrera_nombre_entry = tk.Entry(pestana_carrera)
carrera_semestres_entry = tk.Entry(pestana_carrera)
carrera_id_entry = tk.Entry(pestana_carrera, state="disabled")

carrera_materia_selection = tk.StringVar(main)
carrera_materia_options = ("materia", "materia2", "materia#")
carrera_materia_optionMenu = tk.OptionMenu(pestana_carrera, carrera_materia_selection, *carrera_materia_options)
carrera_materia_optionMenu.configure(state="normal")

#- - - - - - - - - - - - - - - - - - - - - - - - - - Botones - - - - - - - - - - - - - - - - - - - - - - -

carrera_buscar_btn = tk.Button(pestana_carrera, text="Buscar")
carrera_buscar_btn.configure(width=10)
carrera_nuevo_btn = tk.Button(pestana_carrera, text="Nuevo")
carrera_nuevo_btn.configure(width=10)
carrera_guardar_btn = tk.Button(pestana_carrera, text="Guardar")
carrera_guardar_btn.configure(width=10, state="disabled")
carrera_cancelar_btn = tk.Button(pestana_carrera, text="Cancelar")
carrera_cancelar_btn.configure(width=10, state="disabled")
carrera_editar_btn = tk.Button(pestana_carrera, text="Editar")
carrera_editar_btn.configure(width=10, state="disabled")
carrera_baja_btn = tk.Button(pestana_carrera, text="Baja")
carrera_baja_btn.configure(width=10, state="disabled")
#- - - - - - - - - - - - - - - - - - - - - - - - - - Posiciones - - - - - - - - - - - - - - - - - - - - - - -
carrera_code_label.grid(column=1, columnspan=2, row=0, padx=10, pady=10, sticky=tk.E)
carrera_id_label.grid(column=1, columnspan=1, row=1, padx=10, pady=10, sticky=tk.E)
carrera_nombre_label.grid(column=1, columnspan=1, row=2, padx=10, pady=10, sticky=tk.E)
carrera_semestres_label.grid(column=1, columnspan=1, row=3, padx=10, pady=10, sticky=tk.E)
carrera_code_entry.grid(column=3, columnspan=2, row=0, padx=10, pady=10, sticky=tk.W)
carrera_code_entry.configure(width=30)
carrera_nombre_entry.grid(column=2, columnspan=2, row=2, padx=10, pady=10, sticky=tk.W)
carrera_nombre_entry.configure(width=30)
carrera_semestres_entry.grid(column=2, columnspan=2, row=3, padx=10, pady=10, sticky=tk.W)
carrera_semestres_entry.configure(width=30)
carrera_id_entry.grid(column=2, columnspan=2, row=1, padx=10, pady=10, sticky=tk.W)
carrera_id_entry.configure(width=15)

carrera_materia_label.grid(column=1, columnspan=1, row=4, padx=10, pady=10, sticky=tk.E)
carrera_materia_optionMenu.grid(column=2, columnspan=2, row=4, padx=10, pady=10, sticky=tk.W)
carrera_materia_optionMenu.configure(width=20)



carrera_buscar_btn.grid(column=5, columnspan=1, row=0, padx=10, pady=10, sticky=tk.E)
carrera_nuevo_btn.grid(column=1, columnspan=1, row=6, padx=10, pady=10, sticky=tk.E)
carrera_guardar_btn.grid(column=2, columnspan=1, row=6, padx=10, pady=10, sticky=tk.E)
carrera_cancelar_btn.grid(column=3, columnspan=1, row=6, padx=10, pady=10, sticky=tk.E)
carrera_editar_btn.grid(column=4, columnspan=1, row=6, padx=10, pady=10, sticky=tk.E)
carrera_baja_btn.grid(column=5, columnspan=1, row=6, padx=10, pady=10, sticky=tk.E)
#-------------------------------------------------------PLANEACIÓN -------------------------------------------------
pestana_planeacion = ttk.Frame(pestanas)
pestanas.add(pestana_planeacion, text="Planeación")
pestanas.tab(9, state="normal")
#==============================================================================================================

#=======================================================AJUSTES DE POSICION====================================
void_label_usuarios = tk.Label(pestana_usuarios, text="")
void_label_usuarios.grid(column=6, row=6, sticky=tk.NSEW)
void_label_usuarios.configure(width=18)
void_label_usuarios2 = tk.Label(pestana_usuarios, text="")
void_label_usuarios2.grid(column=0, row=0, sticky=tk.NSEW)
void_label_usuarios2.configure(width=18, height=2)
void_label_materias1 = tk.Label(pestana_materias, text="")
void_label_materias1.grid(column=0, row=0, sticky=tk.NSEW)
void_label_materias1.configure(width=18, height=2)
void_label_horario = tk.Label(pestana_horario, text="")
void_label_horario.configure(width=15)
void_label_horario.grid(column=0, row=3, sticky=tk.NSEW)
void_label_horario2 = tk.Label(pestana_horario, text="")
void_label_horario2.configure(width=15, height=2)
void_label_horario2.grid(column=0, row=0, sticky=tk.NSEW)
void_label_salon1 = tk.Label(pestana_salon, text="")
void_label_salon1.configure(width=15, height=2)
void_label_salon1.grid(column=0, row=0, sticky=tk.NSEW)
void_label_carrera1 = tk.Label(pestana_carrera, text="")
void_label_carrera1.configure(width=13, height=2)
void_label_carrera1.grid(column=0, row=0, sticky=tk.NSEW)
pestana_usuarios.columnconfigure(0, weight=1)
pestana_usuarios.columnconfigure(6, weight=1)
pestana_login.columnconfigure(0, weight=1)
pestana_login.columnconfigure(3, weight=1)
pestana_login.rowconfigure(0, weight=1)
pestana_login.rowconfigure(5, weight=1)
pestana_alumnos.columnconfigure(6, weight=1)
pestana_maestros.columnconfigure(6, weight=1)
pestana_materias.rowconfigure(5, weight=1)
pestana_horario.rowconfigure(4, weight=1)
pestana_horario.columnconfigure(6, weight=1)
pestana_salon.rowconfigure(5, weight=1)
pestana_salon.columnconfigure(6, weight=1)
pestana_carrera.rowconfigure(6, weight=1)
pestana_carrera.columnconfigure(6, weight=1)
#===============================================================================================================

#======================================================FUNCIONES================================================
#----------------------------------------------Funcionamiento general-------------------------------------------
def dormirPestanas(code): #Se introduce un binario que indica que pestañas dormir y cuáles mantener despiertas
    for x in range(0, len(code)):
        if code[x] == '0':
            pestanas.tab(x, state="disable")
        else:
            pestanas.tab(x, state="normal")

def validarCampoNoVacio(lista, mensaje): #Se usa cuando hay que verificar qun campo no se quede vacío
    for x in lista:
        if x.get() == "":
            if mensaje == 1:
                messagebox.showwarning(title="Campo vacío", message="El campo \"" + str(x.winfo_name()) + "\" no puede estar vacío")
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

def limpiarCampos(listaCampos):
    for campo in listaCampos:
        campo.delete(0, tk.END)

#-----------------------------------------------------Login----------------------------------------------------
def login():
    Objeto = Conexion()
    listaCampos = {username_entry, password_entry}
    Objeto = Objeto.obtenerObjeto("usuarios", "usuario", username_entry.get())
    if validarCampoNoVacio(listaCampos, 1):
        if username_entry.get() == Objeto.get("usuario"):
            if password_entry.get() == Objeto.get("password"):
                if Objeto.get("perfil") == "Admin":
                    dormirPestanas("1111111111")
                elif Objeto.get("perfil") == "Maestro":
                    dormirPestanas("1101000000")
                elif Objeto.get("perfil") == "Alumno":
                    dormirPestanas("1110000000")
                messagebox.showinfo(title="Bienvenido!", message="Bienvenido " + Objeto.get("nombre") + "!")
                pestanas.select(pestana_usuarios)
                limpiarCampos(listaCampos)
                return 0
            else:
                messagebox.showerror(title="Credenciales erróneas", message="Ha introducido una contraseña inválida")
                return 0
        messagebox.showerror(title="Credenciales erróneas", message="No se encontró el nombre de usuario")

#--------------------------------------------------------------------------------------------------------------
#----------------------------------------------------Usuarios--------------------------------------------------
def buscarUsuarios():
    listaCampos = {user_code_entry}
    if validarCampoNoVacio(listaCampos, 0):
        Usuario = Conexion()
        Usuario = Usuario.obtenerObjeto("usuarios", "idusuario", user_code_entry.get())
        if Usuario:            
            user_editar_btn.configure(state="normal")
            user_cancelar_btn.configure(state="normal")
            user_baja_btn.configure(state="normal")
            listaCampos = ( user_id_entry, 
                            user_nombre_entry, 
                            user_apellidoP_entry, 
                            user_apellidoM_entry, 
                            user_email_entry, 
                            user_username_entry, 
                            user_password_entry)
            listaDatos = ("idusuario", "nombre", "ap", "am", "correo", "usuario", "password")
            llenarCampos(listaCampos, listaDatos, Usuario)
            user_perfil_selection.set(Usuario.get("perfil"))    
            return 0
        else:
            messagebox.showerror(title="No se encuentra", message= "No se encontró el código")
    else: 
        objetos = []
        mensaje = "Lista de usuarios: \n"
        conexion = Conexion()
        ids = conexion.obtenerColumna("usuarios", "idusuario")
        for idindex in range(0, len(ids)):
            objetos.append(conexion.obtenerObjeto("usuarios", "idusuario", ids[idindex]))
            mensaje += "\nID: " + str(objetos[idindex].get("idusuario")) + "  \t|  Usuario: " + str(objetos[idindex].get("usuario")) + "\n"
        messagebox.showinfo(title="Búsqueda general", message=mensaje)
        listaCampos = ( user_id_entry, 
                        user_nombre_entry, 
                        user_apellidoP_entry, 
                        user_apellidoM_entry, 
                        user_email_entry, 
                        user_username_entry, 
                        user_password_entry)
        bloquearCampos(False, listaCampos)
        limpiarCampos(listaCampos)
        bloquearCampos(True, listaCampos)

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
                           user_baja_btn,
                           user_buscar_btn,
                           user_code_entry}
    listaOtros = {user_editar_btn,
                  user_perfil_optionMenu,
                  user_cancelar_btn,
                  user_guardar_btn}
    bloquearCampos(False, listaCampos)
    bloquearCampos(False, listaOtros)
    bloquearCampos(True, listaCamposBloquear)

def cancelarUsuario():
    listaCampos = {user_code_entry, 
                    user_id_entry,
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
    limpiarCampos(listaCampos)
    bloquearCampos(True, listaCampos)
    bloquearCampos(True, listaOtros)
    bloquearCampos(False, listaCamposBloquear)
    # buscarUsuarios()

def guardarUsuario():
    Usuario = {"nombre" : user_nombre_entry.get(),
                "ap" : user_apellidoP_entry.get(),
                "am" : user_apellidoM_entry.get(),
                "correo" : user_email_entry.get(),
                "usuario" : user_username_entry.get(),
                "password" : user_password_entry.get(),
                "perfil" : user_perfil_selection.get()}
    objeto = Conexion()
    listaCampos = {user_id_entry}
    if validarCampoNoVacio(listaCampos, 0):
        messagebox.showinfo(title="Operación exitosa", message= "Se ha editado el registro con exito"), cancelarUsuario() if objeto.actualizarObjeto(Usuario, "usuarios", "idusuario", user_id_entry.get()) == 0 else  messagebox.showerror(title="Error", message= "No se ha podido realizar la operación")
    else:
        listaCampos = {user_nombre_entry, user_username_entry, user_password_entry}
        if validarCampoNoVacio(listaCampos, 1):
            if objeto.insertarNuevoObjeto(Usuario, "usuarios") == 0:
                Usuario = objeto.obtenerObjeto("usuarios", "nombre", user_nombre_entry.get())
                messagebox.showinfo(title="Operación exitosa", message= "Se ha agregado el registro con exito\nEl ID del nuevo usuario es: " + str(Usuario.get("idusuario")))
                cancelarUsuario() 
                user_code_entry.configure(state="normal")
                user_code_entry.delete(0, tk.END)
                user_code_entry.insert(0, Usuario.get("idusuario"))
                buscarUsuarios()
            else:  
                messagebox.showerror(title="Error", message= "No se ha podido agregar el registro")

def nuevoUsuario():
    cancelarUsuario()
    editarUsuario()

def bajaUsuario():
    listaCampos = {user_id_entry}
    if validarCampoNoVacio(listaCampos, 1):
        objeto = Conexion()
        returnValue = 0
        popupWindow = tk.Toplevel(main)
        popupWindow.wm_title("¡Advertencia!")
        popupWindow.tkraise(main)
        tk.Label(popupWindow, text="¿Está seguro que desea eliminar el registro con ID = " + str(user_id_entry.get()) + "?\nEsta operación no se puede deshacer").grid(columnspan=2, column=0, row=0, padx=15, pady=15)
        tk.Button(popupWindow, text="Cancelar", command=lambda:[popupWindow.destroy()]).grid(column=0, row=1, padx=10, pady=10)
        tk.Button(popupWindow, text="Eliminar", command=lambda:[messagebox.showinfo(title="Operación exitosa", message="Se ha eliminado el registro") if
                                                                objeto.eliminarObjeto("usuarios", str(user_id_entry.get()), "idusuario") == 0 else 
                                                                messagebox.showerror(title="Operación fallida", message="No se ha podido eliminar el registro"),
                                                                popupWindow.destroy(), cancelarUsuario()]).grid(column=1, row=1, padx=10, pady=10)


#--------------------------------------------------------------------------------------------------------------
#===============================================================================================================

dormirPestanas("1111111111")
pestanas.select(pestana_maestros)

main.mainloop()
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
conexion = Conexion()
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

#- - - - - - - - - - - - - - - - - - - - - - - Entries y etiquetas - - - - - - - - - - - - - - - - - - - -
alumno_code_label = tk.Label(pestana_alumnos, text="Ingrese codigo de alumno: ")
alumno_id_label = tk.Label(pestana_alumnos, text="ID:")
alumno_nombre_label = tk.Label(pestana_alumnos, text="Nombre: ")
alumno_apellidoP_label = tk.Label(pestana_alumnos, text="Apellido Paterno: ")
alumno_apellidoM_label = tk.Label(pestana_alumnos, text="Apellido Materno: ")
alumno_email_label = tk.Label(pestana_alumnos, text="Email: ")
alumno_estado_label = tk.Label(pestana_alumnos, text="Estado: ")
alumno_fechanac_label = tk.Label(pestana_alumnos, text="Fech. de Nac.: ")
alumno_carrera_label = tk.Label(pestana_alumnos, text="Carrera: ")
alumno_grupo_label = tk.Label(pestana_alumnos, text="Grupo: ")
alumno_code_entry = tk.Entry(pestana_alumnos)
alumno_id_entry = tk.Entry(pestana_alumnos, state="disabled")
alumno_nombre_entry = tk.Entry(pestana_alumnos, state="disabled")
alumno_apellidoP_entry = tk.Entry(pestana_alumnos, state="disabled")
alumno_apellidoM_entry = tk.Entry(pestana_alumnos, state="disabled")
alumno_email_entry = tk.Entry(pestana_alumnos, state="disabled")
alumno_estado_selection = tk.StringVar(value="Jalisco")
alumno_estado_options = ("Aguascalientes", "Colima", "Jalisco", "Nayarit")
alumno_estado_optionMenu = tk.OptionMenu(pestana_alumnos, alumno_estado_selection, *alumno_estado_options)
alumno_estado_optionMenu.configure(state="disabled")
alumno_fechanac_entry = tk.Entry(pestana_alumnos, state="disabled")
alumno_carrera_selection = tk.StringVar(main)
alumno_carrera_options = conexion.obtenerColumna("carrera", "nombre")
alumno_carrera_optionMenu = tk.OptionMenu(pestana_alumnos, alumno_carrera_selection, *alumno_carrera_options)
alumno_carrera_optionMenu.configure(state="disabled")
alumno_grupo_selection = tk.StringVar(main)
alumno_grupo_options = conexion.obtenerColumna("grupos", "nombre")
alumno_grupo_optionMenu = tk.OptionMenu(pestana_alumnos, alumno_grupo_selection, *alumno_grupo_options)
alumno_grupo_optionMenu.configure(state="disabled")

#- - - - - - - - - - - - - - - - - - - - - - - - - - Botones - - - - - - - - - - - - - - - - - - - - - - -
alumno_buscar_btn = tk.Button(pestana_alumnos, text="Buscar", command=lambda:buscarAlumnos())
alumno_buscar_btn.configure(width=10)
alumno_nuevo_btn = tk.Button(pestana_alumnos, text="Nuevo", command=lambda:nuevoAlumno())
alumno_nuevo_btn.configure(width=10)
alumno_guardar_btn = tk.Button(pestana_alumnos, text="Guardar", command=lambda:guardarAlumno())
alumno_guardar_btn.configure(width=10, state="disabled")
alumno_cancelar_btn = tk.Button(pestana_alumnos, text="Cancelar", command=lambda:cancelarAlumno())
alumno_cancelar_btn.configure(width=10, state="disabled")
alumno_editar_btn = tk.Button(pestana_alumnos, text="Editar", command=lambda:editarAlumno())
alumno_editar_btn.configure(width=10, state="disabled")
alumno_baja_btn = tk.Button(pestana_alumnos, text="Baja", command=lambda:bajaAlumno())
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
alumno_grupo_label.grid(column=3, columnspan=1, row=4, padx=10, pady=10, sticky=tk.E)
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
alumno_grupo_optionMenu.grid(column=4, columnspan=2, row=4, padx=10, pady=10, sticky=tk.W)
alumno_grupo_optionMenu.configure(width=20)
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
maestro_grupo_label = tk.Label(pestana_maestros, text="Grupo: ")
maestro_code_entry = tk.Entry(pestana_maestros)
maestro_id_entry = tk.Entry(pestana_maestros, state="disabled")
maestro_nombre_entry = tk.Entry(pestana_maestros, state="disabled")
maestro_apellidoP_entry = tk.Entry(pestana_maestros, state="disabled")
maestro_apellidoM_entry = tk.Entry(pestana_maestros, state="disabled")
maestro_email_entry = tk.Entry(pestana_maestros, state="disabled")
maestro_carrera_selection = tk.StringVar(main)
maestro_carrera_options = conexion.obtenerColumna("carrera", "nombre")
maestro_carrera_optionMenu = tk.OptionMenu(pestana_maestros, maestro_carrera_selection, *maestro_carrera_options)
maestro_carrera_optionMenu.configure(state="normal")
maestro_materia_selection = tk.StringVar(main)
maestro_materia_options = conexion.obtenerColumna("materias", "nombre")
maestro_materia_optionMenu = tk.OptionMenu(pestana_maestros, maestro_materia_selection, *maestro_materia_options)
maestro_materia_optionMenu.configure(state="normal")
maestro_grupo_selection = tk.StringVar(main)
maestro_grupo_options = conexion.obtenerColumna("grupos", "nombre")
maestro_grupo_optionMenu = tk.OptionMenu(pestana_maestros, maestro_grupo_selection, *maestro_grupo_options)
maestro_grupo_optionMenu.configure(state="normal")

#- - - - - - - - - - - - - - - - - - - - - - - - - - Botones - - - - - - - - - - - - - - - - - - - - - - -
maestro_buscar_btn = tk.Button(pestana_maestros, text="Buscar", command=lambda:buscarMaestros())
maestro_buscar_btn.configure(width=10)
maestro_nuevo_btn = tk.Button(pestana_maestros, text="Nuevo", command=lambda:nuevoMaestro())
maestro_nuevo_btn.configure(width=10)
maestro_guardar_btn = tk.Button(pestana_maestros, text="Guardar", command=lambda:guardarMaestro())
maestro_guardar_btn.configure(width=10, state="disabled")
maestro_cancelar_btn = tk.Button(pestana_maestros, text="Cancelar", command=lambda:cancelarMaestro())
maestro_cancelar_btn.configure(width=10, state="disabled")
maestro_editar_btn = tk.Button(pestana_maestros, text="Editar", command=lambda:editarMaestro())
maestro_editar_btn.configure(width=10, state="disabled")
maestro_baja_btn = tk.Button(pestana_maestros, text="Baja", command=lambda:bajaMaestro())
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
maestro_grupo_label.grid(column=3, columnspan=1, row=5, padx=10, pady=10, sticky=tk.E)
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
maestro_grupo_optionMenu.grid(column=4, columnspan=2, row=5, padx=10, pady=10, sticky=tk.W)
maestro_grupo_optionMenu.configure(width=16)
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
materia_carrera_options = conexion.obtenerColumna("carrera", "nombre")
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
grupo_carrera_options = conexion.obtenerColumna("carrera", "nombre")
grupo_carrera_optionMenu = tk.OptionMenu(pestana_grupos, grupo_carrera_selection, *grupo_carrera_options)
grupo_carrera_optionMenu.configure(state="normal")
grupo_materia_selection = tk.StringVar(main)
grupo_materia_options = conexion.obtenerColumna("materias", "nombre")
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
horario_turno_options = conexion.obtenerColumna("horario", "turno")
horario_turno_optionMenu = tk.OptionMenu(pestana_horario, horario_turno_selection, *horario_turno_options)
horario_turno_optionMenu.configure(state="normal")
horario_hora_selection = tk.StringVar(main)
horario_hora_options = conexion.obtenerColumna("horario", "hora")
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
salon_nombre_label = tk.Label(pestana_salon, text="Nombre Salon: ")
salon_edificio_label = tk.Label(pestana_salon, text="Edificio: ")
salon_code_entry = tk.Entry(pestana_salon)
salon_nombre_entry = tk.Entry(pestana_salon, state="disabled")
salon_id_entry = tk.Entry(pestana_salon, state="disabled")

salon_edificio_selection = tk.StringVar(main)
salon_edificio_options = conexion.obtenerColumna("salon", "edificio")
salon_edificio_optionMenu = tk.OptionMenu(pestana_salon, salon_edificio_selection, *salon_edificio_options)
salon_edificio_optionMenu.configure(state="disabled")

#- - - - - - - - - - - - - - - - - - - - - - - - - - Botones - - - - - - - - - - - - - - - - - - - - - - -

salon_buscar_btn = tk.Button(pestana_salon, text="Buscar", command=lambda:buscarSalon())
salon_buscar_btn.configure(width=10)
salon_nuevo_btn = tk.Button(pestana_salon, text="Nuevo", command=lambda:nuevoSalon())
salon_nuevo_btn.configure(width=10)
salon_guardar_btn = tk.Button(pestana_salon, text="Guardar", command=lambda:guardarSalon())
salon_guardar_btn.configure(width=10, state="disabled")
salon_cancelar_btn = tk.Button(pestana_salon, text="Cancelar", command=lambda:cancelarSalon())
salon_cancelar_btn.configure(width=10, state="disabled")
salon_editar_btn = tk.Button(pestana_salon, text="Editar", command=lambda:editarSalon())
salon_editar_btn.configure(width=10, state="disabled")
salon_baja_btn = tk.Button(pestana_salon, text="Baja", command=lambda:bajaSalon())
salon_baja_btn.configure(width=10, state="disabled")
#- - - - - - - - - - - - - - - - - - - - - - - - - - Posiciones - - - - - - - - - - - - - - - - - - - - - - -
salon_code_label.grid(column=1, columnspan=2, row=0, padx=10, pady=10, sticky=tk.E)
salon_id_label.grid(column=1, columnspan=1, row=1, padx=10, pady=10, sticky=tk.E)
salon_nombre_label.grid(column=1, columnspan=1, row=2, padx=10, pady=10, sticky=tk.E)
salon_code_entry.grid(column=3, columnspan=2, row=0, padx=10, pady=10, sticky=tk.W)
salon_code_entry.configure(width=30)
salon_nombre_entry.grid(column=2, columnspan=2, row=2, padx=10, pady=10, sticky=tk.W)
salon_nombre_entry.configure(width=30)
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
carrera_materia_options = conexion.obtenerColumna("materias", "nombre")
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

def validarCampoNoVacio(lista, mensaje): #Se usa cuando hay que verificar que un campo no se quede vacío
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

def llenarOptMenu(tabla, columna):
    listaOpciones = ()
    listaOpciones = Conexion().obtenerColumna(tabla, columna)
    return listaOpciones

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
    listaCamposBloquear = {user_nuevo_btn,
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

#----------------------------------------------------Alumnos---------------------------------------------------
def buscarAlumnos():
    listaCampos = {alumno_code_entry}
    if validarCampoNoVacio(listaCampos, 0):
        Alumno = Conexion()
        Alumno = Alumno.obtenerObjeto("alumnos", "id", alumno_code_entry.get())
        if Alumno:
            alumno_editar_btn.configure(state="normal")
            alumno_cancelar_btn.configure(state="normal")
            alumno_baja_btn.configure(state="normal")
            listaCampos = ( alumno_id_entry,
                            alumno_nombre_entry,
                            alumno_apellidoP_entry,
                            alumno_apellidoM_entry,
                            alumno_email_entry,
                            alumno_fechanac_entry)
            listaDatos = ("id", "nombre", "ap", "am", "correo", "fechanacimiento")
            llenarCampos(listaCampos, listaDatos, Alumno)
            alumno_estado_selection.set(Alumno.get("estado"))
            alumno_carrera_selection.set(Alumno.get("carrera_id"))
            alumno_grupo_selection.set(Alumno.get("grupo_id"))

            return 0
        else:
            messagebox.showerror(title="No se encuentra", message= "No se encontró el código")
    else: 
        objetos = []
        mensaje = "Lista de alumnos: \n"
        conexion = Conexion()
        ids = conexion.obtenerColumna("alumnos", "id")
        for idindex in range(0, len(ids)):
            objetos.append(conexion.obtenerObjeto("alumnos", "id", ids[idindex]))
            mensaje += "\nID: " + str(objetos[idindex].get("id")) + "  \t|  Alumno: " + str(objetos[idindex].get("nombre")) + "\n"
        messagebox.showinfo(title="Búsqueda general", message=mensaje)
        listaCampos = ( alumno_id_entry,
                        alumno_nombre_entry,
                        alumno_apellidoP_entry,
                        alumno_apellidoM_entry,
                        alumno_email_entry,
                        alumno_fechanac_entry)
        bloquearCampos(False, listaCampos)
        limpiarCampos(listaCampos)
        bloquearCampos(True, listaCampos)

def editarAlumno():
    listaCampos = { alumno_nombre_entry,
                    alumno_apellidoP_entry,
                    alumno_apellidoM_entry,
                    alumno_email_entry,
                    alumno_fechanac_entry}
    listaCamposBloquear = {alumno_editar_btn,
                           alumno_nuevo_btn,
                           alumno_baja_btn,
                           alumno_buscar_btn,
                           alumno_code_entry}
    listaOtros = {alumno_editar_btn,
                  alumno_grupo_optionMenu,
                  alumno_estado_optionMenu,
                  alumno_carrera_optionMenu,
                  alumno_cancelar_btn,
                  alumno_guardar_btn}
    bloquearCampos(False, listaCampos)
    bloquearCampos(False, listaOtros)
    bloquearCampos(True, listaCamposBloquear)

def cancelarAlumno():
    listaCampos = {alumno_code_entry, 
                    alumno_id_entry,
                    alumno_nombre_entry, 
                    alumno_apellidoP_entry, 
                    alumno_apellidoM_entry, 
                    alumno_email_entry,
                    alumno_fechanac_entry}
    listaCamposBloquear = {alumno_nuevo_btn,
                           alumno_buscar_btn,
                           alumno_code_entry}
    listaOtros = {alumno_baja_btn,
                  alumno_editar_btn,
                  alumno_grupo_optionMenu,
                  alumno_estado_optionMenu,
                  alumno_carrera_optionMenu,
                  alumno_cancelar_btn,
                  alumno_guardar_btn}
    bloquearCampos(False, listaCampos)
    limpiarCampos(listaCampos)
    bloquearCampos(True, listaCampos)
    bloquearCampos(True, listaOtros)
    bloquearCampos(False, listaCamposBloquear)

def guardarAlumno():
    Alumno = {"nombre" : alumno_nombre_entry.get(),
                "ap" : alumno_apellidoP_entry.get(),
                "am" : alumno_apellidoM_entry.get(),
                "correo" : alumno_email_entry.get(),
                "estado" : alumno_estado_selection.get(),
                "fechanacimiento" : alumno_fechanac_entry.get(),
                "carrera_id" : alumno_carrera_selection.get(),
                "grupo_id" : alumno_grupo_selection.get()}
    objeto = Conexion()
    listaCampos = {alumno_id_entry}
    if validarCampoNoVacio(listaCampos, 0):
        messagebox.showinfo(title="Operación exitosa", message= "Se ha editado el registro con exito"), cancelarAlumno() if objeto.actualizarObjeto(Alumno, "alumnos", "id", alumno_id_entry.get()) == 0 else  messagebox.showerror(title="Error", message= "No se ha podido realizar la operación")
    else:
        listaCampos = {alumno_nombre_entry, alumno_apellidoP_entry}
        if validarCampoNoVacio(listaCampos, 1):
            if objeto.insertarNuevoObjeto(Alumno, "alumnos") == 0:
                Alumno = objeto.obtenerObjeto("alumnos", "nombre", alumno_nombre_entry.get())
                messagebox.showinfo(title="Operación exitosa", message= "Se ha agregado el registro con exito\nEl ID del nuevo Alumno es: " + str(Alumno.get("id")))
                cancelarAlumno() 
                alumno_code_entry.configure(state="normal")
                alumno_code_entry.delete(0, tk.END)
                alumno_code_entry.insert(0, Alumno.get("id"))
                buscarAlumnos()
            else:  
                messagebox.showerror(title="Error", message= "No se ha podido agregar el registro")

def nuevoAlumno():
    cancelarAlumno()
    editarAlumno()

def bajaAlumno():
    listaCampos = {alumno_id_entry}
    if validarCampoNoVacio(listaCampos, 1):
        objeto = Conexion()
        popupWindow = tk.Toplevel(main)
        popupWindow.wm_title("¡Advertencia!")
        popupWindow.tkraise(main)
        tk.Label(popupWindow, text="¿Está seguro que desea eliminar el registro con ID = " + str(alumno_id_entry.get()) + "?\nEsta operación no se puede deshacer").grid(columnspan=2, column=0, row=0, padx=15, pady=15)
        tk.Button(popupWindow, text="Cancelar", command=lambda:[popupWindow.destroy()]).grid(column=0, row=1, padx=10, pady=10)
        tk.Button(popupWindow, text="Eliminar", command=lambda:[messagebox.showinfo(title="Operación exitosa", message="Se ha eliminado el registro") if
                                                                objeto.eliminarObjeto("alumnos", str(alumno_id_entry.get()), "id") == 0 else 
                                                                messagebox.showerror(title="Operación fallida", message="No se ha podido eliminar el registro"),
                                                                popupWindow.destroy(), cancelarAlumno()]).grid(column=1, row=1, padx=10, pady=10)


#--------------------------------------------------------------------------------------------------------------

#----------------------------------------------------Maestros--------------------------------------------------
def buscarMaestros():
    listaCampos = {maestro_code_entry}
    if validarCampoNoVacio(listaCampos, 0):
        Maestro = Conexion()
        Maestro = Maestro.obtenerObjeto("maestros", "id", maestro_code_entry.get())
        if Maestro:            
            maestro_editar_btn.configure(state="normal")
            maestro_cancelar_btn.configure(state="normal")
            maestro_baja_btn.configure(state="normal")
            listaCampos = ( maestro_id_entry,
                            maestro_nombre_entry,
                            maestro_apellidoP_entry,
                            maestro_apellidoM_entry,
                            maestro_email_entry)
            listaDatos = ("id", "nombre", "ap", "am", "correo")
            llenarCampos(listaCampos, listaDatos, Maestro)
            maestro_carrera_selection.set(Maestro.get("carrera"))
            maestro_materia_selection.set(Maestro.get("materia"))    
            maestro_grupo_selection.set(Maestro.get("grupo_id"))

            return 0
        else:
            messagebox.showerror(title="No se encuentra", message= "No se encontró el código")
    else: 
        objetos = []
        mensaje = "Lista de Maestros: \n"
        conexion = Conexion()
        ids = conexion.obtenerColumna("maestros", "id")
        for idindex in range(0, len(ids)):
            objetos.append(conexion.obtenerObjeto("maestros", "id", ids[idindex]))
            mensaje += "\nID: " + str(objetos[idindex].get("id")) + "  \t|  Maestro: " + str(objetos[idindex].get("nombre")) + "\n"
        messagebox.showinfo(title="Búsqueda general", message=mensaje)
        listaCampos = ( maestro_id_entry,
                        maestro_nombre_entry,
                        maestro_apellidoP_entry,
                        maestro_apellidoM_entry,
                        maestro_email_entry)
        bloquearCampos(False, listaCampos)
        limpiarCampos(listaCampos)
        bloquearCampos(True, listaCampos)

def editarMaestro():
    listaCampos = { maestro_nombre_entry,
                    maestro_apellidoP_entry,
                    maestro_apellidoM_entry,
                    maestro_email_entry}
    listaCamposBloquear = {maestro_editar_btn,
                           maestro_nuevo_btn,
                           maestro_baja_btn,
                           maestro_buscar_btn,
                           maestro_code_entry}
    listaOtros = {maestro_editar_btn,
                  maestro_carrera_optionMenu,
                  maestro_materia_optionMenu,
                  maestro_grupo_optionMenu,
                  maestro_cancelar_btn,
                  maestro_guardar_btn}
    bloquearCampos(False, listaCampos)
    bloquearCampos(False, listaOtros)

    bloquearCampos(True, listaCamposBloquear)

def cancelarMaestro():
    listaCampos = {maestro_code_entry, 
                    maestro_id_entry,
                    maestro_nombre_entry, 
                    maestro_apellidoP_entry, 
                    maestro_apellidoM_entry, 
                    maestro_email_entry}
    listaCamposBloquear = {maestro_nuevo_btn,
                           maestro_buscar_btn,
                           maestro_code_entry}
    listaOtros = {maestro_baja_btn,
                  maestro_editar_btn,
                  maestro_carrera_optionMenu,
                  maestro_materia_optionMenu,
                  maestro_grupo_optionMenu,
                  maestro_cancelar_btn,
                  maestro_guardar_btn}
    bloquearCampos(False, listaCampos)
    limpiarCampos(listaCampos)
    bloquearCampos(True, listaCampos)
    bloquearCampos(True, listaOtros)
    bloquearCampos(False, listaCamposBloquear)

def guardarMaestro():
    Maestro = {"nombre" : maestro_nombre_entry.get(),
                "ap" : maestro_apellidoP_entry.get(),
                "am" : maestro_apellidoM_entry.get(),
                "correo" : maestro_email_entry.get(),
                "carrera" : maestro_carrera_selection.get(),
                "materia" : maestro_materia_selection.get(),
                "grupo_id" : maestro_grupo_selection.get()}
    objeto = Conexion()
    listaCampos = {maestro_id_entry}
    if validarCampoNoVacio(listaCampos, 0):
        messagebox.showinfo(title="Operación exitosa", message= "Se ha editado el registro con exito"), cancelarMaestro() if objeto.actualizarObjeto(Maestro, "maestros", "id", maestro_id_entry.get()) == 0 else  messagebox.showerror(title="Error", message= "No se ha podido realizar la operación")
    else:
        listaCampos = {maestro_nombre_entry, maestro_apellidoP_entry}
        if validarCampoNoVacio(listaCampos, 1):
            if objeto.insertarNuevoObjeto(Maestro, "maestros") == 0:
                Maestro = objeto.obtenerObjeto("maestros", "nombre", maestro_nombre_entry.get())
                messagebox.showinfo(title="Operación exitosa", message= "Se ha agregado el registro con exito\nEl ID del nuevo Maestro es: " + str(Maestro.get("id")))
                cancelarMaestro() 
                maestro_code_entry.configure(state="normal")
                maestro_code_entry.delete(0, tk.END)
                maestro_code_entry.insert(0, Maestro.get("id"))
                buscarMaestros()
            else:  
                messagebox.showerror(title="Error", message= "No se ha podido agregar el registro")

def nuevoMaestro():
    cancelarMaestro()
    editarMaestro()

def bajaMaestro():
    listaCampos = {maestro_id_entry}
    if validarCampoNoVacio(listaCampos, 1):
        objeto = Conexion()
        popupWindow = tk.Toplevel(main)
        popupWindow.wm_title("¡Advertencia!")
        popupWindow.tkraise(main)
        tk.Label(popupWindow, text="¿Está seguro que desea eliminar el registro con ID = " + str(maestro_id_entry.get()) + "?\nEsta operación no se puede deshacer").grid(columnspan=2, column=0, row=0, padx=15, pady=15)
        tk.Button(popupWindow, text="Cancelar", command=lambda:[popupWindow.destroy()]).grid(column=0, row=1, padx=10, pady=10)
        tk.Button(popupWindow, text="Eliminar", command=lambda:[messagebox.showinfo(title="Operación exitosa", message="Se ha eliminado el registro") if
                                                                objeto.eliminarObjeto("maestros", str(maestro_id_entry.get()), "id") == 0 else 
                                                                messagebox.showerror(title="Operación fallida", message="No se ha podido eliminar el registro"),
                                                                popupWindow.destroy(), cancelarMaestro()]).grid(column=1, row=1, padx=10, pady=10)

#--------------------------------------------------------------------------------------------------------------

#------------------------------------------------------Salon---------------------------------------------------
def buscarSalon():
    listaCampos = {salon_code_entry}
    if validarCampoNoVacio(listaCampos, 0):
        Salon = Conexion()
        Salon = Salon.obtenerObjeto("salon", "id", salon_code_entry.get())
        if Salon:            
            salon_editar_btn.configure(state="normal")
            salon_cancelar_btn.configure(state="normal")
            salon_baja_btn.configure(state="normal")
            listaCampos = ( salon_id_entry,
                            salon_nombre_entry)
            listaDatos = ("id", "nombre")
            llenarCampos(listaCampos, listaDatos, Salon)
            salon_edificio_optionMenu.configure(state="normal")
            salon_edificio_selection.set(Salon.get("edificio"))
            salon_edificio_optionMenu.configure(state="disabled")
            return 0
        else:
            messagebox.showerror(title="No se encuentra", message= "No se encontró el código")
    else: 
        objetos = []
        mensaje = "Lista de Salon: \n"
        conexion = Conexion()
        ids = conexion.obtenerColumna("salon", "id")
        for idindex in range(0, len(ids)):
            objetos.append(conexion.obtenerObjeto("salon", "id", ids[idindex]))
            mensaje += "\nID: " + str(objetos[idindex].get("id")) + "  \t|  Salon: " + str(objetos[idindex].get("nombre")) + "\n"
        messagebox.showinfo(title="Búsqueda general", message=mensaje)
        listaCampos = ( salon_id_entry,
                        salon_nombre_entry)
        bloquearCampos(False, listaCampos)
        limpiarCampos(listaCampos)
        bloquearCampos(True, listaCampos)

def editarSalon():
    listaCampos = { salon_nombre_entry}
    listaCamposBloquear = {salon_editar_btn,
                           salon_nuevo_btn,
                           salon_baja_btn,
                           salon_buscar_btn,
                           salon_code_entry}
    listaOtros = {salon_editar_btn,
                  salon_cancelar_btn,
                  salon_guardar_btn,
                  salon_edificio_optionMenu}
    bloquearCampos(False, listaCampos)
    bloquearCampos(False, listaOtros)
    bloquearCampos(True, listaCamposBloquear)

def cancelarSalon():
    listaCampos = {salon_code_entry, 
                    salon_id_entry,
                    salon_nombre_entry}
    listaCamposBloquear = {salon_nuevo_btn,
                           salon_buscar_btn,
                           salon_code_entry}
    listaOtros = {salon_baja_btn,
                  salon_editar_btn,
                  salon_cancelar_btn,
                  salon_guardar_btn,
                  salon_edificio_optionMenu}
    bloquearCampos(False, listaCampos)
    limpiarCampos(listaCampos)
    bloquearCampos(True, listaCampos)
    bloquearCampos(True, listaOtros)
    bloquearCampos(False, listaCamposBloquear)

def guardarSalon():
    Salon = {"nombre" : salon_nombre_entry.get(),
             "edificio" : int(salon_edificio_selection.get())}
    objeto = Conexion()
    listaCampos = {salon_id_entry}
    if validarCampoNoVacio(listaCampos, 0):
        messagebox.showinfo(title="Operación exitosa", message= "Se ha editado el registro con exito"), cancelarSalon() if objeto.actualizarObjeto(Salon, "salon", "id", int(salon_id_entry.get())) == 0 else  messagebox.showerror(title="Error", message= "No se ha podido realizar la operación")
    else:
        listaCampos = {salon_nombre_entry}
        if validarCampoNoVacio(listaCampos, 1):
            if objeto.insertarNuevoObjeto(Salon, "salon") == 0:
                Salon = objeto.obtenerObjeto("salon", "nombre", salon_nombre_entry.get())
                messagebox.showinfo(title="Operación exitosa", message= "Se ha agregado el registro con exito\nEl ID del nuevo salon es: " + str(Salon.get("id")))
                cancelarSalon() 
                salon_code_entry.configure(state="normal")
                salon_code_entry.delete(0, tk.END)
                salon_code_entry.insert(0, Salon.get("id"))
                buscarSalon()
            else:  
                messagebox.showerror(title="Error", message= "No se ha podido agregar el registro")

def nuevoSalon():
    cancelarSalon()
    editarSalon()

def bajaSalon():
    listaCampos = {salon_id_entry}
    if validarCampoNoVacio(listaCampos, 1):
        objeto = Conexion()
        popupWindow = tk.Toplevel(main)
        popupWindow.wm_title("¡Advertencia!")
        popupWindow.tkraise(main)
        tk.Label(popupWindow, text="¿Está seguro que desea eliminar el registro con ID = " + str(salon_id_entry.get()) + "?\nEsta operación no se puede deshacer").grid(columnspan=2, column=0, row=0, padx=15, pady=15)
        tk.Button(popupWindow, text="Cancelar", command=lambda:[popupWindow.destroy()]).grid(column=0, row=1, padx=10, pady=10)
        tk.Button(popupWindow, text="Eliminar", command=lambda:[messagebox.showinfo(title="Operación exitosa", message="Se ha eliminado el registro") if
                                                                objeto.eliminarObjeto("salon", str(salon_id_entry.get()), "id") == 0 else 
                                                                messagebox.showerror(title="Operación fallida", message="No se ha podido eliminar el registro"),
                                                                popupWindow.destroy(), cancelarSalon()]).grid(column=1, row=1, padx=10, pady=10)

#--------------------------------------------------------------------------------------------------------------

#===============================================================================================================

dormirPestanas("1111111111")
pestanas.select(pestana_maestros)

main.mainloop()
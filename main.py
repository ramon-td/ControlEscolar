import tkinter as tk
import os
import sys

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
# conexion.usuarioActivo(0)
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
maestro_carrera_optionMenu.configure(state="disabled")
maestro_materia_selection = tk.StringVar(main)
maestro_materia_options = conexion.obtenerColumna("materias", "nombre")
maestro_materia_optionMenu = tk.OptionMenu(pestana_maestros, maestro_materia_selection, *maestro_materia_options)
maestro_materia_optionMenu.configure(state="disabled")
maestro_grupo_selection = tk.StringVar(main)
maestro_grupo_options = conexion.obtenerColumna("grupos", "nombre")
maestro_grupo_optionMenu = tk.OptionMenu(pestana_maestros, maestro_grupo_selection, *maestro_grupo_options)
maestro_grupo_optionMenu.configure(state="disabled")

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
pestanas.tab(4, state="disabled")
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
materia_carrera_optionMenu.configure(state="disabled")

#- - - - - - - - - - - - - - - - - - - - - - - - - - Botones - - - - - - - - - - - - - - - - - - - - - - -
materia_buscar_btn = tk.Button(pestana_materias, text="Buscar", command=lambda:buscarMaterias())
materia_buscar_btn.configure(width=10)
materia_nuevo_btn = tk.Button(pestana_materias, text="Nuevo", command=lambda:nuevoMateria())
materia_nuevo_btn.configure(width=10)
materia_guardar_btn = tk.Button(pestana_materias, text="Guardar", command=lambda:guardarMateria())
materia_guardar_btn.configure(width=10, state="disabled")
materia_cancelar_btn = tk.Button(pestana_materias, text="Cancelar", command=lambda:cancelarMateria())
materia_cancelar_btn.configure(width=10, state="disabled")
materia_editar_btn = tk.Button(pestana_materias, text="Editar", command=lambda:editarMateria())
materia_editar_btn.configure(width=10, state="disabled")
materia_baja_btn = tk.Button(pestana_materias, text="Baja", command=lambda:bajaMateria())
materia_baja_btn.configure(width=10, state="disabled")
#- - - - - - - - - - - - - - - - - - - - - - - - - - Posiciones - - - - - - - - - - - - - - - - - - - - - - -

materia_code_label.grid(column=1, columnspan=1, row=0, padx=10, pady=10, sticky=tk.E)
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
materia_nuevo_btn.grid(column=1, columnspan=1, row=5, padx=10, pady=10, sticky=tk.E)
materia_guardar_btn.grid(column=2, columnspan=1, row=5, padx=10, pady=10, sticky=tk.E)
materia_cancelar_btn.grid(column=3, columnspan=1, row=5, padx=10, pady=10, sticky=tk.E)
materia_editar_btn.grid(column=4, columnspan=1, row=5, padx=10, pady=10, sticky=tk.E)
materia_baja_btn.grid(column=5, columnspan=1, row=5, padx=10, pady=10, sticky=tk.E)

#--------------------------------------------------------GRUPOS ----------------------------------------------------
pestana_grupos = ttk.Frame(pestanas)
pestanas.add(pestana_grupos, text="Grupos")
pestanas.tab(5, state="normal")
#- - - - - - - - - - - - - - - - - - - - - - - Entries y etiquetas - - - - - - - - - - - - - - - - - - - -
grupo_code_label = tk.Label(pestana_grupos, text="Ingrese código de grupo: ")
grupo_id_label = tk.Label(pestana_grupos, text="ID:")
grupo_nombre_label = tk.Label(pestana_grupos, text="Nombre de Grupo: ")
grupo_fecha_label = tk.Label(pestana_grupos, text="Fecha: ")
grupo_carrera_label = tk.Label(pestana_grupos, text="Carrera: ")
grupo_materia_label = tk.Label(pestana_grupos, text="Materia: ")
grupo_maestro_label = tk.Label(pestana_grupos, text="Maestro: ")
grupo_salon_label = tk.Label(pestana_grupos, text="Salon: ")
grupo_horario_label = tk.Label(pestana_grupos, text="Horario: ")
grupo_semestre_label = tk.Label(pestana_grupos, text="Semestre: ")
grupo_alumnos_label = tk.Label(pestana_grupos, text="Numero de\n alumnos: ")
grupo_code_entry  = tk.Entry(pestana_grupos, state="normal")
grupo_code_entry.configure(width=30, state="normal")
grupo_id_entry  = tk.Entry(pestana_grupos, state="disabled")
grupo_id_entry.configure(width=8, state="disabled")
grupo_nombre_entry  = tk.Entry(pestana_grupos, state="disabled")
grupo_nombre_entry.configure(width=30, state="disabled")
grupo_fecha_selection  = tk.StringVar(main)
grupo_fecha_options  = conexion.obtenerColumna("horario", "turno")
grupo_fecha_optionMenu  = tk.OptionMenu(pestana_grupos, grupo_fecha_selection, *grupo_fecha_options)
grupo_fecha_optionMenu.configure(width=30, state="disabled")
grupo_carrera_selection = tk.StringVar(main)
grupo_carrera_options = conexion.obtenerColumna("carrera", "nombre")
grupo_carrera_optionMenu  = tk.OptionMenu(pestana_grupos, grupo_carrera_selection, *grupo_carrera_options)
grupo_carrera_optionMenu.configure(width=22, state="disabled")
grupo_materia_selection = tk.StringVar(main)
grupo_materia_options = conexion.obtenerColumna("materias", "nombre")
grupo_materia_optionMenu  = tk.OptionMenu(pestana_grupos, grupo_materia_selection, *grupo_materia_options)
grupo_materia_optionMenu.configure(width=22, state="disabled")
grupo_maestro_selection = tk.StringVar(main)
grupo_maestro_options = conexion.obtenerColumna("maestros", "nombre")
grupo_maestro_optionMenu  = tk.OptionMenu(pestana_grupos, grupo_maestro_selection, *grupo_maestro_options)
grupo_maestro_optionMenu.configure(width=22, state="disabled")
grupo_salon_selection = tk.StringVar(main)
grupo_salon_options = conexion.obtenerColumna("salon", "nombre")
grupo_salon_optionMenu  = tk.OptionMenu(pestana_grupos, grupo_salon_selection, *grupo_salon_options)
grupo_salon_optionMenu.configure(width=15, state="disabled")
grupo_horario_selection = tk.StringVar(main)
grupo_horario_options = conexion.obtenerColumna("horario", "hora")
grupo_horario_optionMenu  = tk.OptionMenu(pestana_grupos, grupo_horario_selection, *grupo_horario_options)
grupo_horario_optionMenu.configure(width=15, state="disabled")
grupo_semestre_selection = tk.StringVar(main)
grupo_semestre_options = ("1ro", "2do", "3ro", "4to", "5to", "6to", "7mo") #Hay que hacerla dinámica
grupo_semestre_optionMenu  = tk.OptionMenu(pestana_grupos, grupo_semestre_selection, *grupo_semestre_options)
grupo_semestre_optionMenu.configure(width=15, state="disabled")
grupo_alumnos_entry  = tk.Entry(pestana_grupos, state="disabled", width=8)


#- - - - - - - - - - - - - - - - - - - - - - - - - - Botones - - - - - - - - - - - - - - - - - - - - - - -
grupo_buscar_btn = tk.Button(pestana_grupos, text="Buscar", command=lambda:buscarGrupo())
grupo_buscar_btn.configure(width=10)
grupo_nuevo_btn = tk.Button(pestana_grupos, text="Nuevo", command=lambda:nuevoGrupo())
grupo_nuevo_btn.configure(width=10)
grupo_guardar_btn = tk.Button(pestana_grupos, text="Guardar", command=lambda:guardarGrupo())
grupo_guardar_btn.configure(width=10, state="disabled")
grupo_cancelar_btn = tk.Button(pestana_grupos, text="Cancelar", command=lambda:cancelarGrupo())
grupo_cancelar_btn.configure(width=10, state="disabled")
grupo_editar_btn = tk.Button(pestana_grupos, text="Editar", command=lambda:editarGrupo())
grupo_editar_btn.configure(width=10, state="disabled")
grupo_baja_btn = tk.Button(pestana_grupos, text="Baja", command=lambda:bajaGrupo())
grupo_baja_btn.configure(width=10, state="disabled")
#- - - - - - - - - - - - - - - - - - - - - - - - - - Posiciones - - - - - - - - - - - - - - - - - - - - - - -
grupo_code_label.grid(column=2, columnspan=2, row=1, padx=10, pady=10, sticky=tk.E)
grupo_id_label.grid(column=1, columnspan=1, row=2, padx=10, pady=10, sticky=tk.E)
grupo_nombre_label.grid(column=1, columnspan=1, row=3, padx=10, pady=10, sticky=tk.E)
grupo_fecha_label.grid(column=1, columnspan=1, row=4, padx=10, pady=10, sticky=tk.E)
grupo_carrera_label.grid(column=1, columnspan=1, row=5, padx=10, pady=10, sticky=tk.E)
grupo_materia_label.grid(column=1, columnspan=1, row=6, padx=10, pady=10, sticky=tk.E)
grupo_maestro_label.grid(column=1, columnspan=1, row=7, padx=10, pady=10, sticky=tk.E)
grupo_salon_label.grid(column=4, columnspan=1, row=3, padx=10, pady=10, sticky=tk.E)
grupo_horario_label.grid(column=4, columnspan=1, row=4, padx=10, pady=10, sticky=tk.E)
grupo_semestre_label.grid(column=4, columnspan=1, row=5, padx=10, pady=10, sticky=tk.E)
grupo_alumnos_label.grid(column=4, columnspan=1, row=6, padx=10, pady=10, sticky=tk.E)
grupo_code_entry.grid(column=4, columnspan=2, row=1, padx=10, pady=10, sticky=tk.W)
grupo_id_entry.grid(column=2, columnspan=1, row=2, padx=10, pady=10, sticky=tk.W)
grupo_nombre_entry.grid(column=2, columnspan=2, row=3, padx=10, pady=10, sticky=tk.W)
grupo_fecha_optionMenu.grid(column=2, columnspan=2, row=4, padx=10, pady=10, sticky=tk.W)
grupo_carrera_optionMenu.grid(column=2, columnspan=2, row=5, padx=10, pady=10, sticky=tk.W)
grupo_materia_optionMenu.grid(column=2, columnspan=2, row=6, padx=10, pady=10, sticky=tk.W)
grupo_maestro_optionMenu.grid(column=2, columnspan=2, row=7, padx=10, pady=10, sticky=tk.W)
grupo_salon_optionMenu.grid(column=5, columnspan=2, row=3, padx=10, pady=10, sticky=tk.W)
grupo_horario_optionMenu.grid(column=5, columnspan=2, row=4, padx=10, pady=10, sticky=tk.W)
grupo_semestre_optionMenu.grid(column=5, columnspan=2, row=5, padx=10, pady=10, sticky=tk.W)
grupo_alumnos_entry.grid(column=5, columnspan=2, row=6, padx=10, pady=10, sticky=tk.W)

grupo_buscar_btn.grid(column=6, columnspan=1, row=1, padx=10, pady=10, sticky=tk.E)
grupo_nuevo_btn.grid(column=2, columnspan=1, row=8, padx=10, pady=10, sticky=tk.E)
grupo_guardar_btn.grid(column=3, columnspan=1, row=8, padx=10, pady=10, sticky=tk.W)
grupo_cancelar_btn.grid(column=4, columnspan=1, row=8, padx=10, pady=10, sticky=tk.W)
grupo_editar_btn.grid(column=5, columnspan=1, row=8, padx=10, pady=10, sticky=tk.E)
grupo_baja_btn.grid(column=6, columnspan=1, row=8, padx=10, pady=10, sticky=tk.E)

#--------------------------------------------------------HORARIO ---------------------------------------------------
pestana_horario = ttk.Frame(pestanas)
pestanas.add(pestana_horario, text="Horario")
pestanas.tab(6, state="disabled")
#- - - - - - - - - - - - - - - - - - - - - - - Entries y etiquetas - - - - - - - - - - - - - - - - - - - -
horario_code_label = tk.Label(pestana_horario, text="Ingrese codigo de horario: ")
horario_id_label = tk.Label(pestana_horario, text="ID:")
horario_turno_label = tk.Label(pestana_horario, text="Turno: ")
horario_hora_label = tk.Label(pestana_horario, text="Hora: ")
horario_code_entry = tk.Entry(pestana_horario)
horario_id_entry = tk.Entry(pestana_horario, state="disabled")
horario_turno_selection = tk.StringVar(main)
horario_turno_options = ("L - I", "M - J", "V", "S")
horario_turno_optionMenu = tk.OptionMenu(pestana_horario, horario_turno_selection, *horario_turno_options)
horario_turno_optionMenu.configure(state="disabled")
horario_hora_selection = tk.StringVar(main)
horario_hora_options = ("7:00:00", "9:00:00", "11:00:00", "13:00:00", "15:00:00", "17:00:00", "19:00:00", "21:00:00")
horario_hora_optionMenu = tk.OptionMenu(pestana_horario, horario_hora_selection, *horario_hora_options)
horario_hora_optionMenu.configure(state="disabled")

#- - - - - - - - - - - - - - - - - - - - - - - - - - Botones - - - - - - - - - - - - - - - - - - - - - - -
horario_buscar_btn = tk.Button(pestana_horario, text="Buscar", command=lambda:buscarHorario())
horario_buscar_btn.configure(width=10)
horario_nuevo_btn = tk.Button(pestana_horario, text="Nuevo", command=lambda:nuevoHorario())
horario_nuevo_btn.configure(width=10)
horario_guardar_btn = tk.Button(pestana_horario, text="Guardar", command=lambda:guardarHorario())
horario_guardar_btn.configure(width=10, state="disabled")
horario_cancelar_btn = tk.Button(pestana_horario, text="Cancelar", command=lambda:cancelarHorario())
horario_cancelar_btn.configure(width=10, state="disabled")
horario_editar_btn = tk.Button(pestana_horario, text="Editar", command=lambda:editarHorario())
horario_editar_btn.configure(width=10, state="disabled")
horario_baja_btn = tk.Button(pestana_horario, text="Baja", command=lambda:bajaHorario())
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
pestanas.tab(7, state="disabled")
#- - - - - - - - - - - - - - - - - - - - - - - Entries y etiquetas - - - - - - - - - - - - - - - - - - - -
salon_code_label = tk.Label(pestana_salon, text="Ingrese codigo de salón: ")
salon_id_label = tk.Label(pestana_salon, text="ID:")
salon_nombre_label = tk.Label(pestana_salon, text="Nombre Salon: ")
salon_edificio_label = tk.Label(pestana_salon, text="Edificio: ")
salon_aula_label = tk.Label(pestana_salon, text="Aula: ")
salon_code_entry = tk.Entry(pestana_salon)
salon_nombre_entry = tk.Entry(pestana_salon, state="disabled")
salon_id_entry = tk.Entry(pestana_salon, state="disabled")

salon_edificio_selection = tk.StringVar(main)
salon_edificio_options = ("Edificio 1", "Edificio 2", "Edificio 3", "Edificio Alpha", "Edificio Beta", "Edificio X")
salon_edificio_optionMenu = tk.OptionMenu(pestana_salon, salon_edificio_selection, *salon_edificio_options)
salon_edificio_optionMenu.configure(state="disabled")

salon_aula_selection = tk.StringVar(main)
salon_aula_options = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
salon_aula_optionMenu = tk.OptionMenu(pestana_salon, salon_aula_selection, *salon_aula_options)
salon_aula_optionMenu.configure(state="disabled")

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
salon_edificio_optionMenu.grid(column=2, columnspan=2, row=3, padx=10, pady=10, sticky=tk.W)
salon_edificio_optionMenu.configure(width=20)

salon_aula_label.grid(column=1, columnspan=1, row=4, padx=10, pady=10, sticky=tk.E)
salon_aula_optionMenu.grid(column=2, columnspan=1, row=4, padx=10, pady=10, sticky=tk.W)
salon_aula_optionMenu.configure(width=8)


salon_buscar_btn.grid(column=5, columnspan=1, row=0, padx=10, pady=10, sticky=tk.E)
salon_nuevo_btn.grid(column=1, columnspan=1, row=6, padx=10, pady=10, sticky=tk.E)
salon_guardar_btn.grid(column=2, columnspan=1, row=6, padx=10, pady=10, sticky=tk.E)
salon_cancelar_btn.grid(column=3, columnspan=1, row=6, padx=10, pady=10, sticky=tk.E)
salon_editar_btn.grid(column=4, columnspan=1, row=6, padx=10, pady=10, sticky=tk.E)
salon_baja_btn.grid(column=5, columnspan=1, row=6, padx=10, pady=10, sticky=tk.E)

#--------------------------------------------------------CARRERA ---------------------------------------------------
pestana_carrera = ttk.Frame(pestanas)
pestanas.add(pestana_carrera, text="Carrera")
pestanas.tab(8, state="disabled")
#- - - - - - - - - - - - - - - - - - - - - - - Entries y etiquetas - - - - - - - - - - - - - - - - - - - -
carrera_code_label = tk.Label(pestana_carrera, text="Ingrese codigo de carrera: ")
carrera_id_label = tk.Label(pestana_carrera, text="ID:")
carrera_nombre_label = tk.Label(pestana_carrera, text="Nombre de Carrera: ")
carrera_semestres_label = tk.Label(pestana_carrera, text="Numero de Semestres: ")
carrera_materia_label = tk.Label(pestana_carrera, text="Materia: ")
carrera_code_entry = tk.Entry(pestana_carrera)
carrera_nombre_entry = tk.Entry(pestana_carrera, state="disabled")
carrera_semestres_entry = tk.Entry(pestana_carrera, state="disabled")
carrera_id_entry = tk.Entry(pestana_carrera, state="disabled")

carrera_materia_selection = tk.StringVar(main)
carrera_materia_options = conexion.obtenerColumna("materias", "nombre")
carrera_materia_optionMenu = tk.OptionMenu(pestana_carrera, carrera_materia_selection, *carrera_materia_options)
carrera_materia_optionMenu.configure(state="disabled")

#- - - - - - - - - - - - - - - - - - - - - - - - - - Botones - - - - - - - - - - - - - - - - - - - - - - -

carrera_buscar_btn = tk.Button(pestana_carrera, text="Buscar", command=lambda:buscarCarrera())
carrera_buscar_btn.configure(width=10)
carrera_nuevo_btn = tk.Button(pestana_carrera, text="Nuevo", command=lambda:nuevoCarrera())
carrera_nuevo_btn.configure(width=10)
carrera_guardar_btn = tk.Button(pestana_carrera, text="Guardar", command=lambda:guardarCarrera())
carrera_guardar_btn.configure(width=10, state="disabled")
carrera_cancelar_btn = tk.Button(pestana_carrera, text="Cancelar", command=lambda:cancelarCarrera())
carrera_cancelar_btn.configure(width=10, state="disabled")
carrera_editar_btn = tk.Button(pestana_carrera, text="Editar", command=lambda:editarCarrera())
carrera_editar_btn.configure(width=10, state="disabled")
carrera_baja_btn = tk.Button(pestana_carrera, text="Baja", command=lambda:bajaCarrera())
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
pestanas.tab(9, state="disabled")
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
void_label_materias1.configure(width=15, height=2)
void_label_usuarios2.configure(width=15, height=2)
# void_label_grupos = tk.Label(pestana_grupos, text="")
# void_label_grupos.grid(column=0, row=8, sticky=tk.NSEW)
# void_label_grupos.configure(width=6, height=2)
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
pestana_grupos.columnconfigure(7, weight=1)
pestana_grupos.rowconfigure(8, weight=1)
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
    log_in = Conexion()
    listaCampos = {username_entry, password_entry}
    Objeto = log_in.obtenerObjeto("usuarios", "usuario", username_entry.get())
    if validarCampoNoVacio(listaCampos, 1):
        if username_entry.get() == Objeto.get("usuario"):
            if password_entry.get() == Objeto.get("password"):
                log_in.usuarioActivo(Objeto.get("idusuario"))
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
    user_perfil_selection.set("")
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
        conexion = Conexion()
        Alumno = conexion.obtenerObjeto("alumnos", "id", alumno_code_entry.get())
        if Alumno:
            if not (str(conexion.obtenerColumnaEspecifica("usuarios", "perfil", "estatus", "1")) == "(\'Alumno\',)"):
                alumno_editar_btn.configure(state="normal")
                alumno_baja_btn.configure(state="normal")
            alumno_cancelar_btn.configure(state="normal")
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
    alumno_estado_selection.set("")
    alumno_carrera_selection.set("")
    alumno_grupo_selection.set("")
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
    maestro_carrera_selection.set("")
    maestro_materia_selection.set("")
    maestro_grupo_selection.set("")
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

#----------------------------------------------------Materias--------------------------------------------------
def buscarMaterias():
    listaCampos = {materia_code_entry}
    if validarCampoNoVacio(listaCampos, 0):
        Materia = Conexion()
        Materia = Materia.obtenerObjeto("materias", "id", materia_code_entry.get())
        if Materia:            
            materia_editar_btn.configure(state="normal")
            materia_cancelar_btn.configure(state="normal")
            materia_baja_btn.configure(state="normal")
            listaCampos = (materia_id_entry,
                           materia_asignatura_entry,
                           materia_creditos_entry,
                           materia_semestre_entry)
            listaDatos = ("id", "nombre", "creditos", "semestre")
            llenarCampos(listaCampos, listaDatos, Materia)
            materia_carrera_selection.set(Materia.get("carrera_id"))

            return 0
        else:
            messagebox.showerror(title="No se encuentra", message= "No se encontró el código")
    else: 
        objetos = []
        mensaje = "Lista de Materias: \n"
        conexion = Conexion()
        ids = conexion.obtenerColumna("materias", "id")
        for idindex in range(0, len(ids)):
            objetos.append(conexion.obtenerObjeto("materias", "id", ids[idindex]))
            mensaje += "\nID: " + str(objetos[idindex].get("id")) + "  \t|  Materia: " + str(objetos[idindex].get("nombre")) + "\n"
        messagebox.showinfo(title="Búsqueda general", message=mensaje)
        listaCampos = ( materia_id_entry,
                        materia_asignatura_entry,
                        materia_creditos_entry,
                        materia_semestre_entry)
        bloquearCampos(False, listaCampos)
        limpiarCampos(listaCampos)
        bloquearCampos(True, listaCampos)

def editarMateria():
    listaCampos = { materia_asignatura_entry,
                    materia_creditos_entry,
                    materia_semestre_entry}
    listaCamposBloquear = {materia_editar_btn,
                           materia_nuevo_btn,
                           materia_baja_btn,
                           materia_buscar_btn,
                           materia_code_entry}
    listaOtros = {materia_carrera_optionMenu,
                  materia_cancelar_btn,
                  materia_guardar_btn}
    bloquearCampos(False, listaCampos)
    bloquearCampos(False, listaOtros)

    bloquearCampos(True, listaCamposBloquear)

def cancelarMateria():
    listaCampos = {materia_code_entry, 
                    materia_asignatura_entry,
                    materia_creditos_entry,
                    materia_semestre_entry}
    listaCamposBloquear = {materia_nuevo_btn,
                           materia_buscar_btn,
                           materia_code_entry}
    listaOtros = {materia_baja_btn,
                  materia_editar_btn,
                  materia_carrera_optionMenu,
                  materia_cancelar_btn,
                  materia_guardar_btn}
    materia_carrera_selection.set("")
    bloquearCampos(False, listaCampos)
    limpiarCampos(listaCampos)
    bloquearCampos(True, listaCampos)
    bloquearCampos(True, listaOtros)
    bloquearCampos(False, listaCamposBloquear)

def guardarMateria():
    Materia = {"nombre" : materia_asignatura_entry.get(),
                "creditos" : materia_creditos_entry.get(),
                "semestre" : materia_semestre_entry.get(),
                "carrera_id" : materia_carrera_selection.get()}
    objeto = Conexion()
    listaCampos = {materia_id_entry}
    if validarCampoNoVacio(listaCampos, 0):
        messagebox.showinfo(title="Operación exitosa", message= "Se ha editado el registro con exito"), cancelarMateria() if objeto.actualizarObjeto(Materia, "materias", "id", materia_id_entry.get()) == 0 else  messagebox.showerror(title="Error", message= "No se ha podido realizar la operación")
    else:
        listaCampos = {materia_asignatura_entry, materia_creditos_entry, materia_semestre_entry}
        if validarCampoNoVacio(listaCampos, 1):
            if objeto.insertarNuevoObjeto(Materia, "materias") == 0:
                Materia = objeto.obtenerObjeto("materias", "nombre", materia_asignatura_entry.get())
                messagebox.showinfo(title="Operación exitosa", message= "Se ha agregado el registro con exito\nEl ID de la nueva Materia es: " + str(Materia.get("id")))
                cancelarMateria() 
                materia_code_entry.configure(state="normal")
                materia_code_entry.delete(0, tk.END)
                materia_code_entry.insert(0, Materia.get("id"))
                buscarMaterias()
            else:  
                messagebox.showerror(title="Error", message= "No se ha podido agregar el registro")

def nuevoMateria():
    cancelarMateria()
    editarMateria()

def bajaMateria():
    listaCampos = {materia_id_entry}
    if validarCampoNoVacio(listaCampos, 1):
        objeto = Conexion()
        popupWindow = tk.Toplevel(main)
        popupWindow.wm_title("¡Advertencia!")
        popupWindow.tkraise(main)
        tk.Label(popupWindow, text="¿Está seguro que desea eliminar el registro con ID = " + str(materia_id_entry.get()) + "?\nEsta operación no se puede deshacer").grid(columnspan=2, column=0, row=0, padx=15, pady=15)
        tk.Button(popupWindow, text="Cancelar", command=lambda:[popupWindow.destroy()]).grid(column=0, row=1, padx=10, pady=10)
        tk.Button(popupWindow, text="Eliminar", command=lambda:[messagebox.showinfo(title="Operación exitosa", message="Se ha eliminado el registro") if
                                                                objeto.eliminarObjeto("materias", str(materia_id_entry.get()), "id") == 0 else 
                                                                messagebox.showerror(title="Operación fallida", message="No se ha podido eliminar el registro"),
                                                                popupWindow.destroy(), cancelarMateria()]).grid(column=1, row=1, padx=10, pady=10)

#--------------------------------------------------------------------------------------------------------------

#----------------------------------------------------Horario--------------------------------------------------
def buscarHorario():
    listaCampos = {horario_code_entry}
    if validarCampoNoVacio(listaCampos, 0):
        Horario = Conexion()
        Horario = Horario.obtenerObjeto("horario", "id", horario_code_entry.get())
        if Horario:            
            horario_editar_btn.configure(state="normal")
            horario_cancelar_btn.configure(state="normal")
            horario_baja_btn.configure(state="normal")
            listaCampos = (horario_id_entry, horario_id_entry)
            listaDatos = ("id", "id")
            llenarCampos(listaCampos, listaDatos, Horario)
            horario_turno_selection.set(Horario.get("turno"))
            horario_hora_selection.set(Horario.get("hora"))
            return 0
        else:
            messagebox.showerror(title="No se encuentra", message= "No se encontró el código")
    else: 
        objetos = []
        mensaje = "Lista de Horarios: \n"
        conexion = Conexion()
        ids = conexion.obtenerColumna("horario", "id")
        for idindex in range(0, len(ids)):
            objetos.append(conexion.obtenerObjeto("horario", "id", ids[idindex]))
            mensaje += "\nID: " + str(objetos[idindex].get("id")) + "  \t|  Horario: " + str(objetos[idindex].get("hora")) + "\n"
        messagebox.showinfo(title="Búsqueda general", message=mensaje)
        listaCampos = (horario_id_entry, horario_id_entry)
        bloquearCampos(False, listaCampos)
        limpiarCampos(listaCampos)
        bloquearCampos(True, listaCampos)

def editarHorario():
    listaCamposBloquear = {horario_editar_btn,
                           horario_nuevo_btn,
                           horario_baja_btn,
                           horario_buscar_btn,
                           horario_code_entry}
    listaOtros = {horario_turno_optionMenu,
                  horario_hora_optionMenu,
                  horario_cancelar_btn,
                  horario_guardar_btn}
    bloquearCampos(False, listaOtros)
    bloquearCampos(True, listaCamposBloquear)

def cancelarHorario():
    listaCampos = {horario_code_entry, horario_id_entry}
    listaCamposBloquear = {horario_nuevo_btn,
                           horario_buscar_btn,
                           horario_code_entry}
    listaOtros = {horario_baja_btn,
                  horario_editar_btn,
                  horario_turno_optionMenu,
                  horario_hora_optionMenu,
                  horario_cancelar_btn,
                  horario_guardar_btn}
    horario_turno_selection.set("")
    horario_hora_selection.set("")
    bloquearCampos(False, listaCampos)
    limpiarCampos(listaCampos)
    bloquearCampos(True, listaCampos)
    bloquearCampos(True, listaOtros)
    bloquearCampos(False, listaCamposBloquear)

def guardarHorario():
    Horario = {"turno" : horario_turno_selection.get(),
                "hora" : horario_hora_selection.get()}
    objeto = Conexion()
    listaCampos = {horario_id_entry}
    if validarCampoNoVacio(listaCampos, 0):
        messagebox.showinfo(title="Operación exitosa", message= "Se ha editado el registro con exito"), cancelarHorario() if objeto.actualizarObjeto(Horario, "horario", "id", horario_id_entry.get()) == 0 else  messagebox.showerror(title="Error", message= "No se ha podido realizar la operación")
    else:
        listaCampos = (horario_turno_selection, horario_hora_selection)
        if validarCampoNoVacio(listaCampos, 1):
            if objeto.insertarNuevoObjeto(Horario, "horario") == 0:
                Horario = objeto.obtenerObjeto("horario", "hora", horario_hora_selection.get())
                messagebox.showinfo(title="Operación exitosa", message= "Se ha agregado el registro con exito\nEl ID de la nueva Horario es: " + str(Horario.get("id")))
                cancelarHorario() 
                horario_code_entry.configure(state="normal")
                horario_code_entry.delete(0, tk.END)
                horario_code_entry.insert(0, Horario.get("id"))
                buscarHorario()
            else:  
                messagebox.showerror(title="Error", message= "No se ha podido agregar el registro")

def nuevoHorario():
    cancelarHorario()
    editarHorario()

def bajaHorario():
    listaCampos = {horario_id_entry, horario_id_entry}
    if validarCampoNoVacio(listaCampos, 1):
        objeto = Conexion()
        popupWindow = tk.Toplevel(main)
        popupWindow.wm_title("¡Advertencia!")
        popupWindow.tkraise(main)
        tk.Label(popupWindow, text="¿Está seguro que desea eliminar el registro con ID = " + str(horario_id_entry.get()) + "?\nEsta operación no se puede deshacer").grid(columnspan=2, column=0, row=0, padx=15, pady=15)
        tk.Button(popupWindow, text="Cancelar", command=lambda:[popupWindow.destroy()]).grid(column=0, row=1, padx=10, pady=10)
        tk.Button(popupWindow, text="Eliminar", command=lambda:[messagebox.showinfo(title="Operación exitosa", message="Se ha eliminado el registro") if
                                                                objeto.eliminarObjeto("horario", str(horario_id_entry.get()), "id") == 0 else 
                                                                messagebox.showerror(title="Operación fallida", message="No se ha podido eliminar el registro"),
                                                                popupWindow.destroy(), cancelarHorario()]).grid(column=1, row=1, padx=10, pady=10)

#--------------------------------------------------------------------------------------------------------------

#------------------------------------------------------Carrera---------------------------------------------------
def buscarCarrera():
    listaCampos = {carrera_code_entry}
    if validarCampoNoVacio(listaCampos, 0):
        Carrera = Conexion()
        Carrera = Carrera.obtenerObjeto("carrera", "id", carrera_code_entry.get())
        if Carrera:            
            carrera_editar_btn.configure(state="normal")
            carrera_cancelar_btn.configure(state="normal")
            carrera_baja_btn.configure(state="normal")
            listaCampos = ( carrera_id_entry,
                            carrera_nombre_entry,
                            carrera_semestres_entry)
            listaDatos = ("id", "nombre", "semestres")
            llenarCampos(listaCampos, listaDatos, Carrera)
            carrera_materia_optionMenu.configure(state="normal")
            carrera_materia_selection.set(Carrera.get("materias"))
            carrera_materia_optionMenu.configure(state="disabled")
            return 0
        else:
            messagebox.showerror(title="No se encuentra", message= "No se encontró el código")
    else: 
        objetos = []
        mensaje = "Lista de Carreras: \n"
        conexion = Conexion()
        ids = conexion.obtenerColumna("carrera", "id")
        for idindex in range(0, len(ids)):
            objetos.append(conexion.obtenerObjeto("carrera", "id", ids[idindex]))
            mensaje += "\nID: " + str(objetos[idindex].get("id")) + "  \t|  Carrera: " + str(objetos[idindex].get("nombre")) + "\n"
        messagebox.showinfo(title="Búsqueda general", message=mensaje)
        listaCampos = ( carrera_id_entry,
                        carrera_nombre_entry,
                        carrera_semestres_entry)
        bloquearCampos(False, listaCampos)
        limpiarCampos(listaCampos)
        bloquearCampos(True, listaCampos)

def editarCarrera():
    listaCampos = { carrera_nombre_entry,
                    carrera_semestres_entry}
    listaCamposBloquear = {carrera_editar_btn,
                           carrera_nuevo_btn,
                           carrera_baja_btn,
                           carrera_buscar_btn,
                           carrera_code_entry}
    listaOtros = {carrera_editar_btn,
                  carrera_cancelar_btn,
                  carrera_guardar_btn,
                  carrera_materia_optionMenu}
    bloquearCampos(False, listaCampos)
    bloquearCampos(False, listaOtros)
    bloquearCampos(True, listaCamposBloquear)

def cancelarCarrera():
    listaCampos = {carrera_code_entry, 
                    carrera_id_entry,
                    carrera_nombre_entry,
                    carrera_semestres_entry}
    listaCamposBloquear = {carrera_nuevo_btn,
                           carrera_buscar_btn,
                           carrera_code_entry}
    listaOtros = {carrera_baja_btn,
                  carrera_editar_btn,
                  carrera_cancelar_btn,
                  carrera_guardar_btn,
                  carrera_materia_optionMenu}
    carrera_materia_selection.set("")
    bloquearCampos(False, listaCampos)
    limpiarCampos(listaCampos)
    bloquearCampos(True, listaCampos)
    bloquearCampos(True, listaOtros)
    bloquearCampos(False, listaCamposBloquear)

def guardarCarrera():
    Carrera = {"nombre" : carrera_nombre_entry.get(),
               "semestres" : carrera_semestres_entry.get(),
                "materias" : carrera_materia_selection.get()}
    objeto = Conexion()
    listaCampos = {carrera_id_entry}
    if validarCampoNoVacio(listaCampos, 0):
        messagebox.showinfo(title="Operación exitosa", message= "Se ha editado el registro con exito"), cancelarCarrera() if objeto.actualizarObjeto(Carrera, "carrera", "id", int(carrera_id_entry.get())) == 0 else  messagebox.showerror(title="Error", message= "No se ha podido realizar la operación")
    else:
        listaCampos = {carrera_nombre_entry}
        if validarCampoNoVacio(listaCampos, 1):
            if objeto.insertarNuevoObjeto(Carrera, "carrera") == 0:
                Carrera = objeto.obtenerObjeto("carrera", "nombre", carrera_nombre_entry.get())
                messagebox.showinfo(title="Operación exitosa", message= "Se ha agregado el registro con exito\nEl ID del nuevo Carrera es: " + str(Carrera.get("id")))
                cancelarCarrera() 
                carrera_code_entry.configure(state="normal")
                carrera_code_entry.delete(0, tk.END)
                carrera_code_entry.insert(0, Carrera.get("id"))
                buscarCarrera()
            else:  
                messagebox.showerror(title="Error", message= "No se ha podido agregar el registro")

def nuevoCarrera():
    cancelarCarrera()
    editarCarrera()

def bajaCarrera():
    listaCampos = {carrera_id_entry}
    if validarCampoNoVacio(listaCampos, 1):
        objeto = Conexion()
        popupWindow = tk.Toplevel(main)
        popupWindow.wm_title("¡Advertencia!")
        popupWindow.tkraise(main)
        tk.Label(popupWindow, text="¿Está seguro que desea eliminar el registro con ID = " + str(carrera_id_entry.get()) + "?\nEsta operación no se puede deshacer").grid(columnspan=2, column=0, row=0, padx=15, pady=15)
        tk.Button(popupWindow, text="Cancelar", command=lambda:[popupWindow.destroy()]).grid(column=0, row=1, padx=10, pady=10)
        tk.Button(popupWindow, text="Eliminar", command=lambda:[messagebox.showinfo(title="Operación exitosa", message="Se ha eliminado el registro") if
                                                                objeto.eliminarObjeto("carrera", str(carrera_id_entry.get()), "id") == 0 else 
                                                                messagebox.showerror(title="Operación fallida", message="No se ha podido eliminar el registro"),
                                                                popupWindow.destroy(), cancelarCarrera()]).grid(column=1, row=1, padx=10, pady=10)

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
            salon_aula_optionMenu.configure(state="normal")
            salon_edificio_selection.set(Salon.get("edificio"))
            salon_aula_selection.set(Salon.get("aula"))
            salon_edificio_optionMenu.configure(state="disabled")
            salon_aula_optionMenu.configure(state="disabled")
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
                  salon_edificio_optionMenu,
                  salon_aula_optionMenu}
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
                  salon_edificio_optionMenu,
                  salon_aula_optionMenu}
    salon_edificio_selection.set("")
    salon_aula_selection.set("")
    bloquearCampos(False, listaCampos)
    limpiarCampos(listaCampos)
    bloquearCampos(True, listaCampos)
    bloquearCampos(True, listaOtros)
    bloquearCampos(False, listaCamposBloquear)

def guardarSalon():
    Salon = {"nombre" : salon_nombre_entry.get(),
             "edificio" : salon_edificio_selection.get(),
             "aula" : salon_aula_selection.get()}
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

#------------------------------------------------------Grupos---------------------------------------------------
def validarGrupo(objeto):
    conexion = Conexion()
    ids = conexion.obtenerColumna("grupos", "id")
    horarios = conexion.obtenerColumna("grupos", "horario")
    fechas = conexion.obtenerColumna("grupos", "fecha")
    for idgrupo, hora, fecha in zip(ids, horarios, fechas):
        if objeto.get("horario") == hora:
            if objeto.get("fecha") == fecha:
                if (objeto.get("maestro") == str(conexion.obtenerColumnaEspecifica("grupos", "maestro", "id", idgrupo))[2:-3]):
                    messagebox.showerror(title="Operación fallida", message="No puede agregar dos grupos al mismo tiempo con el mismo profesor")
                    return False
                elif (objeto.get("salon") == str(conexion.obtenerColumnaEspecifica("grupos", "salon", "id", idgrupo))[2:-3]):
                    messagebox.showerror(title="Operación fallida", message="No puede agregar dos grupos al mismo tiempo en el mismo salon")
                    return False
                else:
                    return True
    return True

def buscarGrupo():
    listaCampos = {grupo_code_entry}
    if validarCampoNoVacio(listaCampos, 0):
        Grupo = Conexion()
        Grupo = Grupo.obtenerObjeto("grupos", "id", grupo_code_entry.get())
        if Grupo:            
            grupo_editar_btn.configure(state="normal")
            grupo_cancelar_btn.configure(state="normal")
            grupo_baja_btn.configure(state="normal")
            listaCampos = ( grupo_id_entry,
                            grupo_nombre_entry,
                            grupo_alumnos_entry)
            listaDatos = ("id", "nombre", "maxalumnos")
            llenarCampos(listaCampos, listaDatos, Grupo)
            grupo_carrera_optionMenu.configure(state="normal")
            grupo_materia_optionMenu.configure(state="normal")
            grupo_maestro_optionMenu.configure(state="normal")
            grupo_salon_optionMenu.configure(state="normal")
            grupo_horario_optionMenu.configure(state="normal")
            grupo_semestre_optionMenu.configure(state="normal")
            grupo_fecha_optionMenu.configure(state="normal")
            grupo_carrera_selection.set(Grupo.get("carrera"))
            grupo_materia_selection.set(Grupo.get("materia"))
            grupo_maestro_selection.set(Grupo.get("maestro"))
            grupo_salon_selection.set(Grupo.get("salon"))
            grupo_horario_selection.set(Grupo.get("horario"))
            grupo_semestre_selection.set(Grupo.get("semestre"))
            grupo_fecha_selection.set(Grupo.get("fecha"))
            grupo_carrera_optionMenu.configure(state="disabled")
            grupo_materia_optionMenu.configure(state="disabled")
            grupo_maestro_optionMenu.configure(state="disabled")
            grupo_salon_optionMenu.configure(state="disabled")
            grupo_horario_optionMenu.configure(state="disabled")
            grupo_semestre_optionMenu.configure(state="disabled")
            grupo_fecha_optionMenu.configure(state="disabled")
            return 0
        else:
            messagebox.showerror(title="No se encuentra", message= "No se encontró el código")
    else: 
        objetos = []
        mensaje = "Lista de Grupo: \n"
        conexion = Conexion()
        ids = conexion.obtenerColumna("grupos", "id")
        for idindex in range(0, len(ids)):
            objetos.append(conexion.obtenerObjeto("grupos", "id", ids[idindex]))
            mensaje += "\nID: " + str(objetos[idindex].get("id")) + "  \t|  Grupo: " + str(objetos[idindex].get("nombre")) + "\n"
        messagebox.showinfo(title="Búsqueda general", message=mensaje)
        listaCampos = ( grupo_id_entry,
                        grupo_nombre_entry)
        bloquearCampos(False, listaCampos)
        limpiarCampos(listaCampos)
        bloquearCampos(True, listaCampos)

def editarGrupo():
    listaCampos = { grupo_nombre_entry,
                    grupo_alumnos_entry}
    listaCamposBloquear = {grupo_editar_btn,
                           grupo_nuevo_btn,
                           grupo_baja_btn,
                           grupo_buscar_btn,
                           grupo_code_entry}
    listaOtros = {grupo_editar_btn,
                  grupo_cancelar_btn,
                  grupo_guardar_btn,
                  grupo_carrera_optionMenu,
                  grupo_materia_optionMenu,
                  grupo_maestro_optionMenu,
                  grupo_salon_optionMenu,
                  grupo_horario_optionMenu,
                  grupo_semestre_optionMenu,
                  grupo_fecha_optionMenu}
    bloquearCampos(False, listaCampos)
    bloquearCampos(False, listaOtros)
    bloquearCampos(True, listaCamposBloquear)

def cancelarGrupo():
    listaCampos = {grupo_code_entry, 
                    grupo_id_entry,
                    grupo_nombre_entry,
                    grupo_alumnos_entry}
    listaCamposBloquear = {grupo_nuevo_btn,
                           grupo_buscar_btn,
                           grupo_code_entry}
    listaOtros = {grupo_baja_btn,
                  grupo_editar_btn,
                  grupo_cancelar_btn,
                  grupo_guardar_btn,
                  grupo_carrera_optionMenu,
                  grupo_materia_optionMenu,
                  grupo_maestro_optionMenu,
                  grupo_salon_optionMenu,
                  grupo_horario_optionMenu,
                  grupo_fecha_optionMenu,
                  grupo_semestre_optionMenu}
    grupo_carrera_selection.set("")
    grupo_materia_selection.set("")
    grupo_maestro_selection.set("")
    grupo_salon_selection.set("")
    grupo_horario_selection.set("")
    grupo_semestre_selection.set("")
    grupo_fecha_selection.set("")
    bloquearCampos(False, listaCampos)
    limpiarCampos(listaCampos)
    bloquearCampos(True, listaCampos)
    bloquearCampos(True, listaOtros)
    bloquearCampos(False, listaCamposBloquear)

def guardarGrupo():
    Grupo = {"nombre"       : grupo_nombre_entry.get(),
             "fecha"        : grupo_fecha_selection.get(),
             "carrera"      : grupo_carrera_selection.get(),
             "materia"      : grupo_materia_selection.get(),
             "maestro"      : grupo_maestro_selection.get(),
             "salon"        : grupo_salon_selection.get(),
             "horario"      : grupo_horario_selection.get(),
             "semestre"     : grupo_semestre_selection.get(),
             "maxalumnos"   : grupo_alumnos_entry.get()}
    objeto = Conexion()
    listaCampos = {grupo_id_entry}
    if validarCampoNoVacio(listaCampos, 0):
        listaCampos = (grupo_nombre_entry, grupo_fecha_selection, grupo_carrera_selection, grupo_materia_selection, grupo_maestro_selection, grupo_salon_selection, grupo_horario_selection, grupo_semestre_selection, grupo_alumnos_entry)
        if validarCampoNoVacio(listaCampos, 1):
            objeto.eliminarObjeto("grupos", str(grupo_id_entry.get()), "id")
            if validarGrupo(Grupo):
                Grupo["id"] = grupo_id_entry.get()
                messagebox.showinfo(title="Operación exitosa", message= "Se ha editado el registro con exito"), cancelarGrupo() if objeto.insertarNuevoObjeto(Grupo, "grupos") == 0 else  messagebox.showerror(title="Error", message= "No se ha podido realizar la operación")
    else:
        listaCampos = (grupo_nombre_entry, grupo_fecha_selection, grupo_carrera_selection, grupo_materia_selection, grupo_maestro_selection, grupo_salon_selection, grupo_horario_selection, grupo_semestre_selection, grupo_alumnos_entry)
        if validarCampoNoVacio(listaCampos, 1):
            if validarGrupo(Grupo):
                if objeto.insertarNuevoObjeto(Grupo, "grupos") == 0:
                    Grupo = objeto.obtenerObjeto("grupos", "nombre", grupo_nombre_entry.get())
                    messagebox.showinfo(title="Operación exitosa", message= "Se ha agregado el registro con exito\nEl ID del nuevo Grupo es: " + str(Grupo.get("id")))
                    cancelarGrupo() 
                    grupo_code_entry.configure(state="normal")
                    grupo_code_entry.delete(0, tk.END)
                    grupo_code_entry.insert(0, Grupo.get("id"))
                    buscarGrupo()
                else:  
                    messagebox.showerror(title="Error", message= "No se ha podido agregar el registro")

def nuevoGrupo():
    cancelarGrupo()
    editarGrupo()

def bajaGrupo():
    listaCampos = {grupo_id_entry}
    if validarCampoNoVacio(listaCampos, 1):
        objeto = Conexion()
        popupWindow = tk.Toplevel(main)
        popupWindow.wm_title("¡Advertencia!")
        popupWindow.tkraise(main)
        tk.Label(popupWindow, text="¿Está seguro que desea eliminar el registro con ID = " + str(grupo_id_entry.get()) + "?\nEsta operación no se puede deshacer").grid(columnspan=2, column=0, row=0, padx=15, pady=15)
        tk.Button(popupWindow, text="Cancelar", command=lambda:[popupWindow.destroy()]).grid(column=0, row=1, padx=10, pady=10)
        tk.Button(popupWindow, text="Eliminar", command=lambda:[messagebox.showinfo(title="Operación exitosa", message="Se ha eliminado el registro") if
                                                                objeto.eliminarObjeto("grupos", str(grupo_id_entry.get()), "id") == 0 else 
                                                                messagebox.showerror(title="Operación fallida", message="No se ha podido eliminar el registro"),
                                                                popupWindow.destroy(), cancelarGrupo()]).grid(column=1, row=1, padx=10, pady=10)

#--------------------------------------------------------------------------------------------------------------
#---------------------------------------------------Planeación-------------------------------------------------
def llenarPlaneacion():
    conexion = Conexion()
    listaDiccionarios = [{}]
    listaDiccionarios = conexion.obtenerTablaCompleta("grupos")
    columna = 0
    fila = 0
    texto = ""
    pestana_planeacion.columnconfigure(6, weight=1)
    pestana_planeacion.rowconfigure(3, weight=2)
    for registro in listaDiccionarios:
        # print(registro.values())
        texto = "Grupo:\t" + registro.get("nombre")
        texto += "\nSalon:\t" + registro.get("salon")
        texto += "\nMateria:\t" + registro.get("materia")
        texto += "\nMaestro:\t" + registro.get("maestro")
        texto += "\nDías:\t" + registro.get("fecha")
        texto += "\nHorario:\t" + registro.get("horario")
        if columna < 6:
            if columna %2 != 0:
                tk.Label(pestana_planeacion, text=texto, bg="#CCCCCC", justify=tk.LEFT).grid(column=columna, row=fila, sticky=tk.W)
            else:
                tk.Label(pestana_planeacion, text=texto, justify=tk.LEFT).grid(column=columna, row=fila)
            columna+=1
        else:
            fila +=1
            columna = 0
            tk.Label(pestana_planeacion, text=texto, justify=tk.LEFT).grid(column=columna, row=fila)


#--------------------------------------------------------------------------------------------------------------

#===============================================================================================================

# dormirPestanas("1000000000")
dormirPestanas("1111111111")
llenarPlaneacion()
pestanas.select(pestana_planeacion)

main.mainloop()
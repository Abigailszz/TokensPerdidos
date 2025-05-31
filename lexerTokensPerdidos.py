import re
import ply.lex as lex
import tkinter as tk
from tkinter import filedialog, scrolledtext


# Lista de tokens
tokens = [
    'EQUIPOS', 'NOMBRE_EQUIPO','IDENTIDAD_EQUIPO', 'LINK','ASIGNATURA','CARRERA', 'UNIVERSIDAD',
    'DIRECCION', 'CALLE', 'CIUDAD','PAIS','ALIANZA_EQUIPO','INTEGRANTES',
    'NOMBRE', 'EDAD', 'CARGO' ,'FOTO','EMAIL', 'HABILIDADES', 'SALARIO','ACTIVO',
    'PROYECTOS','RESUMEN',
    'TAREAS','INFO_TAREA', 'VIDEO','CONCLUSION','STRING_EMAIL','ESTADO','FECHA_INICIO','FECHA_FIN',
     'VERSION', 'FIRMA_DIGITAL', 'STRING_URL', 'DATE', 'FLOAT', 'INTEGER', 'BOOL',
    'STRING', 'COMILLAS', 'COMA', 'APERTURA_LLAVE', 'CIERRE_LLAVE', 'APERTURA_CORCHETE', 'CIERRE_CORCHETE', 'DOS_PUNTOS'
]


# Expresiones regulares para tokens específicos
t_EQUIPOS = r'"equipos"'
t_NOMBRE_EQUIPO = r'"nombre_equipo"'
t_IDENTIDAD_EQUIPO = r'"identidad_equipo"'
t_LINK = r' "link" '
t_ASIGNATURA = r'"asignatura"' 
t_CARRERA = r'"carrera"' 
t_UNIVERSIDAD = r'"universidad_regional"' 
t_DIRECCION = r'"direccion"'
t_CALLE = r'"calle"'
t_CIUDAD = r'"ciudad"'
t_PAIS = r' "pais" '
t_ALIANZA_EQUIPO = r'"alianza_equipo"'


t_INTEGRANTES = r'"integrantes"'
t_NOMBRE = r'"nombre"'
t_EDAD = r' "edad" '
t_CARGO = r'"cargo"'
t_FOTO = r' "foto" '
t_EMAIL = r' "email" '
t_HABILIDADES = r' "habilidades" '
t_SALARIO = r'"salario"'
t_ACTIVO = r'"activo"'


t_PROYECTOS = r'"proyectos"'


t_TAREAS = r'"tareas"'
t_ESTADO = r'"estado"'
t_RESUMEN= r'"resumen"'
t_FECHA_INICIO = r'"fecha_inicio"'
t_FECHA_FIN= r'"fecha_fin"'

t_VIDEO = r'"video"'
t_CONCLUSION = r'"conclusion"'


t_VERSION = r'"version"'
t_FIRMA_DIGITAL = r'"firma_digital"'
# Expresiones regulares para tokens generales
t_STRING_EMAIL=r'"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"'


t_STRING_URL = r'"(http|https)://[a-zA-Z0-9\-\.]+(:[0-9]+)?(/[a-zA-Z0-9\-\._~:/?#\[\]@!\$&\'\(\)\*\+,;=%]*)?"'
t_DATE = r'"(19[0-9]{2}|20[0-9]{2})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])"'
t_FLOAT = r'\b[0-9]+\.[0-9]{2}\b'
t_INTEGER = r'\b[0-9]+\b'
t_BOOL = r'\btrue\b|\bfalse\b'
t_COMILLAS = r'"'
t_DOS_PUNTOS = r':'
t_COMA = r','
t_APERTURA_LLAVE = r'\{'
t_CIERRE_LLAVE = r'\}'
t_APERTURA_CORCHETE = r'\['
t_CIERRE_CORCHETE = r'\]'
t_STRING = r'"[^"]*"'
# Ignorar espacios y tabulaciones
t_ignore = ' \t\n'


# Función para manejar errores
def t_error(t):
    error_message = f"Carácter ilegal:'{t.value[0]}'\n\n"
    output_text.insert(tk.END, error_message)
    t.lexer.skip(1)


# Crear el lexer
lexer = lex.lex()


# Función para analizar texto
def analyze_text(text):
    lexer.input(text)
    tokens = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append(tok)
    return tokens


# Función para abrir archivo y mostrar tokens
def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            text = file.read()
        output_text.delete(1.0, tk.END)
        tokens = analyze_text(text)
        for token in tokens:
            output_text.insert(tk.END, f"El TOKEN {token.type} ha sido encontrado:'{token.value}'\n\n")


# Mensaje para mostrar en pantalla
mensaje = "Ingrese manualmente el texto que desea analizar:"


# Función para procesar texto ingresado manualmente
def process_input(event=None):
    text = input_text.get("1.0", tk.END)
    if text.startswith(mensaje):
        text = text[len(mensaje):].strip()
    output_text.delete(1.0, tk.END)
    tokens = analyze_text(text)
    for token in tokens:
        output_text.insert(tk.END, f"El TOKEN {token.type} ha sido encontrado: '{token.value}' \n\n")


# Función para limpiar el cuadro de texto de entrada y salida
def clear_text():
    input_text.delete(1.0, tk.END)
    input_text.insert(tk.END, mensaje)
    output_text.delete(1.0, tk.END)


# Ventana con tkinter

root = tk.Tk()
root.title("Analizador Léxico | TokensPerdidos")
root.geometry("1000x600")
root.configure(bg="#1e1e1e")
root.resizable(False, False)


sidebar = tk.Frame(root, bg="#121212", width=200)
sidebar.pack(side=tk.LEFT, fill=tk.Y)

btn_style = {'bg': "#4d4d4d", 'fg': 'white', 'activebackground': '#444', 'width': 20, 'height': 2, 'bd': 0}

tk.Label(sidebar, text="Menú", bg="#121212", fg="#fff", font=("Arial", 14, "bold")).pack(pady=20)

tk.Button(sidebar, text="📂 Abrir Archivo", command=open_file, **btn_style).pack(pady=10)
tk.Button(sidebar, text="🧠 Compilar", command=process_input, **btn_style).pack(pady=10)
tk.Button(sidebar, text="🧹 Limpiar", command=clear_text, **btn_style).pack(pady=10)
tk.Button(sidebar, text="❌ Salir", command=root.quit, **btn_style).pack(pady=10)


main_frame = tk.Frame(root, bg="#1e1e1e")
main_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

# Editor de texto
input_label = tk.Label(main_frame, text="Ingrese el texto a analizar", bg="#1e1e1e", fg="white", font=("Consolas", 12, "bold"))
input_label.pack(pady=(10, 0))

input_text = scrolledtext.ScrolledText(main_frame, width=100, height=12, bg="#2e2e2e", fg="white", insertbackground='white',
                                       font=("Consolas", 12), borderwidth=2, relief="solid")
input_text.pack(pady=10)

# Consola de salida
output_label = tk.Label(main_frame, text="Consola de tokens", bg="#1e1e1e", fg="white", font=("Consolas", 12, "bold"))
output_label.pack(pady=(10, 0))

output_text = scrolledtext.ScrolledText(main_frame, width=100, height=15, bg="#1e1e1e", fg="#00ff00", insertbackground='white',
                                        font=("Consolas", 11), borderwidth=2, relief="solid")
output_text.pack(pady=10)

# Tecla Enter = Compilar
input_text.bind("<Return>", process_input)

root.mainloop()

import re
import ply.lex as lex
import tkinter as tk
from tkinter import filedialog, scrolledtext

# Lista de tokens
tokens = [
   'EMPRESAS', 'NOMBRE_EMPRESA', 'FUNDACION', 'DIRECCION', 'CALLE', 'CIUDAD','PAIS','INGRESOS_ANUALES', 'PYME', 'LINK',
    'DEPARTAMENTOS', 'NOMBRE', 'JEFE', 'SUBDEPARTAMENTOS', 'EMPLEADOS', 'EDAD', 'CARGO', 'SALARIO', 'ACTIVO', 'FECHA_CONTRATACION',
    'PROYECTOS', 'ESTADO', 'FECHA_INICIO', 'FECHA_FIN', 'VERSION', 'FIRMA_DIGITAL', 'STRING_URL', 'DATE', 'FLOAT', 'INTEGER', 'BOOL',
    'STRING', 'COMILLAS', 'COMA', 'APERTURA_LLAVE', 'CIERRE_LLAVE', 'APERTURA_CORCHETE', 'CIERRE_CORCHETE', 'DOS_PUNTOS', 'TOKENS_PERDIDOS'
]

# Expresiones regulares para tokens específicos
t_EMPRESAS = r'"empresas"'
t_NOMBRE_EMPRESA = r'"nombre_empresa"'
t_FUNDACION = r'"fundación"'
t_DIRECCION = r'"dirección"'
t_CALLE = r'"calle"'
t_CIUDAD = r'"ciudad"'
t_PAIS = r' "país" '
t_INGRESOS_ANUALES = r'"ingresos_anuales"'
t_PYME = r' "pyme" '
t_LINK = r' "link" '
t_DEPARTAMENTOS = r'"departamentos"'
t_SUBDEPARTAMENTOS = r'"subdepartamentos"'
t_EMPLEADOS = r'"empleados"'
t_NOMBRE = r'"nombre"'
t_JEFE = r' "jefe" '
t_EDAD = r' "edad" '
t_CARGO = r'"cargo"'
t_SALARIO = r'"salario"'
t_ACTIVO = r'"activo"'
t_FECHA_CONTRATACION = r'"fecha_contratación"'
t_PROYECTOS = r'"proyectos"'
t_ESTADO = r'"estado"'
t_FECHA_INICIO = r'"fecha_inicio"'
t_FECHA_FIN = r'"fecha_fin"'
t_VERSION = r'"version"'
t_FIRMA_DIGITAL = r'"firma_digital"'
# Expresiones regulares para tokens generales
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

# Configurar la ventana principal de tkinter
root = tk.Tk()
root.title("Visor de Tokens de Lexer by AlphaCode")
root.configure(bg="gray14")  # Cambiar el color de fondo de la ventana principal

frame = tk.Frame(root, bg="gray14")
frame.pack(pady=10)

# Cuadro de texto1
input_text = scrolledtext.ScrolledText(frame, width=100, height=10, bg="thistle3", fg="black")
input_text.pack(pady=10)
input_text.insert(tk.END, mensaje)

# Vincular la tecla Enter a la función process_input
input_text.bind("<Return>", process_input)

# Cuadro de texto2
output_text = scrolledtext.ScrolledText(frame, width=100, height=20, bg="thistle3", fg="black")
output_text.pack(pady=10)

# Tamaño de botones y fondo
button_frame = tk.Frame(root, bg="gray14")
button_frame.pack(pady=10, side=tk.BOTTOM)

# Botones
open_button = tk.Button(button_frame, text="Abrir Archivo", command=open_file, bg="thistle3", fg="black")
open_button.pack(side=tk.LEFT, padx=10)

process_button = tk.Button(button_frame, text="Compilar", command=process_input, bg="thistle3", fg="black")
process_button.pack(side=tk.LEFT, padx=10)

clear_button = tk.Button(button_frame, text="Limpiar Pantalla", command=clear_text, bg="thistle3", fg="black")
clear_button.pack(side=tk.LEFT, padx=10)

exit_button = tk.Button(button_frame, text="Salir", command=root.quit, bg="thistle3", fg="black")
exit_button.pack(side=tk.LEFT, padx=10)

# Hacer que la ventana no sea redimensionable
root.resizable(False, False)

root.mainloop()

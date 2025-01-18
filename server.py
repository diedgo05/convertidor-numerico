import tkinter as tk
from tkinter import messagebox

def convert_number():
    try:
        input_value = entry.get()

        if not input_value.isdigit():
            raise ValueError("Por favor, ingresa un número entero positivo.")

        number = int(input_value)

        selected_format = number_format_var.get()
        if selected_format == "BIN":
            result = bin(number)[2:]
        elif selected_format == "DEC":
            result = str(number)
        elif selected_format == "HEX":
            result = hex(number)[2:].upper()
        elif selected_format == "OCT":
            result = oct(number)[2:]
        else:
            raise ValueError("Por favor, selecciona un formato.")

        result_label.config(text=f"Resultado ({selected_format}): {result}")

    except ValueError as e:
        messagebox.showerror("Error de entrada", str(e))

def convert_text():
    try:
        text_value = text_entry.get()
        if len(text_value) > 10:
            raise ValueError("El texto no puede tener más de 10 caracteres.")
        if not text_value:
            raise ValueError("Por favor, ingresa un texto.")

        result = ' '.join(str(ord(char)) for char in text_value)
        ascii_result_label.config(text=f"ASCII (DEC): {result}")

    except ValueError as e:
        messagebox.showerror("Error de entrada", str(e))

# VENTANA PRINCIPAL
root = tk.Tk()
root.title("Conversor de Números y ASCII")
root.geometry("500x500")

# CONVERSIÓN DECIMAL A BINARIO, HEXADECIMAL Y OCTAL
label = tk.Label(root, text="Ingresa un número entero:", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14), justify="center")
entry.pack(pady=5)

# OPCIONES DE CONVERSIÓN
number_format_var = tk.StringVar(value="DEC")
bin_radio = tk.Radiobutton(root, text="BIN", variable=number_format_var, value="BIN", font=("Arial", 12))
bin_radio.pack(pady=2)

hex_radio = tk.Radiobutton(root, text="HEX", variable=number_format_var, value="HEX", font=("Arial", 12))
hex_radio.pack(pady=2)

oct_radio = tk.Radiobutton(root, text="OCT", variable=number_format_var, value="OCT", font=("Arial", 12))
oct_radio.pack(pady=2)

convert_button = tk.Button(root, text="Convertir Número", font=("Arial", 12), command=convert_number)
convert_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Courier", 12), justify="left")
result_label.pack(pady=20)

# Separador
separator = tk.Frame(root, height=2, bd=1, relief="sunken")
separator.pack(fill="x", pady=10)

# TEXTO A ASCII
text_label = tk.Label(root, text="Ingresa un texto (máximo 10 caracteres):", font=("Arial", 12))
text_label.pack(pady=10)

text_entry = tk.Entry(root, font=("Arial", 14), justify="center")
text_entry.pack(pady=5)

convert_text_button = tk.Button(root, text="Convertir Texto", font=("Arial", 12), command=convert_text)
convert_text_button.pack(pady=10)

ascii_result_label = tk.Label(root, text="", font=("Courier", 12), justify="left")
ascii_result_label.pack(pady=20)

# Iniciar el bucle de la aplicación
root.mainloop()

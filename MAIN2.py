import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class Alumno:
    def __init__(self, codigo, apellido_paterno, apellido_materno, nombres, carrera, domicilio, fecha_nacimiento):
        self.codigo = codigo
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.nombres = nombres
        self.carrera = carrera
        self.domicilio = domicilio
        self.fecha_nacimiento = fecha_nacimiento

class AlumnoManager:
    def __init__(self):
        self.alumnos = []

    def crear_alumno(self, codigo, apellido_paterno, apellido_materno, nombres, carrera, domicilio, fecha_nacimiento):
        alumno = Alumno(codigo, apellido_paterno, apellido_materno, nombres, carrera, domicilio, fecha_nacimiento)
        self.alumnos.append(alumno)

    def listar_alumnos(self):
        return self.alumnos

    def buscar_alumno(self, codigo):
        for alumno in self.alumnos:
            if alumno.codigo == codigo:
                return alumno
        return None

    def actualizar_alumno(self, codigo, **kwargs):
        alumno = self.buscar_alumno(codigo)
        if alumno:
            for key, value in kwargs.items():
                setattr(alumno, key, value)

    def borrar_alumno(self, codigo):
        alumno = self.buscar_alumno(codigo)
        if alumno:
            self.alumnos.remove(alumno)

class AlumnoGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestión de Alumnos")

        self.manager = AlumnoManager()

        self.codigo_var = tk.StringVar()
        self.apellido_paterno_var = tk.StringVar()
        self.apellido_materno_var = tk.StringVar()
        self.nombres_var = tk.StringVar()
        self.carrera_var = tk.StringVar()
        self.domicilio_var = tk.StringVar()
        self.fecha_nacimiento_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        self.tree = ttk.Treeview(self.master, columns=("Código", "Apellidos", "Nombres", "Carrera", "Domicilio", "Fecha de Nacimiento"))
        self.tree.heading("#0", text="ID")
        self.tree.heading("#1", text="Código")
        self.tree.heading("#2", text="Apellidos")
        self.tree.heading("#3", text="Nombres")
        self.tree.heading("#4", text="Carrera")
        self.tree.heading("#5", text="Domicilio")
        self.tree.heading("#6", text="Fecha de Nacimiento")
        self.tree.grid(row=0, column=0, columnspan=2)

        tk.Label(self.master, text="Código:").grid(row=1, column=0, sticky="e")
        tk.Entry(self.master, textvariable=self.codigo_var).grid(row=1, column=1)

        tk.Label(self.master, text="Apellido Paterno:").grid(row=2, column=0, sticky="e")
        tk.Entry(self.master, textvariable=self.apellido_paterno_var).grid(row=2, column=1)

        tk.Label(self.master, text="Apellido Materno:").grid(row=3, column=0, sticky="e")
        tk.Entry(self.master, textvariable=self.apellido_materno_var).grid(row=3, column=1)

        tk.Label(self.master, text="Nombres:").grid(row=4, column=0, sticky="e")
        tk.Entry(self.master, textvariable=self.nombres_var).grid(row=4, column=1)

        tk.Label(self.master, text="Carrera:").grid(row=5, column=0, sticky="e")
        tk.Entry(self.master, textvariable=self.carrera_var).grid(row=5, column=1)

        tk.Label(self.master, text="Domicilio:").grid(row=6, column=0, sticky="e")
        tk.Entry(self.master, textvariable=self.domicilio_var).grid(row=6, column=1)

        tk.Label(self.master, text="Fecha de Nacimiento:").grid(row=7, column=0, sticky="e")
        tk.Entry(self.master, textvariable=self.fecha_nacimiento_var).grid(row=7, column=1)

        tk.Button(self.master, text="Crear Alumno", command=self.crear_alumno).grid(row=8, column=0, columnspan=2, pady=10)
        tk.Button(self.master, text="Listar Alumnos", command=self.listar_alumnos).grid(row=9, column=0, columnspan=2, pady=10)
        tk.Button(self.master, text="Buscar Alumno", command=self.buscar_alumno).grid(row=10, column=0, columnspan=2, pady=10)
        tk.Button(self.master, text="Actualizar Alumno", command=self.actualizar_alumno).grid(row=11, column=0, columnspan=2, pady=10)
        tk.Button(self.master, text="Eliminar Alumno", command=self.eliminar_alumno).grid(row=12, column=0, columnspan=2, pady=10)

    def crear_alumno(self):
        codigo = self.codigo_var.get()
        apellido_paterno = self.apellido_paterno_var.get()
        apellido_materno = self.apellido_materno_var.get()
        nombres = self.nombres_var.get()
        carrera = self.carrera_var.get()
        domicilio = self.domicilio_var.get()
        fecha_nacimiento = self.fecha_nacimiento_var.get()

        if codigo and apellido_paterno and apellido_materno and nombres and carrera and domicilio and fecha_nacimiento:
            self.manager.crear_alumno(codigo, apellido_paterno, apellido_materno, nombres, carrera, domicilio, fecha_nacimiento)
            self.listar_alumnos()
            messagebox.showinfo("Éxito", "Alumno creado exitosamente.")
            self.limpiar_campos()
        else:
            messagebox.showerror("Error", "Por favor completa todos los campos.")

    def listar_alumnos(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for idx, alumno in enumerate(self.manager.listar_alumnos(), start=1):
            self.tree.insert("", "end", text=str(idx), values=(
                alumno.codigo,
                f"{alumno.apellido_paterno if alumno.apellido_paterno else ''} {alumno.apellido_materno if alumno.apellido_materno else ''}",
                alumno.nombres if alumno.nombres else '',
                alumno.carrera if alumno.carrera else '',
                alumno.domicilio if alumno.domicilio else '',
                alumno.fecha_nacimiento if alumno.fecha_nacimiento else ''
            ))

    def buscar_alumno(self):
        codigo = self.codigo_var.get()
        if codigo:
            alumno = self.manager.buscar_alumno(codigo)
            if alumno:
                self.limpiar_campos()
                self.codigo_var.set(alumno.codigo)
                self.apellido_paterno_var.set(alumno.apellido_paterno)
                self.apellido_materno_var.set(alumno.apellido_materno)
                self.nombres_var.set(alumno.nombres)
                self.carrera_var.set(alumno.carrera)
                self.domicilio_var.set(alumno.domicilio)
                self.fecha_nacimiento_var.set(alumno.fecha_nacimiento)
                messagebox.showinfo("Alumno encontrado", f"Alumno encontrado:\n{alumno}")
            else:
                messagebox.showerror("Error", "Alumno no encontrado.")
        else:
            messagebox.showerror("Error", "Por favor ingrese el código del alumno.")

    def actualizar_alumno(self):
        codigo = self.codigo_var.get()
        if codigo:
            alumno = self.manager.buscar_alumno(codigo)
            if alumno:
                apellido_paterno = self.apellido_paterno_var.get()
                apellido_materno = self.apellido_materno_var.get()
                nombres = self.nombres_var.get()
                carrera = self.carrera_var.get()
                domicilio = self.domicilio_var.get()
                fecha_nacimiento = self.fecha_nacimiento_var.get()
                self.manager.actualizar_alumno(codigo, apellido_paterno=apellido_paterno, apellido_materno=apellido_materno, nombres=nombres, carrera=carrera, domicilio=domicilio, fecha_nacimiento=fecha_nacimiento)
                self.listar_alumnos()
                messagebox.showinfo("Éxito", "Alumno actualizado exitosamente.")
                self.limpiar_campos()
            else:
                messagebox.showerror("Error", "Alumno no encontrado.")
        else:
            messagebox.showerror("Error", "Por favor ingrese el código del alumno.")

    def eliminar_alumno(self):
        codigo = self.codigo_var.get()
        if codigo:
            alumno = self.manager.buscar_alumno(codigo)
            if alumno:
                confirmacion = messagebox.askyesno("Confirmación", f"¿Está seguro de eliminar al alumno {alumno.codigo}?")
                if confirmacion:
                    self.manager.borrar_alumno(codigo)
                    self.listar_alumnos()
                    self.limpiar_campos()
                    messagebox.showinfo("Éxito", "Alumno eliminado exitosamente.")
            else:
                messagebox.showerror("Error", "Alumno no encontrado.")
        else:
            messagebox.showerror("Error", "Por favor ingrese el código del alumno.")

    def limpiar_campos(self):
        self.codigo_var.set("")
        self.apellido_paterno_var.set("")
        self.apellido_materno_var.set("")
        self.nombres_var.set("")
        self.carrera_var.set("")
        self.domicilio_var.set("")
        self.fecha_nacimiento_var.set("")

def main():
    root = tk.Tk()
    app = AlumnoGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

import tkinter as tk


class SistemaClientes:

    def __init__(self):

        # ==========================
        # Ventana Principal
        # ==========================

        self.ventana = tk.Tk()
        self.ventana.title("Sistema de Gestión de Clientes")
        self.ventana.geometry("1100x650")
        self.ventana.resizable(False, False)

        # ==========================
        # Colores
        # ==========================

        self.color_menu = "#4338CA"
        self.color_fondo = "#F8F9FC"
        self.color_boton = "#6366F1"
        self.color_texto = "white"

        self.ventana.configure(bg=self.color_fondo)

        # ==========================
        # Construcción de la interfaz
        # ==========================

        self.crear_menu()
        self.crear_contenido()
        self.mostrar_inicio()

    # =====================================
    # MENÚ LATERAL
    # =====================================

    def crear_menu(self):

        self.menu = tk.Frame(
            self.ventana,
            bg=self.color_menu,
            width=250
        )

        self.menu.pack(side="left", fill="y")
        self.menu.pack_propagate(False)

        titulo = tk.Label(
            self.menu,
            text="Sistema de\nGestión de Clientes",
            bg=self.color_menu,
            fg="white",
            font=("Segoe UI", 18, "bold"),
            justify="center"
        )

        titulo.pack(pady=(30, 10))

        subtitulo = tk.Label(
            self.menu,
            text="Organiza • Consulta • Administra",
            bg=self.color_menu,
            fg="white",
            font=("Segoe UI", 9)
        )

        subtitulo.pack(pady=(0, 25))

        self.crear_boton("🏠 Inicio", self.mostrar_inicio)
        self.crear_boton("👤 Registrar", self.mostrar_registro)
        self.crear_boton("📋 Mostrar", self.mostrar_clientes)
        self.crear_boton("🔍 Buscar", self.mostrar_busqueda)
        self.crear_boton("✏ Editar", self.mostrar_editar)
        self.crear_boton("🗑 Eliminar", self.mostrar_eliminar)
        self.crear_boton("🚪 Salir", self.ventana.destroy)

    # =====================================
    # BOTONES
    # =====================================

    def crear_boton(self, texto, comando):

        boton = tk.Button(
            self.menu,
            text=texto,
            bg=self.color_boton,
            fg="white",
            activebackground="#818CF8",
            activeforeground="white",
            relief="flat",
            font=("Segoe UI", 11),
            cursor="hand2",
            width=20,
            height=2,
            command=comando
        )

        boton.pack(pady=5)

    # =====================================
    # PANEL DERECHO
    # =====================================

    def crear_contenido(self):

        self.contenido = tk.Frame(
            self.ventana,
            bg=self.color_fondo
        )

        self.contenido.pack(
            side="right",
            expand=True,
            fill="both"
        )

    # =====================================
    # LIMPIAR CONTENIDO
    # =====================================

    def limpiar_contenido(self):

        for widget in self.contenido.winfo_children():
            widget.destroy()

    # =====================================
    # PANTALLA DE INICIO
    # =====================================

    def mostrar_inicio(self):

        self.limpiar_contenido()

        titulo = tk.Label(
            self.contenido,
            text="Sistema de Gestión de Clientes",
            font=("Segoe UI", 24, "bold"),
            bg=self.color_fondo
        )

        titulo.pack(pady=(80, 20))

        bienvenida = tk.Label(
            self.contenido,
            text="¡Bienvenido!",
            font=("Segoe UI", 18),
            bg=self.color_fondo
        )

        bienvenida.pack()

        descripcion = tk.Label(
            self.contenido,
            text="Administra la información de tus clientes\n"
                 "de manera rápida, sencilla y organizada.\n\n"
                 "Selecciona una opción del menú para comenzar.",
            font=("Segoe UI", 12),
            justify="center",
            bg=self.color_fondo
        )

        descripcion.pack(pady=20)

    # =====================================
    # PANTALLAS (AÚN VACÍAS)
    # =====================================

    def mostrar_registro(self):

        self.limpiar_contenido()

    def mostrar_clientes(self):

        self.limpiar_contenido()

    def mostrar_busqueda(self):

        self.limpiar_contenido()

    def mostrar_editar(self):

        self.limpiar_contenido()

    def mostrar_eliminar(self):

        self.limpiar_contenido()

    # =====================================
    # EJECUTAR
    # =====================================

    def ejecutar(self):

        self.ventana.mainloop()
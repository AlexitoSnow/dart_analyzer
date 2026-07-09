import os
import customtkinter as ctk
from tkinter import messagebox, simpledialog

class FileExplorer(ctk.CTkFrame):
    def __init__(self, parent, algorithms_dir, on_file_select, on_log, **kwargs):
        super().__init__(parent, **kwargs)
        self.algorithms_dir = algorithms_dir
        self.on_file_select = on_file_select
        self.on_log = on_log
        self.file_buttons = {}
        self.active_file = None

        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Title
        self.lbl_title = ctk.CTkLabel(
            self, 
            text="DART ANALYZER", 
            font=ctk.CTkFont(size=18, weight="bold")
        )
        self.lbl_title.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")

        # Subtitle
        self.lbl_subtitle = ctk.CTkLabel(
            self, 
            text="Algoritmos Disponibles", 
            font=ctk.CTkFont(size=12, weight="normal"),
            text_color="gray"
        )
        self.lbl_subtitle.grid(row=1, column=0, padx=20, pady=(10, 5), sticky="w")

        # Actions Frame
        self.actions_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.actions_frame.grid(row=2, column=0, padx=20, pady=5, sticky="ew")
        self.actions_frame.grid_columnconfigure(0, weight=1)
        self.actions_frame.grid_columnconfigure(1, weight=1)

        self.btn_new = ctk.CTkButton(
            self.actions_frame,
            text="+ Nuevo",
            height=28,
            command=self.create_new_file
        )
        self.btn_new.grid(row=0, column=0, padx=(0, 5), sticky="ew")

        self.btn_refresh = ctk.CTkButton(
            self.actions_frame,
            text="Refrescar",
            height=28,
            fg_color="gray30",
            hover_color="gray40",
            command=self.refresh_file_list
        )
        self.btn_refresh.grid(row=0, column=1, padx=(5, 0), sticky="ew")

        # Scrollable list
        self.scroll_frame = ctk.CTkScrollableFrame(self, label_text="Archivos")
        self.scroll_frame.grid(row=3, column=0, padx=15, pady=10, sticky="nsew")

    def refresh_file_list(self):
        """Scans the algorithms directory and rebuilds the buttons in the scroll list."""
        for btn in self.file_buttons.values():
            btn.destroy()
        self.file_buttons.clear()

        if not os.path.exists(self.algorithms_dir):
            self.on_log("Error: La carpeta de algoritmos no existe.", "error")
            return

        try:
            files = sorted([f for f in os.listdir(self.algorithms_dir) if f.endswith(".dart")])
            for i, filename in enumerate(files):
                btn = ctk.CTkButton(
                    self.scroll_frame,
                    text=filename,
                    fg_color="transparent",
                    text_color="white",
                    hover_color="gray30",
                    anchor="w",
                    command=lambda f=filename: self.select_file(f)
                )
                btn.grid(row=i, column=0, padx=5, pady=2, sticky="ew")
                self.file_buttons[filename] = btn
                
            # If the current active file is no longer in the list, reset active file
            if self.active_file and self.active_file not in self.file_buttons:
                self.active_file = None
                
            # Highlight current active file if it exists
            if self.active_file:
                self.highlight_button(self.active_file)
        except Exception as e:
            self.on_log(f"Error al refrescar archivos: {str(e)}", "error")

    def select_file(self, filename):
        """Triggers callback on parent to load file content and highlights button."""
        self.active_file = filename
        self.highlight_button(filename)
        self.on_file_select(filename)

    def highlight_button(self, filename):
        """Highlights the active button and resets others."""
        for name, btn in self.file_buttons.items():
            if name == filename:
                btn.configure(fg_color="#1f77b4", hover_color="#155d8f")
            else:
                btn.configure(fg_color="transparent", hover_color="gray30")

    def create_new_file(self):
        """Dialog to create a new Dart file."""
        filename = simpledialog.askstring("Nuevo Archivo", "Nombre del archivo (ej. algoritmo_nuevo.dart):")
        if not filename:
            return

        if not filename.endswith(".dart"):
            filename += ".dart"

        file_path = os.path.join(self.algorithms_dir, filename)
        if os.path.exists(file_path):
            messagebox.showerror("Error", f"El archivo '{filename}' ya existe.")
            return

        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write("// Nuevo algoritmo Dart\nvoid main() {\n  \n}\n")
            self.refresh_file_list()
            self.select_file(filename)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo crear el archivo: {str(e)}")

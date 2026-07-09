import customtkinter as ctk

class CodeEditor(ctk.CTkFrame):
    def __init__(self, parent, on_run_analysis, on_clear_console, **kwargs):
        super().__init__(parent, fg_color="transparent", **kwargs)
        self.on_run_analysis = on_run_analysis
        self.on_clear_console = on_clear_console

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # --- HEADER FRAME ---
        self.header_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.header_frame.grid(row=0, column=0, sticky="ew", pady=(0, 10))
        self.header_frame.grid_columnconfigure(0, weight=1)

        self.lbl_active_file = ctk.CTkLabel(
            self.header_frame,
            text="Editor: Sin archivo seleccionado",
            font=ctk.CTkFont(size=14, weight="bold")
        )
        self.lbl_active_file.grid(row=0, column=0, sticky="w")

        # Author selector dropdown
        self.lbl_author = ctk.CTkLabel(self.header_frame, text="Autor / Integrante:")
        self.lbl_author.grid(row=0, column=1, padx=(10, 5), sticky="e")

        self.author_selector = ctk.CTkComboBox(
            self.header_frame,
            values=["AlexanderNieves", "SofiaIzaguirre", "DanielCortez"],
            state="readonly"
        )
        self.author_selector.grid(row=0, column=2, sticky="e")
        self.author_selector.set("AlexanderNieves")

        # --- CODE EDITOR TEXTBOX ---
        self.editor = ctk.CTkTextbox(
            self,
            font=ctk.CTkFont(family="Consolas", size=14),
            wrap="none",
            undo=True
        )
        self.editor.grid(row=1, column=0, sticky="nsew", pady=5)

        # --- ACTION BUTTONS PANEL ---
        self.buttons_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.buttons_frame.grid(row=2, column=0, sticky="ew", pady=10)
        self.buttons_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

        self.btn_lexical = ctk.CTkButton(
            self.buttons_frame,
            text="Ejecutar Analizador Léxico",
            fg_color="#1f77b4",
            hover_color="#155d8f",
            font=ctk.CTkFont(weight="bold"),
            command=lambda: self.on_run_analysis("lexico")
        )
        self.btn_lexical.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        self.btn_syntactic = ctk.CTkButton(
            self.buttons_frame,
            text="Ejecutar Sintáctico",
            fg_color="#2ca02c",
            hover_color="#1e6f1e",
            font=ctk.CTkFont(weight="bold"),
            command=lambda: self.on_run_analysis("sintactico")
        )
        self.btn_syntactic.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        self.btn_semantic = ctk.CTkButton(
            self.buttons_frame,
            text="Ejecutar Semántico",
            fg_color="#9467bd",
            hover_color="#684787",
            font=ctk.CTkFont(weight="bold"),
            command=lambda: self.on_run_analysis("semantico")
        )
        self.btn_semantic.grid(row=0, column=2, padx=5, pady=5, sticky="ew")

        self.btn_clear = ctk.CTkButton(
            self.buttons_frame,
            text="Limpiar Consola",
            fg_color="gray30",
            hover_color="gray40",
            font=ctk.CTkFont(weight="bold"),
            command=self.on_clear_console
        )
        self.btn_clear.grid(row=0, column=3, padx=5, pady=5, sticky="ew")

    def set_active_file(self, filename):
        """Updates the active file label."""
        if filename:
            self.lbl_active_file.configure(text=f"Editor: {filename}")
        else:
            self.lbl_active_file.configure(text="Editor: Sin archivo seleccionado")

    def set_code(self, code_text):
        """Inserts text content into the editor."""
        self.editor.delete("1.0", "end")
        self.editor.insert("1.0", code_text)

    def get_code(self):
        """Retrieves the current code text from the editor."""
        return self.editor.get("1.0", "end-1c")

    def get_selected_author(self):
        """Returns the chosen author's name."""
        return self.author_selector.get()

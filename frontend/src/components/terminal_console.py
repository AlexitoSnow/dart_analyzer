import customtkinter as ctk

class TerminalConsole(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, fg_color="transparent", **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.console = ctk.CTkTextbox(
            self,
            font=ctk.CTkFont(family="Consolas", size=12),
            fg_color="#121212",  # Dark terminal style background
            wrap="word"
        )
        self.console.grid(row=0, column=0, sticky="nsew", padx=0, pady=5)
        self.console.configure(state="disabled")

        # Setup text tags in the underlying Tkinter Text widget for colored console logs
        self.console._textbox.tag_config("success", foreground="#39ff14")
        self.console._textbox.tag_config("error", foreground="#ff3333")
        self.console._textbox.tag_config("info", foreground="#ffffff")
        self.console._textbox.tag_config("header", foreground="#00e5ff", font=ctk.CTkFont(family="Consolas", size=12, weight="bold"))

    def log(self, text, tag="info"):
        """Appends log text with standard tag styling."""
        self.console.configure(state="normal")
        self.console.insert("end", text + "\n", tag)
        self.console.see("end")
        self.console.configure(state="disabled")

    def log_info(self, text):
        self.log(text, "info")

    def log_error(self, text):
        self.log(text, "error")

    def log_success(self, text):
        self.log(text, "success")

    def log_header(self, text):
        self.log(text, "header")

    def clear(self):
        """Clears the console text."""
        self.console.configure(state="normal")
        self.console.delete("1.0", "end")
        self.console.configure(state="disabled")

import os
import sys
import subprocess
import customtkinter as ctk
from tkinter import messagebox

src_dir = os.path.dirname(os.path.abspath(__file__))
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

from components.file_explorer import FileExplorer
from components.code_editor import CodeEditor
from components.terminal_console import TerminalConsole

class DartAnalyzerGUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        # --- PATH CONFIGURATION ---
        self.workspace_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        self.algorithms_dir = os.path.join(self.workspace_root, "backend", "algorithms")
        self.backend_dir = os.path.join(self.workspace_root, "backend")
        
        # Determine the Python executable from the backend's virtual environment
        if sys.platform == "win32":
            self.backend_python = os.path.join(self.backend_dir, "venv", "Scripts", "python.exe")
        else:
            self.backend_python = os.path.join(self.backend_dir, "venv", "bin", "python")
            
        self.bridge_script = os.path.join(self.backend_dir, "src", "gui_bridge.py")

        # --- WINDOW SETUP ---
        self.title("Dart Analyzer - IDE Frontend")
        self.geometry("1100x750")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # --- LAYOUT CONFIGURATION ---
        self.grid_columnconfigure(0, weight=0, minsize=240)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # --- SIDEBAR (FILE EXPLORER) ---
        self.file_explorer = FileExplorer(
            self,
            algorithms_dir=self.algorithms_dir,
            on_file_select=self.load_file,
            on_log=self.log_to_console,
            corner_radius=0
        )
        self.file_explorer.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)

        # --- MAIN PANEL ---
        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=15, pady=15)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=3)  # Code Editor
        self.main_frame.grid_rowconfigure(1, weight=1)  # Terminal Console

        # Code Editor
        self.code_editor = CodeEditor(
            self.main_frame,
            on_run_analysis=self.run_analysis,
            on_clear_console=self.clear_console
        )
        self.code_editor.grid(row=0, column=0, sticky="nsew", pady=5)

        # Terminal Console
        self.terminal_console = TerminalConsole(self.main_frame)
        self.terminal_console.grid(row=1, column=0, sticky="nsew", pady=5)

        # --- INITIALIZATION ---
        self.file_explorer.refresh_file_list()
        self.select_default_file()

    def select_default_file(self):
        """Loads main.dart by default if it exists, otherwise selects the first available file."""
        if "main.dart" in self.file_explorer.file_buttons:
            self.file_explorer.select_file("main.dart")
        elif self.file_explorer.file_buttons:
            first_file = list(self.file_explorer.file_buttons.keys())[0]
            self.file_explorer.select_file(first_file)

    def load_file(self, filename):
        """Autosaves active file, then loads content of selected file into editor."""
        if self.file_explorer.active_file and self.file_explorer.active_file != filename:
            self.save_file_content(self.file_explorer.active_file)

        self.code_editor.set_active_file(filename)

        file_path = os.path.join(self.algorithms_dir, filename)
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            self.code_editor.set_code(content)
            self.terminal_console.log_info(f"Archivo cargado: {filename}")
        except Exception as e:
            self.terminal_console.log_error(f"Error al cargar archivo {filename}: {str(e)}")

    def save_file_content(self, filename):
        """Writes current editor content to the specified file."""
        if not filename:
            return False

        file_path = os.path.join(self.algorithms_dir, filename)
        try:
            content = self.code_editor.get_code()
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            return True
        except Exception as e:
            self.terminal_console.log_error(f"Error al guardar archivo {filename}: {str(e)}")
            return False

    def run_analysis(self, mode):
        """Saves current code and runs the selected analyzer pass via gui_bridge.py."""
        active_file = self.file_explorer.active_file
        if not active_file:
            messagebox.showwarning("Atención", "Por favor, seleccione un archivo antes de ejecutar el análisis.")
            return

        if not self.save_file_content(active_file):
            return

        author_name = self.code_editor.get_selected_author()
        author_map = {"AlexanderNieves": 0, "SofiaIzaguirre": 1, "DanielCortez": 2}
        author_idx = author_map.get(author_name, 0)

        self.clear_console()
        
        mode_label = {
            "lexico": "ANÁLISIS LÉXICO",
            "sintactico": "ANÁLISIS SINTÁCTICO",
            "semantico": "ANÁLISIS SEMÁNTICO"
        }.get(mode, "ANÁLISIS")

        self.terminal_console.log_header(f"=== EJECUTANDO {mode_label} ===")
        self.terminal_console.log_info(f"Archivo: {active_file} | Autor asignado: {author_name}\n")

        # Run bridge process
        try:
            cmd = [
                self.backend_python,
                self.bridge_script,
                mode,
                str(author_idx),
                active_file
            ]
            
            result = subprocess.run(
                cmd,
                cwd=self.backend_dir,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            if result.stdout:
                self.terminal_console.log_info(result.stdout)
                
            if result.stderr:
                self.terminal_console.log_error(result.stderr)

            if result.returncode == 0:
                self.terminal_console.log_success("\n>>> Análisis Exitoso <<<")
            else:
                self.terminal_console.log_error("\n>>> Análisis con Errores <<<")

        except Exception as e:
            self.terminal_console.log_error(f"Fallo en la ejecución del puente backend: {str(e)}")

    def log_to_console(self, text, tag="info"):
        """Logs custom messages to the terminal console (used as callback)."""
        self.terminal_console.log(text, tag)

    def clear_console(self):
        """Clears all logs from the terminal console."""
        self.terminal_console.clear()

if __name__ == "__main__":
    app = DartAnalyzerGUI()
    app.mainloop()

import tkinter as tk
from tkinter import ttk
import subprocess
import threading
import os

scripts = [
    {"name": "Abrir Windows Defender", "path": r"\\192.168.1.3\ti\Dia a dia\ARQUIVOS\Scripts\abrir_windows_defender.bat"},
    {"name": "Abrir Driver Booster", "path": r"\\192.168.1.3\ti\Dia a dia\ARQUIVOS\Scripts\abrir_driver_booster.bat"},
    {"name": "Abrir Windows Update", "path": r"\\192.168.1.3\ti\Dia a dia\ARQUIVOS\Scripts\abrir_windows_update.bat"},
    {"name": "Criar Fiorilli", "path": r"\\192.168.1.3\ti\Dia a dia\ARQUIVOS\Scripts\criar_fiorilli.bat"},
    {"name": "Desativar Windows Defender", "path": r"\\192.168.1.3\ti\Dia a dia\ARQUIVOS\Scripts\abrir_windows_defender.bat"},
    {"name": "Instalar Adobe Reader", "path": r"\\192.168.1.3\ti\Dia a dia\ARQUIVOS\Scripts\instalar_adobe_reader.bat"},
    {"name": "Instalar Chrome", "path": r"\\192.168.1.3\ti\Dia a dia\ARQUIVOS\Scripts\instalar_chrome.bat"},
    {"name": "Limpar Spooler", "path": r"\\192.168.1.3\ti\Dia a dia\ARQUIVOS\Scripts\limpar_spooler_adm.bat"},
]

def on_key_press(event):
    if event.keysym == "1":
        listbox.selection_clear(0, tk.END)
        listbox.selection_set(0)
        listbox.activate(0)
        listbox.see(0)
    elif event.keysym == "Down":
        if listbox.curselection():
            current_index = int(listbox.curselection()[0])
            next_index = (current_index + 1) % listbox.size()
        else:
            next_index = 0
        listbox.selection_clear(0, tk.END)
        listbox.selection_set(next_index)
        listbox.activate(next_index)
        listbox.see(next_index)
    elif event.keysym == "Up":
        if listbox.curselection():
            current_index = int(listbox.curselection()[0])
            prev_index = (current_index - 1) % listbox.size()
        else:
            prev_index = listbox.size() - 1
        listbox.selection_clear(0, tk.END)
        listbox.selection_set(prev_index)
        listbox.activate(prev_index)
        listbox.see(prev_index)
    elif event.keysym == "Return":
        if listbox.curselection():
            confirm_execution(event)

def execute_script(script_path):
    console_text.insert(tk.END, f"Executando script: {script_path}\n")
    
    def run_script():
        process = subprocess.Popen(script_path, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
        for line in process.stdout:
            console_text.insert(tk.END, line.decode("utf-8"))
        process.wait()
        
        console_text.insert(tk.END, f"\nScript executado: {script_path}\n")
    
    thread = threading.Thread(target=run_script)
    thread.start()

def confirm_execution(event):
    index = listbox.curselection()
    if index:
        index = int(index[0])
        script = scripts[index]
        script_name = script["name"]
        script_path = script["path"]

        confirm_window = tk.Toplevel(root)
        confirm_window.title("Confirmação")
        confirm_window.geometry("300x100")

        confirm_label = tk.Label(confirm_window, text=f"Deseja executar o script '{script_name}'?")
        confirm_label.pack(pady=10)

        def execute():
            execute_script(script_path)
            confirm_window.destroy()

        confirm_button = tk.Button(confirm_window, text="Confirmar", command=execute)
        confirm_button.pack(side=tk.LEFT, padx=10)

        cancel_button = tk.Button(confirm_window, text="Cancelar", command=confirm_window.destroy)
        cancel_button.pack(side=tk.RIGHT, padx=10)

        # Configurar o foco na janela de confirmação
        confirm_window.focus_set()

        # Lidar com a pressão da tecla Enter na janela de confirmação
        def on_confirm_window_key_press(event):
            if event.keysym == "Return":
                execute()

        confirm_window.bind("<KeyPress>", on_confirm_window_key_press)

def open_cpuz():
    file_path = r"\\192.168.1.3\ti\Dia a dia\ARQUIVOS\Programas\CPU-Z.exe" 
    if os.path.exists(file_path):
        os.startfile(file_path)

class MultiListbox(tk.Frame):
    def __init__(self, master, columns, data):
        tk.Frame.__init__(self, master)
        self._columns = columns

        self.tree = ttk.Treeview(self, columns=self._columns, show="headings")
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.configure(yscrollcommand=scrollbar.set)

        for col in self._columns:
            self.tree.heading(col, text=col.title())

        self._insert_data(data)

    def _insert_data(self, data):
        for item in data:
            self.tree.insert("", tk.END, values=item)

    def get_selected_item(self):
        selection = self.tree.selection()
        if selection:
            item = self.tree.item(selection[0])["values"]
            return item
        return None

root = tk.Tk()
root.title("ScriptVerse")
root.iconbitmap(r'C:\Users\Administrator\Downloads\icon-_2_.ico')
title_label = tk.Label(root, text="ScriptVerse - v1.0", font=("Arial", 16, "bold"))
title_label.pack()

open_button = tk.Button(root, text="Abrir CPU-Z", command=open_cpuz)
open_button.pack(side=tk.TOP, anchor=tk.NE, padx=10, pady=10)

window_width = 800
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

console_frame = tk.Frame(root)
console_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

console_text = tk.Text(console_frame)
console_text.pack(fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(console_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
scrollbar.config(command=console_text.yview)
console_text.config(yscrollcommand=scrollbar.set)

listbox_frame = tk.Frame(root)
listbox_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))

listbox = tk.Listbox(listbox_frame)
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

listbox.bind("<<ListboxSelect>>", confirm_execution)

root.bind("<KeyPress>", on_key_press)

for script in scripts:
    listbox.insert(tk.END, script["name"])

root.mainloop()
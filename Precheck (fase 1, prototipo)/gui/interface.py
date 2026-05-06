import customtkinter as ctk
from tkinter import filedialog
from core.scanner import escanear_archivo, escanear_url

class AppPrecheck(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuración básica
        self.title("PreCheck Security - Fase 1")
        self.geometry("600x500")
        ctk.set_appearance_mode("dark")

        # Título principal
        self.label_titulo = ctk.CTkLabel(self, text="PRECHECK SCANNER", font=("Roboto", 24, "bold"))
        self.label_titulo.pack(pady=20)

        #  SECCIÓN DE ARCHIVOS 
        self.frame_file = ctk.CTkFrame(self)
        self.frame_file.pack(pady=10, padx=20, fill="x")
        
        self.btn_select = ctk.CTkButton(self.frame_file, text="Seleccionar Archivo", command=self.abrir_explorador)
        self.btn_select.pack(pady=15)

        #  SECCIÓN DE URLS 
        self.frame_url = ctk.CTkFrame(self)
        self.frame_url.pack(pady=10, padx=20, fill="x")
        
        self.entry_url = ctk.CTkEntry(self.frame_url, placeholder_text="Ingrese URL a analizar (ej: https://...)")
        self.entry_url.pack(pady=10, padx=10, fill="x")
        
        self.btn_url = ctk.CTkButton(self.frame_url, text="Analizar Enlace", fg_color="#2c3e50", command=self.analizar_link)
        self.btn_url.pack(pady=10)

        #  ÁREA DE RESULTADOS 
        self.lbl_resultado = ctk.CTkLabel(self, text="Estado: Esperando acción...", font=("Roboto", 14))
        self.lbl_resultado.pack(pady=30)

    def abrir_explorador(self):
        ruta = filedialog.askopenfilename()
        if ruta:
            res, msg = escanear_archivo(ruta)
            self.actualizar_ui(res, msg)

    def analizar_link(self):
        url = self.entry_url.get()
        if url:
            res, msg = escanear_url(url)
            self.actualizar_ui(res, msg)

    def actualizar_ui(self, tipo, mensaje):
        colores = {"Peligro": "#E74C3C", "Advertencia": "#F39C12", "Seguro": "#2ECC71", "Error": "white"}
        self.lbl_resultado.configure(text=f"[{tipo}] {mensaje}", text_color=colores.get(tipo, "white"))

if __name__ == "__main__":
    app = AppPrecheck()
    app.mainloop()
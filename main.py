import tkinter as tk
from tkinter import messagebox
from logica_monty import JuegoMontyHall

class MontyHallGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Monty Hall")
        self.root.geometry("900x650")
        
        self.juego = None 
        self.botones = []
        
        self.colores = {
            "base": "#ecf0f1",
            "puerta": "#34495e",       # Azul oscuro
            "seleccion": "#f1c40f",    # Amarillo
            "abierta": "#95a5a6",      # Gris
            "ganadora": "#2ecc71",     # Verde
            "perdedora": "#e74c3c",    # Rojo
            "texto": "white"
        }
        
        self.crear_menu_principal()

    def crear_menu_principal(self):
        self.limpiar_ventana()
        frame = tk.Frame(self.root, bg=self.colores["base"])
        frame.pack(expand=True, fill="both")
        
        tk.Label(frame, text="Simulacion Monty Hall", 
                 font=("Helvetica", 28, "bold"), bg=self.colores["base"]).pack(pady=30)
        
        tk.Button(frame, text="3 Puertas", font=("Helvetica", 14), 
                  command=lambda: self.iniciar_interfaz_juego(3)).pack(pady=10)
        
        tk.Button(frame, text="52 Cartas", font=("Helvetica", 14), 
                  command=lambda: self.iniciar_interfaz_juego(52)).pack(pady=10)

    def iniciar_interfaz_juego(self, n):
        self.limpiar_ventana()
        
        self.juego = JuegoMontyHall(n) 

        self.etapa_ui = 1
        self.botones = []
        
        self.lbl_info = tk.Label(self.root, text=f"Elige una opción...", 
                                 font=("Helvetica", 16), bg="#3498db", fg="white", pady=10)
        self.lbl_info.pack(fill=tk.X)
        
        frame_grid = tk.Frame(self.root)
        frame_grid.pack(expand=True, padx=20, pady=20)
        
        cols = 13 if n == 52 else 3
        for i in range(n):
            btn = tk.Button(frame_grid, text=f"{i+1}", font=("Helvetica", 10, "bold"),
                            bg=self.colores["puerta"], fg=self.colores["texto"],
                            width=4 if n == 52 else 10, height=2 if n == 52 else 5,
                            command=lambda idx=i: self.manejar_clic(idx))
            
            btn.grid(row=i//cols, column=i%cols, padx=2, pady=2)
            self.botones.append(btn)
            
        tk.Button(self.root, text="Volver", command=self.crear_menu_principal).pack(pady=10)

    def manejar_clic(self, indice):
        if self.etapa_ui == 1:
            self.juego.seleccionar_puerta_inicial(indice)
            
            self.botones[indice].config(bg=self.colores["seleccion"], fg="black")
            
            abrir, alternativa = self.juego.obtener_puertas_para_abrir()
            
            for p in abrir:
                self.botones[p].config(text="🐐", state="disabled", bg=self.colores["abierta"])
            
            self.lbl_info.config(text=f"¡Opciones descartadas! ¿Cambias a la {alternativa + 1} o te quedas?")
            self.etapa_ui = 2
            
        elif self.etapa_ui == 2:
            if self.botones[indice]['state'] != 'disabled':
                victoria = self.juego.verificar_victoria(indice)
                ganadora_real = self.juego.obtener_ganadora()
                self.mostrar_resultado(indice, victoria, ganadora_real)

    def mostrar_resultado(self, eleccion_final, victoria, ganadora_real):
        for i, btn in enumerate(self.botones):
            if i == ganadora_real:
                btn.config(text="🏆", bg=self.colores["ganadora"])
            elif i == eleccion_final and not victoria:
                btn.config(text="❌", bg=self.colores["perdedora"])
            else:
                btn.config(state="disabled")

        msj = "¡GANASTE!" if victoria else "PERDISTE"
        messagebox.showinfo("Fin del juego", f"{msj}\nEl premio estaba en la {ganadora_real + 1}")
        self.crear_menu_principal()

    def limpiar_ventana(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = MontyHallGUI(root)
    root.mainloop()
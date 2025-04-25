import tkinter as tk

from ActivitiesController import ActivitiesController

#-----------------------------------------------------------------------------#
# Main 
#-----------------------------------------------------------------------------#
def main():
    root = tk.Tk()
    root.title("Activities Application")
    root.geometry("1280x720")  # Redimensionando a janela para 1280x720
    app = ActivitiesController(root)  # Página inicial agora é Activities
    root.mainloop()

if __name__ == "__main__":
    main()

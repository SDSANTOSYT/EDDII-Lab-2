import customtkinter as ctk


class App:

    def __init__(self) -> None:
        root= ctk.CTk() 
        root.geometry("1200x800")
        root.title("FligthScanner")
        root.mainloop()

DebugApp=App()
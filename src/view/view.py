import customtkinter as ctk


class App:

    def __init__(self) -> None:
        root= ctk.CTk() 
        root.geometry("1200x800")
        root.title("FligthScanner")
        #Cuadros principales
        frame1=ctk.CTkFrame(root, 580, 780,fg_color='#f6b6a8')
        frame1.place(x=10,y=10)
        frame2=ctk.CTkFrame(root, 580, 780,fg_color='#f6b6a8')
        frame2.place(x=610,y=10)
        #Componentes del cuadro 1
        isConexLbl=ctk.CTkLabel(frame1,text='No es conexo',font=('Nunito',30),text_color='#000000')
        isConexLbl.place(relx=0.5,y=20,anchor='center')
        numberOfComponentsLbl=ctk.CTkLabel(frame1,text='Tiene 7 Componentes',font=('Nunito',30),text_color='#000000')
        numberOfComponentsLbl.place(relx=0.5,y=80,anchor='center')
        #Componentes del cuadro 2




        root.mainloop()
#Cuadros de las componentes  
class GraphCompontensInfo(ctk.CTkFrame):
    def __init__(self,nVertices,minimunExpansionTreeWeight,componentNumbe,master) -> None:
        self.config(master=master,width=275,height=300)






DebugApp=App()
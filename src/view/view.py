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
class GraphComponentsInfo(ctk.CTkFrame):
    def __init__(self, nVertices, minimumExpansionTreeWeight, componentNumber, master=None, **kwargs):
        # Llamada al constructor de la clase padre
        super().__init__(master, width=275, height=300, fg_color='#f6b6a8',**kwargs)

        componentNumberLbl=ctk.CTkLabel(master=self,text=componentNumber, font=('Nunito',30),text_color='#000000').place(relx=0.5, y=20, anchor='center')
        nVerticesLbl=ctk.CTkLabel(master=self,text=nVertices, font=('Nunito',30),text_color='#000000').place(relx=0.5, y=60, anchor='center')
        minimumExpansionTreeWeightLbl=ctk.CTkLabel(master=self, text=minimumExpansionTreeWeight, font=('Nunito',30),text_color='#000000').place(relx=0.5,y=100,anchor='center')
class minimumPathsAirports(ctk.CTkFrame):
    def __init__(self, airportCode, airportName, airportCity, airportCountry, airportLatitude,airportlongitude, master=None, **kwargs):
        # Llamada al constructor de la clase padre
        super().__init__(master, width=275, height=300, fg_color='#f6b6a8',**kwargs)
        airportCodeLbl=ct
        airportNameLbl=1
        airportCityLbl=1
        airportCountryLbl=1
        airportLatitude=1
        airportlongitude=1




#prueba del frame 
ruta= ctk.CTk()
ruta.geometry("500x500")
ruta.title("Prueba")
cuadro=GraphComponentsInfo(nVertices=1,minimumExpansionTreeWeight=2,componentNumber=3,master=ruta)
cuadro.place(x=10,y=10)
ruta.mainloop()

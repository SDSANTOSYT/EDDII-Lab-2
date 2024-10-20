import customtkinter as ctk
ctk.set_appearance_mode("light")


class App:

    def __init__(self) -> None:
        root= ctk.CTk() 
        root.geometry("1200x800")
        root.title("FligthScanner")
        #Cuadros principales
        frame1=ctk.CTkFrame(root, 580, 780,fg_color='#d4e6f1')
        frame1.place(x=10,y=10)
        frame2=ctk.CTkFrame(root, 580, 780,fg_color='#d4e6f1')
        frame2.place(x=610,y=10)
        #Componentes del cuadro 1
        isConexLbl=ctk.CTkLabel(frame1,text='No es conexo',font=('Nunito',30),text_color='#000000')
        isConexLbl.place(relx=0.5,y=20,anchor='center')

        numberOfComponentsLbl=ctk.CTkLabel(frame1,text='Tiene 7 Componentes',font=('Nunito',30),text_color='#000000')
        numberOfComponentsLbl.place(relx=0.5,y=80,anchor='center')

        infoComponent=ctk.CTkScrollableFrame(master=frame1,width=580,height=320,fg_color='#ffffff',orientation='horizontal',scrollbar_fg_color='#e3e3e3')
        infoComponent.place(x=0,y=120)
        self.fillIComponentFrame(infoComponent)

        #Componentes del cuadro 2

 










        root.mainloop()

    def fillIComponentFrame(self,master):
        for i in range(1,8):
            GraphComponentsInfo(nVertices=1,minimumExpansionTreeWeight=2,componentNumber=i,master=master).pack(side=ctk.LEFT, padx=10)





        
#Cuadros de las componentes  
class GraphComponentsInfo(ctk.CTkFrame):
    def __init__(self, nVertices, minimumExpansionTreeWeight, componentNumber, master=None, **kwargs):
        # Llamada al constructor de la clase padre
        super().__init__(master, width=275, height=300, fg_color='#ebf5fb',**kwargs)

        componentNumberLbl=ctk.CTkLabel(master=self,text=componentNumber, font=('Nunito',30),text_color='#000000').place(relx=0.5, y=20, anchor='center')
        nVerticesLbl=ctk.CTkLabel(master=self,text=nVertices, font=('Nunito',30),text_color='#000000').place(relx=0.5, y=60, anchor='center')
        minimumExpansionTreeWeightLbl=ctk.CTkLabel(master=self, text=minimumExpansionTreeWeight, font=('Nunito',30),text_color='#000000').place(relx=0.5,y=100,anchor='center')


class minimumPathsAirports(ctk.CTkFrame):
    def __init__(self, airportCode, airportName, airportCity, airportCountry, airportLatitude,airportlongitude, master=None, **kwargs):
        # Llamada al constructor de la clase padre
        super().__init__(master, width=275, height=300, fg_color='#ebf5fb',**kwargs)
        airportCodeLbl=ctk.CTkLabel(master=self,text=airportCode,font=('Nunito',30),text_color='#000000').place(relx=0.5, y=20, anchor='center')
        airportNameLbl=ctk.CTkLabel(master=self,text=airportName,font=('Nunito',30),text_color='#000000').place(relx=0.5, y=60, anchor='center')
        airportCityLbl=ctk.CTkLabel(master=self,text=airportCity,font=('Nunito',30),text_color='#000000').place(relx=0.5, y=100, anchor='center')
        airportCountryLbl=ctk.CTkLabel(master=self,text=airportCountry,font=('Nunito',30),text_color='#000000').place(relx=0.5, y=140, anchor='center')
        airportLatitudeLbl=ctk.CTkLabel(master=self,text=airportLatitude,font=('Nunito',30),text_color='#000000').place(relx=0.5, y=180, anchor='center')
        airportlongitudeLbl=ctk.CTkLabel(master=self,text=airportlongitude,font=('Nunito',30),text_color='#000000').place(relx=0.5, y=220, anchor='center')




""""#prueba del frame 
ruta= ctk.CTk()
ruta.geometry("500x500")
ruta.title("Prueba")
cuadro=minimumPathsAirports(master=ruta,airportCode=1,airportCity='Barranquilla',airportCountry='Colombia',airportName='Ernesto',airportLatitude=11,airportlongitude=22)
#GraphComponentsInfo(nVertices=1,minimumExpansionTreeWeight=2,componentNumber=3,master=ruta)
cuadro.place(x=10,y=10)
ruta.mainloop()"""

debug=App()

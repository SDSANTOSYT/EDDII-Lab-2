import customtkinter as ctk
import folium.map, folium.plugins.marker_cluster
from controller.dataset_manager import grafo, arbol
ctk.set_appearance_mode("light")
import folium 
import webbrowser
import os


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
        seeMapBtn=ctk.CTkButton(master=frame1,text='Ver Mapa',command=lambda: self.createMap())
        seeMapBtn.place(relx=0.5,y=540,anchor='center')

        #Componentes del cuadro 2
        #Frames del cuadro 2
        frame2Up=ctk.CTkFrame(master=frame2, width=560,height=520,fg_color='#ffffff')
        frame2Up.place(x=10,y=10)
        frame2down=ctk.CTkFrame(master=frame2, width=560,height=225,fg_color='#ffffff')
        frame2down.place(x=10,y=540)

        #Componentes del cuadro superior 2
        AirportCode=ctk.CTkEntry(master=frame2Up,placeholder_text='Codigo del aeropuerto',width=150)
        AirportCode.place(relx=0.5,y=30,anchor='center')
        searchBtn1=ctk.CTkButton(master=frame2Up,text='Buscar',command=lambda: self.search(airportname=airportInfNameoLbl,airporCity=airportInfCityLbl,airportCountry=airportInfCountryLbl, airportLatitude=airportInfLatitudeLbl, airpotLongitude=airportInfLongitudeLbl,airportcode=AirportCode,masterused=infoAirports))
        searchBtn1.place(relx=0.8,anchor='center',y=30)

        airportInfNameoLbl=ctk.CTkLabel(frame2Up,text='Nombre',font=('Nunito',15),text_color='#000000')
        airportInfNameoLbl.place(relx=0.05,y=70)

        airportInfCityLbl=ctk.CTkLabel(frame2Up,text='Ciudad',font=('Nunito',15),text_color='#000000')
        airportInfCityLbl.place(relx=0.05,y=95)

        airportInfCountryLbl=ctk.CTkLabel(frame2Up,text='Pais',font=('Nunito',15),text_color='#000000')
        airportInfCountryLbl.place(relx=0.05,y=125)

        airportInfLatitudeLbl=ctk.CTkLabel(frame2Up,text='Latitud',font=('Nunito',15),text_color='#000000')
        airportInfLatitudeLbl.place(relx=0.65,y=70)

        airportInfLongitudeLbl=ctk.CTkLabel(frame2Up,text='Longitud',font=('Nunito',15),text_color='#000000')
        airportInfLongitudeLbl.place(relx=0.65,y=95)

        infoAirports=ctk.CTkScrollableFrame(width=560, master=frame2Up,height=320,fg_color='#ffffff',orientation='horizontal',scrollbar_fg_color='#e3e3e3')
        infoAirports.place(x=0,y=160)


        #componentes del cuadro inferior 2
        AirportCode2=ctk.CTkEntry(master=frame2down,placeholder_text='Codigo del aeropuerto',width=150)
        AirportCode2.place(relx=0.5,y=30,anchor='center')
        searchBtn2=ctk.CTkButton(master=frame2down,text='Buscar',command=lambda: self.search2(airportname=airportInfNameoLbl2,airporCity=airportInfCityLbl2,airportCountry=airportInfCountryLbl2, airportLatitude=airportInfLatitudeLbl2, airpotLongitude=airportInfLongitudeLbl2,airportcode=AirportCode2, airportcode2=AirportCode))
        searchBtn2.place(relx=0.8,anchor='center',y=30)

        airportInfNameoLbl2=ctk.CTkLabel(frame2down,text='Nombre',font=('Nunito',15),text_color='#000000')
        airportInfNameoLbl2.place(relx=0.05,y=70)

        airportInfCityLbl2=ctk.CTkLabel(frame2down,text='Ciudad',font=('Nunito',15),text_color='#000000')
        airportInfCityLbl2.place(relx=0.05,y=95)

        airportInfCountryLbl2=ctk.CTkLabel(frame2down,text='Pais',font=('Nunito',15),text_color='#000000')
        airportInfCountryLbl2.place(relx=0.05,y=125)

        airportInfLatitudeLbl2=ctk.CTkLabel(frame2down,text='Latitud',font=('Nunito',15),text_color='#000000')
        airportInfLatitudeLbl2.place(relx=0.65,y=70)

        airportInfLongitudeLbl2=ctk.CTkLabel(frame2down,text='Longitud',font=('Nunito',15),text_color='#000000')
        airportInfLongitudeLbl2.place(relx=0.65,y=95)

        






 










        root.mainloop()
    def search(self, airportcode: ctk.CTkEntry, airportname: ctk.CTkLabel, airporCity:ctk.CTkLabel, airportCountry: ctk.CTkLabel, airportLatitude: ctk.CTkLabel, airpotLongitude:ctk.CTkLabel, masterused: ctk.CTkScrollableFrame=None):
        code=airportcode.get()
        airportname.configure(text=f"Nombre: {grafo.airports[code].name}")
        airporCity.configure(text=f"Ciudad: {grafo.airports[code].city}")
        airportCountry.configure(text=f"País: {grafo.airports[code].country}")
        airpotLongitude.configure(text=f"Longitud: {grafo.airports[code].longitude}")
        airportLatitude.configure(text=f"Latitud: {grafo.airports[code].latitude}")
        if masterused != None:
            self.fillAirportsFrame(master=masterused, airportCode=code)

    def search2(self, airportcode: ctk.CTkEntry, airportname: ctk.CTkLabel, airporCity:ctk.CTkLabel, airportCountry: ctk.CTkLabel, airportLatitude: ctk.CTkLabel, airpotLongitude:ctk.CTkLabel, airportcode2: ctk.CTkEntry,masterused: ctk.CTkScrollableFrame=None):
        code=airportcode.get()
        airportname.configure(text=f"Nombre: {grafo.airports[code].name}")
        airporCity.configure(text=f"Ciudad: {grafo.airports[code].city}")
        airportCountry.configure(text=f"País: {grafo.airports[code].country}")
        airpotLongitude.configure(text=f"Longitud: {grafo.airports[code].longitude}")
        airportLatitude.configure(text=f"Latitud: {grafo.airports[code].latitude}")
        if masterused != None:
            self.fillAirportsFrame(master=masterused, airportCode=code)
        self.createMap(airportcode,airportcode2,False)

    def fillIComponentFrame(self,master):
        for component in arbol[0].keys() :
            GraphComponentsInfo(nVertices=arbol[0][component][0],minimumExpansionTreeWeight=arbol[0][component][1],componentNumber=component,master=master).pack(side=ctk.LEFT, padx=10)
    def fillAirportsFrame(self,master,airportCode):
        for widget in master.winfo_children():
            widget.destroy()
        listOfMaxMinAirports=grafo.tails(airportCode)
        for MaxMinAirports in listOfMaxMinAirports :
           maximunPathsAirports(airportCode=MaxMinAirports[0],airportName=grafo.airports[MaxMinAirports[0]].name,airportCity=grafo.airports[MaxMinAirports[0]].city,airportCountry=grafo.airports[MaxMinAirports[0]].country,airportLatitude=grafo.airports[MaxMinAirports[0]].latitude,airportlongitude=grafo.airports[MaxMinAirports[0]].longitude,minDistance=MaxMinAirports[1],master=master).pack(side=ctk.LEFT, padx=10)
    def createMap(self, code1:ctk.CTkEntry = None, code2: ctk.CTkEntry = None,wich = True):
        m=folium.Map(min_zoom=1)
        if wich:
            self.addPoints(m)
        else:
            self.addMinimunPath(m,code1.get(),code2.get())
        m.save('mapa.html')
        webbrowser.open(f"file://{os.path.abspath('mapa.html')}")
    
    def addPoints(self, map: folium.map):
        marker_cluster = folium.plugins.MarkerCluster().add_to(map)
        for airport in grafo.airports.values():
            folium.Marker(location=[airport.latitude,airport.longitude],popup=folium.Popup(str(f"Codigo: {airport.code} <br> Nombre: {airport.name}<br> Ciudad: {airport.city}<br> Pais: {airport.country}<br> Longitud: {airport.longitude}<br> Latitud: {airport.latitude}"),False,200), icon=folium.Icon(icon='plane', prefix='fa', color='blue')).add_to(marker_cluster)
    def addMinimunPath(self, map, vertexBegin,vertexEnd):
        d, p = grafo.dijktra(vertexBegin)
        path = grafo.path(vertexBegin,vertexEnd)
        path_coordinates = [(grafo.airports[aiport].latitude,grafo.airports[aiport].longitude)for aiport in path]
        folium.PolyLine(path_coordinates,tooltip=f"{round(d[vertexEnd],2)}Km").add_to(map)
        for airport in path:
            folium.Marker(location=[grafo.airports[airport].latitude,grafo.airports[airport].longitude],popup=folium.Popup(str(f"Codigo: {grafo.airports[airport].code}<br> Nombre: {grafo.airports[airport].name}<br> Ciudad: {grafo.airports[airport].city}<br> Pais: {grafo.airports[airport].country}<br> Longitud: {grafo.airports[airport].longitude}<br> Latitud: {grafo.airports[airport].latitude}"),False,200), icon=folium.Icon(icon='plane', prefix='fa', color='blue')).add_to(map)

        

        





        
#Cuadros de las componentes  
class GraphComponentsInfo(ctk.CTkFrame):
    def __init__(self, nVertices, minimumExpansionTreeWeight, componentNumber, master=None, **kwargs):
        # Llamada al constructor de la clase padre
        super().__init__(master, width=275, height=300, fg_color='#ebf5fb',**kwargs)

        componentNumberLbl=ctk.CTkLabel(master=self,text=f"inicio: {componentNumber}", font=('Nunito',15),text_color='#000000').place(relx=0.5, y=20, anchor='center')
        nVerticesLbl=ctk.CTkLabel(master=self,text=f"vertices: {nVertices}", font=('Nunito',15),text_color='#000000').place(relx=0.5, y=60, anchor='center')
        minimumExpansionTreeWeightLbl=ctk.CTkLabel(master=self, text=f"peso: {minimumExpansionTreeWeight}Km", font=('Nunito',15),text_color='#000000').place(relx=0.5,y=100,anchor='center')


class maximunPathsAirports(ctk.CTkFrame):
    def __init__(self, airportCode, airportName, minDistance, airportCity, airportCountry, airportLatitude,airportlongitude, master=None, **kwargs):
        # Llamada al constructor de la clase padre
        super().__init__(master, width=275, height=300, fg_color='#ebf5fb',**kwargs)
        airportCodeLbl=ctk.CTkLabel(master=self,text=airportCode,font=('Nunito',15),text_color='#000000').place(relx=0.5, y=20, anchor='center')
        airportNameLbl=ctk.CTkLabel(master=self,text=airportName,font=('Nunito',15),text_color='#000000').place(relx=0.5, y=60, anchor='center')
        airportCityLbl=ctk.CTkLabel(master=self,text=airportCity,font=('Nunito',15),text_color='#000000').place(relx=0.5, y=100, anchor='center')
        airportCountryLbl=ctk.CTkLabel(master=self,text=airportCountry,font=('Nunito',15),text_color='#000000').place(relx=0.5, y=140, anchor='center')
        airportLatitudeLbl=ctk.CTkLabel(master=self,text=airportLatitude,font=('Nunito',15),text_color='#000000').place(relx=0.5, y=180, anchor='center')
        airportlongitudeLbl=ctk.CTkLabel(master=self,text=airportlongitude,font=('Nunito',15),text_color='#000000').place(relx=0.5, y=220, anchor='center')
        minDistanceLbl=ctk.CTkLabel(master=self,text=minDistance,font=('Nunito',15),text_color='#000000').place(relx=0.5, y=260, anchor='center')




""""#prueba del frame 
ruta= ctk.CTk()
ruta.geometry("500x500")
ruta.title("Prueba")
cuadro=minimumPathsAirports(master=ruta,airportCode=1,airportCity='Barranquilla',airportCountry='Colombia',airportName='Ernesto',airportLatitude=11,airportlongitude=22)
#GraphComponentsInfo(nVertices=1,minimumExpansionTreeWeight=2,componentNumber=3,master=ruta)
cuadro.place(x=10,y=10)
ruta.mainloop()"""



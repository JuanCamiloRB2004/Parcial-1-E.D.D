class datos():
    def __init__(self):
        self.diccionario0 = {}
        self.diccionario1 = {}
        self.lista = []
        self.diccionario2 = {}
        self.lista2= []
        self.lista3 = []
        self.diccionario3 = {}
    
    
    def llenarDatos(self):
        print('ingresa 3 series por favor')
        contador = 0
        while contador <= 2:
            serie = str(input('serie: '))
            while True:
                try:
                    numero_temporadas = int(input('number seasons: '))
                    break
                except: 
                    print('number pls ')
            lenguaje_original = str(input('original lenguaje: '))
            ###################
            print('feature seasons')
            while True:
                try:
                    numero_de_temporada = int(input('season number: '))
                    break
                except:
                    print('number pls')
            nombre_temporada =  str(input('season name: '))
            fecha = str(input('premier date: '))
            print('ingresa solo 3 actores por favor')
            actor1 = str(input('ingrese nombre del primer actor: '))
            actor2 = str(input('ingrese nombre del segudo actor: '))
            actor3 = str(input('ingrese nombre del tercer actor: '))
            ####################
            print('episodes')
            nombre_episodio = str(input('episode name: '))
            while True:
                try:
                    duracion = int(input('duration: '))
                    break
                except:
                    print('number pls')
                    
            self.diccionario1["serie"] = serie
            self.diccionario1["number_season"] = numero_temporadas
            self.diccionario1["original_lenguaje"] = lenguaje_original
            
            self.diccionario2["season_number"] = numero_de_temporada
            self.diccionario2["season_name"] = nombre_temporada
            self.diccionario2["premier_date"] = fecha
            self.lista2.append(actor1)
            self.lista2.append(actor2)
            self.lista2.append(actor3)
            self.diccionario2["cast"] = self.lista2
            
            self.diccionario3["episode_name"] = nombre_episodio
            self.diccionario3["time_duration"] = duracion
            self.lista3.append(self.diccionario3)
            
            self.diccionario2["episodes"] = self.lista3
            self.lista.append(self.diccionario2)
            
            self.diccionario1["features_seasons"] = self.lista
            
            self.diccionario0["serie"+str(contador)] = self.diccionario1
            contador+=1
            
    def buscarActor(self):
        actor_a_buscar = str(input('ingrese el nombre de actor a buscar: '))
        resultado = []
        arr = []
        contador1 = 0
        while contador1 <= len(self.diccionario0):
            contador2 = 0
            while contador2 <= 2:
                arr.append(self.diccionario0["serie"+str(contador1)]["features_seasons"][0]["cast"][contador2])
                contador2 += 1
            if actor_a_buscar in arr:
                resultado.append(self.diccionario0["serie"+str(contador1)]["serie"])
            contador1 += 1
        return resultado    

    def buscarPorLenguajeOriginal(self):
        lenguaje = str(input('ingrese el lenguaje para ver todas las series con este'))
        resultado = []
        contador1 = 0
        while contador1 <= len(self.diccionario0):
            arr = self.diccionario0["serie"+str(contador1)]["original_lenguaje"]
            if arr == lenguaje:
                resultado.append(self.diccionario0["serie"+str(contador1)]["serie"])
            contador1 += 1
        return resultado
    
    def eliminarSeriePorPremierDate(self):
        fecha = str(input('ingrese fecha de estreno'))
        contador1 = 0
        while contador1 <= len(self.diccionario0):
            arr = self.diccionario0["serie"+str(contador1)]["features_seasons"][0]["premier_date"]
            if arr == fecha:
                self.diccionario0["serie"+str(contador1)] = "eliminado"
            contador1 += 1
    
            
            
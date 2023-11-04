from DoubleList import DoubleList
class SongCollection():

    def __init__(self):
        self.__songs= DoubleList()
        
    def get(self):
        return self.__songs

    def add(self, s):
        self.__songs.addFirst(s) #Funciona

    def find(self, name): #Funciona
        temp = self.__songs.first()
        while temp != None and temp.data.name != name:
            temp = temp.next

        if temp == None:
            return None
        else:
            return temp #Si quito el data, me da el espacion en memoria

    # Método que intenta eliminar una canción de la lista songs, si la elimina, debe ir a la lista de canciones de cada usuario y eliminarla de ahí también
    def remove(self, name, userCollection):
        temp = self.find(name)
        print("song", temp)
        
        if temp is not None:
            self.__songs.remove(temp)

            #* Eliminar la canción de la lista de canciones de cada usuario
            # users = userCollection.get()
            temp = userCollection.get().first()
            while temp != None:                
                user = userCollection.find(temp.data.username)
                user = user.data
                #? Verificar si el usuario tiene esa cancion
                if user.findSong(name) != None:
                    print("entró")
                    user.removeSong(name)
                else:              
                    print("jmm") #!ESTÁ ENTRANDO NONE
                # print(user.playList())                
                
                # temp.data.removeSong(name)
                temp = temp.next
            
            return temp
        else:
            return None

    def play(self): #Funciona
        temp= self.__songs.first()
        while temp!=None:
            print(temp.data)
            temp= temp.next
from DoubleList import DoubleList
class UserCollection():

    def __init__(self):
        self.__users= DoubleList()

    @property
    def user(self):
        return self.__users
    
    def get(self):
        return self.__users

    def add(self, u):
        self.__users.addFirst(u)

    def find(self, username):
        temp = self.__users.first()
        while temp != None and temp.data.username != username:
            temp = temp.next

        if temp == None:
            return None
        else:
            return temp

    def remove(self, username):
        temp = self.find(username)
        if temp is not None:
            self.__users.remove(temp)
            return temp # Este retorno no puede tener un .data porque debe retornar el nodo doble
        else:
            print('Usuario no existe')

    def print(self):
        temp= self.__users.first()
        while temp!=None:
            print(temp.data)
            temp= temp.next

    # Método que agrega una canción a la lista de canciones de un usuario, antes de agregarla verifica que la canción exista en la colección de canciones
    # y que el usuario exista en la colección de usuarios

    def addUserSong(self, username, songname, songList):
        temp = self.__users.first()
        while temp is not None:
            if temp.data.username == username:
                song = songList.find(songname)
                if song is not None:
                    temp.data.addSong(song)
                    return temp.data  # Devuelve el usuario encontrado
                else:
                    print("La canción no existe")
                    return None  # La canción no existe
            temp = temp.next
        print("El usuario no existe")
        return None  # El usuario no existe

    # Método que reproduce la lista de canciones de un usuario, antes de reproducir verifica que el usuario exista en la colección de usuarios
    # def playUserList(self, username):
    #     temp = self.__users.first()
    #     while temp is not None:
    #         if temp.data.username == username:
    #             # Reproduzco la playlist del usuario
                
    #             print(temp.data.playList()) #! No deja usar playList
    #             break
    #         temp = temp.next
    #     else:
    #         print("El usuario no existe")

    def playUserList(self, username):
        temp = self.__users.first()
        while temp is not None:
            if temp.data.username == username:
                # Check if temp.data has method 'playList'
                if hasattr(temp.data, 'playList'):
                    print("si")
                    # Call the 'playList' method
                    print(temp.data.playList())
                    break
                else:
                    print("El usuario no tiene una playlist")
                    break
            temp = temp.next
        else:
            print("El usuario no existe")


    



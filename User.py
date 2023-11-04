from DoubleList import DoubleList
class User():

    def __init__(self, username):
        self.__username= username
        self.__userSongList= DoubleList()

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, u):
        self.__username =u

    def addSong(self, s):
        self.__userSongList.addFirst(s)

    # def findSong(self, name):
    #     temp = self.__userSongList.first()
    #     while temp != None:
    #         # Check if temp.data has attribute 'name'
    #         if hasattr(temp.data, 'name'):
    #             if temp.data != name:
    #                 temp = temp.next
    #             else:
    #                 return temp
    #         else:
    #             print("temp.data does not have attribute 'name'")
    #             return None

    #     return None

    def findSong(self, name):
        temp = self.__userSongList.first() # 
        print("En find",temp)
        print("name", name)
        while temp != None and temp != name:
            temp = temp.next

        if temp == None:
            return None
        else:
            return temp

    def removeSong(self, name):
        temp = self.findSong(name)
        if temp != None:
            self.__userSongList.remove(temp)
            return temp.data
        else:
            return None

# Este método reproduce la lista de canciones del usuario
    def playList(self):
        temp= self.__userSongList.first()
        print(".....",temp )
        while temp!=None:
            print("***",temp.data)
            temp= temp.next

    def __str__(self):
        return str(self.__username)
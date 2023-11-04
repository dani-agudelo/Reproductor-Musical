import Song as s
import User as u
import SongCollection as sc
import UserCollection as uc

try:
    # Apertura Archivos
    songs = open("Songs.csv", "r", encoding='latin-1')
    users = open("Users.csv", "r", encoding='latin-1')
    
    # Creación de Objetos SongCollection y UserCollection
    songList=sc.SongCollection()
    userList=uc.UserCollection() # Lista de Usuarios
    
    # Lectura de lineas archivos Songs.csv
    songLine=songs.readline()
    songLine=songs.readline()
    
    while songLine!="":
        data=songLine.split(";")
        # Creando objetos de tipo Song
        song=s.Song(data[0], data[1][:-1], data[2], data[3], int(data[4]))
        songList.add(song)
        songLine=songs.readline()

    # Lectura de lineas archivos Users.csv
    userLine=users.readline()
    userLine=users.readline()
    
    while userLine!="":
        # Creando objetos de tipo User
        user=u.User(userLine[:-1])
        userList.add(user)
        userLine=users.readline()
    
    # Cierre de Archivos
    songs.close()
    users.close()
except Exception as e: 
    print("Error", e)
    


'''print("\n\nLista de Canciones\n")#GOOD
songList.play()'''

'''print("\n\nLista de Usuarios\n")#GOOD
userList.print()

print("\n\nEliminacion de Usuarios\n")
print(userList.remove("Bruise"))
print(userList.remove("Kenny"))'''

'''userList.addUserSong("Lynch", "La bamba", songList)
userList.addUserSong("Lynch", "Jump", songList)
userList.addUserSong("Aspect", "Jump", songList)
userList.addUserSong("Aspect", "Beat It", songList)
userList.addUserSong("Kraken", "Beat It", songList)
userList.addUserSong("Kraken", "Stairway To Heaven", songList)
userList.addUserSong("Psycho", "Hotel California", songList)

print("\n\nAgregando Canciones a Un Usuario Eliminado\n")
userList.addUserSong("Bruise", "Hey Jude", songList)

print("\n\nAgregando Canciones que no Existen\n")
userList.addUserSong("Kraken", "One", songList)

print("\n\nReproduciendo Lista de Canciones de Usuario\n")
#userList.playUserList("Kraken")
#userList.playUserList("Aspect")

print("\n\nEliminando Cancion\n")
songList.remove("Beat It", userList)

print("\n\nReproduciendo Lista de Canciones Luego de Eliminación\n")
userList.playUserList("Kraken")

print("\n\nReproduciendo Lista de Canciones Luego de Eliminación\n")

userList.playUserList("Aspect")
print('--------------------------------------------')
userList.addUserSong("Bender", "Heartbreak Hotel", songList)
userList.addUserSong("Bender", "La bamba", songList)
userList.addUserSong("Bender", "Jump", songList)
userList.addUserSong("Lynch", "Beat It", songList)
userList.addUserSong("Bender", "Stairway To Heaven", songList)
userList.addUserSong("Lynch", "Hotel California", songList)'''

userList.addUserSong("Lynch", "La bamba", songList)
userList.addUserSong("Lynch", "Jump", songList)
userList.addUserSong("Aspect", "Jump", songList)
userList.addUserSong("Aspect", "Beat It", songList)
userList.addUserSong("Kraken", "Beat It", songList)
userList.addUserSong("Kraken", "Stairway To Heaven", songList)
userList.addUserSong("Psycho", "Hotel California", songList)
userList.playUserList('Lynch')
userList.remove('Lynch')
userList.playUserList('Lynch')
songList.remove('La bamba', userList)
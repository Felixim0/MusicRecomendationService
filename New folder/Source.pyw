from tkinter import *
import sqlite3
import webbrowser
root=Tk()                                                                        # Makes Tk window root

sizex = 1000
sizey = 800    
root.wm_geometry("%dx%d" % (sizex, sizey))                                       # Sets the size of window
root.resizable(False, False)

font = ("Times", 16)

connection = sqlite3.connect('./database1.db')
cursor = connection.cursor()
frame= Frame(root)   
def loginScreen(pframe):
    pframe.destroy()
    loginScreenFrame = Frame(root,width=sizex, height=sizey)
    loginScreenFrame.pack()

    centeredFrame = Frame(loginScreenFrame,highlightbackground="Blue", highlightthickness=7)
    centeredFrame.place(relx=.5, rely=.5, anchor="center")

    loginStuffFrame = Frame(centeredFrame)
    loginStuffFrame.grid(row=0,column=0)

    loginLabel = Label(loginStuffFrame,text="Login Screen ★",font=str(font[0] + ", 40"))
    loginLabel.grid(row=0,column=0,columnspan = 2,pady = 50)

    userNameEntry = Entry(loginStuffFrame,font=font,borderwidth=4)
    userNameEntry.grid(row=1,column=1)

    userNameLabel = Label(loginStuffFrame,font=font,text="Username ")
    userNameLabel.grid(row=1,column=0)

    passwordEntry = Entry(loginStuffFrame,font=font,borderwidth=4,show="*")
    passwordEntry.grid(row=2,column=1,pady = 15,padx = 10)

    passwordLabel = Label(loginStuffFrame,font=font,text="Password ")
    passwordLabel.grid(row=2,column=0,pady = 15,padx = 10)

    enterButton = Button(loginStuffFrame,font=str(font[0] + ", 30"),text = "Login", command = lambda: checkLogin(userNameEntry.get(),passwordEntry.get(),loginScreenFrame))
    enterButton.grid(row = 4, column = 0 ,columnspan = 2, pady = 30)

    logoImagePath="./env/logo.gif"
    logoImage=PhotoImage(file=logoImagePath)
    logoLabel= Label(centeredFrame, image=logoImage)
    logoLabel.grid(column=1,row=0)
    root.mainloop()
    
def checkLogin(userName,password,pFrame):
    
    
    query = ("SELECT * FROM users WHERE userName = '" + str(userName) + "' AND password = '" + str(password) + "'")
    cursor.execute(query)
    user = []
    for row in cursor:
        user.append(row[:])
    if len(user) > 1:
        print("2 identical users smh")
    elif len(user) == 0:
        print("user/passwd not found")

    else:
        mainMenu(user[0],pFrame)

#    connection.commit()


def mainMenu(userData,pFrame):
    pFrame.destroy()
    mmFrame = Frame(root,width=sizex, height=sizey)
    mmFrame.pack()

    centeredFrame = Frame(mmFrame,highlightbackground="Blue", highlightthickness=7)
    centeredFrame.place(relx=.5, rely=.5, anchor="center")
    
    titleLabel = Label(centeredFrame,text="★ Main Menu ★",font=str(font[0] + ", 40"))
    titleLabel.grid(row=0,column=0,columnspan = 2,pady = 50)
    
    glassImagePath=".\env\\magGlass.gif"
    glassImage=PhotoImage(file=glassImagePath)
    glassLabel= Label(centeredFrame, image=glassImage)
    glassLabel.grid(column=0,row=1)

    previousRecImagePath=".\env\\previousReceomendationsPic.gif"
    previousRecImage=PhotoImage(file=previousRecImagePath)
    previousRecLabel= Label(centeredFrame, image=previousRecImage)
    previousRecLabel.grid(column=1,row=1)

    findRecomendationButton = Button(centeredFrame,font=font,text="Find A Recomendation",command=lambda:findRecomendation(userData,mmFrame))
    findRecomendationButton.grid(row=2,column=0,pady=10,padx=10)

    previousRecomendationButton = Button(centeredFrame,font=font,text="Find A Previous Recomendation",command=lambda:findPreviousRecomendations(userData,mmFrame))
    previousRecomendationButton.grid(row=2,column=1,padx=10,pady=10)    

    Button(centeredFrame,font=font,text="Logout",command=lambda:loginScreen(mmFrame)).grid(row=3,column=2,padx=10,pady=10)  

    
    root.mainloop()

def findRecomendation(userData,pFrame):
    pFrame.destroy()
    loginScreenFrame = Frame(root,width=sizex, height=sizey)
    loginScreenFrame.pack()

    centeredFrame = Frame(loginScreenFrame,highlightbackground="Blue", highlightthickness=7)
    centeredFrame.place(relx=.5, rely=.5, anchor="center")

    loginStuffFrame = Frame(centeredFrame)
    loginStuffFrame.grid(row=0,column=0)

    loginLabel = Label(loginStuffFrame,text="★Find a recomemndation★",font=str(font[0] + ", 40"))
    loginLabel.grid(row=0,column=0,columnspan = 2,pady = 50)

    userNameEntry = Entry(loginStuffFrame,font=font,borderwidth=4)
    userNameEntry.grid(row=2,column=1)

    userNameLabel = Label(loginStuffFrame,font=font,text="Song Recomendation")
    userNameLabel.grid(row=2,column=0)
    userNameEntry.insert(END,"a song that you like")

    passwordEntry = Entry(loginStuffFrame,font=font,borderwidth=4)
    passwordEntry.grid(row=3,column=1,pady = 15,padx = 10)

    passwordLabel = Label(loginStuffFrame,font=font,text="Artist Recomendation")
    passwordLabel.grid(row=3,column=0,pady = 15,padx = 10)

    passwordEntry.insert(END,"An artist you like")

    enterButton = Button(loginStuffFrame,font=str(font[0] + ", 30"),text = "Reccomend", command = lambda: getSongArtist(passwordEntry.get(),userNameEntry.get(),loginScreenFrame,userData))
    enterButton.grid(row = 3, column = 2 , pady = 20 , padx=10)
    
    enterButton2 = Button(loginStuffFrame,font=str(font[0] + ", 30"),text = "Reccomend", command = lambda: getSongSong(passwordEntry.get(),userNameEntry.get(),loginScreenFrame,userData))
    enterButton2.grid(row = 2, column = 2 , pady = 20, padx=10)

    enterButton3 = Button(loginStuffFrame,font=str(font[0] + ", 30"),text = "Logout", command = lambda: loginScreen(loginScreenFrame))
    enterButton3.grid(row = 4, column = 2 , pady = 20, padx=10)    
    Button(loginStuffFrame,font=str(font[0] + ", 30"),text="Main Menu",command=lambda:mainMenu(userData,loginScreenFrame)).grid(row=5,column=2,padx=10,pady=10)
    
def getSongArtist(artistName,songName,pFrame,userData):
    pFrame.destroy()
    loginScreenFrame = Frame(root,width=sizex, height=sizey)
    loginScreenFrame.pack()
    centeredFrame = Frame(loginScreenFrame,highlightbackground="Blue", highlightthickness=7)
    centeredFrame.place(relx=.5, rely=.5, anchor="center")

    loginStuffFrame = Frame(centeredFrame)
    loginStuffFrame.grid(row=0,column=0)

    loginLabel = Label(loginStuffFrame,text="★Song Recomendations★",font=str(font[0] + ", 40"))
    loginLabel.grid(row=0,column=0,columnspan = 2,pady = 50)
        
    query = ("SELECT * FROM songData WHERE songArtist = '" + str(artistName) + "'")
    cursor.execute(query)
    similarSongs = []
    for row in cursor:
        similarSongs.append(row) #Get the genre of the song
    if len(similarSongs) == 0:
        similarSongs = "No Results Found"
    else:
        query = ("SELECT * FROM userSearchHistory WHERE userID = '" + str(userData[0]) + "' AND userInput = '" + str(artistName) + "' AND type = 'artist'")
        cursor.execute(query)
        results = []
        for row in cursor:
            results.append(row)
        if len(results) == 0:
            query = ("INSERT INTO userSearchHistory (userID, userInput,type) VALUES ('" + str(userData[0]) + "','" + str(artistName) + "','artist');")
            cursor.execute(query)
            connection.commit()
        
    similarSongsListFrame=Frame(centeredFrame,relief=GROOVE,width=200,height=400,bd=3)                 
    similarSongsListFrame.grid(column=0,row=1,rowspan=2,padx=10,pady=10)
    similarSongsCanvas=Canvas(similarSongsListFrame)                                                                              
    frame=Frame(similarSongsCanvas)                     
                                                 
    scrollbar=Scrollbar(similarSongsListFrame,orient="vertical")      
    similarSongsCanvas.configure(yscrollcommand=scrollbar.set)
    scrollbar.config(command=similarSongsCanvas.yview)                    
    scrollbar.pack(side="right",fill="y")                          
    similarSongsCanvas.pack(side="left")                                             
    similarSongsCanvas.create_window((0,0),window=frame,anchor='nw')
    x=0
    frame.bind("<Configure>",lambda x: moveCanvas(similarSongsCanvas))
    moveCanvas(similarSongsCanvas)
    
    frameForButtons = Frame(frame)                                                                                           
    frameForButtons.pack()

    for i in range(0,len(similarSongs)):
        if similarSongs != "No Results Found":
            Button(frameForButtons,text=str((similarSongs[i][1]) + ", by: " + str(similarSongs[i][2])),font=(font),
                  command=lambda i=i:openSong(similarSongs[i]),width=30).grid(row=i,column=1)
        else:
            Label(frameForButtons,text="No Results Found",font=(font[0],int(font[1]*1.5))).grid(row=0,column=0)

    Button(centeredFrame,font=str(font[0] + ", 30"),text = "Logout", command = lambda: loginScreen(loginScreenFrame)).grid(row = 1, column = 2 , pady = 20, padx=10)  
      
    Button(centeredFrame,font=str(font[0] + ", 30"),text="Main Menu",command=lambda:mainMenu(userData,loginScreenFrame)).grid(row=2,column=2,padx=10,pady=10)

    
def getSongSong(artistName,songName,pFrame,userData):
    pFrame.destroy()
    loginScreenFrame = Frame(root,width=sizex, height=sizey)
    loginScreenFrame.pack()
    centeredFrame = Frame(loginScreenFrame,highlightbackground="Blue", highlightthickness=7)
    centeredFrame.place(relx=.5, rely=.5, anchor="center")

    loginStuffFrame = Frame(centeredFrame)
    loginStuffFrame.grid(row=0,column=0)

    loginLabel = Label(loginStuffFrame,text="★Song Recomendations★",font=str(font[0] + ", 40"))
    loginLabel.grid(row=0,column=0,columnspan = 2,pady = 50)

    query = ("SELECT * FROM songData WHERE songName = '" + str(songName) + "'")
    cursor.execute(query)
    genre = []
    for row in cursor:
        genre.append(row[3]) #Get the genre of the song
    if len(genre)>0:
        query = ("SELECT * FROM songData WHERE songGenre = '" + str(genre[0]) + "'")
        cursor.execute(query)
        similarSongs = []
        for row in cursor:
            similarSongs.append(row)

# add history if results found
        query = ("SELECT * FROM userSearchHistory WHERE userID = '" + str(userData[0]) + "' AND userInput = '" + str(songName) + "' AND type = 'song'")
        cursor.execute(query)
        results = []
        for row in cursor:
            results.append(row)
        if len(results) == 0:
            query = ("INSERT INTO userSearchHistory (userID, userInput,type) VALUES ('" + str(userData[0]) + "','" + str(songName) + "','song');")
            cursor.execute(query)
            connection.commit()

            
    else:
        similarSongs= "No Results Found"
        
    similarSongsListFrame=Frame(centeredFrame,relief=GROOVE,width=200,height=400,bd=3)                 
    similarSongsListFrame.grid(column=0,row=1,rowspan=2,padx=10,pady=10)
    similarSongsCanvas=Canvas(similarSongsListFrame)                                                                              
    frame=Frame(similarSongsCanvas)                     
                                                 
    scrollbar=Scrollbar(similarSongsListFrame,orient="vertical")      
    similarSongsCanvas.configure(yscrollcommand=scrollbar.set)
    scrollbar.config(command=similarSongsCanvas.yview)                    
    scrollbar.pack(side="right",fill="y")                          
    similarSongsCanvas.pack(side="left")                                             
    similarSongsCanvas.create_window((0,0),window=frame,anchor='nw')
    x=0
    frame.bind("<Configure>",lambda x: moveCanvas(similarSongsCanvas))
    moveCanvas(similarSongsCanvas)
    
    frameForButtons = Frame(frame)                                                                                           
    frameForButtons.pack()

    for i in range(0,len(similarSongs)):
        if similarSongs != "No Results Found":
            Button(frameForButtons,text=str((similarSongs[i][1]) + ", by: " + str(similarSongs[i][2])),font=(font),
                  command=lambda i=i:openSong(similarSongs[i]),width=30).grid(row=i,column=1)
        else:
            Label(frameForButtons,text="No Results Found",font=(font[0],int(font[1]*1.5))).grid(row=0,column=0)

    Button(centeredFrame,font=str(font[0] + ", 30"),text = "Logout", command = lambda: loginScreen(loginScreenFrame)).grid(row = 1, column = 2 , pady = 20, padx=10)  
      
    Button(centeredFrame,font=str(font[0] + ", 30"),text="Main Menu",command=lambda: mainMenu(userData,loginScreenFrame)).grid(row=2,column=2,padx=10,pady=10)

def findPreviousRecomendations(userData,pFrame):
    pFrame.destroy()
    previousRecFrame = Frame(root,width=sizex, height=sizey)
    previousRecFrame.pack()
    centeredFrame = Frame(previousRecFrame,highlightbackground="Blue", highlightthickness=7)
    centeredFrame.place(relx=.5, rely=.5, anchor="center")

    loginLabel = Label(centeredFrame,text="★Previous Recomendations★",font=str(font[0] + ", 40"))
    loginLabel.grid(row=0,column=0,columnspan = 2,pady = 50)

    query = ("SELECT * FROM userSearchhistory WHERE userID = '" + str(userData[0]) + "' AND type = 'song'")
    cursor.execute(query)
    priorSongRecs = []
    for row in cursor:
        priorSongRecs.append(row[1])
    # [songName]
    temp=[]
    for i in range (0,len(priorSongRecs)):
        query=("SELECT * FROM songData WHERE songName = '" + str(priorSongRecs[i]) + "'")
        cursor.execute(query)
        for row in cursor:
            temp.append(row)
    priorSongRecs = temp[:]
    
    if int(len(priorSongRecs)) == 0:
        (priorSongRecs) = "No Results Found"



    query = ("SELECT * FROM userSearchhistory WHERE userID = '" + str(userData[0]) + "' AND type = 'artist'")
    cursor.execute(query)
    priorArtistRecs = []
    for row in cursor:
        priorArtistRecs.append(row[1])
    # [artistName,]

    temp=[]

    for i in range (0,len(priorArtistRecs)):
        query=("SELECT * FROM songData WHERE songArtist = '" + str(priorArtistRecs[i]) + "'")
        cursor.execute(query)
        for row in cursor:
            temp.append(row)
    priorArtistRecs = temp[:]

    if int(len(priorArtistRecs)) == 0:
        (priorArtistRecs) = "No Results Found"
        
    prevRecSongFrame=Frame(centeredFrame,relief=GROOVE,width=200,height=400,bd=3)                 
    prevRecSongFrame.grid(column=0,row=2,rowspan=2,padx=10,pady=10)
    prevRecSongCanvas=Canvas(prevRecSongFrame)                                                                              
    frame=Frame(prevRecSongCanvas)                     
    Label(centeredFrame,font=font,text="Previous Songs").grid(row=1,column=1)
    
    scrollbar=Scrollbar(prevRecSongFrame,orient="vertical")      
    prevRecSongCanvas.configure(yscrollcommand=scrollbar.set)
    scrollbar.config(command=prevRecSongCanvas.yview)                    
    scrollbar.pack(side="right",fill="y")                          
    prevRecSongCanvas.pack(side="left")                                             
    prevRecSongCanvas.create_window((0,0),window=frame,anchor='nw')
    x=0
    frame.bind("<Configure>",lambda x: moveCanvas(prevRecSongCanvas))
    moveCanvas(prevRecSongCanvas)
    
    frameForButtons = Frame(frame)                                                                                           
    frameForButtons.pack()

    for i in range(0,len(priorSongRecs)):
        if priorSongRecs != "No Results Found":
            Button(frameForButtons,text=str((priorSongRecs[i][1]) + ", by: " + str(priorSongRecs[i][2])),font=(font),
                  command=lambda i=i:openSong(priorSongRecs[i]),width=30).grid(row=i,column=1)
        else:
            Label(frameForButtons,text="No Results Found",font=(font[0],int(font[1]*1.5))).grid(row=0,column=0)
    
#######
#######
    
    prevArtSongFrame=Frame(centeredFrame,relief=GROOVE,width=200,height=400,bd=3)                 
    prevArtSongFrame.grid(column=1,row=2,rowspan=2,padx=10,pady=10)
    prevArtSongCanvas=Canvas(prevArtSongFrame)                                                                              
    frame=Frame(prevArtSongCanvas)
    Label(centeredFrame,font=font,text="Previous Artstist's Songs").grid(row=1,column=0)
                                                 
    scrollbar=Scrollbar(prevArtSongFrame,orient="vertical")      
    prevArtSongCanvas.configure(yscrollcommand=scrollbar.set)
    scrollbar.config(command=prevArtSongCanvas.yview)                    
    scrollbar.pack(side="right",fill="y")                          
    prevArtSongCanvas.pack(side="left")                                             
    prevArtSongCanvas.create_window((0,0),window=frame,anchor='nw')
    x=0
    frame.bind("<Configure>",lambda x: moveCanvas(prevArtSongCanvas))
    moveCanvas(prevArtSongCanvas)
    
    frameForButtons = Frame(frame)                                                                                           
    frameForButtons.pack()
    
    for i in range(0,len(priorArtistRecs)):
        if priorArtistRecs != "No Results Found":
            Button(frameForButtons,text=str((priorArtistRecs[i][1]) + ", by: " + str(priorArtistRecs[i][2])),font=(font),
                  command=lambda i=i:openSong(priorArtistRecs[i]),width=30).grid(row=i,column=1)
        else:
            Label(frameForButtons,text="No Results Found",font=(font[0],int(font[1]*1.5))).grid(row=0,column=0)

    Button(centeredFrame,font=font,text = "Logout", command =
           lambda: loginScreen(previousRecFrame)).grid(row = 4, column = 1 , pady = 20, padx=10)  
      
    Button(centeredFrame,font=font,text="Main Menu",command=
           lambda: mainMenu(userData,previousRecFrame)).grid(row=4,column=0,padx=10,pady=10)
    

def moveCanvas(canvasForButtons):
    canvasForButtons.configure(scrollregion=canvasForButtons.bbox("all"),width=400,height=300)

def openSong(songData):
    webbrowser.open_new(str(songData[4]))

if __name__ == "__main__":
    loginScreen(frame)
    root.mainloop()


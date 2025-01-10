try:
    import myPythonFunctions
    userName=input("donnez votre nom :")
    UserScore=int(myPythonFunctions.getUserPoint(userName))
    NewUser = False
    if UserScore == -1:
        NewUser = True
        UserScore = 0
    userChoice="0"
    while userChoice!="-1":
        score = myPythonFunctions.generateQuestion()
        UserScore += score 
        userChoice = input("Entrez '-1' pour terminer ou bien continuez: ")
    myPythonFunctions.updateUserPoints(NewUser,userName, UserScore)
except ValueError:
     print("Une erreur est survenue. Le programme va se terminer.")
    

#Importation de modules
import random
import os
#la fonction getUserPoint()
def  getUserPoint(UtilisateurName):
    with open('userScores.txt','r')as file:       
      for line in file:
            liste=line.strip().split(',')
      
            if liste[0].strip()==UtilisateurName:
                return int(liste[1].strip())     
    return '-1'
#Utilisateur=input("donnez le nom du l'utilisateur:")
#print(getUserPoint(Utilisateur))

#la fonction updateUserPoints()
def updateUserPoints(newUser,userName,score):
    temp_file_path = 'userScores.tmp'
    if newUser==True:
        with open('userScores.txt','a')as file:
            file.write(userName+','+str(score)+'\n')
    else:   
        with open('userScores.txt', 'r') as file, open(temp_file_path, 'w') as temp_file:
            for line in file:
                liste=line.split(',')
                if liste[0].strip()==userName:
                    temp_file.write(userName + ','+str(score))
                else:
                    temp_file.write(line+'\n')
                    
    if  os.path.exists(temp_file_path):           
       os.remove('userScores.txt')
       os.rename('userScores.tmp', 'userScores.txt')                   
#updateUserPoints(True, "s", 150)            
#updateUserPoints(False, "C", 200)
#Génération des questions
def generateQuestion():
    operand_list=[0,0,0,0,0]
    operator_list=["","","",""]
    operator_dict={1: '+', 2: '-', 3: '*', 4: '**'}
# Mise à jour d’operandList avec des nombres aléatoires
    for i in range(len(operand_list)):
        operand_list[i]=random.randint(1,10)
    print(operand_list)    
#Mise à jour liste operatorList avec des symboles mathématiques
    for i in range(len(operator_list)):
        operator_list[i]=operator_dict[random.randint(1,4)]
        if i > 0 and operator_list[i] == '**' and operator_list[i - 1] == '**':
            while operator_list[i] == '**':
                operator_list[i] = operator_dict[random.randint(1, 4)]
    print(operator_list)
#Générer une expression mathématique
    questionString=""
    for i in range (4):
        questionString+=str(operand_list[i])+""+operator_list[i]
    questionString+=str(operand_list[-1])
#evaluation du resultat
    resultat=eval(questionString)
#interagir avec l'utilisateur
#etape 1
    questionString = questionString.replace("**","^")
    print("question est : ", questionString)
##etape 2
    while True:
        try:
            reponse=int(input("Entrez votre réponse : "))
            if (reponse==resultat):
                print("c'est une bonne reponse")
                score=1
            else:
                print("c'est une mauvaise reponse ! la bonne reponse est :"+str(resultat))
                score=0
            break    
        except ValueError:
            print("Erreur : Veuillez entrer un nombre entier valide.")
    return score       
        
#print(generateQuestion())          
            























        

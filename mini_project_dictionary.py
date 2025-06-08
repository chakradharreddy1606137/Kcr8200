"MINI PROJECT "
# DICTIONARY OF WORDS

dictionary={}
while True:
    print("                            ")
    print("/n Dictionary Management system")
    print("1.  Add a word")
    print("2.  Search for a meaning ")
    print("3.  Display All words")
    print("4.  Update Meaning ")
    print("5.  Delete Word")
    print("6.  EXIT ")
    
    choice=input("Enter your choice:")
    
    if choice=="1":
        word=input("Enter your word :")
        meaning=input("Enter the meaning: ")
        dictionary[word]=[meaning]
        print("word added successfully")
        
    elif choice=="2":
        word=input("Enter your word: ")
        if word in dictionary:
            print(f"word is found the meaning is {dictionary[word]}")
        else:
            print("word not found in the dictionary ={word}")
            
            
    elif choice=="3":
        if dictionary:
            print("Words and their meaning :")
            for word,meaning in dictionary.items():
                print(f"{word}:{meaning}")
        else:
            print("Dictionary is empty.")
    
    
    elif choice=="4":
        word=input("Enter your word:")
        if word in dictionary:#if we found the word in Dict
            new_meaning=input("Enter the new meaning of the word:  ")
            dictionary[word]=[new_meaning]
            print("the meaning is updated succesffuly")
            print(f"Updated meaning {new_meaning}")
            
        else:
            print("the word is not found in the dictionary")
    
    elif choice=="5":
        word=input("Enter your word :")
        if word in dictionary:
            del dictionary[word]
            print("the word is delted successfully")
        else:
            print("the word is not found in the dictionary") \
                
    elif choice=="6":
        print("Exit program....")     
        break      
    
    else:
        print("Its a Invalid option ! please enter a valid option: ")   
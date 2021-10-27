# Nicholas Handberg, Assignment 5, 2/9/2021
# Topics: Map
# Create a English to Hmong translator program


def load_dictionary(filename):                                                      # Defines the load_dictionary() function with parameter 'filename'
    english_list = []                                                               # Creates the empty list 'english_list'
    hmong_list = []                                                                 # Creates the empty list 'hmong_list'
    
    with open(filename, 'r') as f:                                                  # Opens the filename in read mode and stores it in 'f'                                                   
        for line in f:                                                              # For loop to go through each line of the file                                                                  
            (n,h,e) = line.strip().split(",")                                       # Splits each line by spaces and stores them into variables 'n','h', and 'e'                                           
            english_list+=[e]                                                       # Adds variable 'e' to the list 'english_list'                                                      
            hmong_list+=[h]                                                         # Adds variable 'h' to the list 'hmong_list'
    
    
    dictionary = {}                                                                 # Creates the empty dictionary 'dictionary'       
            
    for i in range(0, len(english_list),1):                                         # For loop that loops for the amount of elements in 'english_list'
        dictionary[english_list[i]] = hmong_list[i]                                 # Stores the key as the current element in 'english_list' and the value as the current element in 'hmong_list' into 'dictionary'
            
    return dictionary                                                               # Returns 'dictionary'  
      
    
def main():                                                                         # Defines the main() function
    words_used = []                                                                 # Creates the empty list 'words_used'
    another_translation = 'temp'                                                    # Stores "temp" into 'another_translation' to start the while loop
    while another_translation != 'n':                                               # Creates while loop that continues to loop until 'another_translation' is equal to "n"
        
        sentence = input("Type your English sentence:   ").lower().split()          # Gets the user's input, makes it lowercase, and splits the sentence by spaces. Stores the result into 'sentence'                

        words_used += sentence                                                      # Stores all words the user inputs into the 'words_used' list for future use in finding the word frequency
        
        for i in range(0, len(sentence),1):                                         # For loop that loops for the amount of elements in 'sentence'
            sentence[i] = sentence[i].strip('.,?!')                                 # Strips each element in the sentence of punctuation marks
        
        translate(sentence)                                                         # Calls the translate() function with argument 'sentence'
        
        another_translation = input("Another translation? (Y/N):  ").lower()        # Gets the user's input if they would like the translate another sentence and stores the resulting string in 'another_translation'
        
        while another_translation != 'y' and another_translation != 'n':            # While loop to check if the user has not entered either "Y" or "N" . Asks the user to re-enter their answer
            print("\nInvalid answer. Please answer with 'Y' or 'N'")
            another_translation = input("Another translation? (Y/N):  ").lower()
        print("")                                                                     
            
    print_word_frequency(words_used)                                                # Calls print_word_frequency() function with argument 'words_used' once the while loop breaks 
   
    
def translate(sentence):                                                            # Defines the translate() function with paramater 'sentence'
    filename = 'Hmong.txt'                                                          # Stores the string "Hmong.txt" into the variable 'filename'
    translated_list = []                                                            # Creates the empty list 'translated_list'
    translated_sentence = ""                                                        # Stores an empty string into 'translated_sentence'
    
    
    dictionary = load_dictionary(filename)                                          # Calls the load_dictionary() function with argument 'filename' and stores the return into 'dictionary'
    
    for i in range (0, len(sentence),1):                                            # For loop that will loop for the amount of elements in 'sentence'
        if sentence[i] in dictionary:                                               # If statement to check if the current element of 'sentence' is in 'dictionary'
            translated_list.append(dictionary[sentence[i]])                         # Appends the translated list with the respective value from 'dictionary' given the current element in 'sentence' as the key
        else:                                                                       # Else statement in case the word from the current element of 'sentence' is not a key in 'dictionary'
            translated_list.append('?')                                             # Appends the 'translated_list' with "?" instead to notify that the word is not in the dictionary
            
    for i in range (0, len(translated_list),1):                                     # For loop that will loop for the amount of elements in 'translated_list'
        translated_sentence += translated_list[i] + " "                             # Adds the respective elements in the list 'translated_list' to the string 'translated_sentence' with spaces in between
        
    print(f"\nHmong:  {translated_sentence}\n")                                     # Prints the translated sentence to the user
            
       
def print_word_frequency(words_used):                                               # Defines the function print_word_frequency() with parameter 'words_used'
    word_count = {}                                                                 # Creates the empty list 'word_count'                                               
    
    for word in words_used:                                                         # For loop that will loop for each element in 'word_used' and stores the respective element in 'word'                                        
        
        if word not in word_count:                                                  # If statement to check if the string stored in 'word' is not in the dictionary 'word_count'                           
            word_count[word] = 1                                                    # Stores the key 'word' in the dictionary and assigns it a value of 1
        else:                                                                       # Else statement in case the string stored in 'word' is already a key within the dictionary 'word_count'                                
            word_count[word] += 1                                                   # Increase the respective key's value by 1 in the dictionary 'word_count'
            
    print("\nWord\t\t Frequency\n-----------------------------")                    # Prints titles for the data that will be printed                              
    for word, word_count in word_count.items():                                     # For loop that will loop for the amount of items within the dictionary                 
        
        print(word, "\t\t", word_count)                                             # Prints the respective key and value within the dictionary to the user's display


main()                                                                              # Calls the main() function
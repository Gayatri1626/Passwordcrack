import hashlib

#reading the dictionary file with functiion read_dictionary
def read_dictionary(dictionary): 
    
    with open("C:/Users/shree/Documents/dictionary.txt",'r') as file:  #open the txt file in read mode
        
        return [line.strip() for line in file]  #strip function eliminates the spaces in between letters and words

#hash_password function converts the password into a hash value    
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

#Checks for the password hash value if matches with the words in the dictionary file
def crack_password(target_hash,dictionary):
    for word in dictionary:
        hashed_word=hash_password(word)
        if hashed_word == target_hash:
            return word
    return None

if __name__== "__main__":
    target_hash = "604b736ebf9a8ac8caab888b3f94a8a5ed0b85674a9b14e51fa9f426edb19670"

    dictionary_file = "C:/Users/shree/Documents/dictionary.txt"

    dictionary = read_dictionary(dictionary_file)

    cracked_password = crack_password(target_hash,dictionary)

    if cracked_password:
        print("password has been cracked,Password is:",cracked_password)
    else:
        print("Password not found in the dictionary")

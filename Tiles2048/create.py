#############################################
##### Edited by: Sam Spearman (sjs0048) #####
######  Today's date: March 11, 2021   ######
#############################################
import random
import hashlib

def _create(userParms):
    ####################################
    ##initialization of the game board##
    ####################################
    initial = '0000000000000000'                                #initialized to all 0's
    locOne = random.randint(0, 15)                              #determine one random location for '2' placement
    locTwo = random.randint(0, 15)                              #determine second random location for '2' placement
    
    while locOne == locTwo:                                     #must continually generate a new random number
        locTwo = random.randint(0,15)                           #until the locations are not the same
           
    translation = list(initial)                                 #convert initial board to a list for insertion of 2's
    translation[locOne] = '2'                                   #insert first 2
    translation[locTwo] = '2'                                   #insert second 2
    grid = ''.join(translation)                                 #convert list back into a string 
    
    ####################################
    ### Initialization of the score ####
    ####################################
    score = 0                                                   #score is supposed to be zero
    
    
    ####################################
    ### Creation of the SHA256 Hash ####
    ####################################
    encoded = (grid + '.' + str(score)).encode()                #concatenates grid and score as str with a '.' between them. Then encodes it
    integrity = hashlib.sha256(encoded).hexdigest().upper()     #changes the above encoded str into a hashed string with uppercase letters
    
    ####################################
    ###Creation of the status key-pair##
    ####################################
    status = 'ok'
    
    ####################################
    ####Create a dictionary and add#####
    ###all previous vars as key-pairs###
    ####################################  
    result = {'grid': grid, 'score': score, 'integrity': integrity, 'status': status}
    
    ####################################
    ###return the created dictionary####
    ####################################
    
    return result

############################################
##### Edited by Sam Spearman (sjs0048) #####
######  Today's Date: April 3, 2021   ######
############################################
import random
import hashlib

def _shift(userParms):
    ###############################################
    ###Basic conditionals to make sure the grid####
    ####  cannot be a size that should be, in  ####
    ###        theory, impossible              ####
    ###############################################
    
    if 'direction' not in userParms:
        print("Please specify a direction that you want to shift")
        return 
    
    
    result = stringIntoList(userParms['grid'])
    
    if len(result) < 16:
        errorMes = "Error: This grid is too small. Please check the input string."
        return errorMes
    elif len(result) > 16:
        errorMes = "Error: This grid is too large. Please check the input string."
        return errorMes
    
    gameboard = create2DList(result)
    
    return gameboard


        ####################################################################################################
        ####################################################################################################
        #####Below this comment are some of if not all of the functions that are used in the above code#####
        ####################################################################################################
        ####################################################################################################
    
###############################################
##### Takes any string and outputs a list #####
##### that is 1-D and only contains powers#####
##### of 2 (exception: 0). This is how the#####
#####  game board looks before it is 2-D  #####
###############################################

def stringIntoList(temp: str) -> list:
    i = 0
    output = []

#############################################
###  Must iterate through entire string  ####
#############################################
    while i < len(temp):
       
        ################################################
        ### If first digit in num is 0 then num is 0.###
        ###  Add to list. Increment index (i) by 1   ###
        ################################################
        if int(temp[i]) == 0:
            output.append(0)
            i = i + 1
            continue

        ################################################
        ###    If first digit in num is 1 then ....  ###
        ################################################        
        elif int(temp[i]) == 1:
            if int(temp[i + 1]) == 2:   ###check if next digit is 2###
                output.append(128)      ###if it is, add 128 to list###
                i = i + 3               ###increment i by 3 and continue at top of loop### 
                continue
            elif int(temp[i + 1]) == 0: ###check if next digit is 0###
                output.append(1024)     ###if it is, add 1024 to list###
                i = i + 4               ###increment i by 4 and continue at top of loop###
                continue
            elif int(temp[i + 1]) == 6: ###if next digit is 6###
                output.append(16)       ###then add 16 to list###
                i = i + 2               ###increment i by 2 and continue at top of loop###
                continue
            
        elif int(temp[i]) == 2:         ###if first digit is 2###
            if int(temp[i + 1]) == 5:   ###if next digit is 5 ###
                output.append(256)      ###add 256 to the list###
                i = i + 3               ###increment i by 3 and continue at top of loop###
                continue
            else:
                output.append(2)        ###if next digit is not 5###
                i = i + 1               ###add 2 to the list and incrememnt i by 1###
                continue                ###continue at top of loop###
            
        elif int(temp[i]) == 3:         ###if first digit is 3###
            output.append(32)           ###add 32 to list and increment i by 2###
            i = i + 2                   ###continue at top of list###
            continue
        
        elif int(temp[i]) == 4:         ###if first digit is 4###
            output.append(4)            ###no other possible powers of 2 start with 4, so add 4 to list###
            i = i + 1                   ###increment i by 1###
            continue                    ###continue at top of loop###
        
        elif int(temp[i]) == 5:         ###if first digit is 5###
            output.append(512)          ###add 512 to list###
            i = i + 3                   ###increment i by 512###
            continue                    ###continue loop###
        
        elif int(temp[i]) == 6:         ###if first digit is 6###
            output.append(64)           ###add 64 to list###
            i = i + 2                   ###increment i by 2###
            continue
        
        elif int(temp[i]) == 8:         ###if first digit is 8 then add 8 to list###
            output.append(8)            ###incrmement by 1 and continue loop###
            i = i + 1
            continue
        
        else:
            print("Input string contains either: \nNumbers that are not powers of 2 (plus 0) ")
            print("OR\nCharacters that are not numbers.")
            print("Please try again with a valid string.")
            print("Please note: This will most likely result in an invalid grid size.")
            print("That error message may appear as well as a result.")
    return output





###################################################
### We know that if the list is not exactly 16 ####
### elements then we throw an error. So we can ####
### evenly subdivide the list into 4 rows with ####
### 1 column for each row (2D list). We do this####
### by creating a new list that appends every 4####
### elements (as its own list) to a new list   ####
###################################################
def create2DList(listIn: list) -> list:
    
    board = []                      ###initialize empty list###
    board.append(listIn[0:4])       ###append first set of 4 elements###
    board.append(listIn[4:8])       ###append second set of 4 elements###
    board.append(listIn[8:12])      ###append third set of 4 elements###
    board.append(listIn[12:])       ###append last set of 4 elements###
    
    return board                    ###return final game board###




###################################################
###We want to convert the 2D list back into a 1D###
###because we want to be able to add a number   ###
###every time we shift. However, adding a number###
###to a 2D list is more difficult to keep track ###
###of because we need to keep track of both row ###
### and column. So we convert it back to 1D to ####
### ensure we know all the available spaces    ####
###################################################
def convertTo1DList(listIn: list) -> list:
        
    checkForError(listIn)
    
    output = []                     ###initialize empty list###
    for element in listIn:          ###since every element is a list itself###
        output.extend(element)      ###we can use extend on every element. appending it to the output###
        
    return output                   ###return new list###



####################################################
###In order to randomly fill in a spot after shift##
###we must fill a spot with either a 2 or 4. Also###
###we must know where to put it. In order to do ####
###this we must identify available locations.   ####
###This is determined by zeros in the 1D list. So###
###identifying the index of all zeros is vital. ####
####################################################
def indicesOfAllZeros(listIn: list) -> list:
    
    output = []                     ###list of possible locations###
    for i in range(len(listIn)):    ###for every elem in the list###
        if listIn[i] == 0:          ###check if the value there is 0###
            output.append(i)        ###if it is, append the index of said element###

    return output                   ###return full list###



####################################################
### This function should take as input a 2D List ###
###and output the transpose of said 2D List. This###
###is necessary because shifting vertically can be##
###the exact same process as shifting horizontally##
###        after a transpose has occurred.        ##
####################################################
def getTranspose(listIn: list) -> list:
    
    checkForError(listIn)
    
    output = []                                 ###needs new output list###
    for i in range(len(listIn)):                ###for every row in the original matrix###
        output.append([])                       ###append a new list inside output###
        for j in range(len(listIn[i])):         ###for every column in the original matrix###
            output[i].append(listIn[j][i])      ###append the the ith element in every column###
            
    return output                               ###return new column###



#######################################################
### This function should take in as input a 2D List ###
### and output another 2D list where all of the rows###
### are backwards. This is necessary because in terms##
### of shifting. Shifting left = shifting right so ####
### long as when you shift right you reverse the rows##
###  and then shift left and finally reverse again  ###
#######################################################
def reverseList(listIn: list) -> list:
    
    checkForError(listIn)
    
    output = []
    for i in range(len(listIn)):
        output.append([])
        for j in range(len(listIn[i]) - 1, -1, -1):
            output[i].append(listIn[i][j])
            
            
    return output



##########################################################
### This function should take in as input a 2D list and###
###should check each position individually. If the spot###
### is 0 then the newly generate board is not changed. ###
### However if it is not 0 then we put that at the left###
### most position in the new board. Then we increment ####
### in order to not overwrite the recently shifted num.###
### Do this for every row. Then return the new board.  ###
##########################################################
def shiftLeft(listIn: list):
    
    checkForError(listIn)           ### check if inputed board is valid###
    
    newBoard = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]] ###initialize the new board to all 0s###
    for i in range(len(listIn)):                        ###for every row in the original board###
        index = 0                                       ###placeholder in the new board. starts at left-most position###
        for j in range(len(listIn[i])):                 ###for every column in the original board###
            if listIn[i][j] != 0:                       ###if a position is not 0 in the old board###
                newBoard[i][index] = listIn[i][j]       ###put it in the left-most position of the new board###
                index += 1                              ###increment position on the new board to not overwrite anything###
    return newBoard                         ###return the newBoard###



def shiftRight(listIn: list):
    
    newBoard = reverseList(listIn)
    newBoard = shiftLeft(newBoard)
    newBoard = reverseList(newBoard)
    
    return newBoard



def shiftUp(listIn: list):
    
    return None



def shiftDown(listIn: list):
    
    return None


####################################################
###Simply checks if there are 4 rows in the list ###
### then confirms that there are the same num of ###
###          columns as there are rows.          ###
####################################################
def checkForError(listIn: list):
    
    
    if len(listIn) != 4:                    
        print("The input grid must contain 4 rows.\nPlease try again")
        return 
    
    for i in range(len(listIn)):
        if (not isinstance(listIn[i], list) or len(listIn[i]) != len(listIn)):
            print("The input grid must contain the same number of rows as columns.")
            print("Please Try again")
            return
        
        

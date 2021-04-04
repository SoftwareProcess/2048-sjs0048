############################################
##### Edited by Sam Spearman (sjs0048) #####
######  Today's Date: April 3, 2021   ######
############################################
import random
import hashlib




def _shift(userParms):
    ###############################################
    ###Basic conditionals to make sure the grid ###
    ### does not violate any rules as described ###
    ###      by the customer specifications     ###
    ###############################################
    score = 0
    output = {}
    if 'grid' not in userParms:
        output['status'] = 'error: missing grid'
        return output
    
    if (userParms['direction'].lower() != 'up' and userParms['direction'].lower() != 'down'
          and userParms['direction'].lower() != 'right' and userParms['direction'].lower() != 'left'
          and userParms['direction'] != ''):
        output['status'] = 'error: invalid direction'
        return output
    
    userEncoded = (str(userParms['grid']) + '.' + str(userParms['score'])).encode()
    if userParms['integrity'] != hashlib.sha256(userEncoded).hexdigest().upper():
        output['status'] = 'error: bad integrity value'
        return output
    
    #print(type(userParms['score'])) ### just a test###
    
    if userParms['score'] %2 != 0 or type(userParms['score']) is not int:
        output['status'] = 'error: invalid score'
        return output
    else:
        score = userParms['score']
    
    result = stringIntoList(userParms['grid'])      ###creates a 1D list of the grid###
    
    if len(result) != 16:
        output['status'] = 'error: invalid grid'
        return output
    
    
    gameboard = create2DList(result)                ###converts 1D list into 2D###
    
        ################################################
        ### This section determines the desired shift###
        ###        direction. Default is down.       ###
        ################################################
    if userParms['direction'].lower() == 'up':
        newBoard, score = shiftUp(gameboard, score)
    elif userParms['direction'].lower() == 'right':
        newBoard, score = shiftDown(gameboard, score)
    elif userParms['direction'].lower() == 'left':
        newBoard, score = shiftLeft(gameboard, score)
    else:
        newBoard, score = shiftDown(gameboard, score)
    
    boardAs1D = convertTo1DList(newBoard)
    openSpots = indicesOfAllZeros(boardAs1D)
    twoOrFour = random.randint(0, 1)
    
    if twoOrFour == 0:
        nextPiece = 2
    else:
        nextPiece = 4
    
    nextSpot = random.randint(0, len(openSpots) - 1)
    
    boardAs1D[openSpots[nextSpot]] = nextPiece
    
    newGrid = ''
    for element in boardAs1D:
        newGrid += str(element)
    
    output['grid'] = newGrid
    
    output['score'] = score
    
    encoded = (newGrid + '.' + str(score)).encode()
    integrity = hashlib.sha256(encoded).hexdigest().upper()
    
    output['integrity'] = integrity
    
    if 2048 in boardAs1D:
        output['status'] = 'win'
        
    elif boardAs1D == result or 0 not in boardAs1D:
        output['status'] = 'lose'
    else:
        output['status'] = 'okay'
    
    
    
    return output


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
            if i != len(temp) - 1:              ###got error when 2 was the last element. so this is necessary###
                if int(temp[i + 1]) == 5:   ###if next digit is 5 ###
                    output.append(256)      ###add 256 to the list###
                    i = i + 3               ###increment i by 3 and continue at top of loop###
                    continue
                else:
                    output.append(2)        ###if next digit is not 5###
                    i = i + 1               ###add 2 to the list and increment i by 1###
                    continue                ###continue at top of loop###
            else:
                output.append(2)        ###if next digit is not 5###
                i = i + 1               ###add 2 to the list and increment i by 1###
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
            output.append(8)            ###increment by 1 and continue loop###
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
###Shift left simply shifts the tiles, combines all the###
###numbers that it can, and then shifts left once again###
### in order for there to be no blank spots left open  ###
##########################################################
def shiftLeft(listIn: list, score: int):
    
    newBoard = shift(listIn)
    newBoard, score = combine(newBoard, score)
    newBoard = shift(newBoard)
    
    return newBoard, score                   ###return the newBoard###


##########################################################
###Shift right is simply left-shift that's reversed both##
###before and after the shift. This results in the same###
########             board anyways.              #########
##########################################################

def shiftRight(listIn: list, score: int):
    
    newBoard = reverseList(listIn)
    newBoard, score = shiftLeft(newBoard, score)
    newBoard = reverseList(newBoard)
    
    return newBoard, score


##########################################################
###Shift Up is a shift that gets the transpose of the ####
###board both before and after shifting left. The end ####
########          result is the same              ########
##########################################################
def shiftUp(listIn: list, score: int):
    
    newBoard = getTranspose(listIn)
    newBoard, score = shiftLeft(newBoard, score)
    newBoard = getTranspose(newBoard)
    
    return newBoard, score



##########################################################
### Shift down is the most complicated. It requires a  ###
### Transpose before being reversed. Then the board is ###
### shifted left. Afterwards the board is reversed once###
### again and is then transposed again. The board must ###
###be manipulated in that exact order or the end result###
#####        will not be the desire output           #####
##########################################################
def shiftDown(listIn: list, score: int):
    
    newBoard = getTranspose(listIn)
    newBoard, score = shiftRight(newBoard, score)
    newBoard = getTranspose(newBoard)
    
    return newBoard, score



##########################################################
### This function should take in as input a 2D list and###
###should check each position individually. If the spot###
### is 0 then the newly generate board is not changed. ###
### However if it is not 0 then we put that at the left###
### most position in the new board. Then we increment ####
### in order to not overwrite the recently shifted num.###
### Do this for every row. Then return the new board.  ###
##########################################################
def shift(listIn: list):
    
    checkForError(listIn)           ### check if inputed board is valid###
    
    newBoard = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]] ###initialize the new board to all 0s###
    for i in range(len(listIn)):                        ###for every row in the original board###
        index = 0                                       ###placeholder in the new board. starts at left-most position###
        for j in range(len(listIn[i])):                 ###for every column in the original board###
            if listIn[i][j] != 0:                       ###if a position is not 0 in the old board###
                newBoard[i][index] = listIn[i][j]       ###put it in the left-most position of the new board###
                index += 1                              ###increment position on the new board to not overwrite anything###
    return newBoard
    
    
##########################################################
### This function's job is to check elements that are  ###
### directly next to each other and combine them if the###
### numbers are equal. If they are not it ignores the  ###
### number and goes on to the next pair. Does this for ###
###  every number in each row. It only needs to worry  ###
###    about rows because of matrix manipulation       ###
##########################################################
def combine(listIn: list, score: int):
    
    for i in range(len(listIn)):
        for j in range(len(listIn[i]) - 1):

            if listIn[i][j] == listIn[i][j + 1]:

                listIn[i][j] = listIn[i][j] * 2
                listIn[i][j + 1] = 0
                score += listIn[i][j]
                
                
    return listIn, score            

    
####################################################
###Simply checks if there are 4 rows in the list ###
### then confirms that there are the same num of ###
###          columns as there are rows.          ###
####################################################
def checkForError(listIn: list):    ####This function was primarily used for testing. It is not truly necessary####
    
    
    if len(listIn) != 4:                    
        print("The input grid must contain 4 rows.\nPlease try again")
        return 
    
    for i in range(len(listIn)):
        if (not isinstance(listIn[i], list) or len(listIn[i]) != len(listIn)):
            print("The input grid must contain the same number of rows as columns.")
            print("Please Try again")
            return
        
        

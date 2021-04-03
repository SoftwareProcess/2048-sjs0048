def _shift(userParms):
    ###############################################
    ###Basic conditionals to make sure the grid####
    ####  cannot be a size that should be, in  ####
    ###        theory, impossible              ####
    ###############################################
    
    result = stringIntoList(userParms['grid'])
    
    if len(result) < 16:
        errorMes = "Error: This grid is too small. Please check the input string."
        return errorMes
    elif len(result) > 16:
        errorMes = "Error: This grid is too large. Please check the input string."
        return errorMes
    
    gameboard = create2DList(result)
    
    return gameboard


    
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
    for i in range(len(listIn)):         ###for every elem in the list###
        if listIn[i] == 0:          ###check if the value there is 0###
            output.append(i)        ###if it is, append the index of said element###

    return output                   ###return full list###
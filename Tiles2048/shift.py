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



def create2DList(input: list) -> list:
    
    board = []
    board.append(input[0:4])
    board.append(input[4:8])
    board.append(input[8:12])
    board.append(input[12:])
    
    return board
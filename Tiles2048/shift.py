def _shift(userParms):
    ###############################################
    ###Basic conditionals to make sure the grid####
    ####  cannot be a size that should be, in  ####
    ###        theory, impossible              ####
    ###############################################
    
    result = stringIntoList(userParms['grid'])
    
    if len(result) < 16:
        errorMes = ""
        return result
    elif len(result) > 16:
        errorMes = "Error: This grid is too large. Please check the input string."
        return errorMes
    
    return result




    
###############################################
##### Takes any string and outputs a list #####
##### that is 1-D and only contains powers#####
##### of 2 (exception: 0). This is how the#####
#####  game board looks before it is 2-D  #####
###############################################

def stringIntoList(temp: str) -> list:
    i = 0
    output = []

    while i < len(temp):
        
        if int(temp[i]) == 0:
            output.append(0)
            i = i + 1
            continue
        
        elif int(temp[i]) == 1:
            if int(temp[i + 1]) == 2:
                output.append(128)
                i = i + 3
                continue
            elif int(temp[i + 1]) == 0:
                output.append(1024)
                i = i + 4
                continue
            elif int(temp[i + 1]) == 6:
                output.append(16)
                i = i + 2
                continue
            else:
                print("Error occured here. Found an independent or stray \"1\".")
                print(" This could be a result of counting wrong or an invalid board.")
                print(output)
                break
            
        elif int(temp[i]) == 2:
            if int(temp[i + 1]) == 5:
                output.append(256)
                i = i + 3
                continue
            else:
                output.append(2)
                i = i + 1
                continue
            
        elif int(temp[i]) == 3:
            output.append(32)
            i = i + 2
            continue
        
        elif int(temp[i]) == 4:
            output.append(4)
            i = i + 1
            continue
        
        elif int(temp[i]) == 5:
            output.append(512)
            i = i + 3
            continue
        
        elif int(temp[i]) == 6:
            output.append(64)
            i = i + 2
            continue
        
        elif int(temp[i]) == 8:
            output.append(8)
            i = i + 1
            continue
        
        else:
            print("Input string contains either: \nNumbers that are not powers of 2 (plus 0) ")
            print("OR\nCharacters that are not numbers.")
            print("Please try again with a valid string.")
            print("Please note: This will most likely result in an invalid grid size.")
            print("That error message may appear as well as a result.")
    return output

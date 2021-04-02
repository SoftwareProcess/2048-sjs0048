def _shift(userParms):
    ###############################################
    ###Basic conditionals to make sure the grid####
    ####  cannot be a size that should be, in  ####
    ###        theory, impossible              ####
    ###############################################
    temp = userParms['grid']
    if len(temp) < 16:
        result = "Error: This grid is too small."
        return result
    elif len(temp) > 64:
        result = "Error: This grid is too large."
        return result
    
    ###############################################
    ##### Starts to take the given string and #####
    ##### begins converting into 1-D int list #####
    ###############################################
    
    i = 0
    result = []
    while i < len(temp):
        if temp[i] == 0:
            result.append(None)
        elif temp[i] == 1:
            if temp[i + 1] == 2:
                result.append(128)
                i = i + 3
                continue
            elif temp[i + 1] == 0:
                result.append(1024)
                i = i + 4
                continue
            else:
                print("Error occured here. Found an independent or stray \"1\".")
                print(" This could be a result of counting wrong or an invalid board.")
            
        elif temp[i] == 2:
            if temp[i + 1] == 5:
                result.append(256)
                i = i + 3
                continue
            elif temp[i + 1] == 0:
                result.append(2048)
                i = i + 4
                continue
            else:
                result.append(2)
                i = i + 1
                continue
            
        elif temp[i] == 3:
            result.append(32)
            i = i + 2
            continue
        
        elif temp[i] == 4:
            result.append(4)
            i = i + 1
            continue
        
        elif temp[i] == 5:
            result.append(512)
            i = i + 3
            continue
        
        elif temp[i] == 6:
            result.append(64)
            i = i + 2
            continue
        
        elif temp[i] == 8:
            result.append(8)
            i = i + 1
            continue
        
    return result

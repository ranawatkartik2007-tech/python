def status(status):
    match status:
        case 200:
            return ("ok")
        case 400:
            return (" not found  ")
        case 500:
            return ("server error")
        case _:
            return (" unknown status code") 
        
        
        
        
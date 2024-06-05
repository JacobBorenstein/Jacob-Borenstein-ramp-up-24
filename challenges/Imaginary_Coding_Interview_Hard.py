def interview(list:list[int],mins:int):
    if mins > 120:
        return 'disqualified'
    
    elif list[0] > 5 or list[1] > 5:
        return 'disqualified'
    
    elif list[2] > 10 or list[3] > 10:
        return 'disqualified'  
    
    elif list[4] > 15 or list[5] > 15:
        return 'disqualified'
    
    elif list[6] > 20 or list[7] > 20:
        return 'disqualified'  
    
    else:
        return 'qualified'  
    



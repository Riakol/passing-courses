from datetime import date 

def get_min_max(date):
    if date:
        return min(date), max(date)
    else:
        return ()

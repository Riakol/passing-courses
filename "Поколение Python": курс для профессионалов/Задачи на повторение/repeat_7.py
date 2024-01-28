def likes(names):
    if names:
        if len(names) == 1:
            return f"{names[0]} оценил(а) данную запись"
        if len(names) == 2:
            return f"{' и '.join(names)} оценили данную запись"
        if len(names) == 3:
            return f"{names[0]}, {' и '.join(names[1:])} оценили данную запись"
        if len(names) > 3:
            return f"{', '.join(names[:2])} и {len(names[2:])} других оценили данную запись"
    else:
        return "Никто не оценил данную запись"

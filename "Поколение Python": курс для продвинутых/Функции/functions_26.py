is_non_negative_num = lambda x: str(x).replace('.', '', 1).replace('-', '', 1).isdigit() and x.rfind('-') <= 0

is_num = is_non_negative_num






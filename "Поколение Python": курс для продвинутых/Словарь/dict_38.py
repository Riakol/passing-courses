def build_query_string(params):
    temp = []
    for key, value in sorted(params.items()):
        temp.append(f"{key}={value}")
    return '&'.join(temp)
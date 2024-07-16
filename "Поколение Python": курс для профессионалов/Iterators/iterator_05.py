def get_min_max(data):
    return (data.index(min(data)), data.index(max(data))) if data else None


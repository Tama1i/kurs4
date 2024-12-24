def calculate_fundament_position(last_fundament, relative_side):
    x, y = last_fundament["position"]
    if relative_side == "right":
        return x + last_fundament["length"], y
    elif relative_side == "left":
        return x - last_fundament["length"], y
    elif relative_side == "front":
        return x, y + last_fundament["width"]
    elif relative_side == "back":
        return x, y - last_fundament["width"]
    return x, y

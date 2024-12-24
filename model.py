from utils import calculate_fundament_position

building_model = {
    "fundaments": [],
    "elements": {},
    "total_units": 0,
}

def add_fundament(length, width, height, relative_side=None):
    fundament_id = len(building_model["fundaments"]) + 1
    fundament = {"id": fundament_id, "length": length, "width": width, "height": height, "position": (0, 0)}
    if building_model["fundaments"] and relative_side:
        fundament["position"] = calculate_fundament_position(building_model["fundaments"][-1], relative_side)
    building_model["fundaments"].append(fundament)
    building_model["elements"][fundament_id] = []

def stretch_wall_between_columns(fundament, column1, column2, height):
    # Implementation for stretching wall
    pass

def add_roof():
    # Implementation for adding roof
    pass

def draw_cube(x, y, z, width, height, depth):
    # OpenGL implementation for drawing cube
    pass

def draw_column(x, y, z, width, height):
    # OpenGL implementation for drawing column
    pass

def draw_wall(x, y, z, width, height):
    # OpenGL implementation for drawing wall
    pass

def draw_roof(x, y, z, length, width, thickness):
    # OpenGL implementation for drawing roof
    pass
def export_to_obj(filename="model.obj"):
    """Экспорт 3D-модели в формат .obj."""
    try:
        with open(filename, "w") as obj_file:
            obj_file.write("# Exported 3D model\n")

            # Счётчик индекса вершины
            vertex_index = 1
            vertex_map = {}

            # Экспорт фундаментов
            for fundament in building_model["fundaments"]:
                x, y = fundament["position"]
                z = 0
                length, height, width = fundament["length"], fundament["height"], fundament["width"]

                # Вершины куба
                vertices = [
                    (x, y, z),
                    (x + length, y, z),
                    (x + length, y + width, z),
                    (x, y + width, z),
                    (x, y, z + height),
                    (x + length, y, z + height),
                    (x + length, y + width, z + height),
                    (x, y + width, z + height),
                ]
                for vx, vy, vz in vertices:
                    obj_file.write(f"v {vx} {vy} {vz}\n")
                    vertex_map[(vx, vy, vz)] = vertex_index
                    vertex_index += 1

                # Грани куба
                faces = [
                    (1, 2, 6, 5),
                    (2, 3, 7, 6),
                    (3, 4, 8, 7),
                    (4, 1, 5, 8),
                    (1, 2, 3, 4),
                    (5, 6, 7, 8),
                ]
                for face in faces:
                    obj_file.write(f"f {' '.join(str(vertex_map[vertices[i - 1]]) for i in face)}\n")

            print(f"Модель успешно экспортирована в файл {filename}.")
    except Exception as e:
        print(f"Ошибка при экспорте модели: {e}")

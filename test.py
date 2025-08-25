import random
import pyxel

class Room:

    def __init__(self, width, height, tiles):
        self.width = width
        self.height = height
        self.tiles = tiles
        self.doors = []

def make_basic_room(width:int, height:int):
    tiles = []
    for y in range(height):
        row = []
        for x in range(width):
            if x == 0 or y == 0 or x == width-1 or y == height-1:
                row.append((1,0))
            else:
                row.append((2,0))
        tiles.append(row)
    return Room(width, height, tiles)

def draw_room(room:Room, ox:int, oy:int):
    for y in range(room.height):
        for x in range(room.width):
            u, v = room.tiles[y][x]
            pyxel.tilemaps[0].pset(ox + x, oy + y, (u, v))
    
    for d in room.doors:
        if d == "N":
            cx = ox + room.width // 2
            for dx in (-1, 0, 1):
                pyxel.tilemaps[0].pset(cx + dx, oy, (2, 0))
        elif d == "S":
            cx = ox + room.width // 2
            for dx in (-1, 0, 1):
                pyxel.tilemaps[0].pset(cx + dx, oy + room.height - 1, (2, 0))
        elif d == "W":
            cy = oy + room.height // 2
            for dy in (-1, 0, 1):
                pyxel.tilemaps[0].pset(ox, cy + dy, (2, 0))
        elif d == "E":
            cy = oy + room.height // 2
            for dy in (-1, 0, 1):
                pyxel.tilemaps[0].pset(ox + room.width - 1, cy + dy, (2, 0))

def place_next_room(curr_room:Room, curr_pos:tuple, new_room:Room, direction:str):
    x, y = curr_pos
    x_diff = (curr_room.width - new_room.width) // 2
    y_diff = (curr_room.height - new_room.height) // 2

    if direction == "E":
        return (x + curr_room.width - 1, y + y_diff)
    if direction == "W":
        return (x - new_room.width + 1, y + y_diff)
    if direction == "S":
        return (x + x_diff, y + curr_room.height - 1)
    if direction == "N":
        return (x + x_diff, y - new_room.height + 1)

def occupy_room(room:Room, pos:tuple, occupied_tiles:set):
    ox, oy = pos
    ox += 1
    oy += 1

    for y in range(room.height - 1):
        for x in range(room.width - 1):
            occupied_tiles.add((ox + x, oy + y))

    return occupied_tiles

def check_room_collision(room:Room, pos:tuple, occupied_tiles:set):
    ox, oy = pos
    ox += 1
    oy += 1

    for y in range(room.height - 1):
        for x in range(room.width - 1):
            pos = (ox + x, oy + y)
            if pos in occupied_tiles:
                return True
    return False

def generate_dungeon(start_room:Room, end_room:Room, rooms:list, nums_rooms:int, ox:int, oy:int):
    x, y = ox, oy
    curr_room = start_room
    curr_room.doors = [random.choice(["N","S","W","E"])]
    curr_dir = start_room.doors[0]
    draw_room(start_room, x, y)
    placed_rooms = 2

    occupied_tiles = set()
    occupied_tiles = occupy_room(curr_room, (x, y), occupied_tiles)

    count_1 = 0
    while placed_rooms < nums_rooms and count_1 < nums_rooms * 10:
        count_1 += 1
        opposite = {"N":"S","S":"N","E":"W","W":"E"}[curr_dir]
        
        next_room = random.choice(rooms)
        next_room.doors = [opposite]

        next_dir = random.choice([d for d in ["N","S","E","W"] if d != opposite])
        next_room.doors.append(next_dir)

        new_x, new_y = place_next_room(curr_room, (x, y), next_room, curr_dir)

        count_2 = 0
        while check_room_collision(next_room, (new_x, new_y), occupied_tiles) and count_2 < 10:
            next_dir = random.choice([d for d in ["N","S","E","W"] if d != opposite])
            next_room.doors.append(next_dir)
            new_x, new_y = place_next_room(curr_room, (x, y), next_room, curr_dir)
            count_2 += 1

        if check_room_collision(next_room, (new_x, new_y), occupied_tiles):
            continue

        placed_rooms += 1
        x, y = new_x, new_y
        draw_room(next_room, x, y)
        curr_dir = next_room.doors[0] if next_room.doors[1] == opposite else next_room.doors[1]
        occupied_tiles = occupy_room(next_room, (x, y), occupied_tiles)
        curr_room = next_room

    opposite = {"N":"S","S":"N","E":"W","W":"E"}[curr_dir]
    end_room.doors = [opposite]
    
    for _ in range(20):
        new_x, new_y = place_next_room(curr_room, (x, y), end_room, curr_dir)
        end_room.doors = {"N":"S","S":"N","E":"W","W":"E"}[curr_dir]
        if not check_room_collision(end_room, (new_x, new_y), occupied_tiles):
            x, y = new_x, new_y
            draw_room(end_room, x, y)
            occupied_tiles = occupy_room(end_room, (x, y), occupied_tiles)
            break
        else:
            curr_dir = random.choice([d for d in ["N","S","E","W"] if d != opposite])

if __name__ == "__main__":
    pyxel.init(228 * 5, 128 * 5)

    pyxel.load("test_assets.pyxres")

    ROOM_1 = [[(1,0),(1,0),(1,0),(1,0),(1,0)],
              [(1,0),(3,0),(3,0),(3,0),(1,0)],
              [(1,0),(3,0),(3,0),(3,0),(1,0)],
              [(1,0),(3,0),(3,0),(3,0),(1,0)],
              [(1,0),(1,0),(1,0),(1,0),(1,0)]]
    
    ROOM_2 = [[(1,0),(1,0),(1,0),(1,0),(1,0)],
              [(1,0),(4,0),(4,0),(4,0),(1,0)],
              [(1,0),(4,0),(4,0),(4,0),(1,0)],
              [(1,0),(4,0),(4,0),(4,0),(1,0)],
              [(1,0),(1,0),(1,0),(1,0),(1,0)]]

    start_room = Room(5, 5, ROOM_1)
    end_room = Room(5, 5, ROOM_2)
    rooms = [make_basic_room(7, 7), make_basic_room(5, 5), make_basic_room(11, 5), make_basic_room(5, 11), make_basic_room(21, 17)]

    generate_dungeon(start_room, end_room, rooms, 30, 100, 100)

    camx, camy = 800, 800

    def update():
        global camx, camy

        if pyxel.btnp(pyxel.KEY_R):
            pyxel.load("test_assets.pyxres")
            generate_dungeon(start_room, end_room, rooms, 30, 100, 100)

        if pyxel.btn(pyxel.KEY_LEFT):
            camx -= 5
        if pyxel.btn(pyxel.KEY_RIGHT):
            camx += 5
        if pyxel.btn(pyxel.KEY_UP):
            camy -= 5
        if pyxel.btn(pyxel.KEY_DOWN):
            camy += 5

        pyxel.camera(camx, camy)

    def draw():
        pyxel.cls(0)

        pyxel.bltm(0, 0, 0, 0, 0, 2000, 2000, 0)

    pyxel.run(update, draw)

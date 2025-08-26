# import random
# import pyxel

# CARDINAL_OPPOSITE = {"N":"S", "S":"N", "W":"E", "E":"W"}

# class Room:

#     def __init__(self, width, height, tiles):
#         self.width = width
#         self.height = height
#         self.tiles = tiles
#         self.doors = []

# def make_basic_room(width:int, height:int, wall_tile:tuple, floor_tile:tuple)-> Room:
#     tiles = []
#     for y in range(height):
#         row = []
#         for x in range(width):
#             if x == 0 or y == 0 or x == width-1 or y == height-1:
#                 row.append(wall_tile)
#             else:
#                 row.append(floor_tile)
#         tiles.append(row)
#     return Room(width, height, tiles)

# def mark_room(room:Room, ox:int, oy:int, occupied_tiles:set)-> set:
#     ox += 1
#     oy += 1
#     for y in range(room.height - 2):
#         for x in range(room.width - 2):
#             occupied_tiles.add((ox + x, oy + y))

#     return occupied_tiles

# def check_room_collision(room:Room, ox:int, oy:int, occupied_tiles:set):
#     for y in range(room.height):
#         for x in range(room.width):
#             pos = (ox + x, oy + y)
#             if pos in occupied_tiles:
#                 return True
#     return False

# def draw_room(room:Room, ox:int, oy:int, direction:str=""):
#     for y in range(room.height):
#         for x in range(room.width):
#             u, v = room.tiles[y][x]
#             pyxel.tilemaps[0].pset(ox + x, oy + y, (u, v))

#     if direction == "N":
#         cx = ox + room.width // 2
#         for dx in (-1, 0, 1):
#             pyxel.tilemaps[0].pset(cx + dx, oy, (0, 2))
#     elif direction == "S":
#         cx = ox + room.width // 2
#         for dx in (-1, 0, 1):
#             pyxel.tilemaps[0].pset(cx + dx, oy + room.height - 1, (0, 2))
#     elif direction == "W":
#         cy = oy + room.height // 2
#         for dy in (-1, 0, 1):
#             pyxel.tilemaps[0].pset(ox, cy + dy, (0, 2))
#     elif direction == "E":
#         cy = oy + room.height // 2
#         for dy in (-1, 0, 1):
#             pyxel.tilemaps[0].pset(ox + room.width - 1, cy + dy, (0, 2))

# def place_next_room(curr_room:Room, curr_pos:tuple, next_room:Room, direction:str):
#     x, y = curr_pos
#     x_diff = (curr_room.width - next_room.width) // 2
#     y_diff = (curr_room.height - next_room.height) // 2

#     if direction == "E":
#         return (x + curr_room.width - 1, y + y_diff)
#     if direction == "W":
#         return (x - next_room.width + 1, y + y_diff)
#     if direction == "S":
#         return (x + x_diff, y + curr_room.height - 1)
#     if direction == "N":
#         return (x + x_diff, y - next_room.height + 1)

# def generate_dungeon(start_room:Room, end_room:Room, fill_rooms:list, special_rooms:list, num_main_rooms:int, num_branches:int, branch_length:int, ox:int=100, oy:int=100):
#     x, y = ox, oy
#     curr_room = start_room
#     curr_dir = ""
#     draw_room(start_room, x, y)
#     next_dir = ""
#     occupied_tiles = set()
#     occupied_tiles = mark_room(curr_room, x, y, occupied_tiles)

#     xs = [x, x + curr_room.width]
#     ys = [y, y + curr_room.height]

#     placed_rooms = 1
#     placed = [(curr_room, x, y, "")]
#     count_1 = 0
#     while placed_rooms < num_main_rooms and count_1 < 50:
#         count_1 += 1

#         next_dir = random.choice([d for d in ["N","S","E","W"] if d != CARDINAL_OPPOSITE.get(curr_dir)])
#         next_room = random.choice(fill_rooms) if placed_rooms < num_main_rooms - 1 else end_room
#         next_x, next_y = place_next_room(curr_room, (x, y), next_room, next_dir)

#         count_2 = 0
#         while check_room_collision(next_room, next_x, next_y, occupied_tiles) and count_2 < 10:
#             next_dir = random.choice([d for d in ["N","S","E","W"] if d != CARDINAL_OPPOSITE.get(curr_dir)])
#             next_room = random.choice(fill_rooms) if placed_rooms < num_main_rooms - 1 else end_room
#             next_x, next_y = place_next_room(curr_room, (x, y), next_room, next_dir)
#             count_2 += 1

#         if check_room_collision(next_room, next_x, next_y, occupied_tiles):
#             continue

#         x, y = next_x, next_y
#         xs += [x, x + curr_room.width]
#         ys += [y, y + curr_room.height]
#         draw_room(next_room, x, y, CARDINAL_OPPOSITE.get(next_dir))
#         curr_room = next_room
#         curr_dir = next_dir
#         occupied_tiles = mark_room(curr_room, x, y, occupied_tiles)
#         placed.append((curr_room, x, y, curr_dir))
#         placed_rooms += 1

#     placed_branches = 0
#     count_3 = 0
#     while placed_branches < num_branches and count_3 < 50:
#         count_3 += 1
#         anchor_room, ax, ay, anchor_dir = random.choice(placed[1:-1])

#         branch_dir = random.choice([d for d in ["N","S","E","W"] if d not in (anchor_dir, CARDINAL_OPPOSITE.get(anchor_dir))])

#         bx, by = ax, ay
#         curr_branch_room = anchor_room
#         curr_branch_dir = branch_dir

#         branch_placed = False
#         for i in range(branch_length):
#             if i == branch_length - 1:
#                 next_room = random.choice(special_rooms)
#             else:
#                 next_room = random.choice(fill_rooms)

#             next_bx, next_by = place_next_room(curr_branch_room, (bx, by), next_room, curr_branch_dir)

#             if check_room_collision(next_room, next_bx, next_by, occupied_tiles):
#                 continue

#             bx, by = next_bx, next_by
#             draw_room(next_room, bx, by, CARDINAL_OPPOSITE.get(curr_branch_dir))
#             occupied_tiles = mark_room(next_room, bx, by, occupied_tiles)

#             xs += [bx, bx + next_room.width]
#             ys += [by, by + next_room.height]

#             curr_branch_room = next_room
#             if i < branch_length - 1:
#                 curr_branch_dir = random.choice([d for d in ["N","S","E","W"] if d != CARDINAL_OPPOSITE.get(curr_branch_dir)])

#             branch_placed = True

#         placed_branches += 1 if branch_placed else 0

#     return (min(xs), min(ys), max(xs), max(ys))

# def get_neighbors(x:int, y:int):
#     n = 0
#     if pyxel.tilemaps[0].pget(x, y - 1) == (1, 0):
#         n += 1
#     if pyxel.tilemaps[0].pget(x + 1, y) == (1, 0):
#         n += 2
#     if pyxel.tilemaps[0].pget(x, y + 1) == (1, 0):
#         n += 4
#     if pyxel.tilemaps[0].pget(x - 1, y) == (1, 0):
#         n += 8

#     return n

# def place_walls(min_x:int, min_y:int, max_x:int, max_y:int):
#     walls = []
#     for y in range(min_y, max_y):
#         for x in range(min_x, max_x):
#             neighbors = get_neighbors(x, y)
#             if pyxel.tilemaps[0].pget(x, y) == (1, 0):
#                 walls.append((x, y, neighbors))

#     for x, y, neighbors in walls:
#         pyxel.tilemaps[0].pset(x, y, (neighbors, 1))

# if __name__ == "__main__":
#     pyxel.init(228 * 5, 128 * 5)

#     pyxel.load("test_assets.pyxres")

#     ROOM_1 = [[(1,0),(1,0),(1,0),(1,0),(1,0)],
#               [(1,0),(3,0),(3,0),(3,0),(1,0)],
#               [(1,0),(3,0),(3,0),(3,0),(1,0)],
#               [(1,0),(3,0),(3,0),(3,0),(1,0)],
#               [(1,0),(1,0),(1,0),(1,0),(1,0)]]
    
#     ROOM_2 = [[(1,0),(1,0),(1,0),(1,0),(1,0)],
#               [(1,0),(4,0),(4,0),(4,0),(1,0)],
#               [(1,0),(4,0),(4,0),(4,0),(1,0)],
#               [(1,0),(4,0),(4,0),(4,0),(1,0)],
#               [(1,0),(1,0),(1,0),(1,0),(1,0)]]

#     start_room = Room(5, 5, ROOM_1)
#     end_room = Room(5, 5, ROOM_2)
#     rooms = [make_basic_room(7, 7), make_basic_room(5, 5), make_basic_room(11, 5), make_basic_room(5, 11), make_basic_room(21, 17)]

#     generate_dungeon(start_room, end_room, rooms, 30, 100, 100)

#     camx, camy = 800, 800

#     def update():
#         global camx, camy

#         if pyxel.btnp(pyxel.KEY_R):
#             pyxel.load("test_assets.pyxres")
#             generate_dungeon(start_room, end_room, rooms, 30, 100, 100)

#         if pyxel.btn(pyxel.KEY_LEFT):
#             camx -= 5
#         if pyxel.btn(pyxel.KEY_RIGHT):
#             camx += 5
#         if pyxel.btn(pyxel.KEY_UP):
#             camy -= 5
#         if pyxel.btn(pyxel.KEY_DOWN):
#             camy += 5

#         pyxel.camera(camx, camy)

#     def draw():
#         pyxel.cls(0)

#         pyxel.bltm(0, 0, 0, 0, 0, 2000, 2000, 0)

#     pyxel.run(update, draw)
import pyxel
import random

class Room:
    def __init__(self, width, height, tiles):
        self.width = width
        self.height = height
        self.tiles = tiles

class DungeonMap:
    def __init__(self, width:int, height:int, default_tile=(0,0)):
        self.width = width
        self.height = height
        self.tiles = [[default_tile for _ in range(width)] for _ in range(height)]

    def set_tile(self, x:int, y:int, tile:tuple):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.tiles[y][x] = tile

    def get_tile(self, x:int, y:int):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.tiles[y][x]
        return None

    def draw(self, cam_x:int, cam_y:int, screen_w:int, screen_h:int):
        """Draw only the visible part of the dungeon."""
        for sy in range(screen_h):
            for sx in range(screen_w):
                tile = self.get_tile(cam_x + sx, cam_y + sy)
                if tile:
                    u, v = tile
                    pyxel.blt(sx*8, sy*8, 0, u*8, v*8, 8, 8, 0)


def make_basic_room(width, height, wall_tile, floor_tile):
    tiles = []
    for y in range(height):
        row = []
        for x in range(width):
            if x == 0 or y == 0 or x == width-1 or y == height-1:
                row.append(wall_tile)
            else:
                row.append(floor_tile)
        tiles.append(row)
    return Room(width, height, tiles)


def draw_room(room, ox, oy, dungeon:DungeonMap):
    for y in range(0, room.height * 2, 2):
        for x in range(0, room.width * 2, 2):
            u, v = room.tiles[y // 2][x // 2]
            dungeon.set_tile(ox + x, oy + y, (u, v))
            dungeon.set_tile(ox + x + 1, oy + y, (u + 1, v))
            dungeon.set_tile(ox + x + 1, oy + y + 1, (u + 1, v + 1))
            dungeon.set_tile(ox + x, oy + y + 1, (u, v + 1))


class App:
    def __init__(self):
        pyxel.init(160, 120, title="Dungeon Test")
        pyxel.load("assets.pyxres")  # <-- make sure you have an image bank with tiles!
        
        # Build a dungeon
        self.dungeon = DungeonMap(200, 200, (0,0))
        r1 = make_basic_room(10, 6, (0, 2), (0, 4))
        r2 = make_basic_room(8, 8, (0, 2), (0, 4))
        draw_room(r1, 5, 5, self.dungeon)
        draw_room(r2, 20, 10, self.dungeon)

        # Camera offset
        self.cam_x = 0
        self.cam_y = 0

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT): self.cam_x -= 1
        if pyxel.btn(pyxel.KEY_RIGHT): self.cam_x += 1
        if pyxel.btn(pyxel.KEY_UP): self.cam_y -= 1
        if pyxel.btn(pyxel.KEY_DOWN): self.cam_y += 1

    def draw(self):
        pyxel.cls(0)
        # How many tiles fit on screen?
        w, h = pyxel.width // 8, pyxel.height // 8
        self.dungeon.draw(self.cam_x, self.cam_y, w, h)


App()

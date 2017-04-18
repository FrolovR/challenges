# don't get me wrong, this is not the final solution; probability of win in both asserts is high, but not a 100% win rate
from random import choice

def StephanMoves(stephan, house):
    moves = [ch for ch in "NWES" if ch not in house[stephan - 1]]
    if stephan % 4 == 0 and "E" in moves:
        moves.remove("E")
    if stephan % 4 == 1 and "W" in moves: 
        moves.remove("W")
    if stephan > 12 and "S" in moves:
        moves.remove("S")
    elif stephan < 5 and "N" in moves:
        moves.remove("N")
    return moves

def FindPath(From, To, house, Ghost):
    # find path From To
    # path is a list of rooms sequentially
    DIRS = {"N": -4, "S": 4, "E": 1, "W": -1}
    ALT = {"N": "S", "S": "N", "E": "W", "W": "E"}
    path = list() # direcrions of all moves
    rooms = list() # numeric path 
    last_move = None
    last_room = None
    Stephan = From
    for i in range(16):
        # case when Stephan is in room 1 and the path is completed
        if Stephan == To:
            path.append("N")
            rooms.append(Stephan)
            safe = rooms[0:5]
            if Ghost not in safe:
                return path
            else:
                return None
        if Stephan < 1 or Stephan > 16:
            return None
        # case when we are out of moves
        if i == 30:
            return None
        
        # possible directions where we can move from current postition
        moves = StephanMoves(Stephan, house)
        # # remove the path to our last postion so we won't come back
        if last_move is not None:
            moves.remove(ALT[last_move])
            
        # if our move will bring us into the room where we've already been, hence it is a wrong path 
        for m in moves:
            if Stephan + DIRS[m] in rooms:
                moves.remove(m)
        # case when there is one possible way
        if len(moves) == 1:
            last_room = Stephan
            last_move = moves[0]
            Stephan += DIRS[moves[0]]
            path.append(moves[0])
            rooms.append(Stephan)
        # case when there is more than one way
        elif len(moves) > 1:
            move = choice(moves)
            last_room = Stephan
            last_move = move
            Stephan += DIRS[move]
            path.append(move)
            rooms.append(Stephan)
        # case when we have no moves which are possible or will bring us to unique place
        elif len(moves) == 0:
            return None
    
def NextMove(stephan, path):
    # returns direction to the next room from current position
    move = 0
    return move

def checkio(house, stephan, ghost):
    # this function return direction in which Stephan should move
    # calculate distance to ghost
    # calculate all possible moves
    moves = StephanMoves(stephan, house)
    # print(moves)
    path = None
    newpath = None
    paths = list()
    for i in range(len(moves)):
        while newpath is None:
            newpath = FindPath(stephan, 1, house, ghost)
            if newpath in paths and len(paths) < len(moves) - 1:
                newpath = FindPath(stephan, 1, house, ghost)
        if path == None:
            while path == None:
                path = FindPath(stephan, 1, house, ghost)
        elif len(newpath) < len(path):
            path = newpath
        paths.append(path)
        newpath = None
    print("move", path[0])
    print(len(path))
    return path[0]


if __name__ == '__main__':
    #This part is using only for self-checking and not necessary for auto-testing
    from random import choice

    DIRS = {"N": -4, "S": 4, "E": 1, "W": -1}

    def check_solution(func, house):
        stephan = 16
        ghost = 1
        for step in range(30):
            direction = func(house[:], stephan, ghost)
            if direction in house[stephan - 1]:
                print('Stefan ran into a closed door. It was hurt.')
                return False
            if stephan == 1 and direction == "N":
                print('Stefan has escaped.')
                return True
            stephan += DIRS[direction] 
            if ((direction == "W" and stephan % 4 == 0) or (direction == "E" and stephan % 4 == 1) or
                    (stephan < 1) or (stephan > 16)):
                print('Stefan has gone out into the darkness.')
                return False
            sx, sy = (stephan - 1) % 4, (stephan - 1) // 4
            ghost_dirs = [ch for ch in "NWES" if ch not in house[ghost - 1]]
            if ghost % 4 == 1 and "W" in ghost_dirs:
                ghost_dirs.remove("W")
            if not ghost % 4 and "E" in ghost_dirs:
                ghost_dirs.remove("E")
            if ghost <= 4 and "N" in ghost_dirs:
                ghost_dirs.remove("N")
            if ghost > 12 and "S" in ghost_dirs:
                ghost_dirs.remove("S")

            ghost_dir, ghost_dist = "", 1000
            for d in ghost_dirs:
                new_ghost = ghost + DIRS[d]
                gx, gy = (new_ghost - 1) % 4, (new_ghost - 1) // 4
                dist = (gx - sx) ** 2 + (gy - sy) ** 2
                if ghost_dist > dist:
                    ghost_dir, ghost_dist = d, dist
                elif ghost_dist == dist:
                    ghost_dir += d
            ghost_move = choice(ghost_dir)
            ghost += DIRS[ghost_move]
            if ghost == stephan:
                print('The ghost caught Stephan.')
                return False
        print("Too many moves.")
        return False

    assert check_solution(checkio,
                          ["", "S", "S", "",
                           "E", "NW", "NS", "",
                           "E", "WS", "NS", "",
                           "", "N", "N", ""]), "1st example"
    assert check_solution(checkio,
                          ["", "", "", "",
                           "E", "ESW", "ESW", "W",
                           "E", "ENW", "ENW", "W",
                           "", "", "", ""]), "2nd example"

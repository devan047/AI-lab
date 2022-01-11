 8 Puzzle Problem A*
class Node:
    def __init__(self, state, level):
        self.grid = state
        self.level = level
        self.cost = 0
def G(state):
    return state.level
def H(state, target):
    grid = state.grid
    dist = 0
    for i in grid:
        d1, d2 = grid.index(i), target.index(i)
        x1, y1 = d1 % 3, d1 // 3
        x2, y2 = d2 % 3, d2 // 3
        dist += abs(x1-x2) + abs(y1-y2)
    return dist
def F(state, target):
    return G(state) + H(state, target)
def printGrid(state):
    state = state.grid.copy()
    state[state.index(-1)] = ' '
    print(state[0], state[1], state[2])
    print(state[3], state[4], state[5])
    print(state[6], state[7], state[8])
    print()
def inFrontier(frontier, neighbour):
    return len([state for state in frontier if state.grid == neighbour.grid]) > 0
def astar(state, target):
    frontier = [Node(state, 1)]
    
    while frontier:
        frontier.sort(key = lambda x: x.cost)
        state = frontier.pop(0)
        print(f'Level: {state.level}')
        printGrid(state)
        
        if state.grid == target:
            print(f"Success!!!")
            return
        
        neighbours = possible_moves(state)
        for neighbour in neighbours:
            neighbour = Node(neighbour, state.level + 1)
            neighbour.cost = F(neighbour, target)
            if not inFrontier(frontier, neighbour):
                frontier.append(neighbour)
    
    print("Fail!!!")
def possible_moves(state):
    b = state.grid.index(-1)  
    d = []
    if b not in [0,1,2]: 
        d += 'u'
    if b not in [6,7,8]:
        d += 'd'
    if b not in [2,5,8]: 
        d += 'r'
    if b not in [0,3,6]: 
        d += 'l'
    pos_moves = []
    for move in d:
        pos_moves.append(gen(state,move,b))
    return pos_moves
def gen(state, move, blank):
    temp = state.grid.copy()                              
    if move == 'u':
        temp[blank-3], temp[blank] = temp[blank], temp[blank-3]
    if move == 'd':
        temp[blank+3], temp[blank] = temp[blank], temp[blank+3]
    if move == 'r':
        temp[blank+1], temp[blank] = temp[blank], temp[blank+1]
    if move == 'l':
        temp[blank-1], temp[blank] = temp[blank], temp[blank-1]
    return temp
#Test 1
src = [1,2,3,-1,4,5,6,7,8]
target = [1,2,3,4,5,-1,6,7,8]         
       


astar(src, target) 
Level: 1
1 2 3
  4 5
6 7 8

Level: 2
1 2 3
4   5
6 7 8

Level: 3
1 2 3
4 5  
6 7 8

Success!!!
# Test 2
src = [1,2,3,-1,4,5,6,7,8] 
target=[1,2,3,6,4,5,-1,7,8]



astar(src, target)
Level: 1
1 2 3
  4 5
6 7 8

Level: 2
1 2 3
6 4 5
  7 8

Success!!!
# Test 3 [Fails]
src = [1,2,3,7,4,5,6,-1,8] 
target=[1,2,3,6,4,5,-1,7,8]



astar(src, target)
Level: 1
1 2 3
7 4 5
6   8

Level: 2
1 2 3
7 4 5
  6 8

Level: 3
1 2 3
  4 5
7 6 8

Level: 3
1 2 3
7 4 5
6   8

Level: 2
1 2 3
7   5
6 4 8

Level: 3
1 2 3
7 4 5
6   8

Level: 3
1 2 3
  7 5
6 4 8

Level: 4
1 2 3
6 7 5
  4 8

Level: 2
1 2 3
7 4 5
6 8  

Level: 3
1 2 3
7 4 5
6   8

Level: 4
1 2 3
7 4 5
  6 8

Level: 5
1 2 3
  7 5
6 4 8

Level: 6
1 2 3
6 7 5
  4 8

Level: 5
1 2 3
6 7 5
4   8

Level: 6
1 2 3
6 7 5
  4 8

Level: 5
1 2 3
  4 5
7 6 8

Level: 5
1 2 3
7 4 5
6   8

Level: 4
  2 3
1 4 5
7 6 8

Level: 5
1 2 3
  4 5
7 6 8

Level: 4
1 2 3
4   5
7 6 8

Level: 5
1 2 3
4 6 5
7   8

Level: 6
1 2 3
4 6 5
  7 8

Level: 5
1 2 3
  4 5
7 6 8

Level: 4
1 2 3
7   5
6 4 8

Level: 5
1 2 3
7 4 5
6   8

Level: 4
  2 3
1 7 5
6 4 8

Level: 4
1 2 3
7 4 5
6 8  

Level: 5
1 2 3
7 4 5
6   8

Level: 6
1 2 3
6   5
4 7 8

Level: 6
1 2 3
7 4 5
  6 8

Level: 3
1   3
7 2 5
6 4 8

Level: 3
1 2 3
7 5  
6 4 8

Level: 3
1 2 3
7 4  
6 8 5

Level: 7
1 2 3
  7 5
6 4 8

Level: 8
1 2 3
6 7 5
  4 8

Level: 7
1 2 3
6 7 5
4   8

Level: 8
1 2 3
6 7 5
  4 8

Level: 7
1 2 3
  6 5
4 7 8

Level: 8
1 2 3
4 6 5
  7 8

Level: 7
1 2 3
4 6 5
7   8

Level: 8
1 2 3
4 6 5
  7 8

Level: 7
1 2 3
  4 5
7 6 8

Level: 7
1 2 3
7 4 5
6   8

Level: 6
1 2 3
6 7 5
4 8  

Level: 6
  2 3
1 4 5
7 6 8

Level: 7
1 2 3
  4 5
7 6 8

Level: 6
1 2 3
4   5
7 6 8

Level: 7
1 2 3
  4 5
7 6 8

Level: 6
1 2 3
4 6 5
7 8  

Level: 6
1 2 3
7   5
6 4 8

Level: 7
1 2 3
7 4 5
6   8

Level: 6
1 2 3
7 4 5
6 8  

Level: 7
1 2 3
7 4 5
6   8

Level: 4
  1 3
7 2 5
6 4 8

Level: 4
1 2 3
7 5 8
6 4  

Level: 4
1 2 3
7   4
6 8 5

Level: 5
1 2 3
  7 4
6 8 5

Level: 6
1 2 3
6 7 4
  8 5

Level: 8
1 2 3
6   5
4 7 8

Level: 8
1 2 3
7 4 5
  6 8

Level: 5
2   3
1 4 5
7 6 8

Level: 5
1   3
4 2 5
7 6 8

Level: 5
1 2 3
4 5  
7 6 8

Level: 5
2   3
1 7 5
6 4 8

Level: 7
1   3
6 2 5
4 7 8

Level: 8
1 2 3
6   5
4 7 8

Level: 7
1 2 3
6 5  
4 7 8

Level: 8
1 2 3
6   5
4 7 8

Level: 9
1 2 3
  7 5
6 4 8

Level: 10
1 2 3
6 7 5
  4 8

Level: 9
1 2 3
6 7 5
4   8

Level: 10
1 2 3
6 7 5
  4 8

Level: 9
1 2 3
  6 5
4 7 8

Level: 10
1 2 3
4 6 5
  7 8

Level: 9
1 2 3
4 6 5
7   8

Level: 10
1 2 3
4 6 5
  7 8

Level: 5
7 1 3
  2 5
6 4 8

Level: 6
7 1 3
6 2 5
  4 8

Level: 5
1 2 3
7 5 8
6   4

Level: 5
1 2 3
7 8 4
6   5

Level: 7
1 2 3
  7 4
6 8 5

Level: 8
1 2 3
6 7 4
  8 5

Level: 7
1 2 3
6 7 4
8   5

Level: 8
1 2 3
6 7 4
  8 5

Level: 9
1 2 3
  4 5
7 6 8

Level: 9
1 2 3
7 4 5
6   8

Level: 4
1 3  
7 2 5
6 4 8

Level: 4
1 2  
7 5 3
6 4 8

Level: 4
1 2  
7 4 3
6 8 5

Level: 8
  2 3
1 7 5
6 4 8

Level: 8
  2 3
1 6 5
4 7 8

Level: 8
  2 3
1 4 5
7 6 8

Level: 9
1 2 3
  4 5
7 6 8

Level: 8
1 2 3
4   5
7 6 8

Level: 9
1 2 3
  4 5
7 6 8

Level: 8
1 2 3
7   5
6 4 8

Level: 9
1 2 3
7 4 5
6   8

Level: 8
1 2 3
7 4 5
6 8  

Level: 9
1 2 3
7 4 5
6   8

Level: 6
  2 3
1 7 4
6 8 5

Level: 6
1 2 3
7   4
6 8 5

Level: 6
2 4 3
1   5
7 6 8

Level: 7
2 4 3
1 6 5
7   8

Level: 8
2 4 3
1 6 5
  7 8

Level: 6
  1 3
4 2 5
7 6 8

Level: 6
1 2 3
4 5 8
7 6  

Level: 6
2 7 3
1   5
6 4 8

Level: 7
2 7 3
1 4 5
6   8

Level: 8
  1 3
6 2 5
4 7 8

Level: 8
1 2 3
6 5 8
4 7  

Level: 10
1 2 3
6   5
4 7 8

Level: 6
  1 3
7 2 5
6 4 8

Level: 6
1 2 3
7 5 8
6 4  

Level: 6
1 2 3
7 5 8
  6 4

Level: 6
1 2 3
7 8 4
  6 5

Level: 8
1 2 3
6   4
8 7 5

Level: 10
1 2 3
7 4 5
  6 8

Level: 8
2 7 3
1 4 5
  6 8

Level: 7
1 2 3
6 7  
4 8 5

Level: 7
1 2 3
4 6  
7 8 5

Level: 7
1   3
7 2 5
6 4 8

Level: 7
1 2 3
7 5  
6 4 8

Level: 7
1 2 3
7 4  
6 8 5

Level: 5
1   3
7 2 4
6 8 5

Level: 9
1   3
6 2 5
4 7 8

Level: 10
1 2 3
6   5
4 7 8

Level: 9
1 2 3
6 5  
4 7 8

Level: 10
1 2 3
6   5
4 7 8

Level: 11
1 2 3
  7 5
6 4 8

Level: 12
1 2 3
6 7 5
  4 8

Level: 11
1 2 3
6 7 5
4   8

Level: 12
1 2 3
6 7 5
  4 8

Level: 11
1 2 3
  6 5
4 7 8

Level: 12
1 2 3
4 6 5
  7 8

Level: 11
1 2 3
4 6 5
7   8

Level: 12
1 2 3
4 6 5
  7 8

Level: 7
7 1 3
  2 5
6 4 8

Level: 8
7 1 3
6 2 5
  4 8

Level: 7
7 1 3
6 2 5
4   8

Level: 8
7 1 3
6 2 5
  4 8

Level: 9
1 2 3
  7 4
6 8 5

Level: 10
1 2 3
6 7 4
  8 5

Level: 9
1 2 3
6 7 4
8   5

Level: 10
1 2 3
6 7 4
  8 5

Level: 5
1 3 5
7 2  
6 4 8

Level: 5
1   2
7 5 3
6 4 8

Level: 5
1   2
7 4 3
6 8 5

Level: 7
1 2 3
7 8 4
6   5

Level: 7
2 4 3
  1 5
7 6 8

Level: 9
2 4 3
  6 5
1 7 8

Level: 10
2 4 3
1 6 5
  7 8

Level: 9
2 4 3
1 6 5
7   8

Level: 10
2 4 3
1 6 5
  7 8

Level: 7
4 1 3
  2 5
7 6 8

Level: 7
1 2 3
4 5 8
7   6

Level: 8
1 2 3
4 5 8
  7 6

Level: 7
2 7 3
  1 5
6 4 8

Level: 8
2 7 3
6 1 5
  4 8

Level: 9
6 1 3
  2 5
4 7 8

Level: 10
6 1 3
4 2 5
  7 8

Level: 9
1 2 3
6 5 8
4   7

Level: 10
1 2 3
6 5 8
  4 7

Level: 7
1 2 3
7 5 8
6   4

Level: 7
1 2 3
  5 8
7 6 4

Level: 7
1 2 3
  8 4
7 6 5

Level: 9
1 2 3
6 4  
8 7 5

Level: 10
1 2 3
6 4 5
8 7  

Level: 9
1 2 3
  6 4
8 7 5

Level: 11
1 2 3
  4 5
7 6 8

Level: 11
1 2 3
7 4 5
6   8

Level: 9
2 7 3
1 4 5
6   8

Level: 11
1 2 3
6 4 5
8   7

Level: 12
1 2 3
6 4 5
  8 7

Level: 6
2 3  
1 4 5
7 6 8

Level: 6
1 3  
4 2 5
7 6 8

Level: 6
1 2  
4 5 3
7 6 8

Level: 6
2 3  
1 7 5
6 4 8

Level: 8
1 3  
6 2 5
4 7 8

Level: 8
1 2  
6 5 3
4 7 8

Level: 10
1 2 3
6 7 5
4 8  

Level: 10
1 2 3
4 6 5
7 8  

Level: 6
7 1 3
2   5
6 4 8

Level: 7
7 1 3
2 4 5
6   8

Level: 6
1 2 3
7   8
6 5 4

Level: 7
1 2 3
7 5 8
6   4

Level: 7
1 2 3
  7 8
6 5 4

Level: 8
1 2 3
6 7 8
  5 4

Level: 6
1 2 3
7 8 4
6 5  

Level: 7
1 2 3
7 8 4
6   5

Level: 8
1 2 3
6 7 4
8 5  

Level: 10
  2 3
1 4 5
7 6 8

Level: 11
1 2 3
  4 5
7 6 8

Level: 10
1 2 3
4   5
7 6 8

Level: 11
1 2 3
  4 5
7 6 8

Level: 10
1 2 3
7   5
6 4 8

Level: 11
1 2 3
7 4 5
6   8

Level: 10
1 2 3
7 4 5
6 8  

Level: 11
1 2 3
7 4 5
6   8

Level: 8
2 4 3
1   5
7 6 8

Level: 8
2 4 3
1 6 5
7 8  

Level: 8
2 7 3
1   5
6 4 8

Level: 9
2 7 3
1 4 5
6   8

Level: 8
2 7 3
1 4 5
6 8  

Level: 9
2 7 3
1 4 5
6   8

Level: 8
1 2 3
6   7
4 8 5

Level: 8
1 2 3
4   6
7 8 5

Level: 9
1 2 3
  4 6
7 8 5

Level: 8
  1 3
7 2 5
6 4 8

Level: 8
1 2 3
7 5 8
6 4  

Level: 8
1 2 3
7   4
6 8 5

Level: 6
  1 3
7 2 4
6 8 5

Level: 10
  1 3
6 2 5
4 7 8

Level: 10
1 2 3
6 5 8
4 7  

Level: 12
1 2 3
6   5
4 7 8

Level: 10
1 2 3
6   4
8 7 5

Level: 6
1 3 5
7 2 8
6 4  

Level: 6
1 3 5
7   2
6 4 8

Level: 7
1 3 5
7 4 2
6   8

Level: 7
1 3 5
  7 2
6 4 8

Level: 8
1 3 5
6 7 2
  4 8

Level: 6
1 5 2
7   3
6 4 8

Level: 7
1 5 2
7 4 3
6   8

Level: 7
1 5 2
  7 3
6 4 8

Level: 8
1 5 2
6 7 3
  4 8

Level: 6
  1 2
7 5 3
6 4 8

Level: 6
1 4 2
7   3
6 8 5

Level: 7
1 4 2
  7 3
6 8 5

Level: 8
1 4 2
6 7 3
  8 5

Level: 6
  1 2
7 4 3
6 8 5

Level: 8
1 2 3
7 8 4
  6 5

Level: 8
2 4 3
7 1 5
  6 8

Level: 10
2 4 3
6   5
1 7 8

Level: 8
  1 3
4 2 5
7 6 8

Level: 8
4 1 3
7 2 5
  6 8

Level: 8
1 2 3
4 5 8
7 6  

Level: 8
1 2 3
7 5 8
  6 4

Level: 10
1 2 3
8 6 4
  7 5

Level: 12
1 2 3
7 4 5
  6 8

Level: 10
2 7 3
1 4 5
  6 8

Level: 12
1 2 3
6 4 5
8 7  

Level: 8
7 1 3
2 4 5
  6 8

Level: 10
1 2 3
7 4 6
  8 5

Level: 8
1 3 5
7 4 2
  6 8

Level: 8
1 5 2
7 4 3
  6 8

Level: 9
2   3
1 7 5
6 4 8

Level: 9
2   3
1 6 5
4 7 8

Level: 9
2   3
1 4 5
7 6 8

Level: 9
1   3
4 2 5
7 6 8

Level: 9
1 2 3
4 5  
7 6 8

Level: 7
2   3
1 7 4
6 8 5

Level: 7
2 4 3
1 5  
7 6 8

Level: 7
2 7 3
1 5  
6 4 8

Level: 9
1   3
6 2 4
8 7 5

Level: 10
1 2 3
6   4
8 7 5

Level: 9
2 7 3
  4 5
1 6 8

Level: 10
2 7 3
1 4 5
  6 8

Level: 11
1   3
6 2 5
4 7 8

Level: 12
1 2 3
6   5
4 7 8

Level: 11
1 2 3
6 5  
4 7 8

Level: 12
1 2 3
6   5
4 7 8

Level: 13
1 2 3
  7 5
6 4 8

Level: 14
1 2 3
6 7 5
  4 8

Level: 13
1 2 3
6 7 5
4   8

Level: 14
1 2 3
6 7 5
  4 8

Level: 13
1 2 3
  6 5
4 7 8

Level: 14
1 2 3
4 6 5
  7 8

Level: 13
1 2 3
4 6 5
7   8

Level: 14
1 2 3
4 6 5
  7 8

Level: 9
7 1 3
  2 5
6 4 8

Level: 10
7 1 3
6 2 5
  4 8

Level: 9
7 1 3
6 2 5
4   8

Level: 10
7 1 3
6 2 5
  4 8

Level: 11
1 2 3
  7 4
6 8 5

Level: 12
1 2 3
6 7 4
  8 5

Level: 11
1 2 3
6 7 4
8   5

Level: 12
1 2 3
6 7 4
  8 5

Level: 11
2 4 3
  6 5
1 7 8

Level: 12
2 4 3
1 6 5
  7 8

Level: 11
2 4 3
1 6 5
7   8

Level: 12
2 4 3
1 6 5
  7 8

Level: 9
1 2 3
  5 8
4 7 6

Level: 10
1 2 3
4 5 8
  7 6

Level: 9
1 2 3
4 5 8
7   6

Level: 10
1 2 3
4 5 8
  7 6

Level: 9
2 7 3
  1 5
6 4 8

Level: 10
2 7 3
6 1 5
  4 8

Level: 9
2 7 3
6 1 5
4   8

Level: 10
2 7 3
6 1 5
  4 8

Level: 11
6 1 3
  2 5
4 7 8

Level: 12
6 1 3
4 2 5
  7 8

Level: 11
6 1 3
4 2 5
7   8

Level: 12
6 1 3
4 2 5
  7 8

Level: 11
1 2 3
  5 8
6 4 7

Level: 12
1 2 3
6 5 8
  4 7

Level: 11
1 2 3
6 5 8
4   7

Level: 12
1 2 3
6 5 8
  4 7

Level: 11
1 2 3
6 4  
8 7 5

Level: 12
1 2 3
6 4 5
8 7  

Level: 13
1 2 3
  4 5
6 8 7

Level: 14
1 2 3
6 4 5
  8 7

Level: 13
1 2 3
6 4 5
8   7

Level: 14
1 2 3
6 4 5
  8 7

Level: 7
2 3 5
1 4  
7 6 8

Level: 7
1 3 5
4 2  
7 6 8

Level: 7
1   2
4 5 3
7 6 8

Level: 7
2 3 5
1 7  
6 4 8

Level: 9
1 3 5
6 2  
4 7 8

Level: 9
1   2
6 5 3
4 7 8

Level: 9
1 2 3
  7 8
6 5 4

Level: 10
1 2 3
6 7 8
  5 4

Level: 9
1 2 3
6 7 8
5   4

Level: 10
1 2 3
6 7 8
  5 4

Level: 9
2 4 3
  1 5
7 6 8

Level: 9
1 2 3
6 8 7
4   5

Level: 10
1 2 3
6 8 7
  4 5

Level: 9
1 2 3
  6 7
4 8 5

Level: 10
1 2 3
4 6 7
  8 5

Level: 9
1 2 3
4 8 6
7   5

Level: 10
1 2 3
4 8 6
  7 5

Level: 9
1 2 3
7 5 8
6   4

Level: 9
1 2 3
7 8 4
6   5

Level: 7
7 1 3
  2 4
6 8 5

Level: 8
7 1 3
6 2 4
  8 5

Level: 11
1 2 3
  6 4
8 7 5

Level: 7
1 3 5
7 2  
6 4 8

Level: 7
1 3 5
7 2 8
6   4

Level: 9
1 3 5
  7 2
6 4 8

Level: 10
1 3 5
6 7 2
  4 8

Level: 9
1 3 5
6 7 2
4   8

Level: 10
1 3 5
6 7 2
  4 8

Level: 7
1   2
7 5 3
6 4 8

Level: 9
1 5 2
  7 3
6 4 8

Level: 10
1 5 2
6 7 3
  4 8

Level: 9
1 5 2
6 7 3
4   8

Level: 10
1 5 2
6 7 3
  4 8

Level: 7
7 1 2
  5 3
6 4 8

Level: 8
7 1 2
6 5 3
  4 8

Level: 7
1   2
7 4 3
6 8 5

Level: 7
1 4 2
7 8 3
6   5

Level: 9
1 4 2
  7 3
6 8 5

Level: 10
1 4 2
6 7 3
  8 5

Level: 9
1 4 2
6 7 3
8   5

Level: 10
1 4 2
6 7 3
  8 5

Level: 7
7 1 2
  4 3
6 8 5

Level: 8
7 1 2
6 4 3
  8 5

Level: 9
1 2 3
  8 4
7 6 5

Level: 9
2 4 3
7 1 5
6   8

Level: 11
2   3
6 4 5
1 7 8

Level: 12
  2 3
6 4 5
1 7 8

Level: 11
2 4 3
6 7 5
1   8

Level: 9
4 1 3
  2 5
7 6 8

Level: 9
4 1 3
7 2 5
6   8

Level: 9
1 2 3
  5 8
7 6 4

Level: 13
1 2 3
  4 5
7 6 8

Level: 13
1 2 3
7 4 5
6   8

Level: 11
2 7 3
1 4 5
6   8

Level: 9
7 1 3
2 4 5
6   8

Level: 11
1 2 3
  4 6
7 8 5

Level: 9
1 3 5
  4 2
7 6 8

Level: 9
1 3 5
7 4 2
6   8

Level: 9
1 5 2
  4 3
7 6 8

Level: 9
1 5 2
7 4 3
6   8

Level: 13
6 2 3
  4 5
1 7 8

Level: 14
6 2 3
1 4 5
  7 8

Level: 8
1 2  
6 7 3
4 8 5

Level: 8
1 2  
4 6 3
7 8 5

Level: 8
1 3  
7 2 5
6 4 8

Level: 8
1 2  
7 5 3
6 4 8

Level: 8
1 2  
7 4 3
6 8 5

Level: 6
1 3  
7 2 4
6 8 5

Level: 12
  2 3
1 7 5
6 4 8

Level: 12
  2 3
1 6 5
4 7 8

Level: 8
7 1 3
6   5
4 2 8

Level: 8
7 1 3
6 2 5
4 8  

Level: 10
  2 3
1 7 4
6 8 5

Level: 8
  4 3
2 1 5
7 6 8

Level: 9
2 4 3
  1 5
7 6 8

Level: 10
  4 3
2 6 5
1 7 8

Level: 8
4 1 3
2   5
7 6 8

Level: 9
4 1 3
2 6 5
7   8

Level: 10
4 1 3
2 6 5
  7 8

Level: 9
4 1 3
  2 5
7 6 8

Level: 8
1 2 3
4   8
7 5 6

Level: 9
1 2 3
  4 8
7 5 6

Level: 8
  7 3
2 1 5
6 4 8

Level: 10
6 1 3
2   5
4 7 8

Level: 10
1 2 3
6   8
4 5 7

Level: 8
  2 3
1 5 8
7 6 4

Level: 9
1 2 3
  5 8
7 6 4

Level: 8
1 2 3
5   8
7 6 4

Level: 9
1 2 3
5 6 8
7   4

Level: 10
1 2 3
5 6 8
  7 4

Level: 9
1 2 3
  5 8
7 6 4

Level: 8
  2 3
1 8 4
7 6 5

Level: 9
1 2 3
  8 4
7 6 5

Level: 8
1 2 3
8   4
7 6 5

Level: 9
1 2 3
  8 4
7 6 5

Level: 10
1 2  
6 4 3
8 7 5

Level: 10
  2 3
1 6 4
8 7 5

Level: 11
1 2 3
  6 4
8 7 5

Level: 12
1 2 3
6   5
8 4 7

Level: 8
7 1 3
2   5
6 4 8

Level: 9
7 1 3
2 4 5
6   8

Level: 8
7 1 3
2 4 5
6 8  

Level: 9
7 1 3
2 4 5
6   8

Level: 8
1 2 3
7   8
6 5 4

Level: 9
1 2 3
7 5 8
6   4

Level: 8
  2 3
1 7 8
6 5 4

Level: 8
1 2 3
7 8 4
6 5  

Level: 9
1 2 3
7 8 4
6   5

Level: 12
  2 3
1 4 5
7 6 8

Level: 13
1 2 3
  4 5
7 6 8

Level: 12
1 2 3
4   5
7 6 8

Level: 13
1 2 3
  4 5
7 6 8

Level: 12
1 2 3
7   5
6 4 8

Level: 13
1 2 3
7 4 5
6   8

Level: 12
1 2 3
7 4 5
6 8  

Level: 13
1 2 3
7 4 5
6   8

Level: 10
2 7 3
1   5
6 4 8

Level: 11
2 7 3
1 4 5
6   8

Level: 10
2 7 3
1 4 5
6 8  

Level: 11
2 7 3
1 4 5
6   8

Level: 10
  2 3
1 4 6
7 8 5

Level: 11
1 2 3
  4 6
7 8 5

Level: 10
1 2 3
4   6
7 8 5

Level: 11
1 2 3
  4 6
7 8 5

Level: 8
1 3 5
7   2
6 4 8

Level: 9
1 3 5
7 4 2
6   8

Level: 8
1 3 5
7 4 2
6 8  

Level: 9
1 3 5
7 4 2
6   8

Level: 8
  3 5
1 7 2
6 4 8

Level: 8
1 5 2
7   3
6 4 8

Level: 9
1 5 2
7 4 3
6   8

Level: 8
1 5 2
7 4 3
6 8  

Level: 9
1 5 2
7 4 3
6   8

Level: 8
  5 2
1 7 3
6 4 8

Level: 8
  4 2
1 7 3
6 8 5

Level: 8
1 4 2
7   3
6 8 5

Level: 10
2 6 3
1   5
4 7 8

Level: 10
2 4 3
1   5
7 6 8

Level: 10
  1 3
4 2 5
7 6 8

Level: 10
1 2 3
4 5 8
7 6  

Level: 8
2 7 3
1   4
6 8 5

Level: 8
2 4 3
1 5 8
7 6  

Level: 8
2 7 3
1 5 8
6 4  

Level: 10
  1 3
6 2 4
8 7 5

Level: 12
  1 3
6 2 5
4 7 8

Level: 12
1 2 3
6 5 8
4 7  

Level: 14
1 2 3
6   5
4 7 8

Level: 10
  1 3
7 2 5
6 4 8

Level: 12
1 2 3
6   4
8 7 5

Level: 12
2 4 3
6   5
1 7 8

Level: 14
1 2 3
6 4 5
8 7  

Level: 8
2 3 5
1 4 8
7 6  

Level: 8
2 3 5
1   4
7 6 8

Level: 9
2 3 5
1 6 4
7   8

Level: 10
2 3 5
1 6 4
  7 8

Level: 8
1 3 5
4 2 8
7 6  

Level: 8
1 3 5
4   2
7 6 8

Level: 9
1 3 5
4 6 2
7   8

Level: 10
1 3 5
4 6 2
  7 8

Level: 9
1 3 5
  4 2
7 6 8

Level: 8
1 5 2
4   3
7 6 8

Level: 9
1 5 2
4 6 3
7   8

Level: 10
1 5 2
4 6 3
  7 8

Level: 9
1 5 2
  4 3
7 6 8

Level: 8
  1 2
4 5 3
7 6 8

Level: 8
2 3 5
1 7 8
6 4  

Level: 8
2 3 5
1   7
6 4 8

Level: 9
2 3 5
1 4 7
6   8

Level: 10
1 3 5
6 2 8
4 7  

Level: 10
1 3 5
6   2
4 7 8

Level: 10
1 5 2
6   3
4 7 8

Level: 10
  1 2
6 5 3
4 7 8

Level: 10
1 2 3
6   8
5 7 4

Level: 10
1 2 3
6 7 8
5 4  

Level: 10
2 4 3
7 1 5
  6 8

Level: 10
1 2 3
6   7
4 8 5

Level: 10
1 2 3
7 5 8
6 4  

Level: 10
1 2 3
7 5 8
  6 4

Level: 10
1 2 3
7 8 4
  6 5

Level: 8
  1 3
7 2 4
6 8 5

Level: 12
1 2 3
8 6 4
  7 5

Level: 8
1 3 5
7 2 8
6 4  

Level: 8
1 3 5
7 2 8
  6 4

Level: 8
  1 2
7 5 3
6 4 8

Level: 8
  1 2
7 4 3
6 8 5

Level: 8
1 4 2
7 8 3
  6 5

Level: 10
1 4 2
6   3
8 7 5

Level: 12
2 4 3
6 7 5
  1 8

Level: 10
4 1 3
7 2 5
  6 8

Level: 14
1 2 3
7 4 5
  6 8

Level: 12
2 7 3
1 4 5
  6 8

Level: 10
7 1 3
2 4 5
  6 8

Level: 12
1 2 3
7 4 6
  8 5

Level: 10
1 3 5
7 4 2
  6 8

Level: 10
1 5 2
7 4 3
  6 8

Level: 14
  2 3
6 4 5
1 7 8

Level: 10
1 2 3
7 4 8
  5 6

Level: 10
1 2 3
5 6 8
7 4  

Level: 10
2 3 5
1 4 7
  6 8

Level: 11
1 2 3
6 7  
4 8 5

Level: 11
1 2 3
4 6  
7 8 5

Level: 7
7   3
2 1 5
6 4 8

Level: 8
  7 3
2 1 5
6 4 8

Level: 7
7 1 3
2 5  
6 4 8

Level: 7
1   3
7 2 8
6 5 4

Level: 7
1 2 3
7 8  
6 5 4

Level: 9
1 2 3
6 7  
8 5 4

Level: 11
1   3
7 2 5
6 4 8

Level: 11
1 2 3
7 5  
6 4 8

Level: 11
1 2 3
7 4  
6 8 5

Level: 9
2 4 3
1 6  
7 8 5

Level: 9
2 7 3
1 4  
6 8 5

Level: 9
1   3
6 2 7
4 8 5

Level: 9
1   3
4 2 6
7 8 5

Level: 9
1   3
7 2 4
6 8 5

Level: 7
1   5
7 3 2
6 4 8

Level: 7
1 5 2
7 3  
6 4 8

Level: 7
1 4 2
7 3  
6 8 5

Level: 8
1 4 2
7 3 5
6 8  

Level: 9
1 4 2
7 3 5
6   8

Level: 8
1 4 2
7   3
6 8 5

Level: 10
1 4 2
7 3 5
  6 8

Level: 11
2 4 3
6 5  
1 7 8

Level: 12
2 4 3
6   5
1 7 8

Level: 11
1 2 3
8 6 4
7   5

Level: 12
1 2 3
8 6 4
  7 5

Level: 9
7 1 3
  4 5
2 6 8

Level: 10
7 1 3
2 4 5
  6 8

Level: 11
1 2 3
7 4 6
8   5

Level: 12
1 2 3
7 4 6
  8 5

Level: 11
1   3
6 2 4
8 7 5

Level: 12
1 2 3
6   4
8 7 5

Level: 11
2 7 3
  4 5
1 6 8

Level: 12
2 7 3
1 4 5
  6 8

Level: 13
1   3
6 2 5
4 7 8

Level: 14
1 2 3
6   5
4 7 8

Level: 13
1 2 3
6 5  
4 7 8

Level: 14
1 2 3
6   5
4 7 8

Level: 15
1 2 3
  7 5
6 4 8

Level: 16
1 2 3
6 7 5
  4 8

Level: 15
1 2 3
6 7 5
4   8

Level: 16
1 2 3
6 7 5
  4 8

Level: 15
1 2 3
  6 5
4 7 8

Level: 16
1 2 3
4 6 5
  7 8

Level: 15
1 2 3
4 6 5
7   8

Level: 16
1 2 3
4 6 5
  7 8

Level: 11
7 1 3
  2 5
6 4 8

Level: 12
7 1 3
6 2 5
  4 8

Level: 11
7 1 3
6 2 5
4   8

Level: 12
7 1 3
6 2 5
  4 8

Level: 13
1 2 3
  7 4
6 8 5

Level: 14
1 2 3
6 7 4
  8 5

Level: 13
1 2 3
6 7 4
8   5

Level: 14
1 2 3
6 7 4
  8 5

Level: 13
2 4 3
  6 5
1 7 8

Level: 14
2 4 3
1 6 5
  7 8

Level: 13
2 4 3
1 6 5
7   8

Level: 14
2 4 3
1 6 5
  7 8

Level: 11
1 2 3
  5 8
4 7 6

Level: 12
1 2 3
4 5 8
  7 6

Level: 11
1 2 3
4 5 8
7   6

Level: 12
1 2 3
4 5 8
  7 6

Level: 11
2 7 3
  1 5
6 4 8

Level: 12
2 7 3
6 1 5
  4 8

Level: 11
2 7 3
6 1 5
4   8

Level: 12
2 7 3
6 1 5
  4 8

Level: 13
6 1 3
  2 5
4 7 8

Level: 14
6 1 3
4 2 5
  7 8

Level: 13
6 1 3
4 2 5
7   8

Level: 14
6 1 3
4 2 5
  7 8

Level: 13
1 2 3
  5 8
6 4 7

Level: 14
1 2 3
6 5 8
  4 7

Level: 13
1 2 3
6 5 8
4   7

Level: 14
1 2 3
6 5 8
  4 7

Level: 13
1 2 3
6 4  
8 7 5

Level: 14
1 2 3
6 4 5
8 7  

Level: 15
1 2 3
  4 5
6 8 7

Level: 16
1 2 3
6 4 5
  8 7

Level: 15
1 2 3
6 4 5
8   7

Level: 16
1 2 3
6 4 5
  8 7

Level: 11
1 2 3
  7 8
6 5 4

Level: 12
1 2 3
6 7 8
  5 4

Level: 11
1 2 3
6 7 8
5   4

Level: 12
1 2 3
6 7 8
  5 4

Level: 11
1 2 3
  8 7
6 4 5

Level: 12
1 2 3
6 8 7
  4 5

Level: 11
1 2 3
6 8 7
4   5

Level: 12
1 2 3
6 8 7
  4 5

Level: 11
1 2 3
  6 7
4 8 5

Level: 12
1 2 3
4 6 7
  8 5

Level: 11
1 2 3
4 6 7
8   5

Level: 12
1 2 3
4 6 7
  8 5

Level: 11
1 2 3
  8 6
4 7 5

Level: 12
1 2 3
4 8 6
  7 5

Level: 11
1 2 3
4 8 6
7   5

Level: 12
1 2 3
4 8 6
  7 5

Level: 9
7 1 3
  2 4
6 8 5

Level: 10
7 1 3
6 2 4
  8 5

Level: 9
7 1 3
6 2 4
8   5

Level: 10
7 1 3
6 2 4
  8 5

Level: 11
1 3 5
  7 2
6 4 8

Level: 12
1 3 5
6 7 2
  4 8

Level: 11
1 3 5
6 7 2
4   8

Level: 12
1 3 5
6 7 2
  4 8

Level: 11
1 5 2
  7 3
6 4 8

Level: 12
1 5 2
6 7 3
  4 8

Level: 11
1 5 2
6 7 3
4   8

Level: 12
1 5 2
6 7 3
  4 8

Level: 9
7 1 2
  5 3
6 4 8

Level: 10
7 1 2
6 5 3
  4 8

Level: 9
7 1 2
6 5 3
4   8

Level: 10
7 1 2
6 5 3
  4 8

Level: 11
1 4 2
  7 3
6 8 5

Level: 12
1 4 2
6 7 3
  8 5

Level: 11
1 4 2
6 7 3
8   5

Level: 12
1 4 2
6 7 3
  8 5

Level: 9
7 1 2
  4 3
6 8 5

Level: 10
7 1 2
6 4 3
  8 5

Level: 9
7 1 2
6 4 3
8   5

Level: 10
7 1 2
6 4 3
  8 5

Level: 13
2   3
6 4 5
1 7 8

Level: 14
  2 3
6 4 5
1 7 8

Level: 15
6 2 3
  4 5
1 7 8

Level: 16
6 2 3
1 4 5
  7 8

Level: 15
6 2 3
1 4 5
7   8

Level: 16
6 2 3
1 4 5
  7 8

Level: 9
1   2
6 7 3
4 8 5

Level: 9
1   2
4 6 3
7 8 5

Level: 9
1 3 5
7 2  
6 4 8

Level: 9
1   2
7 5 3
6 4 8

Level: 9
1   2
7 4 3
6 8 5

Level: 7
1 3 4
7 2  
6 8 5

Level: 8
1 3 4
7 2 5
6 8  

Level: 9
1 3 4
7 2 5
6   8

Level: 10
1 3 4
7 2 5
  6 8

Level: 9
7 1 3
  6 5
4 2 8

Level: 10
7 1 3
4 6 5
  2 8

Level: 11
4 1 3
  6 5
2 7 8

Level: 12
4 1 3
2 6 5
  7 8

Level: 11
4 1 3
2 6 5
7   8

Level: 12
4 1 3
2 6 5
  7 8

Level: 11
6 1 3
2 7 5
4   8

Level: 12
6 1 3
2 7 5
  4 8

Level: 11
1 2 3
  6 8
4 5 7

Level: 12
1 2 3
4 6 8
  5 7

Level: 11
1 2 3
  6 8
5 7 4

Level: 12
1 2 3
5 6 8
  7 4

Level: 11
1 2 3
5 6 8
7   4

Level: 12
1 2 3
5 6 8
  7 4

Level: 9
1 2 3
8 4  
7 6 5

Level: 10
1 2 3
8 4 5
7 6  

Level: 11
1   2
6 4 3
8 7 5

Level: 13
1 2 3
  6 5
8 4 7

Level: 9
1 4 2
7 8 3
6   5

Level: 11
2 6 3
1 7 5
4   8

Level: 12
2 6 3
1 7 5
  4 8

Level: 11
2 6 3
  1 5
4 7 8

Level: 12
2 6 3
4 1 5
  7 8

Level: 11
2 4 3
  1 5
7 6 8

Level: 11
4 1 3
  2 5
7 6 8

Level: 9
2 7 3
1 8 4
6   5

Level: 9
2 7 3
  1 4
6 8 5

Level: 10
2 7 3
6 1 4
  8 5

Level: 9
2 4 3
1 5 8
7   6

Level: 10
2 4 3
1 5 8
  7 6

Level: 9
2 7 3
1 5 8
6   4

Level: 11
6 1 3
  2 4
8 7 5

Level: 13
1 2 3
  6 4
8 7 5

Level: 13
2 4 3
6 7 5
1   8

Level: 9
2 3 5
1 4  
7 6 8

Level: 9
2 3 5
1 4 8
7   6

Level: 10
2 3 5
1 4 8
  7 6

Level: 9
2 3 5
  1 4
7 6 8

Level: 11
2 3 5
  6 4
1 7 8

Level: 12
2 3 5
1 6 4
  7 8

Level: 11
2 3 5
1 6 4
7   8

Level: 12
2 3 5
1 6 4
  7 8

Level: 9
1 3 5
4 2  
7 6 8

Level: 9
1 3 5
4 2 8
7   6

Level: 10
1 3 5
4 2 8
  7 6

Level: 11
1 3 5
  6 2
4 7 8

Level: 12
1 3 5
4 6 2
  7 8

Level: 11
1 3 5
4 6 2
7   8

Level: 12
1 3 5
4 6 2
  7 8

Level: 9
1   2
4 5 3
7 6 8

Level: 11
1 5 2
  6 3
4 7 8

Level: 12
1 5 2
4 6 3
  7 8

Level: 11
1 5 2
4 6 3
7   8

Level: 12
1 5 2
4 6 3
  7 8

Level: 9
4 1 2
  5 3
7 6 8

Level: 9
2 3 5
1 7  
6 4 8

Level: 9
2 3 5
1 7 8
6   4

Level: 9
2 3 5
  1 7
6 4 8

Level: 10
2 3 5
6 1 7
  4 8

Level: 11
1 3 5
6 2  
4 7 8

Level: 11
1 3 5
6 2 8
4   7

Level: 12
1 3 5
6 2 8
  4 7

Level: 11
1   2
6 5 3
4 7 8

Level: 11
6 1 2
  5 3
4 7 8

Level: 12
6 1 2
4 5 3
  7 8

Level: 11
1 2 3
6 7  
5 4 8

Level: 11
2 4 3
7 1 5
6   8

Level: 11
1 2 3
7 5 8
6   4

Level: 11
1 2 3
  5 8
7 6 4

Level: 11
1 2 3
  8 4
7 6 5

Level: 11
1 2 3
7 8 4
6   5

Level: 9
1 3 5
7 2 8
6   4

Level: 9
1 3 5
  2 8
7 6 4

Level: 9
1 4 2
  8 3
7 6 5

Level: 11
1 4 2
  6 3
8 7 5

Level: 11
4 1 3
7 2 5
6   8

Level: 15
1 2 3
  4 5
7 6 8

Level: 15
1 2 3
7 4 5
6   8

Level: 13
2 7 3
1 4 5
6   8

Level: 11
7 1 3
2 4 5
6   8

Level: 13
1 2 3
  4 6
7 8 5

Level: 11
1 3 5
  4 2
7 6 8

Level: 11
1 3 5
7 4 2
6   8

Level: 11
1 5 2
  4 3
7 6 8

Level: 11
1 5 2
7 4 3
6   8

Level: 11
1 2 3
  4 8
7 5 6

Level: 11
1 2 3
5 6  
7 4 8

Level: 11
2 3 5
1 4 7
6   8

Level: 11
1 4 2
  3 5
7 6 8

Level: 11
1 4 2
7 3 5
6   8

Level: 11
1 3 4
  2 5
7 6 8

Level: 11
1 3 4
7 2 5
6   8

Level: 11
1 2 3
8 4 5
7   6

Level: 12
1 2 3
8 4 5
  7 6

Level: 13
1 2 3
  4 5
8 7 6

Level: 10
2 3  
1 7 5
6 4 8

Level: 10
2 3  
1 6 5
4 7 8

Level: 10
2 3  
1 4 5
7 6 8

Level: 10
1 3  
4 2 5
7 6 8

Level: 10
1 2  
4 5 3
7 6 8

Level: 8
2 3  
1 7 4
6 8 5

Level: 8
2 4  
1 5 3
7 6 8

Level: 8
2 7  
1 5 3
6 4 8

Level: 10
1 3  
6 2 4
8 7 5

Level: 10
  7 3
2 4 5
1 6 8

Level: 10
2 7 3
4   5
1 6 8

Level: 11
2 7 3
4 6 5
1   8

Level: 12
1 3  
6 2 5
4 7 8

Level: 12
1 2  
6 5 3
4 7 8

Level: 14
1 2 3
6 7 5
4 8  

Level: 14
1 2 3
4 6 5
7 8  

Level: 12
1 2 3
7   4
6 8 5

Level: 12
1 2 3
6 7 4
8 5  

Level: 12
2 4 3
1 6 5
7 8  

Level: 10
  2 3
1 5 8
4 7 6

Level: 10
1 2 3
5   8
4 7 6

Level: 10
2 7 3
6   5
4 1 8

Level: 10
2 7 3
6 1 5
4 8  

Level: 12
6 1 3
4   5
7 2 8

Level: 13
6 1 3
  4 5
7 2 8

Level: 12
6 1 3
4 2 5
7 8  

Level: 12
  2 3
1 5 8
6 4 7

Level: 12
1 2 3
5   8
6 4 7

Level: 13
1 2 3
5 4 8
6   7

Level: 14
  2 3
1 4 5
6 8 7

Level: 14
1 2 3
4   5
6 8 7

Level: 10
1 2 3
6 8 7
4 5  

Level: 10
  2 3
1 6 7
4 8 5

Level: 10
1 2 3
4 8 6
7 5  

Level: 8
7 1 3
2   4
6 8 5

Level: 8
1 3 5
7   8
6 2 4

Level: 9
1 3 5
7 2 8
6   4

Level: 9
1 3 5
  7 8
6 2 4

Level: 10
1 3 5
6 7 8
  2 4

Level: 10
1 3 5
6 7 2
4 8  

Level: 10
1 5 2
6 7 3
4 8  

Level: 8
7 1 2
5   3
6 4 8

Level: 9
7 1 2
5 4 3
6   8

Level: 8
1 4 2
7 8 3
6 5  

Level: 9
1 4 2
7 8 3
6   5

Level: 10
1 4 2
6 7 3
8 5  

Level: 8
7 1 2
4   3
6 8 5

Level: 10
2 4 3
7   5
6 1 8

Level: 11
2 4 3
7 1 5
6   8

Level: 10
2 4 3
7 1 5
6 8  

Level: 11
2 4 3
7 1 5
6   8

Level: 12
2 3  
6 4 5
1 7 8

Level: 12
2 4 3
6 7 5
1 8  

Level: 13
2 4 3
6 7 5
1   8

Level: 10
4 1 3
7   5
6 2 8

Level: 11
4 1 3
7 2 5
6   8

Level: 11
4 1 3
  7 5
6 2 8

Level: 12
4 1 3
6 7 5
  2 8

Level: 10
4 1 3
7 2 5
6 8  

Level: 11
4 1 3
7 2 5
6   8

Level: 10
  3 5
1 4 2
7 6 8

Level: 11
1 3 5
  4 2
7 6 8

Level: 10
  5 2
1 4 3
7 6 8

Level: 11
1 5 2
  4 3
7 6 8

Level: 14
6 2 3
4   5
1 7 8

Level: 10
  4 3
2 1 5
7 6 8

Level: 11
2 4 3
  1 5
7 6 8

Level: 10
4 1 3
2   5
7 6 8

Level: 11
4 1 3
  2 5
7 6 8

Level: 10
4 1 3
2 6 5
7 8  

Level: 10
  2 3
1 4 8
7 5 6

Level: 11
1 2 3
  4 8
7 5 6

Level: 10
1 2 3
4   8
7 5 6

Level: 11
1 2 3
  4 8
7 5 6

Level: 10
  2 3
1 5 8
7 6 4

Level: 11
1 2 3
  5 8
7 6 4

Level: 10
1 2 3
5   8
7 6 4

Level: 11
1 2 3
  5 8
7 6 4

Level: 10
  2 3
1 8 4
7 6 5

Level: 11
1 2 3
  8 4
7 6 5

Level: 10
1 2 3
8   4
7 6 5

Level: 11
1 2 3
  8 4
7 6 5

Level: 12
  2 3
1 6 4
8 7 5

Level: 13
1 2 3
  6 4
8 7 5

Level: 10
7 1 3
2   5
6 4 8

Level: 11
7 1 3
2 4 5
6   8

Level: 10
7 1 3
2 4 5
6 8  

Level: 11
7 1 3
2 4 5
6   8

Level: 10
1 2 3
7   8
6 5 4

Level: 11
1 2 3
7 5 8
6   4

Level: 10
1 2 3
7 8 4
6 5  

Level: 14
  2 3
1 4 5
7 6 8

Level: 15
1 2 3
  4 5
7 6 8

Level: 14
1 2 3
4   5
7 6 8

Level: 15
1 2 3
  4 5
7 6 8

Level: 14
1 2 3
7   5
6 4 8

Level: 15
1 2 3
7 4 5
6   8

Level: 14
1 2 3
7 4 5
6 8  

Level: 15
1 2 3
7 4 5
6   8

Level: 12
2 7 3
1   5
6 4 8

Level: 13
2 7 3
1 4 5
6   8

Level: 12
2 7 3
1 4 5
6 8  

Level: 13
2 7 3
1 4 5
6   8

Level: 12
  2 3
1 4 6
7 8 5

Level: 13
1 2 3
  4 6
7 8 5

Level: 12
1 2 3
4   6
7 8 5

Level: 13
1 2 3
  4 6
7 8 5

Level: 10
1 3 5
7   2
6 4 8

Level: 11
1 3 5
7 4 2
6   8

Level: 10
1 3 5
7 4 2
6 8  

Level: 11
1 3 5
7 4 2
6   8

Level: 10
1 5 2
7   3
6 4 8

Level: 11
1 5 2
7 4 3
6   8

Level: 10
1 5 2
7 4 3
6 8  

Level: 11
1 5 2
7 4 3
6   8

Level: 10
2 3 5
1   4
7 6 8

Level: 10
2 3 5
1 6 4
7 8  

Level: 10
1 3 5
4   2
7 6 8

Level: 11
1 3 5
  4 2
7 6 8

Level: 10
1 3 5
4 6 2
7 8  

Level: 10
1 5 2
4   3
7 6 8

Level: 11
1 5 2
  4 3
7 6 8

Level: 10
1 5 2
4 6 3
7 8  

Level: 10
2 3 5
1   7
6 4 8

Level: 11
2 3 5
1 4 7
6   8

Level: 10
2 3 5
1 4 7
6 8  

Level: 11
2 3 5
1 4 7
6   8

Level: 12
1 2 3
6   7
4 8 5

Level: 8
7 1 3
2 5 8
6 4  

Level: 8
  1 3
7 2 8
6 5 4

Level: 10
1 2 3
6   7
8 5 4

Level: 11
1 2 3
6 5 7
8   4

Level: 12
1 2 3
6 5 7
  8 4

Level: 12
  1 3
7 2 5
6 4 8

Level: 12
1 2 3
7 5 8
6 4  

Level: 10
2 4 3
1   6
7 8 5

Level: 10
2 7 3
1   4
6 8 5

Level: 10
  1 3
6 2 7
4 8 5

Level: 10
  1 3
4 2 6
7 8 5

Level: 10
  1 3
7 2 4
6 8 5

Level: 8
  1 5
7 3 2
6 4 8

Level: 8
1 5 2
7 3 8
6 4  

Level: 10
1 4 2
7   5
6 3 8

Level: 11
1 4 2
7 3 5
6   8

Level: 11
1 4 2
  7 5
6 3 8

Level: 12
1 4 2
6 7 5
  3 8

Level: 10
1 4 2
7 3 5
6 8  

Level: 11
1 4 2
7 3 5
6   8

Level: 12
2 4 3
6 5 8
1 7  

Level: 10
  1 3
7 4 5
2 6 8

Level: 12
  1 3
6 2 4
8 7 5

Level: 14
  1 3
6 2 5
4 7 8

Level: 14
1 2 3
6 5 8
4 7  

Level: 16
1 2 3
6   5
4 7 8

Level: 14
1 2 3
6   4
8 7 5

Level: 14
2 4 3
6   5
1 7 8

Level: 12
1 2 3
4 5 8
7 6  

Level: 16
1 2 3
6 4 5
8 7  

Level: 12
1 2 3
6   8
5 7 4

Level: 12
1 2 3
6 7 8
5 4  

Level: 12
1 3 5
6   2
4 7 8

Level: 12
1 5 2
6   3
4 7 8

Level: 10
  1 2
7 5 3
6 4 8

Level: 12
1 4 2
6   3
8 7 5

Level: 10
  1 2
7 4 3
6 8 5

Level: 16
  2 3
6 4 5
1 7 8

Level: 10
1 7 2
6   3
4 8 5

Level: 10
  1 2
6 7 3
4 8 5

Level: 10
1 6 2
4   3
7 8 5

Level: 11
1 6 2
  4 3
7 8 5

Level: 10
  1 2
4 6 3
7 8 5

Level: 10
1 3 5
7 2 8
6 4  

Level: 8
1 3 4
7   2
6 8 5

Level: 9
1 3 4
  7 2
6 8 5

Level: 10
1 3 4
6 7 2
  8 5

Level: 10
1 3 4
7   5
6 2 8

Level: 11
1 3 4
7 2 5
6   8

Level: 11
1 3 4
  7 5
6 2 8

Level: 12
1 3 4
6 7 5
  2 8

Level: 10
1 3 4
7 2 5
6 8  

Level: 11
1 3 4
7 2 5
6   8

Level: 10
  1 3
7 6 5
4 2 8

Level: 12
  1 3
4 6 5
2 7 8

Level: 12
4 1 3
6   5
2 7 8

Level: 12
1 2 3
5 6 8
7 4  

Level: 12
  1 2
6 4 3
8 7 5

Level: 14
1 2 3
8 6 5
  4 7

Level: 10
1 4 2
7 8 3
  6 5

Level: 12
2 6 3
1   5
4 7 8

Level: 12
2 4 3
7 1 5
  6 8

Level: 12
  1 3
4 2 5
7 6 8

Level: 12
4 1 3
7 2 5
  6 8

Level: 10
2 7 3
1 8 4
  6 5

Level: 10
2 4 3
1 5 8
7 6  

Level: 10
2 7 3
1 5 8
6 4  

Level: 10
2 7 3
1 5 8
  6 4

Level: 12
6 1 3
8 2 4
  7 5

Level: 14
1 2 3
8 6 4
  7 5

Level: 14
2 4 3
6 7 5
  1 8

Level: 10
2 3 5
1 4 8
7 6  

Level: 10
2 3 5
7 1 4
  6 8

Level: 12
2 3 5
6   4
1 7 8

Level: 10
1 3 5
4 2 8
7 6  

Level: 10
  1 2
4 5 3
7 6 8

Level: 10
4 1 2
7 5 3
  6 8

Level: 10
2 3 5
1 7 8
6 4  

Level: 10
2 3 5
1   8
6 7 4

Level: 10
2 3 5
1 7 8
  6 4

Level: 12
1 3 5
6 2 8
4 7  

Level: 12
  1 2
6 5 3
4 7 8

Level: 12
1 2 3
6   7
5 4 8

Level: 13
1 2 3
6 4 7
5   8

Level: 14
1 2 3
6 4 7
  5 8

Level: 12
1 2 3
7 5 8
  6 4

Level: 12
1 2 3
7 8 4
  6 5

Level: 10
1 3 5
7 2 8
  6 4

Level: 12
1 4 2
8 6 3
  7 5

Level: 16
1 2 3
7 4 5
  6 8

Level: 14
2 7 3
1 4 5
  6 8

Level: 12
7 1 3
2 4 5
  6 8

Level: 14
1 2 3
7 4 6
  8 5

Level: 12
1 3 5
7 4 2
  6 8

Level: 12
1 5 2
7 4 3
  6 8

Level: 12
1 2 3
7 4 8
  5 6

Level: 12
1 2 3
5   6
7 4 8

Level: 13
1 2 3
5 4 6
7   8

Level: 14
1 2 3
5 4 6
  7 8

Level: 13
1 2 3
  5 6
7 4 8

Level: 12
2 3 5
1 4 7
  6 8

Level: 12
1 4 2
7 3 5
  6 8

Level: 12
1 3 4
7 2 5
  6 8

Level: 12
1 2 3
8 4 5
7 6  

Level: 14
1 2 3
8 4 5
  7 6

Level: 12
2 7 3
4 6 5
  1 8

Level: 14
  1 3
6 4 5
7 2 8

Level: 14
6 1 3
7 4 5
  2 8

Level: 14
1 2 3
5 4 8
6 7  

Level: 14
1 2 3
5 4 8
  6 7

Level: 10
7 1 2
5 4 3
  6 8

Level: 12
  1 3
4 7 5
6 2 8

Level: 12
1 2 3
6 5 7
8 4  

Level: 12
1 6 2
7 4 3
  8 5

Level: 14
1 2 3
7 5 6
  4 8

Level: 13
2   3
1 7 5
6 4 8

Level: 13
2   3
1 6 5
4 7 8

Level: 9
7   3
6 1 5
4 2 8

Level: 10
  7 3
6 1 5
4 2 8

Level: 9
7 1 3
6 5  
4 2 8

Level: 9
7 1 3
6 2  
4 8 5

Level: 11
2   3
1 7 4
6 8 5

Level: 9
4   3
2 1 5
7 6 8

Level: 11
4   3
2 6 5
1 7 8

Level: 9
4 1 3
2 5  
7 6 8

Level: 9
1   3
4 2 8
7 5 6

Level: 9
1 2 3
4 8  
7 5 6

Level: 10
1 2 3
4 8 6
7 5  

Level: 11
6   3
2 1 5
4 7 8

Level: 11
6 1 3
2 5  
4 7 8

Level: 11
1   3
6 2 8
4 5 7

Level: 11
1 2 3
6 8  
4 5 7

Level: 9
2   3
1 5 8
7 6 4

Level: 9
1   3
5 2 8
7 6 4

Level: 9
1 2 3
5 8  
7 6 4

Level: 10
1 2 3
5 8 4
7 6  

Level: 9
2   3
1 8 4
7 6 5

Level: 9
1   3
8 2 4
7 6 5

Level: 11
2   3
1 6 4
8 7 5

Level: 13
1   3
6 2 5
8 4 7

Level: 13
1 2 3
6 5  
8 4 7

Level: 9
7 1 3
2 4  
6 8 5

Level: 9
2   3
1 7 8
6 5 4

Level: 13
2   3
1 4 5
7 6 8

Level: 13
1   3
4 2 5
7 6 8

Level: 13
1 2 3
4 5  
7 6 8

Level: 11
2 7 3
1 5  
6 4 8

Level: 11
2   3
1 4 6
7 8 5

Level: 9
1 3 5
7 4  
6 8 2

Level: 9
3   5
1 7 2
6 4 8

Level: 9
1 5 2
7 4  
6 8 3

Level: 9
5   2
1 7 3
6 4 8

Level: 9
4   2
1 7 3
6 8 5

Level: 11
2 6 3
1 5  
4 7 8

Level: 11
2 4 3
1 5  
7 6 8

Level: 9
2   5
1 3 4
7 6 8

Level: 10
2 3 5
1   4
7 6 8

Level: 10
  2 5
1 3 4
7 6 8

Level: 11
1 2 5
  3 4
7 6 8

Level: 12
1 2 5
7 3 4
  6 8

Level: 9
1   5
4 3 2
7 6 8

Level: 9
1 5 2
4 3  
7 6 8

Level: 9
2   5
1 3 7
6 4 8

Level: 10
  2 5
1 3 7
6 4 8

Level: 11
1 2 5
  3 7
6 4 8

Level: 12
1 2 5
6 3 7
  4 8

Level: 11
1   5
6 3 2
4 7 8

Level: 12
1 3 5
6   2
4 7 8

Level: 11
1 5 2
6 3  
4 7 8

Level: 12
1 5 2
6   3
4 7 8

Level: 11
1   3
6 2 8
5 7 4

Level: 12
1 2 3
6   8
5 7 4

Level: 11
1 2 3
6 8  
5 7 4

Level: 12
1 2 3
6 8 4
5 7  

Level: 12
1 2 3
6   8
5 7 4

Level: 11
1 4 2
6 3  
8 7 5

Level: 12
1 4 2
6 3 5
8 7  

Level: 12
1 4 2
6   3
8 7 5

Level: 13
2 4 3
  7 5
6 1 8

Level: 14
2 4 3
6 7 5
  1 8

Level: 11
1 2 3
7 4 8
5   6

Level: 12
1 2 3
7 4 8
  5 6

Level: 11
2 3 5
  4 7
1 6 8

Level: 12
2 3 5
1 4 7
  6 8

Level: 9
7   3
2 1 5
6 4 8

Level: 9
1 4 2
7 3  
6 8 5

Level: 13
2 4 3
6 5  
1 7 8

Level: 14
2 4 3
6   5
1 7 8

Level: 13
1 2 3
8 6 4
7   5

Level: 14
1 2 3
8 6 4
  7 5

Level: 11
7 1 3
  4 5
2 6 8

Level: 12
7 1 3
2 4 5
  6 8

Level: 13
1 2 3
7 4 6
8   5

Level: 14
1 2 3
7 4 6
  8 5

Level: 13
1   3
6 2 4
8 7 5

Level: 14
1 2 3
6   4
8 7 5

Level: 13
2 7 3
  4 5
1 6 8

Level: 14
2 7 3
1 4 5
  6 8

Level: 15
1   3
6 2 5
4 7 8

Level: 16
1 2 3
6   5
4 7 8

Level: 15
1 2 3
6 5  
4 7 8

Level: 16
1 2 3
6   5
4 7 8

Level: 17
1 2 3
  7 5
6 4 8

Level: 18
1 2 3
6 7 5
  4 8

Level: 17
1 2 3
6 7 5
4   8

Level: 18
1 2 3
6 7 5
  4 8

Level: 17
1 2 3
  6 5
4 7 8

Level: 18
1 2 3
4 6 5
  7 8

Level: 17
1 2 3
4 6 5
7   8

Level: 18
1 2 3
4 6 5
  7 8

Level: 13
7 1 3
  2 5
6 4 8

Level: 14
7 1 3
6 2 5
  4 8

Level: 13
7 1 3
6 2 5
4   8

Level: 14
7 1 3
6 2 5
  4 8

Level: 15
1 2 3
  7 4
6 8 5

Level: 16
1 2 3
6 7 4
  8 5

Level: 15
1 2 3
6 7 4
8   5

Level: 16
1 2 3
6 7 4
  8 5

Level: 15
2 4 3
  6 5
1 7 8

Level: 16
2 4 3
1 6 5
  7 8

Level: 15
2 4 3
1 6 5
7   8

Level: 16
2 4 3
1 6 5
  7 8

Level: 13
1 2 3
  5 8
4 7 6

Level: 14
1 2 3
4 5 8
  7 6

Level: 13
1 2 3
4 5 8
7   6

Level: 14
1 2 3
4 5 8
  7 6

Level: 13
2 7 3
  1 5
6 4 8

Level: 14
2 7 3
6 1 5
  4 8

Level: 13
2 7 3
6 1 5
4   8

Level: 14
2 7 3
6 1 5
  4 8

Level: 15
6 1 3
  2 5
4 7 8

Level: 16
6 1 3
4 2 5
  7 8

Level: 15
6 1 3
4 2 5
7   8

Level: 16
6 1 3
4 2 5
  7 8

Level: 15
1 2 3
  5 8
6 4 7

Level: 16
1 2 3
6 5 8
  4 7

Level: 15
1 2 3
6 5 8
4   7

Level: 16
1 2 3
6 5 8
  4 7

Level: 15
1 2 3
6 4  
8 7 5

Level: 16
1 2 3
6 4 5
8 7  

Level: 17
1 2 3
  4 5
6 8 7

Level: 18
1 2 3
6 4 5
  8 7

Level: 17
1 2 3
6 4 5
8   7

Level: 18
1 2 3
6 4 5
  8 7

Level: 13
1 2 3
  7 8
6 5 4

Level: 14
1 2 3
6 7 8
  5 4

Level: 13
1 2 3
6 7 8
5   4

Level: 14
1 2 3
6 7 8
  5 4

Level: 13
1 2 3
  8 7
6 4 5

Level: 14
1 2 3
6 8 7
  4 5

Level: 13
1 2 3
6 8 7
4   5

Level: 14
1 2 3
6 8 7
  4 5

Level: 13
1 2 3
  6 7
4 8 5

Level: 14
1 2 3
4 6 7
  8 5

Level: 13
1 2 3
4 6 7
8   5

Level: 14
1 2 3
4 6 7
  8 5

Level: 13
1 2 3
  8 6
4 7 5

Level: 14
1 2 3
4 8 6
  7 5

Level: 13
1 2 3
4 8 6
7   5

Level: 14
1 2 3
4 8 6
  7 5

Level: 11
7 1 3
  2 4
6 8 5

Level: 12
7 1 3
6 2 4
  8 5

Level: 11
7 1 3
6 2 4
8   5

Level: 12
7 1 3
6 2 4
  8 5

Level: 13
1 3 5
  7 2
6 4 8

Level: 14
1 3 5
6 7 2
  4 8

Level: 13
1 3 5
6 7 2
4   8

Level: 14
1 3 5
6 7 2
  4 8

Level: 13
1 5 2
  7 3
6 4 8

Level: 14
1 5 2
6 7 3
  4 8

Level: 13
1 5 2
6 7 3
4   8

Level: 14
1 5 2
6 7 3
  4 8

Level: 11
7 1 2
  5 3
6 4 8

Level: 12
7 1 2
6 5 3
  4 8

Level: 11
7 1 2
6 5 3
4   8

Level: 12
7 1 2
6 5 3
  4 8

Level: 13
1 4 2
  7 3
6 8 5

Level: 14
1 4 2
6 7 3
  8 5

Level: 13
1 4 2
6 7 3
8   5

Level: 14
1 4 2
6 7 3
  8 5

Level: 11
7 1 2
  4 3
6 8 5

Level: 12
7 1 2
6 4 3
  8 5

Level: 11
7 1 2
6 4 3
8   5

Level: 12
7 1 2
6 4 3
  8 5

Level: 15
2   3
6 4 5
1 7 8

Level: 16
  2 3
6 4 5
1 7 8

Level: 17
6 2 3
  4 5
1 7 8

Level: 18
6 2 3
1 4 5
  7 8

Level: 17
6 2 3
1 4 5
7   8

Level: 18
6 2 3
1 4 5
  7 8

Level: 9
1 3 4
7 2  
6 8 5

Level: 11
7 1 3
  6 5
4 2 8

Level: 12
7 1 3
4 6 5
  2 8

Level: 11
7 1 3
4 6 5
2   8

Level: 12
7 1 3
4 6 5
  2 8

Level: 13
4 1 3
  6 5
2 7 8

Level: 14
4 1 3
2 6 5
  7 8

Level: 13
4 1 3
2 6 5
7   8

Level: 14
4 1 3
2 6 5
  7 8

Level: 13
6 1 3
  7 5
2 4 8

Level: 14
6 1 3
2 7 5
  4 8

Level: 13
6 1 3
2 7 5
4   8

Level: 14
6 1 3
2 7 5
  4 8

Level: 13
1 2 3
  6 8
4 5 7

Level: 14
1 2 3
4 6 8
  5 7

Level: 13
1 2 3
4 6 8
5   7

Level: 14
1 2 3
4 6 8
  5 7

Level: 13
1 2 3
  6 8
5 7 4

Level: 14
1 2 3
5 6 8
  7 4

Level: 13
1 2 3
5 6 8
7   4

Level: 14
1 2 3
5 6 8
  7 4

Level: 11
1 2 3
8 4  
7 6 5

Level: 12
1 2 3
8 4 5
7 6  

Level: 13
2 6 3
  7 5
1 4 8

Level: 14
2 6 3
1 7 5
  4 8

Level: 13
2 6 3
1 7 5
4   8

Level: 14
2 6 3
1 7 5
  4 8

Level: 13
2 6 3
  1 5
4 7 8

Level: 14
2 6 3
4 1 5
  7 8

Level: 13
2 6 3
4 1 5
7   8

Level: 14
2 6 3
4 1 5
  7 8

Level: 11
2 7 3
  1 4
6 8 5

Level: 12
2 7 3
6 1 4
  8 5

Level: 11
2 7 3
6 1 4
8   5

Level: 12
2 7 3
6 1 4
  8 5

Level: 11
2 4 3
  5 8
1 7 6

Level: 12
2 4 3
1 5 8
  7 6

Level: 11
2 4 3
1 5 8
7   6

Level: 12
2 4 3
1 5 8
  7 6

Level: 11
2 3 5
  4 8
1 7 6

Level: 12
2 3 5
1 4 8
  7 6

Level: 11
2 3 5
1 4 8
7   6

Level: 12
2 3 5
1 4 8
  7 6

Level: 13
2 3 5
  6 4
1 7 8

Level: 14
2 3 5
1 6 4
  7 8

Level: 13
2 3 5
1 6 4
7   8

Level: 14
2 3 5
1 6 4
  7 8

Level: 11
1 3 5
  2 8
4 7 6

Level: 12
1 3 5
4 2 8
  7 6

Level: 11
1 3 5
4 2 8
7   6

Level: 12
1 3 5
4 2 8
  7 6

Level: 13
1 3 5
  6 2
4 7 8

Level: 14
1 3 5
4 6 2
  7 8

Level: 13
1 3 5
4 6 2
7   8

Level: 14
1 3 5
4 6 2
  7 8

Level: 13
1 5 2
  6 3
4 7 8

Level: 14
1 5 2
4 6 3
  7 8

Level: 13
1 5 2
4 6 3
7   8

Level: 14
1 5 2
4 6 3
  7 8

Level: 11
2 3 5
  1 7
6 4 8

Level: 12
2 3 5
6 1 7
  4 8

Level: 11
2 3 5
6 1 7
4   8

Level: 12
2 3 5
6 1 7
  4 8

Level: 13
1 3 5
  2 8
6 4 7

Level: 14
1 3 5
6 2 8
  4 7

Level: 13
1 3 5
6 2 8
4   7

Level: 14
1 3 5
6 2 8
  4 7

Level: 13
6 1 2
  5 3
4 7 8

Level: 14
6 1 2
4 5 3
  7 8

Level: 13
6 1 2
4 5 3
7   8

Level: 14
6 1 2
4 5 3
  7 8

Level: 13
1 2 3
8 4 5
7   6

Level: 14
1 2 3
8 4 5
  7 6

Level: 11
2 3 5
1 7  
6 4 8

Level: 11
2 3 5
1 6  
4 7 8

Level: 11
2 3 5
1 4  
7 6 8

Level: 11
1 3 5
4 2  
7 6 8

Level: 11
1   2
4 5 3
7 6 8

Level: 9
2 3 4
1 7  
6 8 5

Level: 10
2 3 4
1 7 5
6 8  

Level: 11
2 3 4
1 7 5
6   8

Level: 12
2 3 4
1   5
6 7 8

Level: 12
2 3 4
1 7 5
  6 8

Level: 9
2   4
1 5 3
7 6 8

Level: 10
  2 4
1 5 3
7 6 8

Level: 11
1 2 4
  5 3
7 6 8

Level: 12
1 2 4
7 5 3
  6 8

Level: 9
2   7
1 5 3
6 4 8

Level: 10
  2 7
1 5 3
6 4 8

Level: 11
1 2 7
  5 3
6 4 8

Level: 12
1 2 7
6 5 3
  4 8

Level: 11
1 3 4
6 2  
8 7 5

Level: 12
1 3 4
6 2 5
8 7  

Level: 11
2   3
4 7 5
1 6 8

Level: 12
  2 3
4 7 5
1 6 8

Level: 13
1 3 5
6 2  
4 7 8

Level: 13
1   2
6 5 3
4 7 8

Level: 13
1 2 3
7 8 4
6   5

Level: 13
1 2 3
7 4  
6 8 5

Level: 11
1 2 3
5 7 8
4   6

Level: 12
1 2 3
5 7 8
  4 6

Level: 11
2   3
6 7 5
4 1 8

Level: 12
  2 3
6 7 5
4 1 8

Level: 11
2 7 3
  6 5
4 1 8

Level: 12
2 7 3
4 6 5
  1 8

Level: 15
1 2 3
4 8 5
6   7

Level: 9
7 1 3
2 8 4
6   5

Level: 11
1 3 5
  7 8
6 2 4

Level: 12
1 3 5
6 7 8
  2 4

Level: 11
1 3 5
6 7 8
2   4

Level: 12
1 3 5
6 7 8
  2 4

Level: 9
7 1 2
4 8 3
6   5

Level: 11
2   3
7 4 5
6 1 8

Level: 12
  2 3
7 4 5
6 1 8

Level: 13
2 3 5
6 4  
1 7 8

Level: 13
4 1 3
  7 5
6 2 8

Level: 14
4 1 3
6 7 5
  2 8

Level: 13
4 1 3
6 7 5
2   8

Level: 14
4 1 3
6 7 5
  2 8

Level: 15
6 2 3
4 7 5
1   8

Level: 11
1 3 5
7 2  
6 4 8

Level: 11
1   2
7 5 3
6 4 8

Level: 11
2 3 5
  1 4
7 6 8

Level: 11
2 3 5
1 4  
6 8 7

Level: 9
7 1 3
2 5 8
6   4

Level: 9
7 1 3
  2 8
6 5 4

Level: 10
7 1 3
6 2 8
  5 4

Level: 11
1 2 3
  6 7
8 5 4

Level: 13
1 2 3
  5 7
6 8 4

Level: 14
1 2 3
6 5 7
  8 4

Level: 13
1 2 3
6 5 7
8   4

Level: 14
1 2 3
6 5 7
  8 4

Level: 13
1 2 3
7 5 8
6   4

Level: 11
2 4 3
1 8 6
7   5

Level: 12
2 4 3
1 8 6
  7 5

Level: 11
2 4 3
  1 6
7 8 5

Level: 11
2 7 3
1 8 4
6   5

Level: 11
6 1 3
  2 7
4 8 5

Level: 12
6 1 3
4 2 7
  8 5

Level: 11
4 1 3
  2 6
7 8 5

Level: 9
7 1 5
  3 2
6 4 8

Level: 10
7 1 5
6 3 2
  4 8

Level: 9
1 5 2
7 3 8
6   4

Level: 11
1   2
7 4 5
6 3 8

Level: 13
1 4 2
  7 5
6 3 8

Level: 14
1 4 2
6 7 5
  3 8

Level: 13
1 4 2
6 7 5
3   8

Level: 14
1 4 2
6 7 5
  3 8

Level: 13
2 4 3
6 5 8
1   7

Level: 11
1   3
7 4 5
2 6 8

Level: 13
6 1 3
  2 4
8 7 5

Level: 15
1 2 3
  6 4
8 7 5

Level: 15
2 4 3
6 7 5
1   8

Level: 13
1 2 3
6 7  
5 4 8

Level: 13
1   2
6 4 3
8 7 5

Level: 13
1 4 2
  6 3
8 7 5

Level: 11
1   2
7 4 3
6 8 5

Level: 11
1   2
6 7 3
4 8 5

Level: 11
1 7 2
6 8 3
4   5

Level: 12
1 7 2
6 8 3
  4 5

Level: 11
1 7 2
  6 3
4 8 5

Level: 12
1 7 2
4 6 3
  8 5

Level: 11
6 1 2
  7 3
4 8 5

Level: 12
6 1 2
4 7 3
  8 5

Level: 11
1   2
4 6 3
7 8 5

Level: 11
1 6 2
4 8 3
7   5

Level: 12
1 6 2
4 8 3
  7 5

Level: 11
4 1 2
  6 3
7 8 5

Level: 11
1 3 5
7 2 8
6   4

Level: 9
1 3 4
7 8 2
6   5

Level: 11
1 3 4
  7 2
6 8 5

Level: 12
1 3 4
6 7 2
  8 5

Level: 11
1 3 4
6 7 2
8   5

Level: 12
1 3 4
6 7 2
  8 5

Level: 13
1 3 4
  7 5
6 2 8

Level: 14
1 3 4
6 7 5
  2 8

Level: 13
1 3 4
6 7 5
2   8

Level: 14
1 3 4
6 7 5
  2 8

Level: 11
1   3
7 6 5
4 2 8

Level: 13
1   3
4 6 5
2 7 8

Level: 13
1 2 3
5 6  
7 4 8

Level: 13
6 1 2
  4 3
8 7 5

Level: 15
1 2 3
  6 5
8 4 7

Level: 11
1 4 2
  8 3
7 6 5

Level: 11
1 4 2
7 8 3
6   5

Level: 13
2 4 3
  1 5
7 6 8

Level: 13
2 4 3
7 1 5
6   8

Level: 13
4 1 3
  2 5
7 6 8

Level: 13
4 1 3
7 2 5
6   8

Level: 11
2 7 3
1 5 8
6   4

Level: 11
2 3 5
7 1 4
6   8

Level: 13
2 3 5
6 7 4
1   8

Level: 11
4 1 2
  5 3
7 6 8

Level: 11
4 1 2
7 5 3
6   8

Level: 11
2 3 5
1 7 8
6   4

Level: 11
2 3 5
  1 8
6 7 4

Level: 12
2 3 5
6 1 8
  7 4

Level: 13
1 2 3
  6 7
5 4 8

Level: 14
1 2 3
5 6 7
  4 8

Level: 15
1 2 3
  4 7
6 5 8

Level: 16
1 2 3
6 4 7
  5 8

Level: 15
1 2 3
6 4 7
5   8

Level: 16
1 2 3
6 4 7
  5 8

Level: 13
1 2 3
  5 8
7 6 4

Level: 13
1 2 3
  8 4
7 6 5

Level: 11
1 3 5
  2 8
7 6 4

Level: 17
1 2 3
  4 5
7 6 8

Level: 17
1 2 3
7 4 5
6   8

Level: 15
2 7 3
1 4 5
6   8

Level: 13
7 1 3
2 4 5
6   8

Level: 15
1 2 3
  4 6
7 8 5

Level: 13
1 3 5
  4 2
7 6 8

Level: 13
1 3 5
7 4 2
6   8

Level: 13
1 5 2
  4 3
7 6 8

Level: 13
1 5 2
7 4 3
6   8

Level: 13
1 2 3
  4 8
7 5 6

Level: 15
1 2 3
  4 6
5 7 8

Level: 16
1 2 3
5 4 6
  7 8

Level: 15
1 2 3
5 4 6
7   8

Level: 16
1 2 3
5 4 6
  7 8

Level: 13
2 3 5
1 4 7
6   8

Level: 13
1 4 2
  3 5
7 6 8

Level: 13
1 4 2
7 3 5
6   8

Level: 13
1 3 4
  2 5
7 6 8

Level: 13
1 3 4
7 2 5
6   8

Level: 15
1 2 3
  4 5
8 7 6

Level: 13
2 7 3
4 6 5
1   8

Level: 15
6 1 3
  4 5
7 2 8

Level: 15
1   3
6 4 5
7 2 8

Level: 15
1 2 3
5 4  
6 7 8

Level: 15
1 2 3
5 4 8
6   7

Level: 11
7 1 2
5 4 3
6   8

Level: 13
1   3
4 7 5
6 2 8

Level: 13
1 6 2
  4 3
7 8 5

Level: 15
1 2 3
  5 6
7 4 8

Level: 11
6 7 3
  1 5
4 2 8

Level: 12
6 7 3
4 1 5
  2 8

Level: 11
1 2 3
5 8 4
7   6

Level: 12
1 2 3
5 8 4
  7 6

Level: 13
1 2 5
  3 4
7 6 8

Level: 13
1 2 5
7 3 4
6   8

Level: 13
1 2 5
  3 7
6 4 8

Level: 14
1 2 5
6 3 7
  4 8

Level: 13
1 2 5
6 3 7
4   8

Level: 14
1 2 5
6 3 7
  4 8

Level: 13
1 2 3
6 8 4
5   7

Level: 14
1 2 3
6 8 4
  5 7

Level: 13
1 4 2
6 3 5
8   7

Level: 14
1 4 2
6 3 5
  8 7

Level: 13
2 3 4
1 7 5
6   8

Level: 13
2 3 4
  1 5
6 7 8

Level: 14
2 3 4
6 1 5
  7 8

Level: 13
1 2 4
  5 3
7 6 8

Level: 13
1 2 4
7 5 3
6   8

Level: 13
1 2 7
  5 3
6 4 8

Level: 14
1 2 7
6 5 3
  4 8

Level: 13
1 2 7
6 5 3
4   8

Level: 14
1 2 7
6 5 3
  4 8

Level: 13
1 3 4
6 2 5
8   7

Level: 14
1 3 4
6 2 5
  8 7

Level: 13
4 2 3
  7 5
1 6 8

Level: 14
4 2 3
1 7 5
  6 8

Level: 13
6 2 3
  7 5
4 1 8

Level: 13
7 2 3
  4 5
6 1 8

Level: 14
7 2 3
6 4 5
  1 8

Level: 15
4 2 3
1 7 5
6   8

Level: 15
7 2 3
6 4 5
1   8

Level: 12
1 2  
6 7 3
4 8 5

Level: 12
1 2  
4 6 3
7 8 5

Level: 8
7 3  
2 1 5
6 4 8

Level: 9
7   3
2 1 5
6 4 8

Level: 8
7 1  
2 5 3
6 4 8

Level: 8
1 3  
7 2 8
6 5 4

Level: 8
1 2  
7 8 3
6 5 4

Level: 10
1 2  
6 7 3
8 5 4

Level: 12
1 3  
7 2 5
6 4 8

Level: 12
1 2  
7 5 3
6 4 8

Level: 12
1 2  
7 4 3
6 8 5

Level: 13
1 2 3
7 4  
6 8 5

Level: 10
2 4  
1 6 3
7 8 5

Level: 10
2 7  
1 4 3
6 8 5

Level: 10
1 3  
6 2 7
4 8 5

Level: 10
1 3  
4 2 6
7 8 5

Level: 10
1 3  
7 2 4
6 8 5

Level: 8
1 5  
7 3 2
6 4 8

Level: 8
1 4  
7 3 2
6 8 5

Level: 9
1 4 2
7 3  
6 8 5

Level: 12
2 4  
6 5 3
1 7 8

Level: 12
1 2 3
8 6 4
7 5  

Level: 10
7 1 3
4   5
2 6 8

Level: 12
1 2 3
7   6
8 4 5

Level: 13
1 2 3
  7 6
8 4 5

Level: 12
1 2 3
7 4 6
8 5  

Level: 16
  2 3
1 7 5
6 4 8

Level: 16
  2 3
1 6 5
4 7 8

Level: 12
7 1 3
6   5
4 2 8

Level: 12
7 1 3
6 2 5
4 8  

Level: 14
  2 3
1 7 4
6 8 5

Level: 14
  4 3
2 6 5
1 7 8

Level: 14
2 4 3
1   5
7 6 8

Level: 12
  7 3
2 1 5
6 4 8

Level: 14
6 1 3
2   5
4 7 8

Level: 14
1 2 3
6   8
4 5 7

Level: 14
1 2  
6 4 3
8 7 5

Level: 16
1 2 3
6   5
8 4 7

Level: 12
  2 3
1 7 8
6 5 4

Level: 12
  2 3
1 8 7
6 4 5

Level: 12
1 2 3
8   7
6 4 5

Level: 13
1 2 3
8 4 7
6   5

Level: 12
1 2 3
4   7
8 6 5

Level: 13
1 2 3
  4 7
8 6 5

Level: 12
1 2 3
4 6 7
8 5  

Level: 12
  2 3
1 8 6
4 7 5

Level: 12
1 2 3
8   6
4 7 5

Level: 10
7 1 3
6   4
8 2 5

Level: 10
7 1 3
6 2 4
8 5  

Level: 12
  3 5
1 7 2
6 4 8

Level: 12
  5 2
1 7 3
6 4 8

Level: 10
7 1 2
6   3
4 5 8

Level: 10
7 1 2
6 5 3
4 8  

Level: 12
  4 2
1 7 3
6 8 5

Level: 12
1 4 2
7   3
6 8 5

Level: 10
7 1 2
6   3
8 4 5

Level: 10
7 1 2
6 4 3
8 5  

Level: 16
6 2 3
1   5
7 4 8

Level: 16
6 2 3
1 4 5
7 8  

Level: 12
6 1 3
2 7 5
4 8  

Level: 12
  2 3
1 6 8
4 5 7

Level: 12
  2 3
1 6 8
5 7 4

Level: 10
1 2  
8 4 3
7 6 5

Level: 14
  2 3
1 6 5
8 4 7

Level: 12
2 6 3
1 7 5
4 8  

Level: 12
  6 3
2 1 5
4 7 8

Level: 10
2 7 3
1 8 4
6 5  

Level: 11
2 7 3
1 8 4
6   5

Level: 10
  7 3
2 1 4
6 8 5

Level: 10
2 4 3
1   8
7 5 6

Level: 10
2 7 3
1   8
6 5 4

Level: 11
2 7 3
1 5 8
6   4

Level: 12
6 1 3
2   4
8 7 5

Level: 13
6 1 3
  2 4
8 7 5

Level: 10
2 3 5
1   8
7 4 6

Level: 10
  3 5
2 1 4
7 6 8

Level: 11
2 3 5
  1 4
7 6 8

Level: 12
  3 5
2 6 4
1 7 8

Level: 10
1 3 5
4   8
7 2 6

Level: 11
1 3 5
  4 8
7 2 6

Level: 12
  3 5
1 6 2
4 7 8

Level: 12
  5 2
1 6 3
4 7 8

Level: 10
4 1 2
5   3
7 6 8

Level: 11
4 1 2
5 6 3
7   8

Level: 12
4 1 2
5 6 3
  7 8

Level: 11
4 1 2
  5 3
7 6 8

Level: 10
  3 5
2 1 7
6 4 8

Level: 12
1 3 5
6   8
4 2 7

Level: 12
6 1 2
5   3
4 7 8

Level: 12
1 2  
6 7 3
5 4 8

Level: 13
1 2 3
6 7  
5 4 8

Level: 10
  3 5
1 2 8
7 6 4

Level: 11
1 3 5
  2 8
7 6 4

Level: 10
1 3 5
2   8
7 6 4

Level: 11
1 3 5
2 6 8
7   4

Level: 12
1 3 5
2 6 8
  7 4

Level: 11
1 3 5
  2 8
7 6 4

Level: 10
  4 2
1 8 3
7 6 5

Level: 11
1 4 2
  8 3
7 6 5

Level: 10
1 4 2
8   3
7 6 5

Level: 11
1 4 2
  8 3
7 6 5

Level: 12
  4 2
1 6 3
8 7 5

Level: 13
1 4 2
  6 3
8 7 5

Level: 12
1 2  
5 6 3
7 4 8

Level: 13
1 2 3
5 6  
7 4 8

Level: 12
  4 2
1 3 5
7 6 8

Level: 13
1 4 2
  3 5
7 6 8

Level: 12
1 4 2
3   5
7 6 8

Level: 13
1 4 2
3 6 5
7   8

Level: 14
1 4 2
3 6 5
  7 8

Level: 13
1 4 2
  3 5
7 6 8

Level: 12
  3 4
1 2 5
7 6 8

Level: 13
1 3 4
  2 5
7 6 8

Level: 12
1 3 4
2   5
7 6 8

Level: 13
1 3 4
2 6 5
7   8

Level: 14
1 3 4
2 6 5
  7 8

Level: 13
1 3 4
  2 5
7 6 8

Level: 12
1 2 3
8   5
7 4 6

Level: 13
1 2 3
  8 5
7 4 6

Level: 14
  2 3
1 4 5
8 7 6

Level: 15
1 2 3
  4 5
8 7 6

Level: 14
1 2 3
4   5
8 7 6

Level: 15
1 2 3
  4 5
8 7 6

Level: 12
2 7 3
4   5
1 6 8

Level: 13
2 7 3
4 6 5
1   8

Level: 12
2 7 3
4 6 5
1 8  

Level: 13
2 7 3
4 6 5
1   8

Level: 14
6 1 3
4   5
7 2 8

Level: 15
6 1 3
  4 5
7 2 8

Level: 14
1 2 3
5   8
6 4 7

Level: 15
1 2 3
5 4 8
6   7

Level: 10
1 3 5
7   8
6 2 4

Level: 11
1 3 5
7 2 8
6   4

Level: 10
  3 5
1 7 8
6 2 4

Level: 10
7 1 2
5   3
6 4 8

Level: 11
7 1 2
5 4 3
6   8

Level: 10
7 1 2
5 4 3
6 8  

Level: 11
7 1 2
5 4 3
6   8

Level: 10
1 4 2
7 8 3
6 5  

Level: 12
2 4 3
7   5
6 1 8

Level: 13
2 4 3
7 1 5
6   8

Level: 12
2 4 3
7 1 5
6 8  

Level: 13
2 4 3
7 1 5
6   8

Level: 14
2 4 3
6 7 5
1 8  

Level: 15
2 4 3
6 7 5
1   8

Level: 12
4 1 3
7   5
6 2 8

Level: 13
4 1 3
7 2 5
6   8

Level: 12
4 1 3
7 2 5
6 8  

Level: 13
4 1 3
7 2 5
6   8

Level: 12
  3 5
1 4 2
7 6 8

Level: 13
1 3 5
  4 2
7 6 8

Level: 12
  5 2
1 4 3
7 6 8

Level: 13
1 5 2
  4 3
7 6 8

Level: 12
  4 3
2 1 5
7 6 8

Level: 12
4 1 3
2   5
7 6 8

Level: 13
4 1 3
  2 5
7 6 8

Level: 12
  2 3
1 4 8
7 5 6

Level: 13
1 2 3
  4 8
7 5 6

Level: 12
1 2 3
4   8
7 5 6

Level: 13
1 2 3
  4 8
7 5 6

Level: 12
  2 3
1 5 8
7 6 4

Level: 13
1 2 3
  5 8
7 6 4

Level: 12
1 2 3
5   8
7 6 4

Level: 13
1 2 3
  5 8
7 6 4

Level: 12
  2 3
1 8 4
7 6 5

Level: 13
1 2 3
  8 4
7 6 5

Level: 12
1 2 3
8   4
7 6 5

Level: 13
1 2 3
  8 4
7 6 5

Level: 14
  2 3
1 6 4
8 7 5

Level: 15
1 2 3
  6 4
8 7 5

Level: 12
7 1 3
2   5
6 4 8

Level: 13
7 1 3
2 4 5
6   8

Level: 12
7 1 3
2 4 5
6 8  

Level: 13
7 1 3
2 4 5
6   8

Level: 12
1 2 3
7   8
6 5 4

Level: 13
1 2 3
7 5 8
6   4

Level: 16
  2 3
1 4 5
7 6 8

Level: 17
1 2 3
  4 5
7 6 8

Level: 16
1 2 3
4   5
7 6 8

Level: 17
1 2 3
  4 5
7 6 8

Level: 16
1 2 3
7   5
6 4 8

Level: 17
1 2 3
7 4 5
6   8

Level: 16
1 2 3
7 4 5
6 8  

Level: 17
1 2 3
7 4 5
6   8

Level: 14
2 7 3
1   5
6 4 8

Level: 15
2 7 3
1 4 5
6   8

Level: 14
2 7 3
1 4 5
6 8  

Level: 15
2 7 3
1 4 5
6   8

Level: 14
  2 3
1 4 6
7 8 5

Level: 15
1 2 3
  4 6
7 8 5

Level: 14
1 2 3
4   6
7 8 5

Level: 15
1 2 3
  4 6
7 8 5

Level: 12
1 3 5
7   2
6 4 8

Level: 13
1 3 5
7 4 2
6   8

Level: 12
1 3 5
7 4 2
6 8  

Level: 13
1 3 5
7 4 2
6   8

Level: 12
1 5 2
7   3
6 4 8

Level: 13
1 5 2
7 4 3
6   8

Level: 12
1 5 2
7 4 3
6 8  

Level: 13
1 5 2
7 4 3
6   8

Level: 12
1 3 5
4   2
7 6 8

Level: 13
1 3 5
  4 2
7 6 8

Level: 12
1 5 2
4   3
7 6 8

Level: 13
1 5 2
  4 3
7 6 8

Level: 12
2 3 5
1   7
6 4 8

Level: 13
2 3 5
1 4 7
6   8

Level: 12
2 3 5
1 4 7
6 8  

Level: 13
2 3 5
1 4 7
6   8

Level: 12
1 2 3
6   7
8 5 4

Level: 12
1 4 2
7   5
6 3 8

Level: 13
1 4 2
7 3 5
6   8

Level: 12
  4 2
1 7 5
6 3 8

Level: 12
1 4 2
7 3 5
6 8  

Level: 13
1 4 2
7 3 5
6   8

Level: 12
  6 2
1 4 3
7 8 5

Level: 13
1 6 2
  4 3
7 8 5

Level: 12
1 6 2
4   3
7 8 5

Level: 13
1 6 2
  4 3
7 8 5

Level: 10
  3 4
1 7 2
6 8 5

Level: 10
1 3 4
7   2
6 8 5

Level: 12
1 3 4
7   5
6 2 8

Level: 13
1 3 4
7 2 5
6   8

Level: 12
  3 4
1 7 5
6 2 8

Level: 12
1 3 4
7 2 5
6 8  

Level: 13
1 3 4
7 2 5
6   8

Level: 14
1 2 3
6   7
5 4 8

Level: 14
1 2 3
6 4 7
5 8  

Level: 14
1 2 3
5   6
7 4 8

Level: 15
1 2 3
  5 6
7 4 8

Level: 14
1 2 3
5 4 6
7 8  

Level: 14
  2 3
1 5 6
7 4 8

Level: 15
1 2 3
  5 6
7 4 8

Level: 14
2 6 3
1   5
4 7 8

Level: 10
7 1 3
6 5 8
4 2  

Level: 10
7 1 3
6   2
4 8 5

Level: 12
2 7 3
1   4
6 8 5

Level: 12
4 6 3
2   5
1 7 8

Level: 13
4 6 3
  2 5
1 7 8

Level: 14
4 6 3
1 2 5
  7 8

Level: 10
4 1 3
2 5 8
7 6  

Level: 10
  1 3
4 2 8
7 5 6

Level: 12
6 1 3
2 5 8
4 7  

Level: 12
  1 3
6 2 8
4 5 7

Level: 12
1 2 3
6 8 7
4 5  

Level: 10
2 5 3
1   8
7 6 4

Level: 11
2 5 3
1 6 8
7   4

Level: 12
2 5 3
1 6 8
  7 4

Level: 10
  1 3
5 2 8
7 6 4

Level: 10
2 8 3
1   4
7 6 5

Level: 11
2 8 3
1 6 4
7   5

Level: 12
2 8 3
1 6 4
  7 5

Level: 10
  1 3
8 2 4
7 6 5

Level: 12
2 6 3
1   4
8 7 5

Level: 14
  1 3
6 2 5
8 4 7

Level: 14
1 2 3
6 5 7
8 4  

Level: 10
7 1 3
2   4
6 8 5

Level: 14
  1 3
4 2 5
7 6 8

Level: 14
1 2 3
4 5 8
7 6  

Level: 12
2 7 3
1 5 8
6 4  

Level: 12
2 4 3
1   6
7 8 5

Level: 10
1 3  
7 4 5
6 8 2

Level: 11
1   3
7 4 5
6 8 2

Level: 10
1 3 5
7   4
6 8 2

Level: 11
1 3 5
  7 4
6 8 2

Level: 12
1 3 5
6 7 4
  8 2

Level: 10
3 7 5
1   2
6 4 8

Level: 11
3 7 5
1 4 2
6   8

Level: 10
1 5 2
7   4
6 8 3

Level: 11
1 5 2
  7 4
6 8 3

Level: 12
1 5 2
6 7 4
  8 3

Level: 10
5 7 2
1   3
6 4 8

Level: 11
5 7 2
1 4 3
6   8

Level: 10
5 2  
1 7 3
6 4 8

Level: 11
5 2 3
1 7  
6 4 8

Level: 10
4 7 2
1   3
6 8 5

Level: 10
4 2  
1 7 3
6 8 5

Level: 11
4 2 3
1 7  
6 8 5

Level: 12
2 6 3
1 5 8
4 7  

Level: 12
2 4 3
1 5 8
7 6  

Level: 12
  2 5
1 3 4
7 6 8

Level: 13
1 2 5
  3 4
7 6 8

Level: 12
1 2 5
3   4
7 6 8

Level: 13
1 2 5
3 6 4
7   8

Level: 14
1 2 5
3 6 4
  7 8

Level: 13
1 2 5
  3 4
7 6 8

Level: 10
  1 5
4 3 2
7 6 8

Level: 10
1 5 2
4 3 8
7 6  

Level: 12
  2 5
1 3 7
6 4 8

Level: 12
1 2 5
3   7
6 4 8

Level: 13
1 2 5
3 4 7
6   8

Level: 12
  1 5
6 3 2
4 7 8

Level: 12
1 5 2
6 3 8
4 7  

Level: 12
  1 3
6 2 8
5 7 4

Level: 12
1 2 3
7 4 8
5 6  

Level: 14
2 4 3
6 5 8
1 7  

Level: 12
  1 3
7 4 5
2 6 8

Level: 14
  1 3
6 2 4
8 7 5

Level: 16
  1 3
6 2 5
4 7 8

Level: 16
1 2 3
6 5 8
4 7  

Level: 18
1 2 3
6   5
4 7 8

Level: 14
  1 3
7 2 5
6 4 8

Level: 16
1 2 3
6   4
8 7 5

Level: 16
2 4 3
6   5
1 7 8

Level: 18
1 2 3
6 4 5
8 7  

Level: 14
1 2 3
6   8
5 7 4

Level: 14
1 2 3
6 7 8
5 4  

Level: 14
1 2 3
6   7
4 8 5

Level: 12
  1 3
7 2 4
6 8 5

Level: 14
1 3 5
6   2
4 7 8

Level: 14
1 5 2
6   3
4 7 8

Level: 12
  1 2
7 5 3
6 4 8

Level: 14
1 4 2
6   3
8 7 5

Level: 12
  1 2
7 4 3
6 8 5

Level: 18
  2 3
6 4 5
1 7 8

Level: 12
  1 3
7 6 5
4 2 8

Level: 14
  1 3
4 6 5
2 7 8

Level: 14
4 1 3
6   5
2 7 8

Level: 14
  1 3
6 7 5
2 4 8

Level: 14
1 2 3
4 6 8
5 7  

Level: 14
1 2 3
5 6 8
7 4  

Level: 12
2 3 5
1 4 8
7 6  

Level: 14
2 3 5
6   4
1 7 8

Level: 12
1 3 5
4 2 8
7 6  

Level: 14
1 3 5
6 2 8
4 7  

Level: 14
  1 2
6 5 3
4 7 8

Level: 14
1 2 3
8 4 5
7 6  

Level: 12
2 3 5
1 7 8
6 4  

Level: 12
2 3 5
1 6 8
4 7  

Level: 12
2 3 5
1   6
4 7 8

Level: 12
  1 2
4 5 3
7 6 8

Level: 10
2 3 4
1   7
6 8 5

Level: 12
2 3 4
1 7 5
6 8  

Level: 13
2 3 4
1 7 5
6   8

Level: 10
2 5 4
1   3
7 6 8

Level: 11
2 5 4
1 6 3
7   8

Level: 12
2 5 4
1 6 3
  7 8

Level: 12
  2 4
1 5 3
7 6 8

Level: 13
1 2 4
  5 3
7 6 8

Level: 12
1 2 4
5   3
7 6 8

Level: 13
1 2 4
5 6 3
7   8

Level: 14
1 2 4
5 6 3
  7 8

Level: 13
1 2 4
  5 3
7 6 8

Level: 10
2 5 7
1   3
6 4 8

Level: 11
2 5 7
1 4 3
6   8

Level: 12
  2 7
1 5 3
6 4 8

Level: 12
1 2 7
5   3
6 4 8

Level: 13
1 2 7
5 4 3
6   8

Level: 12
1 3 4
6   2
8 7 5

Level: 14
1 2 3
7 8 4
  6 5

Level: 12
1 2 3
5 7 8
4 6  

Level: 16
1 2 3
4 8 5
6 7  

Level: 16
1 2 3
4 8 5
  6 7

Level: 10
7 1 3
2 8 4
  6 5

Level: 12
1 3 5
6   8
2 7 4

Level: 12
1 3 5
6 7 8
2 4  

Level: 10
7 1 2
4 8 3
  6 5

Level: 14
2 3 5
6 4 8
1 7  

Level: 14
  1 3
4 7 5
6 2 8

Level: 16
6 2 3
4 7 5
  1 8

Level: 12
1 3 5
7 2 8
6 4  

Level: 12
2 3 5
7 1 4
  6 8

Level: 12
2 3  
1 4 5
6 8 7

Level: 12
2 3 5
1   4
6 8 7

Level: 10
7 1 3
2 5 8
6 4  

Level: 10
7 1 3
2 5 8
  6 4

Level: 10
  1 3
7 2 8
6 5 4

Level: 12
1 2 3
8 6 7
  5 4

Level: 14
1 2 3
7 5 8
6 4  

Level: 14
1 2 3
7 5 8
  6 4

Level: 12
2 4 3
7 1 6
  8 5

Level: 12
2 7 3
1 8 4
  6 5

Level: 12
  1 3
6 2 7
4 8 5

Level: 12
  1 3
4 2 6
7 8 5

Level: 12
4 1 3
7 2 6
  8 5

Level: 10
  1 5
7 3 2
6 4 8

Level: 10
1 5 2
7 3 8
6 4  

Level: 10
1 5 2
7 3 8
  6 4

Level: 12
1 2  
7 4 5
6 3 8

Level: 12
  1 2
7 4 5
6 3 8

Level: 14
1 4 2
6   5
3 7 8

Level: 14
2 4 3
6 5 8
  1 7

Level: 12
1 4 3
7   5
2 6 8

Level: 13
1 4 3
7 6 5
2   8

Level: 14
1 4 3
7 6 5
  2 8

Level: 13
1 4 3
  7 5
2 6 8

Level: 14
1 4 3
2 7 5
  6 8

Level: 15
1 4 3
  6 5
7 2 8

Level: 15
1 4 3
2 7 5
6   8

Level: 14
6 1 3
8 2 4
  7 5

Level: 16
1 2 3
8 6 4
  7 5

Level: 16
2 4 3
6 7 5
  1 8

Level: 14
  1 2
6 4 3
8 7 5

Level: 14
1 4 2
8 6 3
  7 5

Level: 12
1 7 2
6   3
4 8 5

Level: 12
  1 2
6 7 3
4 8 5

Level: 12
  1 2
4 6 3
7 8 5

Level: 12
4 1 2
7 6 3
  8 5

Level: 12
4 1 2
6   3
7 8 5

Level: 12
1 3 5
7 2 8
  6 4

Level: 10
1 3 4
7 8 2
  6 5

Level: 14
1 3 4
6   5
2 7 8

Level: 12
1 6 3
7   5
4 2 8

Level: 13
1 6 3
7 2 5
4   8

Level: 14
1 6 3
7 2 5
  4 8

Level: 13
1 6 3
  7 5
4 2 8

Level: 14
1 6 3
4 7 5
  2 8

Level: 15
1 6 3
  2 5
7 4 8

Level: 14
1 6 3
4   5
2 7 8

Level: 15
1 6 3
  4 5
2 7 8

Level: 16
1 6 3
2 4 5
  7 8

Level: 14
6 1 2
8 4 3
  7 5

Level: 16
1 2 3
8 6 5
  4 7

Level: 12
1 4 2
7 8 3
  6 5

Level: 14
2 4 3
7 1 5
  6 8

Level: 14
4 1 3
7 2 5
  6 8

Level: 12
2 7 3
1 5 8
  6 4

Level: 14
2 3 5
6 7 4
  1 8

Level: 12
4 1 2
7 5 3
  6 8

Level: 12
2 3 5
1   8
6 7 4

Level: 12
2 3 5
1 7 8
  6 4

Level: 18
1 2 3
7 4 5
  6 8

Level: 16
2 7 3
1 4 5
  6 8

Level: 14
7 1 3
2 4 5
  6 8

Level: 16
1 2 3
7 4 6
  8 5

Level: 14
1 3 5
7 4 2
  6 8

Level: 14
1 5 2
7 4 3
  6 8

Level: 14
1 2 3
7 4 8
  5 6

Level: 14
2 3 5
1 4 7
  6 8

Level: 14
1 4 2
7 3 5
  6 8

Level: 14
1 3 4
7 2 5
  6 8

Level: 16
1 2 3
8 4 5
  7 6

Level: 14
2 7 3
4 6 5
  1 8

Level: 16
  1 3
6 4 5
7 2 8

Level: 16
6 1 3
7 4 5
  2 8

Level: 16
1 4 3
6   5
7 2 8

Level: 17
1 4 3
6 2 5
7   8

Level: 18
1 4 3
6 2 5
  7 8

Level: 16
1 2 3
5 4 8
6 7  

Level: 16
1 2 3
5   4
6 7 8

Level: 17
1 2 3
  5 4
6 7 8

Level: 18
1 2 3
6 5 4
  7 8

Level: 16
1 2 3
5 4 8
  6 7

Level: 12
7 1 2
5 4 3
  6 8

Level: 14
1 7 3
4   5
6 2 8

Level: 15
1 7 3
4 2 5
6   8

Level: 15
1 7 3
  4 5
6 2 8

Level: 16
1 7 3
6 4 5
  2 8

Level: 14
1 6 2
7 4 3
  8 5

Level: 16
1 2 3
7 5 6
  4 8

Level: 12
  7 3
6 1 5
4 2 8

Level: 12
6 7 3
1   5
4 2 8

Level: 13
6 7 3
1 2 5
4   8

Level: 14
6 7 3
1 2 5
  4 8

Level: 12
1 2 3
5   4
7 8 6

Level: 13
1 2 3
  5 4
7 8 6

Level: 12
1 2 3
5 8 4
7 6  

Level: 14
1 2 5
7 3 4
  6 8

Level: 14
1 2 3
6   4
5 8 7

Level: 14
1 2 3
6 8 4
5 7  

Level: 14
1 4 2
6 3 5
8 7  

Level: 14
2 3 4
1   5
6 7 8

Level: 14
2 3 4
1 7 5
  6 8

Level: 14
1 2 4
7 5 3
  6 8

Level: 14
1 3 4
6 2 5
8 7  

Level: 14
  2 3
4 7 5
1 6 8

Level: 14
  2 3
6 7 5
4 1 8

Level: 14
  2 3
7 4 5
6 1 8

Level: 16
4 2 3
1   5
6 7 8

Level: 16
4 2 3
1 7 5
  6 8

Level: 16
7 2 3
6 4 5
  1 8

Level: 14
1 2 3
8 7 6
  4 5

Level: 14
1 2 3
8 4 7
  6 5

Level: 12
1 3 5
7 4 8
  2 6

Level: 12
1 3 5
2 6 8
7 4  

Level: 14
1 2 3
7 8 5
  4 6

Level: 14
  6 3
4 2 5
1 7 8

Level: 12
2 5 3
1 6 8
7 4  

Level: 12
1 4 3
7   5
6 8 2

Level: 13
1 4 3
  7 5
6 8 2

Level: 14
1 4 3
6 7 5
  8 2

Level: 12
  1 3
7 4 5
6 8 2

Level: 12
3 7 5
1 4 2
  6 8

Level: 12
5 7 2
1 4 3
  6 8

Level: 12
5 2 3
1 7 8
6 4  

Level: 12
5 2 3
1   7
6 4 8

Level: 13
5 2 3
1 4 7
6   8

Level: 12
4 2 3
1   7
6 8 5

Level: 14
1 2 5
3 4 7
  6 8

Level: 12
2 5 7
1 4 3
  6 8

Level: 14
1 2 7
5 4 3
  6 8

Level: 16
1 4 3
7 6 5
  2 8

Level: 16
1 4 3
2   5
6 7 8

Level: 16
1 4 3
2 7 5
  6 8

Level: 16
1 6 3
7 2 5
  4 8

Level: 16
1 7 3
4 2 5
  6 8

Level: 14
1 2 3
7 5 4
  8 6

Level: 14
5 2 3
1 4 7
  6 8

Level: 11
7   3
2 4 5
1 6 8

Level: 11
2 7 3
4 5  
1 6 8

Level: 15
1 2 3
6 7  
4 8 5

Level: 15
1 2 3
4 6  
7 8 5

Level: 13
1   3
7 2 4
6 8 5

Level: 13
1 2 3
6 7  
8 5 4

Level: 13
2 4 3
1 6  
7 8 5

Level: 11
2   3
1 5 8
4 7 6

Level: 11
1   3
5 2 8
4 7 6

Level: 11
1 2 3
5 8  
4 7 6

Level: 12
1 2 3
5 8 6
4 7  

Level: 11
2 7 3
6 5  
4 1 8

Level: 11
2 7 3
6 1  
4 8 5

Level: 13
6   3
4 1 5
7 2 8

Level: 13
6 1 3
4 5  
7 2 8

Level: 13
6 1 3
4 2  
7 8 5

Level: 13
2   3
1 5 8
6 4 7

Level: 13
1   3
5 2 8
6 4 7

Level: 13
1 2 3
5 8  
6 4 7

Level: 15
2   3
1 4 5
6 8 7

Level: 15
1   3
4 2 5
6 8 7

Level: 15
1 2 3
4 5  
6 8 7

Level: 11
2   3
1 6 7
4 8 5

Level: 9
7   3
2 1 4
6 8 5

Level: 10
7 1 3
2   4
6 8 5

Level: 10
  7 3
2 1 4
6 8 5

Level: 9
1   5
7 3 8
6 2 4

Level: 9
1 3 5
7 8  
6 2 4

Level: 10
1 3 5
7 8 4
6 2  

Level: 11
1 3 5
6 7  
4 8 2

Level: 11
1 5 2
6 7  
4 8 3

Level: 9
7   2
5 1 3
6 4 8

Level: 10
  7 2
5 1 3
6 4 8

Level: 9
7 1 2
5 3  
6 4 8

Level: 9
1 4 2
7 8  
6 5 3

Level: 10
1 4 2
7 8 3
6 5  

Level: 10
1 4 2
7   8
6 5 3

Level: 11
1 4 2
7 5 8
6   3

Level: 11
1 4 2
  7 8
6 5 3

Level: 12
1 4 2
6 7 8
  5 3

Level: 12
1 4 2
7 5 8
  6 3

Level: 11
1 4 2
6 7  
8 5 3

Level: 9
7   2
4 1 3
6 8 5

Level: 10
  7 2
4 1 3
6 8 5

Level: 9
7 1 2
4 3  
6 8 5

Level: 10
7 1 2
4 3 5
6 8  

Level: 11
7 1 2
4 3 5
6   8

Level: 12
7 1 2
4 3 5
  6 8

Level: 11
2 4 3
7 5  
6 1 8

Level: 11
2 4 3
7 1  
6 8 5

Level: 13
2 4 3
6 7  
1 8 5

Level: 11
4   3
7 1 5
6 2 8

Level: 12
  4 3
7 1 5
6 2 8

Level: 11
4 1 3
7 5  
6 2 8

Level: 11
4 1 3
7 2  
6 8 5

Level: 11
3   5
1 4 2
7 6 8

Level: 11
5   2
1 4 3
7 6 8

Level: 15
6   3
4 2 5
1 7 8

Level: 15
6 2 3
4 5  
1 7 8

Level: 11
4 1 3
2 6  
7 8 5

Level: 11
2   3
1 4 8
7 5 6

Level: 11
7 1 3
2 5  
6 4 8

Level: 11
1   3
7 2 8
6 5 4

Level: 11
1 2 3
7 8  
6 5 4

Level: 15
1   3
7 2 5
6 4 8

Level: 15
1 2 3
7 5  
6 4 8

Level: 13
2 7 3
1 4  
6 8 5

Level: 13
1   3
4 2 6
7 8 5

Level: 11
1   5
7 3 2
6 4 8

Level: 11
1 5 2
7 3  
6 4 8

Level: 11
2 3 5
1 6  
7 8 4

Level: 11
1 3 5
4 6  
7 8 2

Level: 11
1 5 2
4 6  
7 8 3

Level: 13
1   3
6 2 7
4 8 5

Level: 11
1   3
6 2 7
8 5 4

Level: 11
1 4 2
7 5  
6 3 8

Level: 11
1 7 2
6 3  
4 8 5

Level: 12
1 7 2
6 3 5
4 8  

Level: 13
1 7 2
6 3 5
4   8

Level: 14
1 7 2
6 3 5
  4 8

Level: 12
1 7 2
6   3
4 8 5

Level: 11
1 6 2
4 3  
7 8 5

Level: 12
1 6 2
4 3 5
7 8  

Level: 13
1 6 2
4 3 5
7   8

Level: 14
1 6 2
4 3 5
  7 8

Level: 9
1   4
7 3 2
6 8 5

Level: 10
1 3 4
7   2
6 8 5

Level: 11
1   4
7 3 5
6 2 8

Level: 11
1 3 4
7 5  
6 2 8

Level: 13
4   3
6 1 5
2 7 8

Level: 14
4 1 3
6   5
2 7 8

Level: 14
  4 3
6 1 5
2 7 8

Level: 13
4 1 3
6 5  
2 7 8

Level: 14
4 1 3
6   5
2 7 8

Level: 15
1 2 3
8 6 5
4   7

Level: 16
1 2 3
8 6 5
  4 7

Level: 11
2 7 3
  8 4
1 6 5

Level: 12
2 7 3
1 8 4
  6 5

Level: 11
2 7 3
  5 8
1 6 4

Level: 12
2 7 3
1 5 8
  6 4

Level: 13
6 1 3
8 2 4
7   5

Level: 14
6 1 3
8 2 4
  7 5

Level: 13
2   5
6 3 4
1 7 8

Level: 14
2 3 5
6   4
1 7 8

Level: 14
  2 5
6 3 4
1 7 8

Level: 11
2   5
1 3 8
6 7 4

Level: 12
2 3 5
1   8
6 7 4

Level: 12
  2 5
1 3 8
6 7 4

Level: 13
1 2 5
  3 8
6 7 4

Level: 14
1 2 5
6 3 8
  7 4

Level: 11
2 3 5
1 8  
6 7 4

Level: 12
2 3 5
1 8 4
6 7  

Level: 12
2 3 5
1   8
6 7 4

Level: 11
2 3 5
  7 8
1 6 4

Level: 12
2 3 5
1 7 8
  6 4

Level: 13
1   3
6 2 7
5 4 8

Level: 14
1 2 3
6   7
5 4 8

Level: 13
1 4 2
8 6 3
7   5

Level: 14
1 4 2
8 6 3
  7 5

Level: 13
1   3
5 2 6
7 4 8

Level: 15
6 1 3
7 4 5
2   8

Level: 16
6 1 3
7 4 5
  2 8

Level: 15
1 2 3
  4 8
5 6 7

Level: 16
1 2 3
5 4 8
  6 7

Level: 11
7 1 2
  4 3
5 6 8

Level: 12
7 1 2
5 4 3
  6 8

Level: 13
1 6 2
7 4 3
8   5

Level: 14
1 6 2
7 4 3
  8 5

Level: 15
1 2 3
7 5 6
4   8

Level: 16
1 2 3
7 5 6
  4 8

Level: 11
7   3
6 1 5
4 2 8

Level: 12
7 1 3
6   5
4 2 8

Level: 12
  7 3
6 1 5
4 2 8

Level: 11
1 2 3
4 8  
7 5 6

Level: 11
1 2 3
5 8  
7 6 4

Level: 12
1 2 3
5 8 4
7 6  

Level: 11
2   5
1 3 4
7 6 8

Level: 11
2   5
1 3 7
6 4 8

Level: 12
  2 5
1 3 7
6 4 8

Level: 13
1   5
6 3 2
4 7 8

Level: 14
1 3 5
6   2
4 7 8

Level: 13
1 5 2
6 3  
4 7 8

Level: 14
1 5 2
6   3
4 7 8

Level: 13
1   3
6 2 8
5 7 4

Level: 14
1 2 3
6   8
5 7 4

Level: 13
1 2 3
6 8  
5 7 4

Level: 14
1 2 3
6 8 4
5 7  

Level: 14
1 2 3
6   8
5 7 4

Level: 13
1 4 2
6 3  
8 7 5

Level: 14
1 4 2
6 3 5
8 7  

Level: 14
1 4 2
6   3
8 7 5

Level: 15
2 4 3
  7 5
6 1 8

Level: 16
2 4 3
6 7 5
  1 8

Level: 13
1 2 3
7 4 8
5   6

Level: 14
1 2 3
7 4 8
  5 6

Level: 13
2 3 5
  4 7
1 6 8

Level: 14
2 3 5
1 4 7
  6 8

Level: 15
2 4 3
6 5  
1 7 8

Level: 16
2 4 3
6   5
1 7 8

Level: 15
1 2 3
8 6 4
7   5

Level: 16
1 2 3
8 6 4
  7 5

Level: 13
7 1 3
  4 5
2 6 8

Level: 14
7 1 3
2 4 5
  6 8

Level: 15
1 2 3
7 4 6
8   5

Level: 16
1 2 3
7 4 6
  8 5

Level: 15
1   3
6 2 4
8 7 5

Level: 16
1 2 3
6   4
8 7 5

Level: 15
2 7 3
  4 5
1 6 8

Level: 16
2 7 3
1 4 5
  6 8

Level: 17
1   3
6 2 5
4 7 8

Level: 18
1 2 3
6   5
4 7 8

Level: 17
1 2 3
6 5  
4 7 8

Level: 18
1 2 3
6   5
4 7 8

Level: 19
1 2 3
  7 5
6 4 8

Level: 20
1 2 3
6 7 5
  4 8

Level: 19
1 2 3
6 7 5
4   8

Level: 20
1 2 3
6 7 5
  4 8

Level: 19
1 2 3
  6 5
4 7 8

Level: 20
1 2 3
4 6 5
  7 8

Level: 19
1 2 3
4 6 5
7   8

Level: 20
1 2 3
4 6 5
  7 8

Level: 15
7 1 3
  2 5
6 4 8

Level: 16
7 1 3
6 2 5
  4 8

Level: 15
7 1 3
6 2 5
4   8

Level: 16
7 1 3
6 2 5
  4 8

Level: 17
1 2 3
  7 4
6 8 5

Level: 18
1 2 3
6 7 4
  8 5

Level: 17
1 2 3
6 7 4
8   5

Level: 18
1 2 3
6 7 4
  8 5

Level: 17
2 4 3
  6 5
1 7 8

Level: 18
2 4 3
1 6 5
  7 8

Level: 17
2 4 3
1 6 5
7   8

Level: 18
2 4 3
1 6 5
  7 8

Level: 15
1 2 3
  5 8
4 7 6

Level: 16
1 2 3
4 5 8
  7 6

Level: 15
1 2 3
4 5 8
7   6

Level: 16
1 2 3
4 5 8
  7 6

Level: 15
2 7 3
  1 5
6 4 8

Level: 16
2 7 3
6 1 5
  4 8

Level: 15
2 7 3
6 1 5
4   8

Level: 16
2 7 3
6 1 5
  4 8

Level: 17
6 1 3
  2 5
4 7 8

Level: 18
6 1 3
4 2 5
  7 8

Level: 17
6 1 3
4 2 5
7   8

Level: 18
6 1 3
4 2 5
  7 8

Level: 17
1 2 3
  5 8
6 4 7

Level: 18
1 2 3
6 5 8
  4 7

Level: 17
1 2 3
6 5 8
4   7

Level: 18
1 2 3
6 5 8
  4 7

Level: 17
1 2 3
6 4  
8 7 5

Level: 18
1 2 3
6 4 5
8 7  

Level: 19
1 2 3
  4 5
6 8 7

Level: 20
1 2 3
6 4 5
  8 7

Level: 19
1 2 3
6 4 5
8   7

Level: 20
1 2 3
6 4 5
  8 7

Level: 15
1 2 3
  7 8
6 5 4

Level: 16
1 2 3
6 7 8
  5 4

Level: 15
1 2 3
6 7 8
5   4

Level: 16
1 2 3
6 7 8
  5 4

Level: 15
1 2 3
  8 7
6 4 5

Level: 16
1 2 3
6 8 7
  4 5

Level: 15
1 2 3
6 8 7
4   5

Level: 16
1 2 3
6 8 7
  4 5

Level: 15
1 2 3
  6 7
4 8 5

Level: 16
1 2 3
4 6 7
  8 5

Level: 15
1 2 3
4 6 7
8   5

Level: 16
1 2 3
4 6 7
  8 5

Level: 15
1 2 3
  8 6
4 7 5

Level: 16
1 2 3
4 8 6
  7 5

Level: 15
1 2 3
4 8 6
7   5

Level: 16
1 2 3
4 8 6
  7 5

Level: 13
7 1 3
  2 4
6 8 5

Level: 14
7 1 3
6 2 4
  8 5

Level: 13
7 1 3
6 2 4
8   5

Level: 14
7 1 3
6 2 4
  8 5

Level: 15
1 3 5
  7 2
6 4 8

Level: 16
1 3 5
6 7 2
  4 8

Level: 15
1 3 5
6 7 2
4   8

Level: 16
1 3 5
6 7 2
  4 8

Level: 15
1 5 2
  7 3
6 4 8

Level: 16
1 5 2
6 7 3
  4 8

Level: 15
1 5 2
6 7 3
4   8

Level: 16
1 5 2
6 7 3
  4 8

Level: 13
7 1 2
  5 3
6 4 8

Level: 14
7 1 2
6 5 3
  4 8

Level: 13
7 1 2
6 5 3
4   8

Level: 14
7 1 2
6 5 3
  4 8

Level: 15
1 4 2
  7 3
6 8 5

Level: 16
1 4 2
6 7 3
  8 5

Level: 15
1 4 2
6 7 3
8   5

Level: 16
1 4 2
6 7 3
  8 5

Level: 13
7 1 2
  4 3
6 8 5

Level: 14
7 1 2
6 4 3
  8 5

Level: 13
7 1 2
6 4 3
8   5

Level: 14
7 1 2
6 4 3
  8 5

Level: 17
2   3
6 4 5
1 7 8

Level: 18
  2 3
6 4 5
1 7 8

Level: 19
6 2 3
  4 5
1 7 8

Level: 20
6 2 3
1 4 5
  7 8

Level: 19
6 2 3
1 4 5
7   8

Level: 20
6 2 3
1 4 5
  7 8

Level: 13
7 1 3
  6 5
4 2 8

Level: 14
7 1 3
4 6 5
  2 8

Level: 13
7 1 3
4 6 5
2   8

Level: 14
7 1 3
4 6 5
  2 8

Level: 15
4 1 3
  6 5
2 7 8

Level: 16
4 1 3
2 6 5
  7 8

Level: 15
4 1 3
2 6 5
7   8

Level: 16
4 1 3
2 6 5
  7 8

Level: 15
6 1 3
  7 5
2 4 8

Level: 16
6 1 3
2 7 5
  4 8

Level: 15
6 1 3
2 7 5
4   8

Level: 16
6 1 3
2 7 5
  4 8

Level: 15
1 2 3
  6 8
4 5 7

Level: 16
1 2 3
4 6 8
  5 7

Level: 15
1 2 3
4 6 8
5   7

Level: 16
1 2 3
4 6 8
  5 7

Level: 15
1 2 3
  6 8
5 7 4

Level: 16
1 2 3
5 6 8
  7 4

Level: 15
1 2 3
5 6 8
7   4

Level: 16
1 2 3
5 6 8
  7 4

Level: 13
1 2 3
8 4  
7 6 5

Level: 14
1 2 3
8 4 5
7 6  

Level: 15
2 6 3
  7 5
1 4 8

Level: 16
2 6 3
1 7 5
  4 8

Level: 15
2 6 3
1 7 5
4   8

Level: 16
2 6 3
1 7 5
  4 8

Level: 15
2 6 3
  1 5
4 7 8

Level: 16
2 6 3
4 1 5
  7 8

Level: 15
2 6 3
4 1 5
7   8

Level: 16
2 6 3
4 1 5
  7 8

Level: 13
2 7 3
  1 4
6 8 5

Level: 14
2 7 3
6 1 4
  8 5

Level: 13
2 7 3
6 1 4
8   5

Level: 14
2 7 3
6 1 4
  8 5

Level: 13
2 4 3
  5 8
1 7 6

Level: 14
2 4 3
1 5 8
  7 6

Level: 13
2 4 3
1 5 8
7   6

Level: 14
2 4 3
1 5 8
  7 6

Level: 13
2 3 5
  4 8
1 7 6

Level: 14
2 3 5
1 4 8
  7 6

Level: 13
2 3 5
1 4 8
7   6

Level: 14
2 3 5
1 4 8
  7 6

Level: 15
2 3 5
  6 4
1 7 8

Level: 16
2 3 5
1 6 4
  7 8

Level: 15
2 3 5
1 6 4
7   8

Level: 16
2 3 5
1 6 4
  7 8

Level: 13
1 3 5
  2 8
4 7 6

Level: 14
1 3 5
4 2 8
  7 6

Level: 13
1 3 5
4 2 8
7   6

Level: 14
1 3 5
4 2 8
  7 6

Level: 15
1 3 5
  6 2
4 7 8

Level: 16
1 3 5
4 6 2
  7 8

Level: 15
1 3 5
4 6 2
7   8

Level: 16
1 3 5
4 6 2
  7 8

Level: 15
1 5 2
  6 3
4 7 8

Level: 16
1 5 2
4 6 3
  7 8

Level: 15
1 5 2
4 6 3
7   8

Level: 16
1 5 2
4 6 3
  7 8

Level: 13
2 3 5
  1 7
6 4 8

Level: 14
2 3 5
6 1 7
  4 8

Level: 13
2 3 5
6 1 7
4   8

Level: 14
2 3 5
6 1 7
  4 8

Level: 15
1 3 5
  2 8
6 4 7

Level: 16
1 3 5
6 2 8
  4 7

Level: 15
1 3 5
6 2 8
4   7

Level: 16
1 3 5
6 2 8
  4 7

Level: 15
6 1 2
  5 3
4 7 8

Level: 16
6 1 2
4 5 3
  7 8

Level: 15
6 1 2
4 5 3
7   8

Level: 16
6 1 2
4 5 3
  7 8

Level: 15
1 2 3
8 4 5
7   6

Level: 16
1 2 3
8 4 5
  7 6

Level: 11
2 3 4
1 7  
6 8 5

Level: 13
2   4
1 3 5
6 7 8

Level: 14
2 3 4
1   5
6 7 8

Level: 14
  2 4
1 3 5
6 7 8

Level: 15
1 2 4
  3 5
6 7 8

Level: 16
1 2 4
6 3 5
  7 8

Level: 13
2 3 4
1 5  
6 7 8

Level: 14
2 3 4
1   5
6 7 8

Level: 13
2 3 4
  7 5
1 6 8

Level: 14
2 3 4
1 7 5
  6 8

Level: 11
2   4
1 5 3
7 6 8

Level: 11
2   7
1 5 3
6 4 8

Level: 12
  2 7
1 5 3
6 4 8

Level: 13
1 3 4
6 2  
8 7 5

Level: 14
1 3 4
6 2 5
8 7  

Level: 13
2   3
4 7 5
1 6 8

Level: 14
  2 3
4 7 5
1 6 8

Level: 13
1 2 3
  7 8
5 4 6

Level: 14
1 2 3
5 7 8
  4 6

Level: 13
1 2 3
5 7 8
4   6

Level: 14
1 2 3
5 7 8
  4 6

Level: 13
2   3
6 7 5
4 1 8

Level: 14
  2 3
6 7 5
4 1 8

Level: 13
2 7 3
  6 5
4 1 8

Level: 14
2 7 3
4 6 5
  1 8

Level: 13
1 3 5
  7 8
6 2 4

Level: 14
1 3 5
6 7 8
  2 4

Level: 13
1 3 5
6 7 8
2   4

Level: 14
1 3 5
6 7 8
  2 4

Level: 13
2   3
7 4 5
6 1 8

Level: 14
  2 3
7 4 5
6 1 8

Level: 15
4 1 3
  7 5
6 2 8

Level: 16
4 1 3
6 7 5
  2 8

Level: 15
4 1 3
6 7 5
2   8

Level: 16
4 1 3
6 7 5
  2 8

Level: 11
7 1 3
  2 8
6 5 4

Level: 12
7 1 3
6 2 8
  5 4

Level: 11
7 1 3
6 2 8
5   4

Level: 12
7 1 3
6 2 8
  5 4

Level: 15
1 2 3
  5 7
6 8 4

Level: 16
1 2 3
6 5 7
  8 4

Level: 15
1 2 3
6 5 7
8   4

Level: 16
1 2 3
6 5 7
  8 4

Level: 13
2 4 3
  8 6
1 7 5

Level: 14
2 4 3
1 8 6
  7 5

Level: 13
2 4 3
1 8 6
7   5

Level: 14
2 4 3
1 8 6
  7 5

Level: 13
6 1 3
  2 7
4 8 5

Level: 14
6 1 3
4 2 7
  8 5

Level: 13
6 1 3
4 2 7
8   5

Level: 14
6 1 3
4 2 7
  8 5

Level: 11
7 1 5
  3 2
6 4 8

Level: 12
7 1 5
6 3 2
  4 8

Level: 11
7 1 5
6 3 2
4   8

Level: 12
7 1 5
6 3 2
  4 8

Level: 15
1 4 2
  7 5
6 3 8

Level: 16
1 4 2
6 7 5
  3 8

Level: 15
1 4 2
6 7 5
3   8

Level: 16
1 4 2
6 7 5
  3 8

Level: 13
1 7 2
  8 3
6 4 5

Level: 14
1 7 2
6 8 3
  4 5

Level: 13
1 7 2
6 8 3
4   5

Level: 14
1 7 2
6 8 3
  4 5

Level: 13
1 7 2
  6 3
4 8 5

Level: 14
1 7 2
4 6 3
  8 5

Level: 13
1 7 2
4 6 3
8   5

Level: 14
1 7 2
4 6 3
  8 5

Level: 13
6 1 2
  7 3
4 8 5

Level: 14
6 1 2
4 7 3
  8 5

Level: 13
6 1 2
4 7 3
8   5

Level: 14
6 1 2
4 7 3
  8 5

Level: 13
1 6 2
  8 3
4 7 5

Level: 14
1 6 2
4 8 3
  7 5

Level: 13
1 6 2
4 8 3
7   5

Level: 14
1 6 2
4 8 3
  7 5

Level: 13
1 3 4
  7 2
6 8 5

Level: 14
1 3 4
6 7 2
  8 5

Level: 13
1 3 4
6 7 2
8   5

Level: 14
1 3 4
6 7 2
  8 5

Level: 15
1 3 4
  7 5
6 2 8

Level: 16
1 3 4
6 7 5
  2 8

Level: 15
1 3 4
6 7 5
2   8

Level: 16
1 3 4
6 7 5
  2 8

Level: 13
2 3 5
  1 8
6 7 4

Level: 14
2 3 5
6 1 8
  7 4

Level: 13
2 3 5
6 1 8
7   4

Level: 14
2 3 5
6 1 8
  7 4

Level: 15
1 2 3
  6 7
5 4 8

Level: 16
1 2 3
5 6 7
  4 8

Level: 15
1 2 3
5 6 7
4   8

Level: 16
1 2 3
5 6 7
  4 8

Level: 17
1 2 3
  4 7
6 5 8

Level: 18
1 2 3
6 4 7
  5 8

Level: 17
1 2 3
6 4 7
5   8

Level: 18
1 2 3
6 4 7
  5 8

Level: 17
1 2 3
  4 6
5 7 8

Level: 18
1 2 3
5 4 6
  7 8

Level: 17
1 2 3
5 4 6
7   8

Level: 18
1 2 3
5 4 6
  7 8

Level: 13
6 7 3
  1 5
4 2 8

Level: 14
6 7 3
4 1 5
  2 8

Level: 13
6 7 3
4 1 5
2   8

Level: 14
6 7 3
4 1 5
  2 8

Level: 13
1 2 3
  8 4
5 7 6

Level: 14
1 2 3
5 8 4
  7 6

Level: 13
1 2 3
5 8 4
7   6

Level: 14
1 2 3
5 8 4
  7 6

Level: 15
1 2 5
  3 7
6 4 8

Level: 16
1 2 5
6 3 7
  4 8

Level: 15
1 2 5
6 3 7
4   8

Level: 16
1 2 5
6 3 7
  4 8

Level: 15
1 2 3
  8 4
6 5 7

Level: 16
1 2 3
6 8 4
  5 7

Level: 15
1 2 3
6 8 4
5   7

Level: 16
1 2 3
6 8 4
  5 7

Level: 15
1 4 2
  3 5
6 8 7

Level: 16
1 4 2
6 3 5
  8 7

Level: 15
1 4 2
6 3 5
8   7

Level: 16
1 4 2
6 3 5
  8 7

Level: 15
2 3 4
  1 5
6 7 8

Level: 16
2 3 4
6 1 5
  7 8

Level: 15
2 3 4
6 1 5
7   8

Level: 16
2 3 4
6 1 5
  7 8

Level: 15
1 2 7
  5 3
6 4 8

Level: 16
1 2 7
6 5 3
  4 8

Level: 15
1 2 7
6 5 3
4   8

Level: 16
1 2 7
6 5 3
  4 8

Level: 15
1 3 4
  2 5
6 8 7

Level: 16
1 3 4
6 2 5
  8 7

Level: 15
1 3 4
6 2 5
8   7

Level: 16
1 3 4
6 2 5
  8 7

Level: 15
4 2 3
  7 5
1 6 8

Level: 16
4 2 3
1 7 5
  6 8

Level: 15
7 2 3
  4 5
6 1 8

Level: 16
7 2 3
6 4 5
  1 8

Level: 13
1   2
6 7 3
4 8 5

Level: 13
1   2
4 6 3
7 8 5

Level: 9
7 3 5
2 1  
6 4 8

Level: 9
7   1
2 5 3
6 4 8

Level: 10
  7 1
2 5 3
6 4 8

Level: 11
2 7 1
  5 3
6 4 8

Level: 12
2 7 1
6 5 3
  4 8

Level: 9
1 3 8
7 2  
6 5 4

Level: 10
1 3 8
7 2 4
6 5  

Level: 11
1 3 8
7 2 4
6   5

Level: 12
1 3 8
7 2 4
  6 5

Level: 9
1   2
7 8 3
6 5 4

Level: 11
1   2
6 7 3
8 5 4

Level: 13
1 3 5
7 2  
6 4 8

Level: 13
1   2
7 5 3
6 4 8

Level: 13
1   2
7 4 3
6 8 5

Level: 11
2   4
1 6 3
7 8 5

Level: 12
  2 4
1 6 3
7 8 5

Level: 13
1 2 4
  6 3
7 8 5

Level: 14
1 2 4
7 6 3
  8 5

Level: 14
1 2 4
6   3
7 8 5

Level: 11
2   7
1 4 3
6 8 5

Level: 12
  2 7
1 4 3
6 8 5

Level: 13
1 2 7
  4 3
6 8 5

Level: 14
1 2 7
6 4 3
  8 5

Level: 11
1 3 7
6 2  
4 8 5

Level: 12
1 3 7
6 2 5
4 8  

Level: 13
1 3 7
6 2 5
4   8

Level: 14
1 3 7
6 2 5
  4 8

Level: 11
1 3 6
4 2  
7 8 5

Level: 12
1 3 6
4 2 5
7 8  

Level: 13
1 3 6
4 2 5
7   8

Level: 14
1 3 6
4 2 5
  7 8

Level: 11
1 3 4
7 2  
6 8 5

Level: 13
2   4
6 5 3
1 7 8

Level: 14
  2 4
6 5 3
1 7 8

Level: 13
1 2 3
7 6  
8 4 5

Level: 14
1 2 3
7 6 5
8 4  

Level: 15
2   3
1 4 5
7 6 8

Level: 15
2 4 3
  1 5
7 6 8

Level: 15
1   2
6 4 3
8 7 5

Level: 17
1 2 3
  6 5
8 4 7

Level: 13
1 2 3
8 7  
6 4 5

Level: 14
1 2 3
8 7 5
6 4  

Level: 13
1 2 3
4 7  
8 6 5

Level: 14
1 2 3
4 7 5
8 6  

Level: 13
1 2 3
4 6  
8 5 7

Level: 13
1 2 3
8 7 6
4   5

Level: 14
1 2 3
8 7 6
  4 5

Level: 13
1 2 3
8 6  
4 7 5

Level: 11
7 1 3
6 4  
8 2 5

Level: 12
7 1 3
6 4 5
8 2  

Level: 11
7 1 3
  6 4
8 2 5

Level: 11
7 1 2
  6 3
4 5 8

Level: 12
7 1 2
4 6 3
  5 8

Level: 13
1 4 2
7 8 3
6   5

Level: 11
7 1 2
  6 3
8 4 5

Level: 17
6 2 3
  1 5
7 4 8

Level: 11
1   2
8 4 3
7 6 5

Level: 11
2 4 3
  1 8
7 5 6

Level: 11
2 7 3
  1 8
6 5 4

Level: 12
2 7 3
6 1 8
  5 4

Level: 13
6 1 3
2 7 4
8   5

Level: 14
6 1 3
2 7 4
  8 5

Level: 13
6 1 3
2 4  
8 7 5

Level: 14
6 1 3
2 4 5
8 7  

Level: 11
2 3 5
  1 8
7 4 6

Level: 13
4 1 2
  6 3
5 7 8

Level: 14
4 1 2
5 6 3
  7 8

Level: 13
4 1 2
5 6 3
7   8

Level: 14
4 1 2
5 6 3
  7 8

Level: 13
1 3 5
  6 8
4 2 7

Level: 14
1 3 5
4 6 8
  2 7

Level: 13
6 1 2
5 7 3
4   8

Level: 14
6 1 2
5 7 3
  4 8

Level: 13
1   2
6 7 3
5 4 8

Level: 13
1 3 5
  6 8
2 7 4

Level: 14
1 3 5
2 6 8
  7 4

Level: 13
1 3 5
2 6 8
7   4

Level: 14
1 3 5
2 6 8
  7 4

Level: 13
1   2
5 6 3
7 4 8

Level: 13
1   2
3 4 5
7 6 8

Level: 15
1 4 2
  6 5
3 7 8

Level: 16
1 4 2
3 6 5
  7 8

Level: 15
1 4 2
3 6 5
7   8

Level: 16
1 4 2
3 6 5
  7 8

Level: 15
1 3 4
  6 5
2 7 8

Level: 16
1 3 4
2 6 5
  7 8

Level: 15
1 3 4
2 6 5
7   8

Level: 16
1 3 4
2 6 5
  7 8

Level: 15
1 2 3
4 7 5
8   6

Level: 16
1 2 3
4 7 5
  8 6

Level: 13
1 3 5
4 2  
7 6 8

Level: 13
1   2
4 5 3
7 6 8

Level: 13
2 3 5
1 7  
6 4 8

Level: 13
2 3 5
1 4  
6 8 7

Level: 13
1 2 3
  6 7
8 5 4

Level: 13
1   2
7 4 5
6 3 8

Level: 13
6   2
1 4 3
7 8 5

Level: 11
1 3 4
7 8 2
6   5

Level: 15
1 2 3
6 7  
5 4 8

Level: 15
1 2 3
6 4  
5 8 7

Level: 15
1 2 3
5 6  
7 4 8

Level: 11
7 1 3
6 5 8
4   2

Level: 12
7 1 3
6 5 8
  4 2

Level: 11
7 1 3
6 8 2
4   5

Level: 12
7 1 3
6 8 2
  4 5

Level: 11
7 1 3
  6 2
4 8 5

Level: 12
7 1 3
4 6 2
  8 5

Level: 13
2 7 3
1 8 4
6   5

Level: 13
4 6 3
2 7 5
1   8

Level: 15
4 6 3
  2 5
1 7 8

Level: 16
4 6 3
1 2 5
  7 8

Level: 15
4 6 3
1 2 5
7   8

Level: 16
4 6 3
1 2 5
  7 8

Level: 11
4 1 3
2 5 8
7   6

Level: 12
4 1 3
2 5 8
  7 6

Level: 11
4 1 3
  2 8
7 5 6

Level: 13
6 1 3
2 5 8
4   7

Level: 14
6 1 3
2 5 8
  4 7

Level: 13
6 1 3
  2 8
4 5 7

Level: 14
6 1 3
4 2 8
  5 7

Level: 11
2 5 3
  1 8
7 6 4

Level: 13
2 5 3
  6 8
1 7 4

Level: 14
2 5 3
1 6 8
  7 4

Level: 13
2 5 3
1 6 8
7   4

Level: 14
2 5 3
1 6 8
  7 4

Level: 11
5 1 3
  2 8
7 6 4

Level: 11
2 8 3
1 4  
7 6 5

Level: 12
2 8 3
1 4 5
7 6  

Level: 11
2 8 3
  1 4
7 6 5

Level: 13
2 8 3
  6 4
1 7 5

Level: 14
2 8 3
1 6 4
  7 5

Level: 13
2 8 3
1 6 4
7   5

Level: 14
2 8 3
1 6 4
  7 5

Level: 11
8 1 3
  2 4
7 6 5

Level: 13
2 6 3
1 7 4
8   5

Level: 14
2 6 3
1 7 4
  8 5

Level: 13
2 6 3
1 4  
8 7 5

Level: 14
2 6 3
1 4 5
8 7  

Level: 13
2 6 3
  1 4
8 7 5

Level: 15
6 1 3
  2 5
8 4 7

Level: 11
7 1 3
2 8 4
6   5

Level: 15
4 1 3
  2 5
7 6 8

Level: 13
2 7 3
1 5 8
6   4

Level: 13
2 4 3
  1 6
7 8 5

Level: 11
1 3 5
7 8 4
6   2

Level: 13
1 3 5
  7 4
6 8 2

Level: 14
1 3 5
6 7 4
  8 2

Level: 13
1 3 5
6 7 4
8   2

Level: 14
1 3 5
6 7 4
  8 2

Level: 11
3 7 5
1 2  
6 4 8

Level: 11
3 7 5
  1 2
6 4 8

Level: 12
3 7 5
6 1 2
  4 8

Level: 11
1   2
7 5 4
6 8 3

Level: 11
1 5 2
7 8 4
6   3

Level: 13
1 5 2
  7 4
6 8 3

Level: 14
1 5 2
6 7 4
  8 3

Level: 13
1 5 2
6 7 4
8   3

Level: 14
1 5 2
6 7 4
  8 3

Level: 11
5 7 2
  1 3
6 4 8

Level: 12
5 7 2
6 1 3
  4 8

Level: 11
4 7 2
1 8 3
6   5

Level: 11
4 7 2
  1 3
6 8 5

Level: 12
4 7 2
6 1 3
  8 5

Level: 13
2 6 3
1 5 8
4   7

Level: 14
2 6 3
1 5 8
  4 7

Level: 13
1 2 5
3 4  
7 6 8

Level: 15
1 2 5
  6 4
3 7 8

Level: 16
1 2 5
3 6 4
  7 8

Level: 15
1 2 5
3 6 4
7   8

Level: 16
1 2 5
3 6 4
  7 8

Level: 11
4 1 5
  3 2
7 6 8

Level: 11
1 5 2
4 3 8
7   6

Level: 12
1 5 2
4 3 8
  7 6

Level: 13
1 2 5
3 7  
6 4 8

Level: 13
6 1 5
  3 2
4 7 8

Level: 14
6 1 5
4 3 2
  7 8

Level: 13
1 5 2
6 3 8
4   7

Level: 14
1 5 2
6 3 8
  4 7

Level: 13
6 1 3
  2 8
5 7 4

Level: 14
6 1 3
5 2 8
  7 4

Level: 13
1 2 3
7 4  
5 6 8

Level: 15
2 4 3
6 5 8
1   7

Level: 13
1   3
7 4 5
2 6 8

Level: 15
6 1 3
  2 4
8 7 5

Level: 17
1 2 3
  6 4
8 7 5

Level: 17
2 4 3
6 7 5
1   8

Level: 15
1 3 5
6 2  
4 7 8

Level: 15
1   2
6 5 3
4 7 8

Level: 15
1 4 2
  6 3
8 7 5

Level: 13
1   3
7 6 5
4 2 8

Level: 15
1   3
4 6 5
2 7 8

Level: 15
1   3
6 7 5
2 4 8

Level: 15
1 2 3
4 6  
5 7 8

Level: 13
2 3 5
1 4  
7 6 8

Level: 15
2 3 5
6 7 4
1   8

Level: 15
2 3 5
6 4  
1 7 8

Level: 13
2 3 5
1 7 8
6   4

Level: 13
2 3 5
1 6  
4 7 8

Level: 13
2 3 5
1 6 8
4   7

Level: 14
2 3 5
1 6 8
  4 7

Level: 13
2 3 5
1 7 6
4   8

Level: 14
2 3 5
1 7 6
  4 8

Level: 13
2 3 5
  1 6
4 7 8

Level: 14
2 3 5
4 1 6
  7 8

Level: 13
4 1 2
  5 3
7 6 8

Level: 11
2 3 4
1 8 7
6   5

Level: 11
2 3 4
  1 7
6 8 5

Level: 12
2 3 4
6 1 7
  8 5

Level: 11
2 5 4
  1 3
7 6 8

Level: 13
2 5 4
  6 3
1 7 8

Level: 14
2 5 4
1 6 3
  7 8

Level: 13
2 5 4
1 6 3
7   8

Level: 14
2 5 4
1 6 3
  7 8

Level: 15
1 2 4
  6 3
5 7 8

Level: 16
1 2 4
5 6 3
  7 8

Level: 15
1 2 4
5 6 3
7   8

Level: 16
1 2 4
5 6 3
  7 8

Level: 11
2 5 7
  1 3
6 4 8

Level: 12
2 5 7
6 1 3
  4 8

Level: 13
1 3 4
  6 2
8 7 5

Level: 15
1 2 3
  8 4
7 6 5

Level: 15
1 2 3
7 8 4
6   5

Level: 13
1 2 3
5 7  
4 6 8

Level: 17
1 2 3
4 8 5
6   7

Level: 13
1 3 5
6 7  
2 4 8

Level: 11
7 1 2
4 8 3
6   5

Level: 15
2 3 5
6 4 8
1   7

Level: 15
1   3
4 7 5
6 2 8

Level: 17
6 2 3
4 7 5
1   8

Level: 13
1 3 5
7 2 8
6   4

Level: 13
2 3 5
  1 4
7 6 8

Level: 13
2 3 5
7 1 4
6   8

Level: 13
2 3 5
1 8 4
6   7

Level: 13
2 3 5
  1 4
6 8 7

Level: 14
2 3 5
6 1 4
  8 7

Level: 11
7 1 3
2 5 8
6   4

Level: 15
1 2 3
7 5 8
6   4

Level: 15
1 2 3
  5 8
7 6 4

Level: 13
4 1 3
  2 6
7 8 5

Level: 11
1 5 2
7 3 8
6   4

Level: 11
1 5 2
  3 8
7 6 4

Level: 13
1 2 5
7 4  
6 3 8

Level: 13
7 1 2
  4 5
6 3 8

Level: 14
7 1 2
6 4 5
  3 8

Level: 15
1   2
6 4 5
3 7 8

Level: 15
1 4 3
7 6 5
2   8

Level: 16
1 4 3
7 6 5
  2 8

Level: 15
1 4 3
  7 5
2 6 8

Level: 16
1 4 3
2 7 5
  6 8

Level: 15
6 1 2
  4 3
8 7 5

Level: 13
4 1 2
  6 3
7 8 5

Level: 13
4 1 2
6 8 3
7   5

Level: 14
4 1 2
6 8 3
  7 5

Level: 13
1 3 5
  2 8
7 6 4

Level: 11
1 3 4
  8 2
7 6 5

Level: 15
1 6 3
7 2 5
4   8

Level: 16
1 6 3
7 2 5
  4 8

Level: 15
1 6 3
  7 5
4 2 8

Level: 16
1 6 3
4 7 5
  2 8

Level: 15
1 6 3
4 7 5
2   8

Level: 16
1 6 3
4 7 5
  2 8

Level: 17
1 6 3
  4 5
2 7 8

Level: 18
1 6 3
2 4 5
  7 8

Level: 17
1 6 3
2 4 5
7   8

Level: 18
1 6 3
2 4 5
  7 8

Level: 13
1 4 2
  8 3
7 6 5

Level: 15
2 4 3
7 1 5
6   8

Level: 15
4 1 3
7 2 5
6   8

Level: 13
4 1 2
7 5 3
6   8

Level: 19
1 2 3
  4 5
7 6 8

Level: 19
1 2 3
7 4 5
6   8

Level: 17
2 7 3
1 4 5
6   8

Level: 15
7 1 3
2 4 5
6   8

Level: 17
1 2 3
  4 6
7 8 5

Level: 15
1 3 5
  4 2
7 6 8

Level: 15
1 3 5
7 4 2
6   8

Level: 15
1 5 2
  4 3
7 6 8

Level: 15
1 5 2
7 4 3
6   8

Level: 15
1 2 3
  4 8
7 5 6

Level: 15
2 3 5
1 4 7
6   8

Level: 15
1 4 2
  3 5
7 6 8

Level: 15
1 4 2
7 3 5
6   8

Level: 15
1 3 4
  2 5
7 6 8

Level: 15
1 3 4
7 2 5
6   8

Level: 17
1 2 3
  4 5
8 7 6

Level: 15
2 7 3
4 6 5
1   8

Level: 17
6 1 3
  4 5
7 2 8

Level: 17
1   3
6 4 5
7 2 8

Level: 17
1 4 3
  6 5
7 2 8

Level: 19
1 4 3
  2 5
6 7 8

Level: 20
1 4 3
6 2 5
  7 8

Level: 19
1 4 3
6 2 5
7   8

Level: 20
1 4 3
6 2 5
  7 8

Level: 17
1 2 3
5 4  
6 7 8

Level: 17
1 2 3
5 4 8
6   7

Level: 17
1 2 3
5 7 4
6   8

Level: 19
1 2 3
  5 4
6 7 8

Level: 20
1 2 3
6 5 4
  7 8

Level: 19
1 2 3
6 5 4
7   8

Level: 20
1 2 3
6 5 4
  7 8

Level: 13
7 1 2
5 4 3
6   8

Level: 17
1 7 3
  4 5
6 2 8

Level: 18
1 7 3
6 4 5
  2 8

Level: 17
1 7 3
6 4 5
2   8

Level: 18
1 7 3
6 4 5
  2 8

Level: 15
1 6 2
  4 3
7 8 5

Level: 17
1 2 3
  5 6
7 4 8

Level: 13
6   3
1 7 5
4 2 8

Level: 15
6 7 3
  2 5
1 4 8

Level: 16
6 7 3
1 2 5
  4 8

Level: 15
6 7 3
1 2 5
4   8

Level: 16
6 7 3
1 2 5
  4 8

Level: 15
1 2 5
  3 4
7 6 8

Level: 15
1 2 5
7 3 4
6   8

Level: 15
1 2 3
  6 4
5 8 7

Level: 16
1 2 3
5 6 4
  8 7

Level: 15
2 3 4
1 7 5
6   8

Level: 15
1 2 4
  5 3
7 6 8

Level: 15
1 2 4
7 5 3
6   8

Level: 17
4 2 3
1 7 5
6   8

Level: 17
4 2 3
  1 5
6 7 8

Level: 18
4 2 3
6 1 5
  7 8

Level: 17
7 2 3
6 4 5
1   8

Level: 15
1 2 3
  7 6
8 4 5

Level: 15
1 2 3
  4 7
8 6 5

Level: 15
1 2 3
8 4 7
6   5

Level: 13
1 3 5
  4 8
7 2 6

Level: 13
1 3 5
2 6  
7 4 8

Level: 15
1 2 3
  8 5
7 4 6

Level: 13
2 5 3
1 6  
7 4 8

Level: 13
1   3
7 4 5
6 8 2

Level: 13
1 4 3
7 8 5
6   2

Level: 15
1 4 3
  7 5
6 8 2

Level: 16
1 4 3
6 7 5
  8 2

Level: 15
1 4 3
6 7 5
8   2

Level: 16
1 4 3
6 7 5
  8 2

Level: 13
7 1 3
  4 5
6 8 2

Level: 14
7 1 3
6 4 5
  8 2

Level: 13
3 7 5
1 4 2
6   8

Level: 13
5 7 2
1 4 3
6   8

Level: 13
5 2 3
1 7  
6 4 8

Level: 13
5 2 3
1 7 8
6   4

Level: 13
5 2 3
  1 7
6 4 8

Level: 14
5 2 3
6 1 7
  4 8

Level: 13
4 2 3
1 8 7
6   5

Level: 13
4 2 3
1 7  
6 8 5

Level: 13
4 2 3
  1 7
6 8 5

Level: 14
4 2 3
6 1 7
  8 5

Level: 15
1 2 5
3 4 7
6   8

Level: 13
2 5 7
1 4 3
6   8

Level: 15
1 2 7
5 4 3
6   8

Level: 17
1   3
2 4 5
6 7 8

Level: 17
1 4 3
2 7 5
6   8

Level: 17
1 6 3
  2 5
7 4 8

Level: 17
1 7 3
4 2 5
6   8

Level: 15
1 2 3
  5 4
7 8 6

Level: 15
5 2 3
1 4 7
6   8

Level: 13
1 2 3
5 8 6
4   7

Level: 14
1 2 3
5 8 6
  4 7

Level: 11
1   2
7 4 8
6 5 3

Level: 13
1 4 2
  7 8
6 5 3

Level: 14
1 4 2
6 7 8
  5 3

Level: 13
1 4 2
6 7 8
5   3

Level: 14
1 4 2
6 7 8
  5 3

Level: 13
1 4 2
  5 8
7 6 3

Level: 13
1 4 2
7 5 8
6   3

Level: 13
7 1 2
4 3 5
6   8

Level: 13
7 4 3
  1 5
6 2 8

Level: 14
7 4 3
6 1 5
  2 8

Level: 15
1 7 2
  3 5
6 4 8

Level: 16
1 7 2
6 3 5
  4 8

Level: 15
1 7 2
6 3 5
4   8

Level: 16
1 7 2
6 3 5
  4 8

Level: 15
1 6 2
  3 5
4 7 8

Level: 16
1 6 2
4 3 5
  7 8

Level: 15
1 6 2
4 3 5
7   8

Level: 16
1 6 2
4 3 5
  7 8

Level: 15
6 4 3
  1 5
2 7 8

Level: 16
6 4 3
2 1 5
  7 8

Level: 15
6 2 5
  3 4
1 7 8

Level: 16
6 2 5
1 3 4
  7 8

Level: 15
1 2 5
  3 8
6 7 4

Level: 16
1 2 5
6 3 8
  7 4

Level: 15
1 2 5
6 3 8
7   4

Level: 16
1 2 5
6 3 8
  7 4

Level: 17
1 2 4
  3 5
6 7 8

Level: 18
1 2 4
6 3 5
  7 8

Level: 17
1 2 4
6 3 5
7   8

Level: 18
1 2 4
6 3 5
  7 8

Level: 13
2 7 1
  5 3
6 4 8

Level: 14
2 7 1
6 5 3
  4 8

Level: 13
2 7 1
6 5 3
4   8

Level: 14
2 7 1
6 5 3
  4 8

Level: 13
1 3 8
  2 4
7 6 5

Level: 13
1 3 8
7 2 4
6   5

Level: 15
1 2 4
  6 3
7 8 5

Level: 15
1 2 4
6 8 3
7   5

Level: 16
1 2 4
6 8 3
  7 5

Level: 15
1 2 7
  4 3
6 8 5

Level: 16
1 2 7
6 4 3
  8 5

Level: 15
1 2 7
6 4 3
8   5

Level: 16
1 2 7
6 4 3
  8 5

Level: 15
1 3 7
  2 5
6 4 8

Level: 16
1 3 7
6 2 5
  4 8

Level: 15
1 3 7
6 2 5
4   8

Level: 16
1 
---------------------------------------------------------------------------
KeyboardInterrupt                         Traceback (most recent call last)
<ipython-input-24-c0f2287c393c> in <module>
      5 
      6 
----> 7 astar(src, target)

<ipython-input-19-81230227caa6> in astar(state, target)
      6         state = frontier.pop(0)
      7         print(f'Level: {state.level}')
----> 8         printGrid(state)
      9 
     10         if state.grid == target:

<ipython-input-17-fd9a53a78f5d> in printGrid(state)
      2     state = state.grid.copy()
      3     state[state.index(-1)] = ' '
----> 4     print(state[0], state[1], state[2])
      5     print(state[3], state[4], state[5])
      6     print(state[6], state[7], state[8])

/opt/conda/lib/python3.7/site-packages/ipykernel/iostream.py in write(self, string)
    398             is_child = (not self._is_master_process())
    399             # only touch the buffer in the IO thread to avoid races
--> 400             self.pub_thread.schedule(lambda : self._buffer.write(string))
    401             if is_child:
    402                 # newlines imply flush in subprocesses

/opt/conda/lib/python3.7/site-packages/ipykernel/iostream.py in schedule(self, f)
    201             self._events.append(f)
    202             # wake event thread (message content is ignored)
--> 203             self._event_pipe.send(b'')
    204         else:
    205             f()

/opt/conda/lib/python3.7/site-packages/zmq/sugar/socket.py in send(self, data, flags, copy, track, routing_id, group)
    398                                  copy_threshold=self.copy_threshold)
    399             data.group = group
--> 400         return super(Socket, self).send(data, flags=flags, copy=copy, track=track)
    401 
    402     def send_multipart(self, msg_parts, flags=0, copy=True, track=False, **kwargs):

zmq/backend/cython/socket.pyx in zmq.backend.cython.socket.Socket.send()

zmq/backend/cython/socket.pyx in zmq.backend.cython.socket.Socket.send()

zmq/backend/cython/socket.pyx in zmq.backend.cython.socket._send_copy()

/opt/conda/lib/python3.7/site-packages/zmq/backend/cython/checkrc.pxd in zmq.backend.cython.checkrc._check_rc()

KeyboardInterrupt: 
 

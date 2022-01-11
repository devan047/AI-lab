8 Puzzle Iterative Breadth First Search
def displayGrid(src):
    state = src.copy()
    state[state.index(-1)] = ' '
    print(state[0], state[1], state[2])
    print(state[3], state[4], state[5])
    print(state[6], state[7], state[8])
    print()


def bfs(src,target):
    queue = [src]
    visited_states = set()
    while len(queue):
        state = queue.pop(0)
        displayGrid(state)
        if state == target:
            print(f"Success")
            return
        for move in possible_moves(state, visited_states):
            if tuple(move) not in queue and tuple(move) not in visited_states:
                queue.append(move)
                visited_states.add(tuple(state))
    print("Fail")
def possible_moves(state, visited_states): 
    b = state.index(-1)  
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
    return [move for move in pos_moves if tuple(move) not in visited_states]
def gen(state, move, blank): 
    temp = state.copy()                              
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
       

bfs(src, target) 
1 2 3
  4 5
6 7 8

  2 3
1 4 5
6 7 8

1 2 3
6 4 5
  7 8

1 2 3
4   5
6 7 8

2   3
1 4 5
6 7 8

1 2 3
6 4 5
7   8

1   3
4 2 5
6 7 8

1 2 3
4 7 5
6   8

1 2 3
4 5  
6 7 8

Success
# Test 2
src = [1,2,3,-1,4,5,6,7,8] 
target=[1,2,3,6,4,5,-1,7,8]
displayGrid(target)


bfs(src, target)
1 2 3
6 4 5
  7 8

1 2 3
  4 5
6 7 8

  2 3
1 4 5
6 7 8

1 2 3
6 4 5
  7 8

Success
 

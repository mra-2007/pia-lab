import heapq

GOAL_STATE = ((1, 2, 3),
              (4, 5, 6),
              (7, 8, 0))

MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def heuristic(state):
    d = 0
    for i in range(3):
        for j in range(3):
            v = state[i][j]
            if v != 0:
                gx = (v - 1) // 3
                gy = (v - 1) % 3
                d += abs(i - gx) + abs(j - gy)
    return d

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def generate_states(state):
    x, y = find_blank(state)
    states = []
    for dx, dy in MOVES:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new = [list(r) for r in state]
            new[x][y], new[nx][ny] = new[nx][ny], new[x][y]
            states.append(tuple(tuple(r) for r in new))
    return states

def a_star(start):
    pq = []
    heapq.heappush(pq, (heuristic(start), 0, start, []))
    visited = set()

    while pq:
        f, g, current, path = heapq.heappop(pq)

        if current == GOAL_STATE:
            return path + [current]

        if current in visited:
            continue

        visited.add(current)

        for n in generate_states(current):
            if n not in visited:
                heapq.heappush(pq,
                    (g + 1 + heuristic(n), g + 1, n, path + [current]))

    return None

START_STATE = ((1, 2, 3),
               (4, 0, 6),
               (7, 5, 8))

solution = a_star(START_STATE)

if solution:
    print("Solution found in", len(solution) - 1, "moves\n")
    for s in solution:
        for r in s:
            print(r)
        print()
else:
    print("No solution found")

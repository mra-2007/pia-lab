def dfs(a, b, visited):
    jug1, jug2, target = 4, 3, 2

    if a == target or b == target:
        print("Goal Reached:", (a, b))
        return True

    if (a, b) in visited:
        return False

    visited.add((a, b))

    return (dfs(jug1, b, visited) or
            dfs(a, jug2, visited) or
            dfs(0, b, visited) or
            dfs(a, 0, visited) or
            dfs(a - min(a, jug2-b), b + min(a, jug2-b), visited) or
            dfs(a + min(b, jug1-a), b - min(b, jug1-a), visited))

dfs(0, 0, set())

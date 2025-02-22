def water_jug_bfs(capacity, goal):
    queue, visited = [(0, 0, [])], {(0, 0)}
    
    while queue:
        x, y, path = queue.pop(0)
        if x == goal or y == goal:
            print("Solution path:")
            for step in path + [(x, y)]:
                print(f"Jug1: {step[0]}, Jug2: {step[1]}")
            return
        
        next_states = [
            (capacity[0], y), (x, capacity[1]), (0, y), (x, 0), 
            (x - min(x, capacity[1] - y), y + min(x, capacity[1] - y)), 
            (x + min(y, capacity[0] - x), y - min(y, capacity[0] - x))
        ]
        
        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append((state[0], state[1], path + [(x, y)]))
    
    print("No solution found.")

def get_input():
    try:
        jug1_capacity = int(input("Enter Jug1 capacity: "))
        jug2_capacity = int(input("Enter Jug2 capacity: "))
        goal = int(input("Enter goal: "))
        if goal > max(jug1_capacity, jug2_capacity):
            print("Goal cannot exceed the capacity of the largest jug.")
        else:
            water_jug_bfs((jug1_capacity, jug2_capacity), goal)
    except ValueError:
        print("Please enter valid integers.")

get_input()

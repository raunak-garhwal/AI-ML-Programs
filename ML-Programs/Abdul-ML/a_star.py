def a_star(start, goal):
    """
    Perform A* search algorithm to find the shortest path from start to goal.

    Args:
        start (tuple): Starting coordinates (x, y).
        goal (tuple): Goal coordinates (x, y).

    Returns:
        list: The path from start to goal, including intermediate steps, or None if no solution is found.
    """
    # Initialize open list with the starting node and heuristic cost
    open_list = [(0 + abs(start[0] - goal[0]) + abs(start[1] - goal[1]), 0, start, [])]  # f = g + h
    closed_list = set()

    while open_list:
        # Pop the node with the smallest f value
        _, g, state, path = open_list.pop(0)

        # Check if the current state is the goal
        if state == goal:
            return path + [state]

        # Process the current state if not already visited
        if state not in closed_list:
            closed_list.add(state)

            # Generate all possible moves (up, down, left, right)
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = state[0] + dx, state[1] + dy

                # Add valid moves to the open list
                open_list.append((
                    g + 1 + abs(nx - goal[0]) + abs(ny - goal[1]),  # f = g + h
                    g + 1,  # Increment g (cost so far)
                    (nx, ny),  # New state
                    path + [state]  # Append current state to path
                ))

            # Sort the open list by f value
            open_list.sort()

    # Return None if no path is found
    return None

def get_input():
    """
    Get user input for starting and goal coordinates.

    Returns:
        tuple: Starting coordinates (x, y) and goal coordinates (x, y).
    """
    start = tuple(map(int, input("Enter starting coordinates (x y): ").split()))
    goal = tuple(map(int, input("Enter goal coordinates (x y): ").split()))
    return start, goal

def main():
    """
    Main function to execute the A* search algorithm with user input.
    """
    print("A* Search Algorithm")
    print("-------------------")

    # Get starting and goal coordinates from the user
    start, goal = get_input()

    # Run A* algorithm
    path = a_star(start, goal)

    # Print the result
    if path:
        print("\nPath found by A*:")
        for step in path:
            print(step)
    else:
        print("\nNo solution found.")

if __name__ == "__main__":
    main()

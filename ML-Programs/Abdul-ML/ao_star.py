def ao_star(start, goal):
    """
    Perform AO* search to find the shortest path from start to goal.

    Args:
        start (tuple): Starting coordinates (x, y).
        goal (tuple): Goal coordinates (x, y).

    Returns:
        list: The path from start to goal, including intermediate steps, or None if no solution is found.
    """
    # Initialize the open list with the starting state and its heuristic cost
    open_list = [(abs(start[0] - goal[0]) + abs(start[1] - goal[1]), start, [])]  # f = h
    closed_list = set()

    while open_list:
        # Pop the node with the smallest heuristic value
        _, state, path = open_list.pop(0)

        # Check if the current state is the goal
        if state == goal:
            return path + [state]

        # Process the current state if not already visited
        if state not in closed_list:
            closed_list.add(state)

            # Generate all possible moves (up, down, left, right)
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = state[0] + dx, state[1] + dy

                # Add the new state to the open list with its heuristic cost
                open_list.append((
                    abs(nx - goal[0]) + abs(ny - goal[1]),  # Heuristic cost (h)
                    (nx, ny),  # New state
                    path + [state]  # Append current state to path
                ))

            # Sort the open list by heuristic cost
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
    Main function to execute the AO* search algorithm with user input.
    """
    print("AO* Search Algorithm")
    print("---------------------")

    # Get starting and goal coordinates from the user
    start, goal = get_input()

    # Run AO* algorithm
    path = ao_star(start, goal)

    # Print the result
    if path:
        print("\nPath found by AO*:")
        for step in path:
            print(step)
    else:
        print("\nNo solution found.")

if __name__ == "__main__":
    main()

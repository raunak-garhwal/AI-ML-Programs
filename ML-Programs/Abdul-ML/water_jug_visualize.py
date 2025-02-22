import tkinter as tk

def visualize_water_jug(jug1_capacity, jug2_capacity, goal):
    def update_canvas(jug1, jug2, step):
        canvas.delete("all")

        # Draw jugs
        canvas.create_rectangle(50, 50, 110, 250, outline="black")
        canvas.create_rectangle(200, 50, 260, 250, outline="black")

        # Fill jugs based on water levels
        canvas.create_rectangle(50, 250 - (jug1 / jug1_capacity) * 200, 110, 250, fill="blue")
        canvas.create_rectangle(200, 250 - (jug2 / jug2_capacity) * 200, 260, 250, fill="blue")

        # Display water levels and step
        canvas.create_text(80, 260, text=f"Jug1: {jug1}/{jug1_capacity}")
        canvas.create_text(230, 260, text=f"Jug2: {jug2}/{jug2_capacity}")
        canvas.create_text(150, 20, text=f"Step: {step}", font=("Arial", 14))

        window.update()

    def bfs():
        queue = [(0, 0, [])]
        visited = set()

        while queue:
            jug1, jug2, path = queue.pop(0)

            if jug1 == goal or jug2 == goal:
                for step, (j1, j2) in enumerate(path + [(jug1, jug2)], start=1):
                    update_canvas(j1, j2, step)
                    window.after(1000)
                return

            if (jug1, jug2) in visited:
                continue

            visited.add((jug1, jug2))

            # Possible transitions
            transitions = [
                (jug1_capacity, jug2),  # Fill Jug1
                (jug1, jug2_capacity),  # Fill Jug2
                (0, jug2),              # Empty Jug1
                (jug1, 0),              # Empty Jug2
                (jug1 - min(jug1, jug2_capacity - jug2), jug2 + min(jug1, jug2_capacity - jug2)),  # Pour Jug1 -> Jug2
                (jug1 + min(jug2, jug1_capacity - jug1), jug2 - min(jug2, jug1_capacity - jug1))   # Pour Jug2 -> Jug1
            ]

            for new_jug1, new_jug2 in transitions:
                if (new_jug1, new_jug2) not in visited:
                    queue.append((new_jug1, new_jug2, path + [(jug1, jug2)]))

        print("No solution found.")

    window = tk.Tk()
    window.title("Water Jug Problem Visualization")
    canvas = tk.Canvas(window, width=300, height=300)
    canvas.pack()

    bfs()
    window.mainloop()

# Get user input
jug1_capacity = int(input("Enter Jug1 capacity: "))
jug2_capacity = int(input("Enter Jug2 capacity: "))
goal = int(input("Enter the goal amount: "))
visualize_water_jug(jug1_capacity, jug2_capacity, goal)

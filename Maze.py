import tkinter as tk
import random

# Constants
CELL_SIZE = 20
MAZE_WIDTH = 40
MAZE_HEIGHT = 30
WALL_COLOR = "black"
PATH_COLOR = "white"
START_COLOR = "green"
END_COLOR = "red"

class MazeApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Maze Game")
        self.canvas = tk.Canvas(master, width=CELL_SIZE * MAZE_WIDTH, height=CELL_SIZE * MAZE_HEIGHT)
        self.canvas.pack()

        # Generate maze
        self.maze = self.generate_maze(MAZE_WIDTH, MAZE_HEIGHT)

        # Draw maze
        self.draw_maze()

        # Mark start and end points
        self.start_x, self.start_y = random.randint(0, MAZE_WIDTH - 1), random.randint(0, MAZE_HEIGHT - 1)
        self.end_x, self.end_y = random.randint(0, MAZE_WIDTH - 1), random.randint(0, MAZE_HEIGHT - 1)
        while self.maze[self.start_y][self.start_x] == 1 or self.maze[self.end_y][self.end_x] == 1:
            self.start_x, self.start_y = random.randint(0, MAZE_WIDTH - 1), random.randint(0, MAZE_HEIGHT - 1)
            self.end_x, self.end_y = random.randint(0, MAZE_WIDTH - 1), random.randint(0, MAZE_HEIGHT - 1)
        self.canvas.create_rectangle(self.start_x * CELL_SIZE, self.start_y * CELL_SIZE,
                                      (self.start_x + 1) * CELL_SIZE, (self.start_y + 1) * CELL_SIZE,
                                      fill=START_COLOR, outline="")
        self.canvas.create_rectangle(self.end_x * CELL_SIZE, self.end_y * CELL_SIZE,
                                      (self.end_x + 1) * CELL_SIZE, (self.end_y + 1) * CELL_SIZE,
                                      fill=END_COLOR, outline="")

        # Bind arrow keys for movement
        self.master.bind("<Left>", self.move_left)
        self.master.bind("<Right>", self.move_right)
        self.master.bind("<Up>", self.move_up)
        self.master.bind("<Down>", self.move_down)

        # Initial player position
        self.player_x, self.player_y = self.start_x, self.start_y
        self.player = self.canvas.create_oval(self.player_x * CELL_SIZE, self.player_y * CELL_SIZE,
                                               (self.player_x + 1) * CELL_SIZE, (self.player_y + 1) * CELL_SIZE,
                                               fill="blue", outline="")

    def generate_maze(self, width, height):
        maze = [[1] * width for _ in range(height)]
        stack = []
        x, y = random.randint(0, width - 1), random.randint(0, height - 1)
        maze[y][x] = 0
        stack.append((x, y))

        while stack:
            neighbors = []
            if x > 1 and maze[y][x - 2]:
                neighbors.append((-2, 0))
            if x < width - 2 and maze[y][x + 2]:
                neighbors.append((2, 0))
            if y > 1 and maze[y - 2][x]:
                neighbors.append((0, -2))
            if y < height - 2 and maze[y + 2][x]:
                neighbors.append((0, 2))

            if neighbors:
                dx, dy = random.choice(neighbors)
                maze[y + dy // 2][x + dx // 2] = 0
                x, y = x + dx, y + dy
                maze[y][x] = 0
                stack.append((x, y))
            else:
                x, y = stack.pop()

        return maze

    def draw_maze(self):
        for y in range(MAZE_HEIGHT):
            for x in range(MAZE_WIDTH):
                if self.maze[y][x] == 1:
                    self.canvas.create_rectangle(x * CELL_SIZE, y * CELL_SIZE,
                                                 (x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE,
                                                 fill=WALL_COLOR, outline="")

    def move_left(self, event):
        if self.player_x > 0 and self.maze[self.player_y][self.player_x - 1] == 0:
            self.canvas.move(self.player, -CELL_SIZE, 0)
            self.player_x -= 1
            self.check_win()

    def move_right(self, event):
        if self.player_x < MAZE_WIDTH - 1 and self.maze[self.player_y][self.player_x + 1] == 0:
            self.canvas.move(self.player, CELL_SIZE, 0)
            self.player_x += 1
            self.check_win()

    def move_up(self, event):
        if self.player_y > 0 and self.maze[self.player_y - 1][self.player_x] == 0:
            self.canvas.move(self.player, 0, -CELL_SIZE)
            self.player_y -= 1
            self.check_win()

    def move_down(self, event):
        if self.player_y < MAZE_HEIGHT - 1 and self.maze[self.player_y + 1][self.player_x] == 0:
            self.canvas.move(self.player, 0, CELL_SIZE)
            self.player_y += 1
            self.check_win()

    def check_win(self):
        if self.player_x == self.end_x and self.player_y == self.end_y:
            self.canvas.create_text(CELL_SIZE * MAZE_WIDTH // 2, CELL_SIZE * MAZE_HEIGHT // 2,
                                    text="You Win!", fill="green", font=("Arial", 30))
            self.master.unbind("<Left>")
            self.master.unbind("<Right>")
            self.master.unbind("<Up>")
            self.master.unbind("<Down>")

# Main
if __name__ == "__main__":
    root = tk.Tk()
    app = MazeApp(root)
    root.mainloop()

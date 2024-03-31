import tkinter as tk
import random

class BrickBreakerGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Brick Breaker")
        self.root.geometry("600x400")

        self.canvas = tk.Canvas(self.root, width=600, height=400, bg="black")
        self.canvas.pack()

        self.paddle = self.canvas.create_rectangle(250, 380, 350, 390, fill="white")
        self.ball = self.canvas.create_oval(300, 200, 320, 220, fill="red")
        self.score_label = tk.Label(self.root, text="Score: 0", font=("Arial", 14), fg="white", bg="black")
        self.score_label.pack()

        self.vx = random.choice([-2, 2])
        self.vy = -2
        self.score = 0
        self.bricks = []

        for i in range(0, 600, 60):
            for j in range(0, 150, 30):
                brick = self.canvas.create_rectangle(i, j, i + 60, j + 30, fill="blue")
                self.bricks.append(brick)

        self.root.bind("<Left>", self.move_paddle_left)
        self.root.bind("<Right>", self.move_paddle_right)

        self.update_ball()

    def move_paddle_left(self, event):
        self.canvas.move(self.paddle, -20, 0)

    def move_paddle_right(self, event):
        self.canvas.move(self.paddle, 20, 0)

    def update_ball(self):
        self.canvas.move(self.ball, self.vx, self.vy)
        ball_coords = self.canvas.coords(self.ball)
        paddle_coords = self.canvas.coords(self.paddle)

        if ball_coords[0] <= 0 or ball_coords[2] >= 600:
            self.vx = -self.vx
        if ball_coords[1] <= 0:
            self.vy = -self.vy
        if ball_coords[3] >= 400:
            self.game_over()

        if paddle_coords[0] <= ball_coords[2] <= paddle_coords[2] and paddle_coords[1] <= ball_coords[3] <= paddle_coords[3]:
            self.vy = -self.vy
            self.score += 10
            self.score_label.config(text=f"Score: {self.score}")

        for brick in self.bricks:
            brick_coords = self.canvas.coords(brick)
            if ball_coords[0] <= brick_coords[2] <= ball_coords[2] and brick_coords[1] <= ball_coords[3] <= brick_coords[3]:
                self.canvas.delete(brick)
                self.bricks.remove(brick)
                self.vy = -self.vy
                self.score += 20
                self.score_label.config(text=f"Score: {self.score}")

        if not self.bricks:
            self.game_win()
        else:
            self.root.after(10, self.update_ball)

    def game_over(self):
        self.canvas.create_text(300, 200, text="Game Over", font=("Arial", 30), fill="red")

    def game_win(self):
        self.canvas.create_text(300, 200, text="You Win!", font=("Arial", 30), fill="green")

if __name__ == "__main__":
    root = tk.Tk()
    game = BrickBreakerGame(root)
    root.mainloop()

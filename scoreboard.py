from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Georgia", 12, "normal")


class Scoreboard(Turtle):
    """
    Create a scoreboard
    """

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Update the scoreboard
        """
        self.clear()
        self.write(f"score: {self.score} highscore: {self.highscore}", align=ALIGNMENT,
                   font=FONT)

    def increase_score(self):
        """
        Increase the score number and update screen text
        """
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        """
        docstring
        """
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()

    

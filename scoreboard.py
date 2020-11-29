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
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Update the scoreboard
        """
        self.write(f"score: {self.score}", align=ALIGNMENT,
                   font=FONT)

    def increase_score(self):
        """
        Increase the score number and update screen text
        """
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        """ 
        Print GameOver text and total score
        """
        self.home()
        self.clear()
        self.write(f"GAME OVER\nscore: {self.score}", align=ALIGNMENT,
                   font=FONT)

class Eff():
    def __init__(self, num):
        self.num = num
        self.eff = ""
        if self.num == 1:
            self.eff = "st"
        elif self.num == 2:
            self.eff = "nd"
        elif self.num == 3:
            self.eff = "rd"
        elif self.num >= 4:
            self.eff = "th"

    def get(self):
        return self.eff
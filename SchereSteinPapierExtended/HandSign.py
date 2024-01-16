class HandSign:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def play(self, handSign):
        if self.value == handSign.value:
            return 0
        elif (self.value + 1) % 5 == handSign.value or (self.value + 3) % 5 == handSign.value:
            return 1
        return -1

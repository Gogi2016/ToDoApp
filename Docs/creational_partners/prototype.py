import copy

class Task:
    def __init__(self, title):
        self.title = title

    def clone(self):
        return copy.deepcopy(self)

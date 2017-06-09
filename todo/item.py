class Item():

    def __init__(self, title=None, completed=False):
        self.title = title
        self.completed = completed

    def __repr__(self):
        return "Item(title={}, completed={})".format(self.title, self.completed)

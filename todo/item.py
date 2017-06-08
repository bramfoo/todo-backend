class Item():

    def __init__(self, title=None):
        self.title = title
        self.completed = False

    def __repr__(self):
        return "Item(title={}, completed={})".format(self.title, self.completed)

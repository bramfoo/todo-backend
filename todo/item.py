class Item():

    def __init__(self, title=None, order=None, completed=False):
        self.title = title
        self.order = order
        self.completed = completed

    def __repr__(self):
        return "Item(title={}, order={}, completed={})".format(self.title, self.order, self.completed)

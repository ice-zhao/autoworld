class TextArea(object):
    buffer = []
    def __init__(self):
        self.buffer = []
    def write(self, *args, **kwargs):
        self.buffer.append(args)
    def clear(self):
        self.buffer = []
    def show(self):
        print buffer


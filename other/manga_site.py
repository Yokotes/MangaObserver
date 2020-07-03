class MangaSite():
    def __init__(self, name, xpaths, test_link = ''):
        self.name = name
        self.xpaths = xpaths
        self.optimized = False
        self.test_link = test_link
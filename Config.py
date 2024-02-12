

class Config(object):
    def __init__(self):
        with open('./resources/synoptic.key') as key:
            self.synoptic = key.read()

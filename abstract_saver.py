class AbstractSaver(object):
    def __init__(self, path_to_save_destination):
        self.path_to_save_destination = path_to_save_destination

    def save(self, note):
        raise NotImplementedError

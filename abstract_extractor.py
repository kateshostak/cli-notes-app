class AbstractExtractor(object):
    def __init__(self, path_to_notes):
        self.path_to_notes = path_to_notes

    def show_all_notes(self):
        raise NotImplementedError

    def search_by_date(self, date):
        raise NotImplementedError

    def search_by_word(self, word):
        raise NotImplementedError

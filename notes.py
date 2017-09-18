import argparse
import os.path
import time


class Note(object):
    """docstring for Note"""
    def __init__(self, note_text):
        self.text = note_text
        self.date_created = self.get_date_time_created()

    def get_date_time_created(self):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())

    def get_text_and_date(self):
        return self.text, self.date_created


class Note_saver(object):
    """docstring for Notes"""
    def __init__(self, note, path_to_file):
        try:
            isinstance(note, Note)
        except TypeError:
            print("The given object is not the 'Note' type.")
        self.note = note
        self.path_to_file = path_to_file

    def save_note(self):
        if self.path_to_file:
            self.write_to_file(path_to_file)
        else:
            self.write_to_file()

    def write_to_file(self, path_to_file='notes'):
        with open(path_to_file, 'w') as f:
            f.write(str(self.note.get_text_and_date()))


def parse_arguments():
    parser = argparse.ArgumentParser(
        "Simple console application for making quick notes."
    )

    parser.add_argument(
        "--add",
        default="Hello!",
        help="Adds a note."
    )

    parser.add_argument(
        "--path",
        default=""
    )

    return parser.parse_args()


def main():
    args = parse_arguments()
    note_to_add = args.add
    file_path = args.path
    note = Note(note_to_add)
    note_saver = Note_saver(note, file_path)
    note_saver.save_note()


if __name__ == "__main__":
    main()

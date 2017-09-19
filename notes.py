import argparse
import os.path
import time


class Note(object):
    def __init__(self, note_text):
        self.text = note_text
        self.date_created = self.get_date_time_created()

    def get_date_time_created(self):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())

    def get_text_and_date(self):
        return self.text, self.date_created


class NoteSaver(object):
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file

    def check_note_is_valid_type(self, note):
        if isinstance(note, Note):
            return True

    def check_path_to_file_exists(self):
        return os.path.exists(os.path.dirname(os.path.abspath(self.path_to_file)))

    def save(self, note):
        if self.check_note_is_valid_type(note):
            self.write_to_file(note)

    def write_to_file(self, note):
        if self.check_path_to_file_exists():
            with open(self.path_to_file, 'w') as f:
                f.write(str(note.get_text_and_date()))


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
        default="notes.txt"
    )

    return parser.parse_args()


def main():
    args = parse_arguments()
    note_to_add = args.add
    file_path = args.path
    note = Note(note_to_add)
    note_saver = Note_saver(file_path)
    note_saver.save(note)


if __name__ == "__main__":
    main()

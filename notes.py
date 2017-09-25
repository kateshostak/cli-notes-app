import argparse
import os.path
import time

from abstract_saver import AbstractSaver


class Note(object):
    def __init__(self, note_text):
        self.text = note_text
        self.timestamp = self._get_timestamp()

    def _get_timestamp(self):
        return time.time()

    def _get_text(self):
        return self.text


class NoteSaverTxt(AbstractSaver):
    def __init__(self, path_to_file):
        super(NoteSaverTxt, self).__init__(path_to_file)

    def save(self, note):
        if self._check_path_to_destination_exists():
            with open(self.path_to_save_destination, 'w') as f:
                f.write(str(self._format_note_representation(note)))

    def _format_note_representation(self, note):
        note_text = note._get_text()
        note_date = time.localtime(note._get_timestamp())
        dateformat = (
            "{day}.{month}.{year} {hour}:{min}".
            format(
                day=note_date.tm_mday,
                month=note_date.tm_mon,
                year=note_date.tm_year,
                hour=note_date.tm_hour,
                min=note_date.tm_min
            )
        )
        return dateformat, note_text

    def _check_path_to_destination_exists(self):
        return (
            os.path.
            exists(
                os.path.
                dirname(
                    os.path.
                    abspath(
                        self.path_to_save_destination
                    )
                )
            )
        )


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
    note_saver = NoteSaverTxt(file_path)
    note_saver.save(note)


if __name__ == "__main__":
    main()

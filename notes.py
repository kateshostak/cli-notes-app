import argparse
import os.path
import time
import sys
import traceback
import logging

from abstract_saver import AbstractSaver
from abstract_extractor import AbstractExtractor


class Note(object):
    def __init__(self, note_text):
        self.text = note_text
        self.timestamp = self._get_timestamp()

    def _get_timestamp(self):
        return time.time()

    def _get_text(self):
        return self.text


class NoteSaverTxt(AbstractSaver):
    def __init__(self, path_to_save_destination):
        super(NoteSaverTxt, self).__init__(path_to_save_destination)

    def save(self, note):
        try:
            with open(self.path_to_save_destination, 'a') as f:
                dateformat, note_text = self._format_note_representation(note)
                print(f"{dateformat} : {note_text}", file=f)
        except Exception as e:
            print("Unable to save the note.")
            logging.error(traceback.format_exc())

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


class NoteExtractor(AbstractExtractor):
    def __init__(self, path_to_notes):
        super(NoteExtractor, self).__init__(path_to_notes)

    def show_all_notes(self):
        try:
            with open(self.path_to_notes) as f:
                for line in f:
                    print(line)
        except Exception as e:
            print("Unable to open notes.")
            logging.error(traceback.format_exc())


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
    note_extractor = NoteExtractor(file_path)
    note_extractor.show_all_notes()


if __name__ == "__main__":
    main()

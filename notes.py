import argparse
import time
import sys
import traceback
import logging
from datetime import datetime

from abstract_saver import AbstractSaver
from abstract_extractor import AbstractExtractor


class Note(object):
    def __init__(self, note_text):
        self.text = note_text
        self.timestamp = time.time()

    def get_text(self):
        return self.text

    def get_timestamp(self):
        return self.timestamp


class NoteSaverTxt(AbstractSaver):
    def __init__(self, path_to_save_destination):
        super(NoteSaverTxt, self).__init__(path_to_save_destination)

    def save(self, note):
        try:
            with open(self.path_to_save_destination, 'a') as f:
                note_timestamp = note.get_timestamp()
                note_text = note.get_text()
                print(f"{note_timestamp} : {note_text}", file=f)
        except Exception as e:
            print("Unable to save the note.")
            logging.error(traceback.format_exc())


class NoteExtractor(AbstractExtractor):
    def __init__(self, path_to_notes):
        super(NoteExtractor, self).__init__(path_to_notes)

    def show_all_notes(self, word, date=None):
        try:
            with open(self.path_to_notes) as f:
                notes = self._parse_note(f)
                if date:
                    self._print_notes(self._search_by_date(notes, date))
                elif word:
                    self._print_notes(self._search_by_word(notes, word))
                else:
                    self._print_notes(notes)
        except Exception as e:
            print("Unable to open notes.")
            logging.error(traceback.format_exc())

    def _parse_note(self, notes):
        return [note.split(":") for note in notes]

    def _search_by_date(self, notes, date):
        return [note for note in notes if datetime.fromtimestamp(float(note[0])).date() == date]

    def _search_by_word(self, notes, keyword):
        return [note for note in notes if keyword in note[1]]

    def _print_notes(self, notes):
        print("Here are your notes.")
        for note in notes:
            note_date = self._get_time_formated(float(note[0]))
            print(f"{note_date} : {note[1]}")

    def _get_time_formated(self, note_timestamp):
        return time.strftime("%a, %d %b %Y %H:%M", time.gmtime(note_timestamp))


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

    parser.add_argument(
        "--keyword",
        default=None
    )

    parser.add_argument(
        "--date",
        default=None
    )

    parser.add_argument(
        "--show",
        default=True
    )

    return parser.parse_args()


def main():
    args = parse_arguments()
    note_to_add = args.add
    file_path = args.path
    keyword = args.keyword
    date_to_search = args.date
    show = args.show

    if date_to_search:
        day, month, year = date_to_search.split("/")
        date_to_search = datetime(int(year), int(month), int(day)).date()

    note = Note(note_to_add)
    note_saver = NoteSaverTxt(file_path)
    note_saver.save(note)

    note_extractor = NoteExtractor(file_path)
    if show:
        note_extractor.show_all_notes(keyword, date_to_search)


if __name__ == "__main__":
    main()

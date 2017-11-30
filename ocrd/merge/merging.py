# -*- coding: utf-8 -*-

import difflib, re

class Lexicon

    def __init__(self):
        """
        The constructor.
        """

        self.clear()

    def clear(self):
        """
        Clears all internal data.
        """

        self.gold = {}


    def load_file(self, file_name):


    def add_entry(self, word, freq=0, add=True):
        if self.gold.has_key(word) and add:
            self.gold[word] += int(freq)

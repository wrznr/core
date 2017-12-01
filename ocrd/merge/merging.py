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


    def add_entry(self, word, freq=0, add=True):
        """
        Add or replace a lexicon entry.
        """

        if self.gold.has_key(word) and add:
            self.gold[word] += int(freq)

    def get_entry(self, word):
        """
        Returns the frequency of a lexicon entry or -1 if it does not exist.
        """
        if self.gold.has_key(word):
            return self.gold[word]
        else:
            return -1

class Merger:

    def __init__(self,lex=None):
        """
        The constructor.
        Maybe called with or without a lexicon.
        """

        self.clear()

        # regex for normalization
        self.normalize_re = re.compile(u"^\W*(.*\w)\W*$", re.U)

        if lex:
            self.load_lexicon(lex)
        else:
            self.lex = Lexicon()

    def clear(self):
        """
        Clears all internal data.
        """

        pass

    def load_lexicon(self,lex):
        """
        Loads a lexicon.
        """

        self.lex = lex


    def merge(self,text,Text,normalize=False):
        """
        Merges two sequences of characters.

        ToDo: split this function into reasonable chunks.
        """

        # output data
        output = []

        # compute diff over inputs
        diff = difflib.SequenceMatcher(None, text, Text)

        # iterate over diff
        for tag, i1, i2, j1, j2 in diff.get_opcodes():
            if tag == "replace":
                left = text[i1:i2]
                right = Text[j1:j2]
                if len(left) != len(right):
                    #
                    # unequal size: fallback to character level
                    # searching for equal subsequences
                    lstream = u" ".join(lword for lword in left)
                    rstream = u" ".join(rword for rword in right)
                    diff2 = difflib.SequenceMatcher(None, lstream, rstream)
                    loutput = u""
                    routput = u""
                    for tag2, I1, I2, J1, J2 in diff2.get_opcodes():
                        lseq = lstream[I1:I2]
                        rseq = rstream[J1:J2]
                        if tag2 == "replace" or tag2 == "equal":

                            # conditional assignment
                            # ToDo: Is there a more elegant way to do this?
                            if len(lseq) < len(rseq):
                               min_len = len(lseq)
                               llonger = False
                            else:
                               min_len = len(rseq)
                               llonger = True

                            for i in range(0,min_len):
                                if lseq[i] == u" ":

                                    # lexicon lookup
                                    # ToDo: respect freq
                                    lfreq = self.lex.get_entry(loutput)
                                    rfreq = self.lex.get_entry(routput)
                                    if lfreq > -1:
                                        output.append(loutput)
                                    elif rfreq > -1:
                                        output.append(routput)
                                    elif normalize:
                                        lnorm = self.normalize_re.sub(u"\\1",loutput)
                                        rnorm = self.normalize_re.sub(u"\\1",routput)
                                        lfreq = self.lex.get_entry(lnorm)
                                        rfreq = self.lex.get_entry(rnorm)
                                        if lnorm and lfreq > -1:
                                            output.append(loutput)
                                        elif rnorm and rfreq > -1:
                                            output.append(routput)
                                        else:
                                            output.append(loutput)
                                    else:
                                        output.append(loutput)
                                    loutput = u""
                                    routput = u""
                                    continue
                                loutput += lseq[i]
                                routput += rseq[i] 

                            if llonger:
                                for i in range(min_len,len(lseq)):
                                    if lseq[i] == u" ":

                                        # lexicon lookup
                                        # ToDo: respect freq
                                        lfreq = self.lex.get_entry(loutput)
                                        rfreq = self.lex.get_entry(routput)
                                        if lfreq > -1:
                                            output.append(loutput)
                                        elif rfreq > -1:
                                            output.append(routput)
                                        elif normalize:
                                            lnorm = self.normalize_re.sub(u"\\1",loutput)
                                            rnorm = self.normalize_re.sub(u"\\1",routput)
                                            lfreq = self.lex.get_entry(lnorm)
                                            rfreq = self.lex.get_entry(rnorm)
                                            if lnorm and lfreq > -1:
                                                output.append(loutput)
                                            elif rnorm and rfreq > -1:
                                                output.append(routput)
                                            else:
                                                output.append(loutput)
                                        else:
                                            output.append(loutput)
                                        loutput = u""
                                        routput = u""
                                        continue
                                    loutput += lseq[i]
                            else:
                                for i in range(min_len,len(rseq)):
                                    routput += rseq[i]
                        elif tag2 == "insert":
                            for i in range(0,len(rseq)):
                                if rseq[i] != u" ":
                                    routput += rseq[i]
                        elif tag2 == "delete":
                            for i in range(min_len,len(lseq)):
                                if lseq[i] == u" ":

                                    # lexicon lookup
                                    # ToDo: respect freq
                                    lfreq = self.lex.get_entry(loutput)
                                    rfreq = self.lex.get_entry(routput)
                                    if lfreq > -1:
                                        output.append(loutput)
                                    elif rfreq > -1:
                                        output.append(routput)
                                    elif normalize:
                                        lnorm = self.normalize_re.sub(u"\\1",loutput)
                                        rnorm = self.normalize_re.sub(u"\\1",routput)
                                        lfreq = self.lex.get_entry(lnorm)
                                        rfreq = self.lex.get_entry(rnorm)
                                        if lnorm and lfreq > -1:
                                            output.append(loutput)
                                        elif rnorm and rfreq > -1:
                                            output.append(routput)
                                        else:
                                            output.append(loutput)
                                    else:
                                        output.append(loutput)
                                    loutput = u""
                                    routput = u""
                                    continue
                                loutput += lseq[i]
                    if loutput:
                        lfreq = self.lex.get_entry(loutput)
                        rfreq = self.lex.get_entry(routput)
                        if lfreq > -1:
                            output.append(loutput)
                        elif rfreq > -1:
                            output.append(routput)
                        elif normalize:
                            lnorm = self.normalize_re.sub(u"\\1",loutput)
                            rnorm = self.normalize_re.sub(u"\\1",routput)
                            lfreq = self.lex.get_entry(lnorm)
                            rfreq = self.lex.get_entry(rnorm)
                            if lnorm and lfreq > -1:
                                output.append(loutput)
                            elif rnorm and rfreq > -1:
                                output.append(routput)
                            else:
                                output.append(loutput)
                        else:
                            output.append(loutput)
                else:
                    for i in range(0,len(left)):
                        lfreq = self.lex.get_entry(left[i])
                        rfreq = self.lex.get_entry(right[i])
                        if rfreq > lfreq:
                            output.append(right[i])
                        elif lfreq > -1:
                            output.append(left[i])
                        else:
                            lnorm = self.normalize_re.sub(u"\\1",loutput)
                            rnorm = self.normalize_re.sub(u"\\1",routput)
                            lfreq = self.lex.get_entry(lnorm)
                            rfreq = self.lex.get_entry(rnorm)
                            if rfreq > lfreq:
                                output.append(right[i])
                            else:
                                output.append(left[i])

            elif tag == "insert":
                # TODO: something more clever?
                pass
            elif tag == "delete":
                # TODO: something more clever?
                for i in range(i1, i2):
                    output.append(text[i])
            else:
                for i in range(i1, i2):
                    output.append(text[i])
        return u"%s\n" % u" ".join(output).replace(u"\n ", u"\n")

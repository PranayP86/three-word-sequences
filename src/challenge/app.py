import sys
import re
import shutil
from typing import List, Tuple, Optional
from nltk.collocations import TrigramCollocationFinder
# import time
# start_time = time.time()


def main():
    """Captures files or stdin and runs program functions.

    Args:
        files (List): Sequence of filenames to process given from command run call.

    """
    if len(sys.argv) > 1:
        # print('Files detected...')  # Remove
        lines = load_text(files=sys.argv[1:])
    else:
        # print('Stdin detected...')  # Remove
        text = ""
        for line in sys.stdin:
            text += line
        lines = load_text(input_text='\\n', stdin=True)
        return
    print_words(lines)


def load_text(files: Optional[List[str]] = None, input_text: Optional[str] = None, stdin: bool = False) -> List[str]:
    """Loads and compiles text from files into a single lowercase text string.

    Args:
        files (List): Sequence of filenames to process given from command run call.
        input_text (str, optional): Text given with stdin method.
        stdin (bool, optional): If True the stdin will be used as text. Defaults to False.

    Returns:
        list: Separated words from text in a list.
    """
    if stdin and input_text:
        lines = input_text
    else:
        with open("full_text.txt", "w") as full:
            if files:
                for file in files:
                    with open(file, "r") as file_piece:
                        shutil.copyfileobj(file_piece, full)
        with open("full_text.txt", "r", encoding='utf8') as full:
            read_lines = full.readlines()
            lines = " ".join(x for x in read_lines)
    words = replace_escapes(lines.lower())
    return words


def print_words(lines: List[str]) -> None:
    """Parses through text lines and prints out most common word trigrams.

    Args:
        lines (list): Separated words from text in a list.
    """
    phrases = process_trigrams(lines)
    for key, value in phrases:
        print(" ".join(key), " - ", value)


def replace_escapes(text: str) -> List[str]:
    """Parses through text and returns separated words in a list without escape characters and punctuation.

    Args:
        text (str): Full text to process, in string format.

    Returns:
        list: Separated words from text in a list.
    """
    escapes = ["\\n", "\\t", "\\r", "\\b", "\\f", "\\a", "\\N", "\\v", "\\", "”", "“", '"', ".", "!", "?", ",", ";", ":"]
    for escape in escapes:
        text = text.replace(escape, "")

    words = re.sub("/[^a-zA-Z]+('A-Za-z]+)?/g", " ", text).split()
    return words

# def replace_escapes(text: str) -> List[str]:
#     res = "".join(re.findall('''[^\n\t\r\b\f\a\v\\\”“".!,:;?]+''', text))
#     words = re.sub("/[^a-zA-Z]+('A-Za-z]+)?/g", " ", res).split()
#     return text


def process_trigrams(lines: List[str]) -> List[Tuple[Tuple[str], int]]:
    """Separates all word trigrams with ordered respective frequency.

    Args:
        lines (list): Separated words from text in a list.

    Returns:
        list: Sequence of tuples containing trigrams and occurrences, ordered by frequency.
    """
    finder = TrigramCollocationFinder.from_words(lines)
    finder.apply_freq_filter(2)
    phrases = sorted(finder.ngram_fd.items(), key=lambda t: (-t[1], t[0]))[:100]
    return phrases


if __name__ == "__main__":
    sys.exit(main())
    # main()
# print("___ {} seconds ___".format(time.time() - start_time))  # Remove

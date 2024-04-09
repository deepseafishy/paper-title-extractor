import argparse
import pypdf
import re
import subprocess as sp
import nltk


def main(
    path: str,
) -> None:
    """
    Read title in the PDF and change the file name to it.
    :params path: a string containing file path
    """
    """ download nltk corpus """
    nltk.download("words")

    """ read in PDF file """
    reader = pypdf.PdfReader(path)

    """ get first page words that will contain the title words """
    first_page_words = reader.pages[0].extract_text()

    """ get words from first two lines """
    lines, line_idx = ["", ""], 0
    for char in first_page_words:
        lines[line_idx] += char
        if char == '\n':
            line_idx += 1
            if line_idx == 2:
                break

    """ preprocess words """
    words = [[], []]
    for idx, line in enumerate(lines):
        for current in line.split():
            for word in current.split('-'):
                words[idx].append(re.sub('[^A-Za-z0-9]+', '', word.lower()))
    # print(words)

    """ check if the second line contain author name """
    authors = True
    for word in words[1][:2]:
        if word in nltk.corpus.words.words():
            print(word, "in corpus")
            authors = False
            break

    """ join title words for new file name """
    title = words[0] if authors else words[0] + words[1]
    file_name = '-'.join(title)

    """ move current file into new file name """
    command = ["mv", path, file_name + ".pdf"]
    print(path, "->", file_name+".pdf")
    sp.run(command)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Paper title extractor")
    parser.add_argument("-p", "--path", type=str, required=True, help="File path")
    args = parser.parse_args()

    main(args.path)
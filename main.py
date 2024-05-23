import argparse
import pypdf
import re
import subprocess as sp


def main(
    path: str,
) -> None:
    """
    Read title in the PDF and change the file name to it.
    :params path: a string containing file path
    """
    """ read in PDF file """
    reader = pypdf.PdfReader(path)

    """ get first page words that will contain the title words """
    candidates = []
    for n_lines in [1, 2, 3]:
        for page in range(2):
            page_words = reader.pages[page].extract_text()

            """ get words from first two lines """
            lines, line_idx = ["" for _ in range(n_lines)], 0
            for char in page_words:
                lines[line_idx] += char
                if char == '\n':
                    line_idx += 1
                    if line_idx == n_lines:
                        break

            """ preprocess words """
            words = [[] for _ in range(n_lines)]
            for idx, line in enumerate(lines):
                for current in line.split():
                    for word in current.split('-'):
                        words[idx].append(re.sub('[^A-Za-z0-9]+', '', word.lower()))

            """ flatten words into a single list """
            title = [item for row in words for item in row]

            """ join the words to create a title candidate and append it to candidates """
            file_name = '-'.join(title)
            candidates.append(file_name)

    """ print candidates and prompt for candidate choice """
    print("Title Candidates:")
    print("\n".join("  [{i}] {s}.pdf".format(i=i, s=s) for i, s in enumerate(candidates)))
    choice = int(input("Your choice of title: "))

    """ move current file into new file name """
    command = ["mv", path, candidates[choice] + ".pdf"]
    print(path, "->", candidates[choice]+".pdf")
    sp.run(command)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Paper title extractor")
    parser.add_argument("-p", "--path", type=str, required=True, help="File path")
    args = parser.parse_args()

    main(args.path)

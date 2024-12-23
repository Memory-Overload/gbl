import os
import sys


def main():
    # redirect stdout to nul unless logging is enabled
    sys.stdout = open(os.devnull, 'w')
    if len(sys.argv) > 1 and sys.argv[1] == '--log':
        sys.stdout = sys.__stdout__

    with open('gbl.md', 'r', encoding="utf-8") as f:
        print('Reading gbl.md in utf-8 encoding')
        lines = f.readlines()

        # ignore metadata at the beginning
        print('Ignoring metadata')
        lines = lines[13:]

        # make a directory to store the chapters if it doesn't exist
        if not os.path.exists('chapters_md'):
            print('Creating chapters_md directory')
            os.makedirs('chapters_md')
            print('Directory created')
        else:
            # otherwise remove all files in the directory
            # b/c we are going to rewrite them
            print('chapters_md already exists')
            print('Removing all files in the directory')
            for file in os.listdir('chapters_md'):
                os.remove(f'chapters_md/{file}')
            print('All files removed')

        # now we can extract the chapters
        print('Extracting chapters')

        chapter = 0
        chapter_name = ''

        for line in lines:
            # if the line starts with '# ' then it is a chapter title
            if line.startswith('# '):
                chapter += 1
                chapter_name = line[2:].strip()
                if "{" in chapter_name:
                    chapter_name = chapter_name.split("{")[0].strip()
                print(f"Chapter found: {chapter_name}")

                # convert chapter name to a valid file name
                # (only used for interlude chapters with ':' in their name)
                # all other chapters are valid file names already yay :D
                chapter_name = chapter_name.replace(':', ' -')

                with open(f'chapters_md/{chapter} - {chapter_name}.md', 'w', encoding="utf-8") as f:
                    # write since we are starting a new chapter
                    # if title has a "{" then we need to cut everything after it
                    if "{" in line:
                        line = line.split("{")[0].strip()
                    f.write(line)
            else:
                with open(f'chapters_md/{chapter} - {chapter_name}.md', 'a', encoding="utf-8") as f:
                    # append since we are continuing the chapter
                    f.write(line)

        print(f'Extracted {chapter} chapters')
        # reroute stdout back to console b/c we don't want to be mean lol :D
        sys.stdout = sys.__stdout__


if __name__ == '__main__':
    main()

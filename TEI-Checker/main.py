import tei_rules as rules

check_file = open('test-tei.xml', 'r')
line_count = 0
parse = []

"""
TODO
    [x] mehrere Elemente in einer Line
    [x] Line Count korrekt anzeigen
    [?] Strings
    [ ] Permitted-List vervollständigen
    [ ] Grammatik in einem Element checken
    [ ] ERROR-Handling
"""


def nonblank_lines(file):  # messes up line count to actual file line count
    for l in file:
        line = l.rstrip()
        if line:
            yield line


def file_grammar(t, line_nr):
    head, sep, tail = t.partition(' ')
    # print("splitting into:", head, sep, tail)
    if tail.endswith('/'):  # checking tei grammar here
        if len(parse) >= 1:
            rules.allowed(parse[-1], head, line_nr)
        print("no need to worry about ", t, " closing itself")
    else:
        if head.startswith('/'):
            if head.replace('/', '') == parse[-1]:
                print("  Closing ", parse[-1], "with ", t)
                del parse[-1]
            else:
                print("something went wrong by closing argument: ", head, "at line ", line_nr)
                print(head, "and ", parse[-1], " are different")
        else:  # checking tei grammar here
            if len(parse) >= 1:
                rules.allowed(parse[-1], head, line_nr)

            parse.append(head)


if __name__ == '__main__':
    print("Using for loop")
    for line in check_file:
        line_count += 1
        print("Line {}: {}".format(line_count, line.strip()))

        tempelem = line.strip()

        if tempelem:  # sorts out empty lines

            tempclean = tempelem.partition("<")[2].partition(">")[0]  # first element of line
            # print("without brackets: ", tempclean)
            temptail = tempelem.partition("<")[2].partition(">")[2]  # multiple elements in same line

            # check line syntax here
            file_grammar(tempclean, line_count)

            while temptail:
                print("Line ", line_count, ": Another Object here: ", temptail)
                tempclean = temptail.partition("<")[2].partition(">")[0]
                file_grammar(tempclean, line_count)
                temptail = temptail.partition("<")[2].partition(">")[2]

    if not parse:
        # print("File is corresponding to TEI-Guidelines.")
        pass

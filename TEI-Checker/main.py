import tei_rules as grammar_rules
import element_rules as element_rules

check_file = open('test-tei.xml', 'r')
line_count = 0
parse = []

"""
TODO
    [x] mehrere Elemente in einer Line
    [x] Line Count korrekt anzeigen
    [?] Strings
    [x] Permitted-List vervollständigen
    [x] Grammatik in einem Element checken
    [...] ERROR-Handling
    [x] baseTypes enthält Space
    [ ] open file through some input (written / dialogue)
    <then/> macht Probleme?
"""


def file_grammar(t, line_nr):
    head, sep, tail = t.partition(' ')
    # print("splitting into:", head, sep, tail)
    if tail.endswith('/'):  # checking tei grammar here
        element_rules.allowed(t, line_nr)
        if len(parse) >= 1:
            grammar_rules.allowed(parse[-1], head, line_nr)
        print("no need to worry about ", t, " closing itself")
    else:
        if head.startswith('/'):
            if len(parse) >= 1:
                if head.replace('/', '') == parse[-1]:
                    print("  Closing {} with {}".format(parse[-1], t))
                    del parse[-1]
                else:
                    print("something went wrong by closing argument: ", head, "at line ", line_nr)
                    print(head, "and ", parse[-1], " are different")
                    raise SystemExit(0)
            else:
                print("There is nothing to close!")
        else:  # checking tei grammar here
            element_rules.allowed(t, line_nr)
            if len(parse) >= 1:
                grammar_rules.allowed(parse[-1], head, line_nr)

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

            #element_rules.allowed(tempclean, line_count)

            file_grammar(tempclean, line_count)  # checking xml grammar here

            while temptail:  # for multiple elements in same line CHECK IF CORRECT
                # line syntax in tail?
                print("Line {}: Another Object here: {}".format(line_count, temptail))
                tempclean = temptail.partition("<")[2].partition(">")[0]
                file_grammar(tempclean, line_count)  # checking xml grammar here
                temptail = temptail.partition("<")[2].partition(">")[2]

    if not parse:
        print("File is corresponding to TEI-Guidelines.")

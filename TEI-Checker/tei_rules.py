permission_list = [
    ['fsdDecl', ['fLib', 'fsDecl', 'fsdLink', 'fvLib']],
    ['fLib', ['f']],
    ['fsDecl', ['fsDescr', 'fsConstraints', 'fDecl']],
    ['fvLib', ['binary', 'default', 'fs', 'numeric', 'string', 'symbol', 'vAlt', 'vColl', 'vLabel', 'vMerge', 'vNot']],
    ['fDecl', ['fDescr', 'vRange', 'vDefault']],
    ['vDefault', ['binary', 'default', 'fs', 'if', 'numeric', 'string', 'symbol', 'vAlt', 'vColl', 'vLabel', 'vMerge', 'vNot']],
    ['vRange', ['binary', 'default', 'fs', 'numeric', 'string', 'symbol', 'vAlt', 'vColl', 'vLabel', 'vMerge', 'vNot']],
    # ...
    ['fs', ['f']],
    ['f', ['binary', 'default', 'fs', 'numeric', 'string', 'symbol', 'vAlt', 'vColl', 'vLabel', 'vMerge', 'vNot']],
    # ...
]

prohibition_list = []  # not sure if needed?


def allowed(test_predecessor, test_element, line_nr):
    permitted = False
    print("  checking: ", test_predecessor, " and ", test_element)
    for rule in permission_list:
        if rule[0] == test_predecessor:
            #print("equal: ", rule, test_predecessor)
            for rule_succ in rule[1]:
                if rule_succ == test_element:
                    #print("equal: ", rule_succ, test_element)
                    permitted = True
    if permitted:
        print("  TEI Rules apply, moving on...")
    else:
        print("Line {}: {} is not allowed after {}".format(line_nr, test_element, test_predecessor))
        #raise SystemExit(0)

    # Maybe raise an exception / throw an error


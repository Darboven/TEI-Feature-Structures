permission_list = [
    ['fsdDecl', ['fLib', 'fsDecl', 'fsdLink', 'fvLib']],
    ['fLib', ['f']],
    ['fsDecl', ['fsDescr', 'fsConstraints', 'fDecl']],
    ['fvLib', ['binary', 'default', 'fs', 'numeric', 'string', 'symbol', 'vAlt', 'vColl', 'vLabel', 'vMerge', 'vNot']],
    ['fDecl', ['fDescr', 'vRange', 'vDefault']],
    ['fsConstraints', ['bicond', 'cond']],
    ['bicond', ['f', 'fs', 'iff']],
    ['cond', ['f', 'fs', 'then']],
    ['vDefault', ['binary', 'default', 'fs', 'if', 'numeric', 'string', 'symbol', 'vAlt', 'vColl', 'vLabel', 'vMerge', 'vNot']],
    ['if', ['binary', 'default', 'f', 'fs', 'numeric', 'string', 'symbol', 'then', 'vAlt', 'vColl', 'vLabel', 'vMerge', 'vNot']],
    ['vRange', ['binary', 'default', 'fs', 'numeric', 'string', 'symbol', 'vAlt', 'vColl', 'vLabel', 'vMerge', 'vNot']],
    ['fs', ['f']],
    ['f', ['binary', 'default', 'fs', 'numeric', 'string', 'symbol', 'vAlt', 'vColl', 'vLabel', 'vMerge', 'vNot']],
    ['vAlt', ['binary', 'default', 'fs', 'numeric', 'string', 'symbol', 'vAlt', 'vColl', 'vLabel', 'vMerge', 'vNot']],
    ['vColl', ['binary', 'default', 'fs', 'numeric', 'string', 'symbol', 'vAlt', 'vLabel']],
    ['vLabel', ['binary', 'default', 'fs', 'numeric', 'string', 'symbol', 'vAlt', 'vColl', 'vLabel', 'vMerge', 'vNot']],
    ['vMerge', ['binary', 'default', 'fs', 'numeric', 'string', 'symbol', 'vAlt', 'vColl', 'vLabel', 'vMerge', 'vNot']],
    ['vNot', ['binary', 'default', 'fs', 'numeric', 'string', 'symbol', 'vAlt', 'vColl', 'vLabel', 'vMerge', 'vNot']]
]

# empty elements do not need to be included

prohibition_list = []  # not sure if needed?


def allowed(test_predecessor, test_element, line_nr):
    permitted = False
    print("  checking: {} and {}".format(test_predecessor, test_element))
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
        raise SystemExit(0)



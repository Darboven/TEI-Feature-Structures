import re

attr_list = [
    # attr      [required]          [optional]
    ['fsdLink', ['type', 'target'], []],
    ['fsDecl',  ['type'],           ['baseTypes']],
    ['fDecl',   ['name'],           ['optional']],
    ['fs',      [],                 ['type', 'feats']],
    ['f',       ['name'],           ['fVal']],
    ['vColl',   [],                 ['org']],
    ['vLabel',  ['name'],           []],
    ['vMerge',  [],                 ['org']],
    ['binary',  ['value'],          []],
    ['numeric', ['value'],          ['max', 'trunc']],
    ['symbol',  ['value'],          []],
]

global_list = ['xml:id', 'n', 'xml:lang', 'xml:base', 'xml:space']  # ...

no_attr_list = ['fsdDecl', 'fLib', 'fvLib', 'fsDescr', 'fsConstraints', 'cond', 'then',
                'bicond', 'iff', 'vRange', 'default', 'string', 'vAlt', 'vNot', ]


def allowed(element, line_nr):
    permitted = False
    ignore = 0  # used to ignore duplications

    elem_clean = re.sub(r'".*?"', '', element)  # ignores everything in quotation marks

    elem_to_comp = elem_clean.partition(" ")[0]  # element
    temp_attribute = elem_clean.partition(" ")[2].partition(" ")[0]  # (first) attribute of element
    temp_attribute_clean = temp_attribute.partition("=")[0]

    temp_ignore = checking(elem_to_comp, temp_attribute_clean, ignore, line_nr)
    ignore = temp_ignore

    temp_attribute_tail = elem_clean.partition(" ")[2].partition(" ")[2]

    while temp_attribute_tail:
        print("Line {}: Another Attribute here: {}".format(line_nr, temp_attribute_tail))
        temp_attribute = temp_attribute_tail.partition(" ")[0]
        temp_attribute_clean = temp_attribute.partition("=")[0]
        temp_ignore = checking(elem_to_comp, temp_attribute_clean, ignore, line_nr)
        ignore = temp_ignore
        temp_attribute_tail = temp_attribute_tail.partition(" ")[2]

    """
    if permitted:
        print("  TEI Rules apply, moving on...")
    else:
        print("Line {}: {} is not allowed with {}".format(line_nr, elem_to_comp, temp_attribute))
        #raise SystemExit(0)
    """


def checking(element, attribute, ignore, line_nr):
    print("  checking attribute {} for {}".format(attribute, element))
    found_elem = False  # make sure that element actually exists in TEI
    if element in no_attr_list:
        found_elem = True
        for rule in global_list:
            if rule == attribute:
                print("    {} is allowed with {}".format(rule, attribute))
                break
        print("    {} needs no Attribute".format(element))  # ...
    else:
        for rule in attr_list:
            if rule[0] == element:
                found_elem = True
                if rule[1] and ignore < len(rule[1]):  # check if element has required attributes
                    if attribute in rule[1]:
                        #print("  found required attribute :)")
                        ignore += 1
                        break
                    else:
                        print("{} has unfulfilled required attributes. Possible attributes are {}".format(element, rule[1]))
                        # raise error here?
                if rule[2]:  # check if element hast optional attributes
                    if attribute in rule[2]:
                        #print("  matched optional attribute")
                        break
                    #print("  has optional attributes, but none matched")
                if attribute in global_list:
                    #print("  found global attribute")
                    break
                print("Line {}: Failure at attribute: {}"
                      "\nReason: The attribute does not match allowed attributes.".format(line_nr, attribute))
                raise SystemExit(0)
                # raise Error here

    if not found_elem:
        print("something bad happened, couldn't find ", element)
        raise SystemExit(0)

    return ignore




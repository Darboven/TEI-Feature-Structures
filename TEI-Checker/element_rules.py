required_list = [

]

optional_list = [

]

def allowed(element, line_nr):
    permitted = False
    elem_to_comp = element.partition(" ")[0]  # element
    temp_attribute = element.partition(" ")[2].partition(" ")[0]  # (first) attribute of element

    # temp_attribute needs further work

    if temp_attribute:
        checking(elem_to_comp, temp_attribute)
    else:
        permitted = True

    temp_attribute_tail = element.partition(" ")[2].partition(" ")[2]

    while temp_attribute_tail:
        print("Line {}: Another Attribute here: {}".format(line_nr, temp_attribute_tail))
        temp_attribute = temp_attribute_tail.partition(" ")[0]
        checking(elem_to_comp, temp_attribute)
        temp_attribute_tail = temp_attribute_tail.partition(" ")[2]

    """
    if permitted:
        print("  TEI Rules apply, moving on...")
    else:
        print("Line {}: {} is not allowed with {}".format(line_nr, elem_to_comp, temp_attribute))
        #raise SystemExit(0)
    """


def checking(element, attribute):
    print("checking ", element, " with ", attribute)

def print_args(*args):
    print("Position tuple:", args)


print(print_args("a", "b", "c"))


def print_moreA(required1, required2, *args):
    print("Need this one:", required1)
    print("Need this one. too:", required2)
    print("All the rest:", args)


print(print_moreA("cap", "gloves", "scarf", "monocle", "mustache wax"))

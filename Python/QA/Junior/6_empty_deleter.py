def delete_empty(string: str):
    list_str = list(filter(lambda x: x.isalpha and not x.isspace() and x != '', string.split("\n")))
    return list_str


if __name__ == "__main__":
    print(delete_empty("L1\nL2\n\nL3\nL4\n  \n\nL5"))

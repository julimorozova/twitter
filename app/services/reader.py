def read_file(filename: str) -> str:
    with open(filename, "r") as fd:
        page = fd.read().encode()
    return page
def read(file):
    with open(file, "r", encoding="utf-8") as f:
        file_content = f.readlines()
        return file_content
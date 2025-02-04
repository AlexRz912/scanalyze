def get_line_num(file):
    with open(file, "r", encoding="utf-8") as f:
        nb_lines = len(f.readlines())
        return nb_lines
    


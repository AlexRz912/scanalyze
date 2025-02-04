def compare(new, previous):
    if not new <= previous:
        print("new domains were added into the mix")
        return True
    print("no new domains for today :)")
    return False
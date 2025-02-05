def is_dupe(domains_file, new_domain):
    with open(domains_file, "r") as f:
        already_existing = {line.strip() for line in f}

    if new_domain in already_existing:
        print(f"domain {new_domain} already exists")
        return True
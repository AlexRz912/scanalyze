def append_to(domains_file, domain):
    with open(domains_file, "a") as file:
        file.write(domain + "\n")
    print(f"Domain : {domain} successfully added")

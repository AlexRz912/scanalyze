import os

def save(domain_file, path):
    os.system(f"cp {domain_file} {path}/previous/domains")

def previous_domain_file_exists(path, domain_file):
    return os.path.exists({path}/domains)
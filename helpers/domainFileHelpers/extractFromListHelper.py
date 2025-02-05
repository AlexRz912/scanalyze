def get_first_domain(domain_list):
    for i in range(len(domain_list)):
        if domain_list[i] == ",":
            domain = domain_list[:i]
            domain_list = domain_list[i+1:]
            return domain_list, domain
    
    return "", domain_list

    
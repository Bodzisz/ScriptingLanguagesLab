import re

domains = {}
emails = []
input_text = ""
email_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


def is_valid(email):
    return re.match(email_regex, email)


def print_domains():
    print('{domain:20s} {occurences:20s}'.format(
    domain="Domain", occurences="Occurences"))
    for domain in domains:
        print('{dom:<20s} {occ:6d}'.format(dom=domain, occ=domains[domain]))


def enter_emails():
    print("Enter emails (enter empty for exit): ")
    while True:
        input_text = input()
        if(input_text == ""):
            break
        elif is_valid(input_text):
            emails.append(input_text)
            domain = input_text.split('@', 1)[1]
            if domain in domains:
                domains[domain] = domains[domain] + 1
            else:
                domains[domain] = 1
        else:
            print("Invalid email!")


enter_emails()
print_domains()

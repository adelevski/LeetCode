from collections import Counter

emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# Output: 2

def numUniqueEmail(emails):
    d = Counter()
    for mail in emails:
        local, domain = mail.split("@")
        local = local.replace(".", "")
        if "+" in local: local = local[:local.index("+")]
        d[local + "@" + domain] += 1
        
    return len(d)




print(numUniqueEmail(emails))
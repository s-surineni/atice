import collections


def subdomainVisits(cpdomains):
    c = collections.Counter()
    for cd in cpdomains:
        n, d = cd.split()
        c[d] += int(n)
        for i in range(len(d)):
            if d[i] == '.': c[d[i + 1:]] += int(n)
    return ["%d %s" % (c[k], k) for k in c]


print(subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))
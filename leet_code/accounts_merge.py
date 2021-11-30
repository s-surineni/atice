from collections import defaultdict


class DSU:
    def __init__(self, size):
        self.replist = []
        self.sizelist = [1] * size

        for idx in range(size):
            self.replist.append(idx)

    def find_rep(self, ele):
        if self.replist[ele] == ele:
            return ele
        return self.find_rep(self.replist[ele])

    def union_by_size(self, ele1, ele2):
        rep1 = self.find_rep(ele1)
        rep2 = self.find_rep(ele2)
        if rep1 == rep2:
            return
        if self.sizelist[rep1] >= self.sizelist[rep2]:
            self.sizelist[rep1] += self.sizelist[rep2]
            self.replist[rep2] = rep1
        else:
            self.sizelist[rep2] += self.sizelist[rep1]
            self.replist[rep1] = rep2


def merge_accounts(accounts):
    email_group = {}
    acc_len = len(accounts)
    dsu = DSU(acc_len)
    for acc_id, acc in enumerate(accounts):
        for email in acc[1:]:
            if email not in email_group:
                email_group[email] = acc_id
            else:
                dsu.union_by_size(acc_id, email_group[email])

    account_mails = defaultdict(list)
    for email, group in email_group.items():
        acc_rep = dsu.find_rep(group)
        account_mails[acc_rep].append(email)

    res = []
    for user, mail in account_mails.items():
        res.append([accounts[user][0]] + sorted(mail))
    return res


accounts = [
    ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
    ["John", "johnsmith@mail.com", "john00@mail.com"],
    ["Mary", "mary@mail.com"],
    ["John", "johnnybravo@mail.com"],
]
accounts = [
    ["David", "David0@m.co", "David4@m.co", "David3@m.co"],
    ["David", "David5@m.co", "David5@m.co", "David0@m.co"],
    ["David", "David1@m.co", "David4@m.co", "David0@m.co"],
    ["David", "David0@m.co", "David1@m.co", "David3@m.co"],
    ["David", "David4@m.co", "David1@m.co", "David3@m.co"],
]
accounts = [
    ["David", "David0@m.co", "David1@m.co"],
    ["David", "David3@m.co", "David4@m.co"],
    ["David", "David4@m.co", "David5@m.co"],
    ["David", "David2@m.co", "David3@m.co"],
    ["David", "David1@m.co", "David2@m.co"],
]
print(merge_accounts(accounts))

class UnionFind:
    def __init__(self, mails: List[str]):
        self.parent = {mail: mail for i, mail in enumerate(mails)}
        self.rank = {mail: 0 for mail in mails}

    def find(self, mail: str) -> str:
        if self.parent[mail] != mail:
            self.parent[mail] = self.find(self.parent[mail])

        return self.parent[mail]

    def union(self, mail1: str, mail2: str) -> bool:
        rootX = self.find(mail1)
        rootY = self.find(mail2)

        # If already on the same root, no need to merge together
        if rootX == rootY:
            return False

        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootX] = rootY
            self.rank[rootY] += 1

        # Return True if the merge was successful
        return True


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emails = set()
        emailToName = {}

        for account in accounts:
            name = account[0]
            for email in account[1:]:
                emails.add(email)
                emailToName[email] = name

        uf = UnionFind(list(emails))

        for account in accounts:
            first_email = account[1]
            
            for other_email in account[2:]:
                uf.union(first_email, other_email)

        groups = defaultdict(list)

        for email in emails:
            root = uf.find(email)
            groups[root].append(email)

        res = []
        for root_email, emails in groups.items():
            name = emailToName[root_email]
            res.append([name] + sorted(emails))

        return res









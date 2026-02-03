from collections import defaultdict
from typing import List

# Good Question
# We use same pattern as lc 3067 - but this is one step higher in terms of diffcultly
# First, since we have to return [name, ...emails] arr
# have a hashMap of email -> name (since email is unique)
# convert emails to vertex(numbers) and numbers to emails (use 2 hashTables for this)
# Do DSU. Take union(first email, all other emails)
# Then apply pattern -> use a hashTable[root], we find root by using find(node)
# numbers of entries in the hashTable reflect the connected components
# iterate the hashTable and form ther res (you know how!!)

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # HashMap of emails(unique), names
        EmailNameMap = defaultdict(str)
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if name not in EmailNameMap[email]:
                    EmailNameMap[email]= name
        
        # Map vertex numbers to emails
        # Have a hashMap here also to map email to numbers
        # Have a array to map number to emails
        Emails = EmailNameMap.keys()
        EmailVertexNodes = defaultdict(int)
        count = 0
        VertexEmail = defaultdict(str)
        for email in Emails:
            if email not in EmailVertexNodes:
                EmailVertexNodes[email] = count
                VertexEmail[count] = email
                count+=1

        n = len(EmailVertexNodes)

        # DSU
        parent = [i for i in range(n)]
        rank = [1]*(n)

        def find(n):
            res = n
            while parent[res] != res:
                parent[res] = parent[parent[res]]
                res = parent[res]
            
            return res
        
        def union(n1,n2):
            p1 = find(n1)
            p2 = find(n2)

            if p1 == p2:
                return 0
            
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1]+=rank[p2]
            else:
                parent[p1] = p2
                rank[p2]+=rank[p1]
            
            return 1
        
        for account in accounts:
            if len(account) <= 2:
                continue
            emailFirst = EmailVertexNodes[account[1]]
            for i in range(2,len(account)):
                emailSecond = EmailVertexNodes[account[i]]
                union(emailFirst, emailSecond)
        
        parentHashMap = defaultdict(list)
        for i in range(n):
            root = find(i)
            parentHashMap[root].append(i)
        
        res = []
        for root, nodes in parentHashMap.items():
            Email_parent = VertexEmail[root]
            name = EmailNameMap[Email_parent]
            email_res = []
            for node in nodes:
                Email_node = VertexEmail[node]
                email_res.append(Email_node)
            email_res.sort()
            res.append([name] + email_res)
        
        return res


        

            
        
        
        




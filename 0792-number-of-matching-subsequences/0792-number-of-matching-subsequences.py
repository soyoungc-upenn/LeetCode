class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int: 
        # {a: [a, acd, ace], b:[bb]}
        # {a: [], b: [bb], c: [cd, ce]}
        # {a: [], b: [bb], c:[], d: [d], e:[e]}
        hm = defaultdict(list)
        for word in words: # O(m)
            hm[word[0]].append(word)
        count = 0
        for ch in s: # O(n)
            bucket = hm[ch]
            hm[ch] = []
            for word in bucket: # O(m)
                next = word[1:]
                if next:
                    hm[next[0]].append(next)
                else:
                    count += 1
        return count

        



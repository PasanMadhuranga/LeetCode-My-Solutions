class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        buckets = {}
        subgroups = []
        l = len(groupSizes)
        for i in range(l):
            if (groupSizes[i] in buckets.keys()):
                buckets[groupSizes[i]].append(i)
            else:
                buckets[groupSizes[i]] = [i]

        for size, ids in buckets.items():
            subgroups += [ids[i:i + size] for i in range(0, len(ids), size)]

        return subgroups
    

# Another Solution found in the discussion section.
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        count = collections.defaultdict(list)
        for i, size in enumerate(groupSizes):
            count[size].append(i)
        return [l[i:i + s]for s, l in count.items() for i in range(0, len(l), s)]
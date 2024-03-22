class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastOccurences = {}
        n = len(s)
        for i in range(n):
            lastOccurences[s[i]] = i

        partitionLens = []
        maxPartition = 0
        preMaxPartition = 0
        i = 0
        while (maxPartition < n):
            while (i <= maxPartition):
                maxPartition = max(maxPartition, lastOccurences[s[i]])
                i += 1
            maxPartition += 1
            partitionLens.append(maxPartition - preMaxPartition)
            preMaxPartition = maxPartition
        
        return partitionLens
    

# Another solution found in the discussion section
class Solution {
    public List<Integer> partitionLabels(String s) {
        Map<Character, Integer> map = new HashMap<>();
        // filling impact of character's
        for(int i = 0; i < s.length(); i++){
            char ch = s.charAt(i);
            map.put(ch, i);
        }
        // making of result
        List<Integer> res = new ArrayList<>();
        int prev = -1;
        int max = 0;
        
        for(int i = 0; i < s.length(); i++){
            char ch = s.charAt(i);
            max = Math.max(max, map.get(ch));
            if(max == i){
                // partition time
                res.add(max - prev);
                prev = max;
            }
        }
        return res;
    }
}
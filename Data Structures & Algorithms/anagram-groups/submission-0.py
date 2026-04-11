#creating DNA of anagram with either  list

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dnaAnagramMap = defaultdict(list)

        for s in strs:
            anagramDna = [0] * 26

            for c in s:
                anagramDna[ord(c) - ord('a')] += 1
            
            dnaAnagramMap[tuple(anagramDna)].append(s)
        
        return list(dnaAnagramMap.values())
        

        
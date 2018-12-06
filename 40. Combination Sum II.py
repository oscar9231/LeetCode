class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result = []
        self.combination_sum(candidates, 0, [], result, target)
        return result

    def combination_sum(self, candidates, start, path, result, target):
        if not candidates:
            return []
        if target == 0:
            result.append(path)
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i-1]:
                continue
            elif candidates[i] > target:
                break
            self.combination_sum(candidates, i+1, path+[candidates[i]], result, target-candidates[i])
        return result

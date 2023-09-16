class Solution:
    def findOriginalArray(self, changed):
        if len(changed) % 2 != 0:
            return []

        counts = Counter(changed)
        original = []

        for num in sorted(changed):
            if num == 0:
                if counts[0] >= 2:
                    original.append(0)
                    counts[0] -= 2
            else:
                if counts[num] > 0 and counts[num * 2] > 0:
                    original.append(num)
                    counts[num] -= 1
                    counts[num * 2] -= 1

        if len(original) == len(changed) // 2:
            return original
        else:
            return []

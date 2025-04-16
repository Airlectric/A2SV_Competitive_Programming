class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        N = len(s)
        s_rev = s[::-1]

        last_idx = {}

        for i in range(N):
            last_idx[s_rev[i]] = N - s_rev.index(s_rev[i]) -1

        start = s[0]
        end = 0

        result = []

        while end < N:
            if end == last_idx[start]:
                result.append(end+1)
                end += 1
                if end < N:
                    start = s[end]
            elif last_idx[s[end]] > last_idx[start]:
                start = s[end]
                end += 1
            elif last_idx[s[end]] <= last_idx[start]:
                end += 1

        for i in range(len(result)-1,0,-1):
            result[i] = result[i] - result[i-1]

        return result

            

        
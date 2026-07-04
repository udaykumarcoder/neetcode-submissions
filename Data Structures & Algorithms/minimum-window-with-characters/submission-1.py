class Solution:
    def minWindow(self, s: str, t: str):
        freqt = {}
        for ch in t:
            freqt[ch] = freqt.get(ch, 0) + 1

        freqs = {}
        left = 0
        ans = ""

        for right in range(len(s)):
            freqs[s[right]] = freqs.get(s[right], 0) + 1

            while True:
                valid = True
                for ch in freqt:
                    if freqs.get(ch, 0) < freqt[ch]:
                        valid = False
                        break

                if not valid:
                    break

                window = s[left:right + 1]
                if ans == "" or len(window) < len(ans):
                    ans = window

                freqs[s[left]] -= 1
                if freqs[s[left]] == 0:
                    del freqs[s[left]]
                left += 1

        return ans
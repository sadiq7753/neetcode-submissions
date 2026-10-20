class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = ""

        for word in strs:
            parts += (str(len(word)) + "#" + word)
        return parts

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            # Find the separator after the length.
            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            start = j + 1
            end = start + length

            result.append(s[start:end])

            # Move to the next length.
            i = end

        return result

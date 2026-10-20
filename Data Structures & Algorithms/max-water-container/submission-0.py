class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_space = 0
        curr_space = 0

        l , r = 0, len(heights)-1

        while l < r:
            w = r - l
            d = min(heights[r], heights[l])

            curr_space = w * d

            max_space = max(max_space, curr_space)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return max_space            

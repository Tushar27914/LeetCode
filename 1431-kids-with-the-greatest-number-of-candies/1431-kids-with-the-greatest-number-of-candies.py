class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
     #def kidsWithCandies(self, candies, extraCandies):
        result = []
        maxCandies = max(candies)
        for kid in candies:
            result.append(((kid + extraCandies) >= maxCandies))
        return result
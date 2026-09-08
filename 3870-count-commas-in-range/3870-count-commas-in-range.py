class Solution:
    def countCommas(self, n: int) -> int:
        count = max(0, min(n, 999_999) - 999) 
        if n >= 1_000_000:
            count += 2 * (min(n, 999_999_999) - 999_999)
        if n >= 1_000_000_000:
            count += 3 * (min(n, 999_999_999_999) - 999_999_999)
        if n >= 1_000_000_000_000:
            count += 4 * (min(n, 999_999_999_999_999) - 999_999_999_999)

        return count

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_tot =0
        for customer in accounts:
            tot = sum(customer)
            max_tot = max(tot,max_tot)
        return max_tot
        
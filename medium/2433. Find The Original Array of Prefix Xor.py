class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        org_arr = [0] * len(pref)
        org_arr[0] = pref[0]
        for i in range(1, len(pref)):
            org_arr[i] = pref[i - 1] ^ pref[i]
        return org_arr

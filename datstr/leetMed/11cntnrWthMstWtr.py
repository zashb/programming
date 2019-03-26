def cntnrWthMstWtr(nums):
    lp, rp, wtr = 0, len(nums) - 1, 0
    while lp < rp:
        ht = min(nums[lp], nums[rp])
        wtr = max(wtr, ht * (rp - lp))
        while nums[lp] <= ht and lp < rp:
            lp += 1
        while nums[rp] <= ht and lp < rp:
            rp -= 1
    return wtr


print(cntnrWthMstWtr([1, 2, 3, 4, 3, 2, 1, 5]))

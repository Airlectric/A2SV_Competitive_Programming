def minCoupons(n,prefixSum,cn,coupons):
    ans = []
    for i in range(cn):
        coupon_price = (prefixSum[n] - prefixSum[n-coupons[i]+1]) + prefixSum[n-coupons[i]]
        ans.append(coupon_price)
    return ans

    
n = int(input())
prices = list(map(int, input().split()))
cn = int(input())
coupons = list(map(int,input().split()))

prices.sort()
prefixSum = [0] * (n+1)
for i in range(n):
    prefixSum[i+1] = prefixSum[i] + prices[i]

results = minCoupons(n,prefixSum,cn,coupons)
for result in results:
    print(result)
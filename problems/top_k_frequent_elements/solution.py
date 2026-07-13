class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count = {}
        # for num in nums:
        #     if num in count:
        #         count[num] += 1
        #     else:
        #         count[num] = 1

        # sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)

        # answer = []

        # for i in range(k):
        #     answer.append(sorted_items[i][0])

        # return answer

        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        bucket = [[] for _ in range(len(nums) + 1)]

        for num, freq in count.items():
            bucket[freq].append(num)

        result = []

        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                result.append(num)

                if len(result) == k:
                    return result
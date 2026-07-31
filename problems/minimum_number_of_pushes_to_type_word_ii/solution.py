class Solution:
    def minimumPushes(self, word: str) -> int:
        my_map = {}
        my_sum = 0
        for i in word:
            if i in my_map:
                my_map[i] += 1
            else:
                my_map[i] = 1
        freq = sorted(my_map.values(), reverse = True)
        for index, frequency in enumerate(freq):
            my_sum += frequency * ((index // 8) + 1)

        return my_sum
import sys

numbers = [int(elem.strip()) for elem in sys.stdin.readlines()]

def reverse_manual(nums):
    def leng(length):
        if length >= 0:
            print(nums[length])
            leng(length - 1)
    leng(len(nums) - 1)

reverse_manual(numbers)

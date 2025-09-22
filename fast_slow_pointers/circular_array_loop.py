def circular_array_loop(nums):
    size = len(nums)

    for i in range(size):
        slow = fast = i
        forward = nums[i] > 0

        while True:
            slow = next_step(slow, nums[slow], size)
            if is_not_cycle(nums, forward, slow):
                break

            fast = next_step(fast, nums[fast], size)
            if is_not_cycle(nums, forward, fast):
                break

            fast = next_step(fast, nums[fast], size)
            if is_not_cycle(nums, forward, fast):
                break

            if slow == fast:
                return True

    return False

def next_step(pointer, value, size):
    return (pointer + value) % size

def is_not_cycle(nums, prev_direction, pointer):
    curr_direction = nums[pointer] >= 0

    if (prev_direction  != curr_direction) or (nums[pointer]% len(nums) == 0):
        return True
    else:
        return False

def main():
    input = (
            [-2, -3, -9],
            [-5, -4, -3, -2, -1],
            [2, 1, -1, -2]
            )
    num = 1
    for i in input:
        print(f"{num}. \t Circular array = {i}")
        print(f"Found loop = {circular_array_loop(i)}")
        num += 1

if __name__ == "__main__":
    main()

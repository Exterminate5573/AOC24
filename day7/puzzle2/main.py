import numpy as np

total = 0

#Bruteforce :sunglasses:
#This one took a second
with open("day7/input.txt") as file:
    for line in file.readlines():
        ans = line.split(":")[0]
        nums = line.split(":")[1].strip().split(" ")

        size = len(nums) - 1

        ops_bin = ""
        for i in range(size):
            ops_bin += "2"

        ops_int = int(ops_bin, base=3)

        while ops_int >= 0:

            ops = np.base_repr(ops_int,base=3)
            ops = ops.zfill(size)
            #print(ops)

            val = nums[0]
            for b in range(size):
                match ops[b]:
                    case "2":
                        val = int(str(val) + nums[b+1])
                        continue
                    case "1":
                        op = "*"
                    case _:
                        op = "+"
                val = eval(str(val) + op + nums[b+1])

            if val == int(ans):
                print("Passed")
                total += val
                break

            ops_int -= 1

print(total)
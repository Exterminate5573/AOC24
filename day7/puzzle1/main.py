
total = 0

#Bruteforce :sunglasses:
with open("day7/input.txt") as file:
    for line in file.readlines():
        ans = line.split(":")[0]
        nums = line.split(":")[1].strip().split(" ")

        size = len(nums) - 1

        ops_bin = "0b"
        for i in range(size):
            ops_bin += "1"

        ops_int = int(ops_bin, base=0)

        while ops_int >= 0:

            ops = bin(ops_int)[2:]
            ops = ops.zfill(size)
            #print(ops)

            val = nums[0]
            for b in range(size):
                op = "*" if ops[b] == "1" else "+"
                val = eval(str(val) + op + nums[b+1])

            if val == int(ans):
                print("Passed")
                total += val
                break

            ops_int -= 1

print(total)
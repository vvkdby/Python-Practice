class flip_bits:
    # @param A : tuple of integers
    # @return a list of integers
    def flip(self, A):
        b = "".join(A.split())
        a = map(int, list(b))
        print a
        maxdiff = 0
        l = 0
        r = 0
        onestoflip = 0
        totalones = 0

        curr_diff = 0
        curr_start = 0
        curr_ones_to_flip = 0
        zero_count = 0

        for i in range(len(a)):
            if a[i] == 0:
                curr_diff -= 1
                zero_count += 1
            else:
                curr_diff += 1
                curr_ones_to_flip += 1
                totalones += 1

            if curr_diff < maxdiff:
                maxdiff = curr_diff
                l = curr_start
                r = i
                onestoflip = curr_ones_to_flip

            else:
                if curr_diff > 0:
                    curr_diff = 0
                    curr_start = i + 1
                    curr_ones_to_flip = 0


        if zero_count != 0:
            return [l,r]
        else:
            return []


s = flip_bits()
print s.flip("0 1 0")
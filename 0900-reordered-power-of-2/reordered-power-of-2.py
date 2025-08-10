class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def get_digit_count(num):
            return ''.join(sorted(str(num)))
    
        n_digits = get_digit_count(n)
        
        # Check all powers of 2 up to 10^9 (covers reasonable input range)
        power = 1
        while power <= 10**9:
            if get_digit_count(power) == n_digits:
                return True
            power *= 2
        
        return False

            
            
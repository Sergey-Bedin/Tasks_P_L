import sys

def min_moves_to_equal_elements(nums):
    nums.sort()
    median = nums[len(nums) // 2]
    return sum(abs(num - median) for num in nums)

def main():
    if len(sys.argv) != 2:
        print("Usage: python Task4.py numbers.txt")
        sys.exit(1)
    
    try:
        with open(sys.argv[1], 'r') as file:
            nums = [int(line.strip()) for line in file if line.strip()]
        
        if not nums:
            print("Error: Input file is empty")
            sys.exit(1)
        
        moves = min_moves_to_equal_elements(nums)
        print(moves)
    
    except FileNotFoundError:
        print(f"Error: File {sys.argv[1]} not found")
        sys.exit(1)
    except ValueError:
        print("Error: Input file contains non-integer values")
        sys.exit(1)

if __name__ == "__main__":
    main()
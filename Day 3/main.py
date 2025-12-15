def find_highest_joltage1(filename : str) -> int :

    answer = 0
    with open(filename, 'r') as file :
        lines = file.readlines()
        
        for line in lines :
            answer += highest_joltage_per_bank1(line)

    return answer


def find_highest_joltage2(filename : str) -> int :

    answer = 0
    with open(filename, 'r') as file :
        lines = file.readlines()

        for line in lines :
            answer += highest_joltage_per_bank2(line)

    return answer


def highest_joltage_per_bank1(line : str) -> int :

    # Idea : to get the max voltage, the first digit has to be the greatest possible
    # and then we find the second greatest digit after his position
    bank = list(map(int, line.strip()))
    tens = max(bank[:-1])
    ones = max(bank[bank.index(tens) + 1:])

    return tens * 10 + ones

def highest_joltage_per_bank2(line : str) -> int :

    bank = list(map(int, line.strip()))
    jolts = 0
    for index in range(11) :
        digit = max(bank[:index - 11])
        bank = bank[bank.index(digit) + 1:]
        jolts = (jolts * 10) + digit

    jolts = (jolts * 10) + max(bank)
    return jolts

if __name__ == '__main__' :
    print(find_highest_joltage2('input.txt'))
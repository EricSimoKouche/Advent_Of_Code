def count_invalid_ID1(filename: str) -> int:

    answer = 0

    with open(filename, 'r') as file :
        intervals = file.readline().split(',')
        for interval in intervals :
            # get the boundaries
            left, right = interval.split("-")

            # convert them from string to integer
            left, right = int(left), int(right)

            for num in range(left, right + 1) :
                s = str(num)
                if (len(s) % 2 == 1) : continue

                first, second = 0, len(s) // 2
                is_correct = True
                while (second < len(s)) :
                    if s[first] != s[second] :
                        is_correct = False
                        break
                    first += 1
                    second += 1

                if is_correct : answer += num

    return answer

def count_invalid_ID2 (filename : str) -> int :

    answer = 0

    with open(filename, 'r') as file :
        intervals = file.readline().split(',')
        for interval in intervals :
            # Get the boundaries
            left, right = interval.split('-')

            # Convert them from string to integer
            left, right = int(left), int(right)

            for num in range(left, right+1) :
                s = str(num)
                if is_valid(s) :
                    answer += num

    return answer


def is_valid(s : str) -> bool :

    temp = ""
    for c in s :
        temp += c
        times = s.count(temp)
        if times > 1 and len(temp) * times == len(s) :
            return True

    return False

if __name__ == "__main__" :
    result = count_invalid_ID2('test.txt')
    print(result)
def countPositionZero_1(filename : str) -> int : 
    dial_position = 50
    password = 0

    with open(filename, 'r') as file :
        for line in file :
            nb_rotation = int(line[1:-1])
            if line[0] == 'R' :
                dial_position = (dial_position + nb_rotation) % 100
            if line[0] == 'L' :
                dial_position = (dial_position - nb_rotation) % 100

            if dial_position == 0 : password += 1

    return password


def countPositionZero_2(filename : str) -> int:
    dial_position = 50
    password = 0

    with open(filename, 'r') as file :
        lines = file.readlines()
        for line in lines :
            nb_rotation = int(line[1:])
            
            if line[0] == 'L' :
                for _ in range(nb_rotation) :
                    dial_position = (dial_position - 1) % 100
                    password += 1 if dial_position == 0 else 0

            if line[0] == 'R' :
                for _ in range(nb_rotation) :
                    dial_position = (dial_position + 1) % 100
                    password += 1 if dial_position == 0 else 0

    return password

if __name__ == "__main__" :
    print(countPositionZero_2('input.txt'))

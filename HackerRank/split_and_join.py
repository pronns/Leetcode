def split_and_join(line):
    parts = line.split(" ")
    newparts = "-".join(parts)
    return newparts
        

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
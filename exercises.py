def read_files():
    inputFile = open("Exercise Files\inputFile.txt")
    for line in inputFile:
        line_split = line.split()
        if line_split[2] == "P":
            print(line)
    inputFile.close()

if __name__ == '__main__':
    read_files()
"""
Example of conversion from Python 2.x to 3
"""

def write_file(filename,version,data):
    try:
        outfile = open(filename,"wb")
        outfile.write("%s\n" % version)
        outfile.write(data)
        outfile.close()
    except Exception as e:
        print(e)


def read_file(filename):
    infile = open(filename,"rb")
    file_version = infile.readline()
    data = infile.read()
    major_version = int(file_version[0])
    minor_version =  int(file_version[2])

    if major_version != 1 or minor_version > 5:
        raise Exception("Wrong file version")

    infile.close()
    return file_version,data


if __name__ == "__main__":
    version = "1.1"
    filename = input("Please enter a filename : ")
    write_file(filename,version,"this is a test data")
    print("File created , reading data from file")
    new_version,data = read_file(filename)
    cents = 73
    quarters = cents // 25
    print("%s=d cents contains %d quarters" % (cents,quarters))
    new_dict = {}
    if not new_version in new_dict:
        new_dict[new_version] = filename

# IMPORT LIB
def read_file(file_name, multidimensional=False):
    file_data = ""
    list_data = ""

    with open(file_name) as file:
        for line in file:
            file_data += (line.strip())
        file.close

    list_data = file_data.split("/")
    
    for key, data in enumerate(list_data):
        if data == '':
            list_data.remove(data)
        else:
            list_data[key] = data[len(str(key+1)):].strip()
    
    return list_data

def write_file(list_data, file_name, multidimensional=False):

    with open(file_name, 'w') as file:
        for line in list_data:
            file.write(line + '\n')
        
        file.close

if __name__ == "__main__":
    print("Hello, World!")
    list_data = read_file("./dataset/test.txt")
    write_file(list_data, "./dataformat/test.txt")
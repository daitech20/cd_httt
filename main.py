# IMPORT LIB
DICTIONARY = []
DOC = []
QUERY = []


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

def setup_file(file_name_input, file_name_output, multidimensional=False):
    input_data = read_file(file_name_input)
    output_data = read_file(file_name_output)
    if output_data == []:
        write_file(input_data,file_name_output)

        return read_file(file_name_input)
    
    return output_data

def setup_dataformat():
    global DOC, DICTIONARY, QUERY

    DOC = setup_file("./dataset/doc-text", "./dataformat/doc.txt")
    QUERY = setup_file("./dataset/query-text", "./dataformat/query.txt")
    DICTIONARY = setup_file("./dataset/term-vocab", "./dataformat/dictionary.txt")

def setup_datatable():
    pass

def setup_data():
    setup_dataformat()
    setup_datatable()

def show_menu():
    pass

if __name__ == "__main__":
    setup_dataformat()
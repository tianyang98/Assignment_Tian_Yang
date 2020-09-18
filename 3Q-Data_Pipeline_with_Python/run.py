import argparse
import os
import sys
import subprocess
from io import StringIO

def navigate(path):
    if type(path) == 'NoneType':
        return
    if path == None:
        print('Wrong path')
    else:
        os.chdir(path)
        print('Current path: ', os.getcwd())
    return

def select_files(path, files):
    res = []
    if(len(files) == 0):
        # print(path)
        for root, dirs, file in os.walk(path):
            temp = file
            for i in range(len(temp)):
                if os.path.splitext(temp[i])[1] == '.py':
                    res.append(temp[i])
    else:
        res = files

    # print(res)
    return res

def pretty_table(rows, column_count, column_spacing=3):
    aligned_columns = []
    for column in range(column_count):
        column_data = list(map(lambda row: row[column], rows))
        aligned_columns.append((max(map(len, column_data)) + column_spacing, column_data))

    for row in range(len(rows)):
        aligned_row = map(lambda x: (x[0], x[1][row]), aligned_columns)
        yield ''.join(map(lambda x: x[1] + ' ' * (x[0] - len(x[1])), aligned_row))



def main():
    parser = argparse.ArgumentParser(usage='python current_file.py [-h] -p path [-o order] [-f file] [-O output]')

    parser.add_argument('-p', '--path',
                        required=True, type=str, help='A folder name – Mandatory - The name of the folder to work upon')
    parser.add_argument('-o', '--order', default='a', type=str,
                        help='Script Order – Optional value: a / d, (Ascending / Descending) – The list of files order to work upon. Default Behavior – Ascending')
    parser.add_argument('-f', '--files', default='', type=str,
                        help='File name – Optional – The exact file name to run. Use "," to separate them. to Default Behavior – All the files')
    parser.add_argument('-O', '--output', default='', type=str,
                        help='Outfile – Optional – Log the output to the mentioned file name. Default behavior – Console')

    input_values = parser.parse_args()
    # print(input_values)
    navigate(input_values.path)

    if len(input_values.files) == 0:
        files = []
    else:
        files = input_values.files.split(',')
    files = select_files(input_values.path, files)

    if(input_values.order == 'a'):
        files.sort()
    elif(input_values.order == 'd'):
        files.sort(reverse=True)
    else:
        print("Cannot recognize the Order")

    rows = [['Folder', 'Files', 'Output']]

    # Print the Output to Console as table
    if input_values.output == '':
        for f in files:
            batcmd="python " + f
            result = subprocess.check_output(batcmd, shell=True, text=True)
            rows.append((input_values.path, f, result))

        for line in pretty_table(rows, 3):
            print(line)

    # Save the Output to the argument file
    else:
        for f in files:
            batcmd="python " + f
            result = subprocess.check_output(batcmd, shell=True, text=True)
            rows.append((input_values.path, f, result))

        for line in pretty_table(rows, 3):
            f = open(input_values.output, "a")
            f.write(line)
            f.close()


if __name__ == '__main__':
    main()
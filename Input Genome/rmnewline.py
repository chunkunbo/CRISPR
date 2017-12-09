import sys

filename = sys.argv[1]
f = open(filename)
contents = f.read()
f.close()
new_contents = contents.replace('\n', '')
f = open('newfile.txt', 'w')
f.write(new_contents)
f.close()

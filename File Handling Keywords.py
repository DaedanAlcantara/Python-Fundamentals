
read()
readline()
readlines()

txt

Apple\n
Banana\n
Cherry\n

read() -> 'Apple\nBanana\nCherry\n'

readline() -> 'Apple\n'
readline() -> 'Banana\n'


readlines() -> ['Apple\n', 'Banana\n', 'Cherry\n']
for line in readlines():
    print(line)

# Output:
Apple

Banana

Cherry

for line in readlines():
    print(line.strip())

# Output:
Apple
Banana
Cherry

strip() -> Removes whitespace (including newline characters) from the beginning and end of a string.

seek() -> Moves the file pointer to a specified position in the file. It takes an offset and an optional whence argument that specifies the reference point for the offset (default is the beginning of the file).

seek(0)

Banana -> [B, a, n, a, n, a]

seek(7) -> Moves the file pointer to the 7th byte in the file, which is the beginning of "Banana".
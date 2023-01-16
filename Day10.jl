using FileIO
using Base

lines = split(read("PuzzleInput10"), "\n")

for instruction in lines
    print(instruction)

end

print("hi")
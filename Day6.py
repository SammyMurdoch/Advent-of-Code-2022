def find_marker_index(marker_length, signal):
    for i in range(len(signal) - marker_length):
        potential_marker = [letter for letter in signal[i:i + marker_length]]

        if check_potential_marker(potential_marker):
            return i + marker_length


def check_potential_marker(potential_marker):
    for letter in potential_marker:
        if potential_marker.count(letter) != 1:
            return False

    return True


with open("PuzzleInput6") as f:
    signal = f.read()

print(find_marker_index(4, signal))
print(find_marker_index(14, signal))




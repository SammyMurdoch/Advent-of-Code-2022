# import re
#
#
# class DirectoriesTree:
#     def __init__(self, index):
#         self.index = index
#         self.parent_index = None
#         self.child_indices = []
#         self.name = None
#         self.files = None
#         self.directories = None
#         self.total_size = None
#
#     def get_directory_local_size(self):
#         if not len(self.files):
#             return 0
#
#         return sum([int(re.findall(r'\d+', file)[0]) for file in self.files])
#
#     def get_directory_total_size(self, tree_size, tree_dict):
#         current_node = self.index
#
#         while len(tree_dict[current_node].child_indices) != 0:
#             current_node = tree_dict[current_node].child_indices[-1]
#
#         included_nodes = list(range(self.index, current_node+1))
#         print(included_nodes, self.index)
#
#         return sum([tree_dict[node].get_directory_local_size() for node in included_nodes])
#
#
# with open("PuzzleInput7") as f:
#     lines = f.read()
#
#
# def total_directory_size(lines):
#     directories = {}
#     for i, match in enumerate(re.finditer("\$ ls", lines)):
#         directory_contents_start_index = match.end() + 1
#         directory_contents_end_index = lines.find("$", directory_contents_start_index)
#
#         directory_content = lines[directory_contents_start_index:directory_contents_end_index].split("\n")
#
#         directory_content = list(filter(None, directory_content))
#
#         directory_directories = list(filter(lambda d: "dir " in d, directory_content))
#         directory_files = list(filter(lambda d: "dir " not in d, directory_content))
#
#         directories_left = lines[:directory_contents_end_index].count("$ cd ..")
#
#         directories[i] = DirectoriesTree(i)
#
#         directories[i].parent_index = i - directories_left - 1
#
#         if directories[i].parent_index != -1:
#             directories[directories[i].parent_index].child_indices.append(i)
#
#         directories[i].directories = directory_directories
#         directories[i].files = directory_files
#         directories[i].name = lines[lines.rfind("$", 0, match.start()) + 5:match.start() - 1]
#
#     total = 0
#
#     for directory in directories.values():
#         directory_total_size = directory.get_directory_total_size(len(directories), directories)
#         print(directory.parent_index, directory.index, directory.name, directory_total_size, directory.files, directory.directories, directory.get_directory_local_size())
#         if directory_total_size <= 100000:
#             total += directory_total_size
#
#     return total
#
#
# total = total_directory_size(lines)
#
# # import math
# # def is_prime(p):
# #     for n in range(2, int(math.sqrt(p))):
# #         if not p % n:
# #             return False
# #
# #     return True
# #
# #
# # print(is_prime(7))
#
#
# hi = [1, 3]
# ho = [4, 6]
#
# print(list(zip(hi, ho)))

from numbers import Number


class Polynomial:

    def __init__(self, coefs):
        self.coefficients = coefs

    def degree(self):
        return len(self.coefficients) - 1

    def __str__(self):
        coefs = self.coefficients
        terms = []

        if coefs[0]:
            terms.append(str(coefs[0]))
        if self.degree() and coefs[1]:
            terms.append(f"{'' if coefs[1] == 1 else coefs[1]}x")

        terms += [f"{'' if c == 1 else c}x^{d}"
                  for d, c in enumerate(coefs[2:], start=2) if c]

        return " + ".join(reversed(terms)) or "0"

    def __repr__(self):
        return self.__class__.__name__ + "(" + repr(self.coefficients) + ")"

    def __eq__(self, other):

        return isinstance(other, Polynomial) and \
            self.coefficients == other.coefficients

    def __add__(self, other):

        if isinstance(other, Polynomial):
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a + b for a, b in zip(self.coefficients,
                                                other.coefficients))
            coefs += self.coefficients[common:] + other.coefficients[common:]

            return Polynomial(coefs)

        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] + other,)
                              + self.coefficients[1:])

        else:
            return NotImplemented

    def __radd__(self, other):
        return self + other

    def __mul__(self, other):
        if isinstance(other, Polynomial):
            coefs = []

            for coef_index in range(self.degree() + other.degree() + 1):
                coef = 0
                i, j = 0, coef_index

                while i <= self.degree() and j > 0:
                    print(i)
                    coef += self.coefficients[i] * other.coefficients[j]

                    i += 1
                    j -= 1

                coefs.append(coef)

        return Polynomial(coefs)

    def __sub__(self, other):
        # return self.__add__(-1 * other)
        return self + (-1) * other

    def __rsub__(self, other):
        return self - other


print(Polynomial((1, 2)) * Polynomial((2, 4)))


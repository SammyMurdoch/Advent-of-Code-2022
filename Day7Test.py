import unittest
from Day7 import total_directory_size


class MyTestCase(unittest.TestCase):
    def test_same_names(self):
        lines = """$ cd /
$ ls
dir a
$ cd a
$ ls
dir ab
dir ac
$ cd ab
$ ls
dir abd
1 a.txt
$ cd abd
$ ls
1 b.txt
$ cd ..
$ cd ..
$ cd ac
$ ls
1 c.txt
"""

        self.assertEqual(10, total_directory_size(lines))

    def test_xxx(self):
        lines = """$ cd /
$ ls
dir a
dir b
$ cd a
$ ls
dir 
"""

    def test_example(self):
        lines = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""

        total = total_directory_size(lines)

        self.assertEqual(95437, total)


if __name__ == '__main__':
    unittest.main()

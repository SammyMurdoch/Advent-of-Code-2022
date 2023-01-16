class Position:
    def __init__(self, row, column):
        self._row = row
        self._column = column

    @classmethod
    def origin(cls):
        return Position(0, 0)

    @property
    def row(self):
        return self._row

    @property
    def column(self):
        return self._column

    def _move_vertically(self, direction):
        return Position(self.row+direction, self.column)

    def _move_horizontally(self, direction):
        return Position(self.row, self.column+direction)

    def up(self):
        return self._move_vertically(1)

    def down(self):
        return self._move_vertically(-1)

    def left(self):
        return self._move_horizontally(-1)

    def right(self):
        return self._move_horizontally(1)


class Rope:
    def __init__(self):
        self._head = Position.origin()
        self._tail = Position.origin()

    def move_head(self, direction, distance):
        move_methods = {
            'U': Position.up,
            'D': Position.down,
            'L': Position.left,
            'R': Position.right
        }
        move_method = move_methods[direction]

        for i in range(distance):
            self._head = move_method(self._head)
            # Move the tail



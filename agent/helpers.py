from gotypes import Point


def is_point_an_eye(board, point, color):
    #An eye is an empty point
    if board.get(point) is not None:
        return False
    for neighbor in point.neighbors():
        # All adjacent points must contain friendly stones
        if board.is_on_grid(neighbor):
            neighbor_color = board.get(neighbor)
            if neighbor_color != color:
                return False

    friendly_corners = 0
    # We must control three out of four corners
    off_board_corners = 0
    corners = [
        Point(point.row - 1, point.col - 1),
        Point(point.row - 1, point.col + 1),
        Point(point.row + 1, point.col - 1),
        Point(point.row + 1, point.col + 1),
    ]
    for corner in corners:
        if board.is_on_grid(corner):
            corner_color = board.get(corner)
            if corner_color == color:
                friendly_corners += 1
        else:
            off_board_corners += 1
    if off_board_corners > 0:
        #Point is on the edge or corner
        return off_board_corners  + friendly_corners == 4
    #Point is in the middle
    return friendly_corners >= 3

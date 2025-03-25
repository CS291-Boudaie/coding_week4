# Problems from class

def number_of_provinces(is_connected):
    """
    From https://leetcode.com/problems/number-of-provinces
    There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b,
    and city b is connected directly with city c, then city a is connected indirectly with city c.
    A province is a group of directly or indirectly connected cities and no other cities outside of the group.
    You are given an n x n matrix is_connected where is_connected[i][j] = 1 if the ith city and the jth city are
    directly connected, and is_connected[i][j] = 0 otherwise.
    Return the total number of provinces.

    Example 1: Input: is_connected = [[1,1,0],[1,1,0],[0,0,1]], Output: 2
    Example 2: Input: is_connected = [[1,0,0],[0,1,0],[0,0,1]], Output: 3
    """
    return 0

def num_connected_islands(matrix):
    """
    From https://leetcode.com/problems/number-of-islands/description/
    Given an m x n 2D binary grid `matrix` which represents a map of '1's (land) and '0's (water), return the number of islands.

    An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
    You may assume all four edges of the grid are all surrounded by water.
    """
    return 0

# Now that you're warmed up

def num_diagonally_connected_islands(matrix):
    """
    Similar to the previous problem, but now you can also traverse islands diagonally. How many are connected now?
    e.g. in the following matrix, there are 3 islands:
    [
        [1, 0, 0, 1],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [1, 0, 0, 1]
    ]
    """
    return 0


def max_area_of_island(grid):
    """
    From https://leetcode.com/problems/max-area-of-island/
    Similar to the previous problems, but now you have to return the area of the largest island.
    Islands can only be connected horizontally and vertically (no diagonals).
    Hint - when you do the "visit" routine, don't just add the current cell to the seen set, but keep track of how many you've seen.
    """
    return 0


def can_visit_all_rooms(rooms):
    """
    From https://leetcode.com/problems/keys-and-rooms/
    There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0.
    Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

    When you visit a room, you may find a set of distinct keys in it.
    Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock
    the other rooms.

    Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if
    you can visit all the rooms, or false otherwise.

    Example 1:

    Input: rooms = [[1],[2],[3],[]]
    Output: true
    Explanation:
    We visit room 0 and pick up key 1.
    We then visit room 1 and pick up key 2.
    We then visit room 2 and pick up key 3.
    We then visit room 3.
    Since we were able to visit every room, we return true.
    Example 2:

    Input: rooms = [[1,3],[3,0,1],[2],[0]]
    Output: false
    Explanation: We can not enter room number 2 since the only key that unlocks it is in that room.
    """
    return False

def rotting_oranges(grid):
    """
    Similar to https://leetcode.com/problems/rotting-oranges/
    You are given an m x n grid where each cell can have one of three values:
    0 representing an empty cell,
    1 representing a fresh orange, or
    2 representing a rotten orange.

    Any orange that is next to a rotting orange will also rot. This is a chain reaction; if orange A is rotten and next
    to orange B, not only will orange B rot, but all oranges next to orange B will also rot, and so on.
    Rot cannot spread diagonally. Only horizontally and vertically.

    E.g. in this grid:
    [
        [2, 1, 1],
        [1, 1, 0],
        [0, 0, 0],
        [1, 1, 1]
    ]

    All oranges except the ones in the bottom row will rot. The final grid will be:
    [
        [2, 2, 2],
        [2, 2, 0],
        [0, 0, 0],
        [1, 1, 1]
    ]
    Return what the final grid will look like after all the rotting has stopped.
    Make a copy of the original grid, do not modify the original grid.
    """
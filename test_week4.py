import unittest
try:
    from week4_answers import number_of_provinces, num_connected_islands, num_diagonally_connected_islands, max_area_of_island, can_visit_all_rooms, rotting_oranges, water_jugs
except:
    from week4 import number_of_provinces, num_connected_islands, num_diagonally_connected_islands, max_area_of_island, can_visit_all_rooms, rotting_oranges, water_jugs

class TestNumberProvinces(unittest.TestCase):

    def test_number_of_provinces(self):
        # Test case from example 1
        self.assertEqual(number_of_provinces([[1,1,0],[1,1,0],[0,0,1]]), 2)
        # Test case from example 2
        self.assertEqual(number_of_provinces([[1,0,0],[0,1,0],[0,0,1]]), 3)
        # All cities connected
        self.assertEqual(number_of_provinces([[1,1,1],[1,1,1],[1,1,1]]), 1)
        # No cities connected
        self.assertEqual(number_of_provinces([[0,0,0],[0,0,0],[0,0,0]]), 3)
        # Single city
        self.assertEqual(number_of_provinces([[1]]), 1)
        self.assertEqual(number_of_provinces([[1,0,1],[0,1,0],[1,0,1]]), 2)

class TestNumberConnectedIslands(unittest.TestCase):
    def test_num_connected_islands(self):
        # Standard case
        self.assertEqual(num_connected_islands([
            ['1','1','0','0','0'],
            ['1','1','0','0','0'],
            ['0','0','1','0','0'],
            ['0','0','0','1','1']
        ]), 3)
        # No islands
        self.assertEqual(num_connected_islands([
            ['0','0'],
            ['0','0']
        ]), 0)
        # All land
        self.assertEqual(num_connected_islands([
            ['1','1'],
            ['1','1']
        ]), 1)
        # Single cell island
        self.assertEqual(num_connected_islands([['1']]), 1)
        # Single cell water
        self.assertEqual(num_connected_islands([['0']]), 0)
        # Checkerboard pattern
        self.assertEqual(num_connected_islands([
            ['1','0','1'],
            ['0','1','0'],
            ['1','0','1']
        ]), 5)

class TestNumberDiagonal(unittest.TestCase):
    def test_num_diagonally_connected_islands(self):
        # Standard case with diagonal connections
        self.assertEqual(num_diagonally_connected_islands([
            ['1','0','0','1'],
            ['0','1','0','0'],
            ['0','0','1','0'],
            ['1','0','0','1']
        ]), 3)
        # All connected diagonally
        self.assertEqual(num_diagonally_connected_islands([
            ['1','0','1'],
            ['0','1','0'],
            ['1','0','1']
        ]), 1)
        # No islands
        self.assertEqual(num_diagonally_connected_islands([
            ['0','0'],
            ['0','0']
        ]), 0)
        # Single island with diagonal connection
        self.assertEqual(num_diagonally_connected_islands([
            ['1','0'],
            ['0','1']
        ]), 1)
        # No islands
        self.assertEqual(num_connected_islands([
            ['0','0'],
            ['0','0']
        ]), 0)
        # All land
        self.assertEqual(num_connected_islands([
            ['1','1'],
            ['1','1']
        ]), 1)

class TestMaxArea(unittest.TestCase):
    def test_max_area_of_island(self):
        # Standard case
        self.assertEqual(max_area_of_island([
            ['1','1','0','0','0'],
            ['1','1','0','0','0'],
            ['0','0','0','1','1'],
            ['0','0','0','1','1']
        ]), 4)
        # Single cell island
        self.assertEqual(max_area_of_island([['1']]), 1)
        # No islands
        self.assertEqual(max_area_of_island([['0']]), 0)
        # Multiple islands with varying sizes
        self.assertEqual(max_area_of_island([
            ['1','0','1','1'],
            ['1','0','1','0'],
            ['0','1','0','0'],
            ['1','1','0','1']
        ]), 3)
        # All land
        self.assertEqual(max_area_of_island([
            ['1','1'],
            ['1','1']
        ]), 4)

class TestCanVisit(unittest.TestCase):
    def test_can_visit_all_rooms(self):
        # Example case 1
        self.assertTrue(can_visit_all_rooms([[1],[2],[3],[]]))
        # Example case 2
        self.assertFalse(can_visit_all_rooms([[1,3],[3,0,1],[2],[0]]))
        # Single room
        self.assertTrue(can_visit_all_rooms([[]]))
        # All rooms accessible from room 0
        self.assertTrue(can_visit_all_rooms([[1,2,3],[],[],[]]))
        # Circular dependencies
        self.assertTrue(can_visit_all_rooms([[1],[2],[0]]))
        # Disconnected graph
        self.assertFalse(can_visit_all_rooms([[1],[],[0,2],[3]]))

class TestRottingOranges(unittest.TestCase):
    def test_rotting_oranges(self):
        # Standard case
        input_grid = [
            [2,1,1],
            [1,1,0],
            [0,0,0],
            [1,1,1]
        ]
        expected_output = [
            [2,2,2],
            [2,2,0],
            [0,0,0],
            [1,1,1]
        ]
        self.assertEqual(rotting_oranges(input_grid), expected_output)
        # All oranges already rotten
        input_grid = [
            [2,2],
            [2,2]
        ]
        expected_output = [
            [2,2],
            [2,2]
        ]
        self.assertEqual(rotting_oranges(input_grid), expected_output)
        # No oranges
        input_grid = [
            [0,0],
            [0,0]
        ]
        expected_output = [
            [0,0],
            [0,0]
        ]
        self.assertEqual(rotting_oranges(input_grid), expected_output)
        # Single fresh orange that can't be rotten
        input_grid = [[1]]
        expected_output = [[1]]
        self.assertEqual(rotting_oranges(input_grid), expected_output)
        # Single rotten orange
        input_grid = [[2]]
        expected_output = [[2]]
        self.assertEqual(rotting_oranges(input_grid), expected_output)
        # Multiple sources of rot
        input_grid = [
            [2,0,1],
            [1,0,1],
            [1,1,2]
        ]
        expected_output = [
            [2,0,2],
            [2,0,2],
            [2,2,2]
        ]
        self.assertEqual(rotting_oranges(input_grid), expected_output)

class TestWaterJugs(unittest.TestCase):
    def test_water_jugs(self):
        self.assertTrue(water_jugs(3, 5, 4))
        self.assertFalse(water_jugs(2, 6, 5))
        self.assertTrue(water_jugs(1, 2, 3))

    def test_target_is_zero(self):
        self.assertTrue(water_jugs(3, 5, 0))  # Target is 0 (always reachable)

    def test_target_is_one_of_the_jugs(self):
        self.assertTrue(water_jugs(3, 5, 3))  # Target is x
        self.assertTrue(water_jugs(3, 5, 5))  # Target is y

    def test_target_is_sum_of_jugs(self):
        self.assertTrue(water_jugs(3, 5, 8))  # Target is x + y

    def test_gcd_condition(self):
        self.assertTrue(water_jugs(4, 6, 2))  # Target is GCD of x and y
        self.assertFalse(water_jugs(4, 6, 5))  # Target is not divisible by GCD

    def test_same_jug_sizes(self):
        self.assertTrue(water_jugs(5, 5, 5))  # Same jug sizes, target is jug size
        self.assertFalse(water_jugs(5, 5, 3))  # Same jug sizes, target not reachable

    def test_large_jugs(self):
        self.assertTrue(water_jugs(100, 150, 50))  # Large jugs, target is GCD
        self.assertTrue(water_jugs(100, 150, 200))  # Large jugs, reachable target

    def test_one_jug_is_enough(self):
        self.assertTrue(water_jugs(1, 10, 1))  # Target is same as smaller jug
        self.assertTrue(water_jugs(1, 10, 10))  # Target is same as larger jug

    def test_target_larger_than_both_jugs(self):
        self.assertFalse(water_jugs(3, 5, 9))  # Target > x + y

if __name__ == '__main__':
    unittest.main()
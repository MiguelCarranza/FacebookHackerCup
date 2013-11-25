import unittest
from square_detector import *
import os

#############################################################################
#  Facebook Hacker Cup 2014: Qualification Round                            #
# --------------------------------------------------------------------------#
#  Square Detector (Tests)                                                          #
# --------------------------------------------------------------------------#
#                    Miguel Carranza 21 Nov 2013                            # 
#   miguel@miguelcarranza.es                 github: MiguelCarranza         #
#############################################################################
class SquareDetectorTests(unittest.TestCase):

  def test_is_inside_square(self):
    upper_left_corner = (1, 1)
    upper_right_corner = (1, 3)

    inside_points = [(1, 1), (1, 2), (1, 3),
                     (2, 1), (2, 2), (2, 3),
                     (3, 1), (3, 2), (3, 3)]

    outside_points = [(0, 0), (1, 0), (2, 0),
                      (3, 0), (1, 4), (2, 4)]

    for point in inside_points:
      self.assertTrue(is_inside_square(point, upper_left_corner,
                                       upper_right_corner))

    for point in outside_points:
      self.assertFalse(is_inside_square(point, upper_left_corner,
                                        upper_right_corner))


  def test_main(self):
    input_file = open(os.path.join('examples', 'example.txt'), 'r')
    output_file = open(os.path.join('examples', 'result.txt'), 'r')

    number_of_cases = get_number_from_line(input_file.readline())

    for i in range(number_of_cases):
      res_line = 'Case #%d: %s\n' % (i + 1, detect_squares(input_file))
      self.assertEquals(res_line, output_file.readline())

    input_file.close()
    output_file.close()


if __name__ == '__main__':
  unittest.main()
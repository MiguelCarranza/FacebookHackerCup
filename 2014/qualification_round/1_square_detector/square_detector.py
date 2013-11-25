#############################################################################
#  Facebook Hacker Cup 2014: Qualification Round                            #
# --------------------------------------------------------------------------#
#  Square Detector                                                          #
# --------------------------------------------------------------------------#
#                    Miguel Carranza 21 Nov 2013                            # 
#   miguel@miguelcarranza.es                 github: MiguelCarranza         #
#############################################################################

import sys


def main():
  check_args()
  input_file = open(sys.argv[1], 'r')
  output_file = open(sys.argv[2], 'w')

  number_of_cases = get_number_from_line(input_file.readline())

  for i in range(number_of_cases):
    output_file.write('Case #%d: %s\n' % (i + 1, detect_squares(input_file)))

  input_file.close()
  output_file.close()
  

def detect_squares(f):
  dim = get_number_from_line(f.readline())
  grid = map(lambda x: f.readline()[:-1], range(dim))

  upper_left_corner = ()
  upper_right_corner = ()


  # Get upper left corner
  i, j = (0, 0)
  while (i < dim and not upper_left_corner):
    while (j < dim and not upper_left_corner):
      if grid[i][j] == '#':
          upper_left_corner = (i, j)
      j += 1
    i += 1
    j = 0

  if not upper_left_corner:
    return 'NO'

  # Get upper right corner
  white = False
  for j in range(upper_left_corner[1] + 1, dim):
    if grid[upper_left_corner[0]][j] == '#':
      if white:
        return 'NO'
      else:
        upper_right_corner = (upper_left_corner[0], j)
    else:
      white = True

  if not upper_right_corner:
    return 'NO'


  # Rest of the grid
  for i in range(upper_left_corner[0] + 1, dim):
    for j in range(dim):
      if (grid[i][j] == '#'):
        if not is_inside_square((i, j), upper_left_corner, 
                                upper_right_corner):
          return 'NO'
      else:
        if is_inside_square((i, j), upper_left_corner,
                            upper_right_corner):
          return 'NO'

  return 'YES'


def is_inside_square(point, upper_left_corner, upper_right_corner):
  dim = upper_right_corner[1] - upper_left_corner[1] + 1

  return (point[0] >= upper_left_corner[0] and
          point[0] < (upper_left_corner[0] + dim) and
          point[1] >= upper_left_corner[1] and
          point[1] <= upper_right_corner[1])



# Get a number for a line
def get_number_from_line(line):
  line = line[:-1]

  if not line.isdigit():
    print_error_and_exit("Invalid line! %s is not an integer!\n" %
                         line)

  return int(line)


def print_error_and_exit(s):
  sys.stderr.write(s)
  sys.exit()


# Check args sanity
def check_args():
  script_name = sys.argv[0]

  if len(sys.argv) != 3:
    print_error_and_exit('Usage: %s <input file> <output fie>\n' % 
                         script_name)


if __name__ == '__main__':
  main()
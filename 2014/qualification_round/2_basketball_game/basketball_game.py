#############################################################################
#  Facebook Hacker Cup 2014: Qualification Round                            #
# --------------------------------------------------------------------------#
#  Basketball Game                                                          #
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
    output_file.write('Case #%d: %s\n' % (i + 1, basketball_game(input_file)))

  input_file.close()
  output_file.close()
  

def basketball_game(f):
  n, m, p = get_n_m_and_p(f.readline())
  players = get_players_ordered_by_draft(f, n)
  team_1, team_2 = divide_into_teams(players) 

  playing_t1 = team_1[:p]
  playing_t1.reverse()
  playing_t2 = team_2[:p]
  playing_t2.reverse()
  bench_t1 = team_1[p:]
  bench_t2 = team_2[p:]

  if len(bench_t2):
    for i in range(m % len(team_2)):
      rotate(playing_t1, bench_t1)
      rotate(playing_t2, bench_t2)

  if len(bench_t1) and len(team_1) > len(team_2):
    rotate(playing_t1, bench_t1)


  return format_teams_to_print(playing_t1, playing_t2)



def rotate(playing, bench):
  leaving = playing.pop(0)
  joining = bench.pop(0)
  playing.append(joining)
  bench.append(leaving)



def get_players_ordered_by_draft(f, n):
  players = map(lambda x: parse_player(f.readline()), 
             range(n))
  players.sort(reverse=True)
  return map(lambda x: x[1], players)



def parse_player(line):
  line = line[:-1]
  name, score, height = line.split()
  score = int(score)
  height = int(height)
  # ponderation, so that we only sort by one
  # parameter. 
  return (score * 1000 + height, name)



def divide_into_teams(players):
  odd = True
  team_1 = []
  team_2 = []

  for player in players:
    if odd:
      team_1.append(player)
      odd = False
    else:
      team_2.append(player)
      odd = True

  return (team_1, team_2)



# Get a number for a line
def get_number_from_line(line):
  line = line[:-1]

  if not line.isdigit():
    print_error_and_exit("Invalid line! %s is not an integer!\n" %
                         line)

  return int(line)


# Parse n, m and p
def get_n_m_and_p(line):
  line = line[:-1]
  return map(lambda x: int(x), line.split(' '))



def format_teams_to_print(playing_t1, playing_t2):
  playing_after_m = playing_t1 + playing_t2
  playing_after_m.sort()

  return ' '.join(playing_after_m)


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
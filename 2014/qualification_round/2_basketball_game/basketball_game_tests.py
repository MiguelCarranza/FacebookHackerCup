import os
import unittest
from basketball_game import *

#############################################################################
#  Facebook Hacker Cup 2014: Qualification Round                            #
# --------------------------------------------------------------------------#
#  Basketball Game (Tests)                                                  #
# --------------------------------------------------------------------------#
#                    Miguel Carranza 21 Nov 2013                            # 
#   miguel@miguelcarranza.es                 github: MiguelCarranza         #
#############################################################################
class BasketballGameTests(unittest.TestCase):

  def setUp(self):
    self.input_file = open(os.path.join('examples', 'example.txt'), 'r')
    self.output_file = open(os.path.join('examples', 'result.txt'), 'r')


  def tearDown(self):
    self.input_file.close()
    self.output_file.close()


  def test_get_n_m_and_p(self):
    line = '6 3 2\n'
    self.assertEquals([6, 3, 2], get_n_m_and_p(line))


  def test_format_teams_to_print(self):
    team_1 = ['Bob', 'Alice']
    team_2 = ['Charlie']
    self.assertEquals(format_teams_to_print(team_1, team_2),
                      "Alice Bob Charlie")


  def test_parse_player(self):
    line = 'Miguel 100 196\n'
    self.assertEquals(parse_player(line),
                      (100196, 'Miguel'))


  def test_divide_into_teams(self):
    players = [1, 2, 3, 4, 5, 6, 7]
    self.assertEquals(divide_into_teams(players),
                      ([1, 3, 5, 7], [2, 4, 6]))


  def test_get_players_ordered_by_draft(self):
    self.input_file.readline()
    n = get_n_m_and_p(self.input_file.readline())[0]
    players = get_players_ordered_by_draft(self.input_file, n)
    self.assertEquals(players,
                      ['Wai', 'Purav', 'Weiyan', 'Slawek', 
                       'Lin', 'Meihong'])


  def test_main(self):
    number_of_cases = get_number_from_line(self.input_file.readline())

    for i in range(number_of_cases):
      res_line = 'Case #%d: %s\n' % (i + 1, basketball_game(self.input_file))
      self.assertEquals(res_line, self.output_file.readline())


if __name__ == '__main__':
  unittest.main()
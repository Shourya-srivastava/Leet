from collections import Counter
from typing import List


class Solution:

  def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
    loss_count = Counter()
    all_players = set()

    for winner, loser in matches:
      all_players.add(winner)
      all_players.add(loser)
      loss_count[loser] += 1

    zero_losses = sorted(
        player for player in all_players if loss_count[player] == 0
    )
    one_loss = sorted(
        player for player in all_players if loss_count[player] == 1
    )

    return [zero_losses, one_loss]
import random
from pprint import pprint

class card:
  def __init__(self, mark, num):
    self.num = num
    self.mark = mark

def pair_check(cards):
  card_multi = 0
  for s in set(cards):
    if card_multi < cards.count(s):
      card_multi = cards.count(s)
  return card_multi

def mark_check(cards_mark):
  mark_multi = 0
  for s in set(cards_mark):
    if mark_multi < cards_mark.count(s):
      mark_multi = cards_mark.count(s)
  return mark_multi


def check_roll(cards):
  hand = [card for card in cards]
  hand_nums = [c.num for c in hand]
  hand_marks = [c.mark for c in hand]

  if mark_check(hand_marks) == 4:
    return "flash!!"
  if len(set(hand_nums)) == 3:
    return "1 Pair"
  elif len(set(hand_nums)) == 2 and pair_check(hand_nums) == 3:
    return "3 Card"
  elif len(set(hand_nums)) == 2 and pair_check(hand_nums) == 2:
    return "2 Pair"
  elif len(set(hand_nums)) == 1:
    return "4 Card"
  else:
    high = max(hand_nums)
    roll = "high card:{}".format(high)
    return roll

if __name__=='__main__':
  bill = []
  marks = ('♣︎', '🔸', '❤️', '♠️')

  bill = [card(k, j) for k in marks for j in range(1, 14)]
  random.shuffle(bill)

  hand = bill[:4]
  hand_nums = [c.num for c in hand]
  hand_marks = [c.mark for c in hand]

  for i in range(len(hand_nums)):
    print("Card", i + 1, ":", hand_nums[i], hand_marks[i])
  print("handle", check_roll(hand))
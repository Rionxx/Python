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
    return 0 #flash
  if len(set(hand_nums)) == 3:
    return 1 #1 Pair
  elif len(set(hand_nums)) == 2 and pair_check(hand_nums) == 3:
    return 2 #3 Card
  elif len(set(hand_nums)) == 2 and pair_check(hand_nums) == 2:
    return 3 #2 Pair
  elif len(set(hand_nums)) == 1:
    return 4 #4 Card
  else:
    return 5 #Buta


if __name__=='__main__':
  bill = []
  marks = ('♣︎', '🔸', '❤️', '♠️')
  roles = ("flash", "1 Pair", "3 Card", "2 Pair", "4 Card", "Buta")
  role_count = [0 for x in range(len(roles))]

  count = 0
  while count < 10000:
    count += 1

    bill = [card(k, j) for k in marks for j in range(1, 14)]
    random.shuffle(bill)

    hand = bill[:4]
    hand_nums = [c.num for c in hand]
    hand_marks = [c.mark for c in hand]

    for i in range(len(hand_nums)):
      print("Card", i + 1, ":", hand_nums[i], hand_marks[i])
    
    roll = check_roll(hand)
    role_count[roll] += 1
  
  print("-"*20)
  print('{}result'.format(count))
  print("-"*20)

  for i in range(len(roles)):
    print('{}:{}回 確率:{}%'.format(roles[i], role_count[i], role_count[i] / count * 100))
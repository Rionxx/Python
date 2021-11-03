import random
import collections
import datetime
import poker as pkg

class card:
  def __init__(self, mark, num):
    self.num = num
    self.mark = mark


def straight_check(hand_nums):
  if 1 in hand_nums and 10 in hand_nums:
    hand_nums.remove(1)
    hand_nums.append(14)

  max_num = max(hand_nums)
  min_num = min(hand_nums)
  ave_num = (max_num + min_num) / 2

  if max_num - min_num == 4 and ave_num - 1 in hand_nums and ave_num + 1 in hand_nums:
    return True 


def check_roll(cards):
  hand = [card for card in cards]
  hand_nums = [c.num for c in hand]
  hand_marks = [c.mark for c in hand]

  if pkg.mark_check(hand_marks) == 5 and straight_check(hand_nums) != True:
    return 0 #flash!!
  elif len(set(hand_nums)) == 4 and pkg.pair_check(hand_nums) == 2:
    return 1 #1 Pair
  elif len(set(hand_nums)) == 3 and pkg.pair_check(hand_nums) == 3:
    return 2 #3 Card
  elif len(set(hand_nums)) == 3 and pkg.pair_check(hand_nums) == 2:
    return 3 #2 Pair
  elif len(set(hand_nums)) == 2 and pkg.mark_check(hand_nums) == 4:
    return 4 #4 Card
  elif straight_check(hand_nums) and pkg.mark_check(hand_marks) != 5:
    return 5 #Straight!!
  elif len(set(hand_nums)) == 2 and pkg.pair_check(hand_nums) == 3:
    return 6 #Full House
  elif straight_check(hand_nums) and pkg.mark_check(hand_marks) == 5:
    if 1 in hand_nums and 10 in hand_nums:
      return 8 #Loyal Straight Flash
    else:
      return 7 #Straight Flash
  else:
    high = max(hand_nums)
    roll = "high card:{}".format(high)
    return 9


if __name__== "__main__":
  bill = []
  marks = ('♣︎', '🔸', '❤️', '♠️')
  roles = ("flash", "1 Pair", "3 Card", "2 Pair", "4 Card","Straight", "Full House", "Straight Flash", "Loyal Stright Flash", "Buta")
  role_count = [0 for x in range(len(roles))]

  bill = [card(k, j) for k in marks for j in range(1, 14)]
  random.shuffle(bill)
  start_time = datetime.datetime.now()

  count = 0
  while count < 50000:
    count += 1

    bill = [card(k, j) for k in marks for j in range(1, 14)]
    random.shuffle(bill)
    hand = bill[:5]
    hand_nums = [c.num for c in hand]
    hand_marks = [c.mark for c in hand]
    for i in range(len(hand_nums)):
      print("Card", i + 1, ":", hand_nums[i], hand_marks[i])

    roll = check_roll(hand)
    role_count[roll] += 1

  print("-"*20)
  print('{}count Result'.format(count))
  print("-"*20)

  for i in range(len(roles)):
    print('{}:{}回 確率:{}%'.format(roles[i], role_count[i], role_count[i] / count * 100))

  end_time = datetime.datetime.now()
  print("Pass time:{}".format(end_time - start_time))

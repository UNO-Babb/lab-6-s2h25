#DiceRoll.py
#Name:
#Date:
#Assignment:
import random

def main():
  #Create an empty list with possible roll values
    rolls = [0,0,0,0,0,0,0,0,0,0,0]
    total_rolls = 10000
  #Create two dice values ranging from 1 - 6 each
    for _ in range(10000):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        total = dice1 + dice2
        rolls[total -2] += 1


  #find the sum total of the two dice
    print("sum | count | percentage")
    print("------------------------")
    for i in range(11):
        percentage = (rolls[i] / total_rolls) * 100
        print(f"{i + 2:>3} | {rolls[i]:>5} | {percentage:>8.2f}%")
  #print statictics for dice rolls


if __name__ == '__main__':
  main()

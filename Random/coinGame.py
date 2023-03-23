
import random, time
print(''''



''')

def chance(coins,turn,gain,dices):
      
      coin = coins
      
      for i in range(1,turn+1):

         dice = random.randint(1,((6**dices)))
      #print(dice)
         if dice == 6**dices:
            coin =coin + gain
         else:
            coin = coin-1
            
      
         if coin == 0:
            break
         else:
            pass
         
         #time.sleep(.20)
         print(dice,'\t',coin)
      
      print(coin)
            
            
         
for p in range(1):
   coins = 10000#int(input('Enter no of coins here   '))
   turn = 10000#int(input('Enter no of turn here   '))
   dices = 1#int(input('Enter no of dice here   '))
   gain = 6**dices#int(input('Enter no of coin gain here   '))
   chance(coins,turn,gain,dices)
   time.sleep(0)

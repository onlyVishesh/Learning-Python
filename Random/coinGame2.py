
import random, time
print(''''



''')

def chance(coins,turn,gain,dices,num):
      
      coin = coins*turn
      
      for i in range(1,turn+1):

         dice = random.randint(1,((6**dices)))
         if dice == num:
            coin =coin + gain
            print(f"\n   WIN - number on dice = {dice} \t coins = {coin}\n")
            time.sleep(2)
         else:
            coin = coin-coins
            print(f"   LOST - number on dice = {dice} \t coins = {coin}")
     
         if coin == 0:
            print("   Out of coins")
            break
         
        
      if coin > 100:
            print(f"   Coins lift {coin} Profit = {coin-coins*turn}")
      else:
            print(f"   Coins lift {coin} Loss = {coins*turn-coin}")
            
            
print('''                        ******* GAME RULES ******

      1. This game is all about chance you will earn coins if you win and 
         lose on lost
      2. You have to enter no. as input when asked
      3. Next enter no. of dice to play with 
         no. of dice      prob of win/       prob of losing/                                            coins win            coin loss    
            1              1/6  =  06            5/6  = -1
            2              1/36 =  36           35/36 = -1
      4. Enter no. on which you want to bet on
      5. Higher the betting amount higher the risk
      ''')
for p in range(1):
   coins = int(input('   Enter no of coins per turn   '))
   turn =  int(input('   Enter no of turn here   '))
   print(f"   Total coins for {turn} is {coins*turn}")
   dices = int(input('   Enter no of dice you want to play with here   '))
   num = int(input('   Enter no. which you bet on   ')) 
   gain = turn*(6**dices)#int(input('Enter no of coin gain here   '))
   chance(coins,turn,gain,dices,num)
   time.sleep(0)

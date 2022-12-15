import random
 
print("Hello, Welcome To My Coin-Flip Game")

# You enter 1 flip, and it will flip the coin once, and you can run the code again to keep going.

def flip_coin():
  return random.choice(["Heads", "Tails"])
 
print(flip_coin())
 
for i in range(1):
   print("Flip " + str(i+1) + ": " + flip_coin())
 
   flips = int(input("Flips: "))
 
   total_heads = 0
   total_tails = 0
 
   for i in range(flips):
    if (flip_coin() == "Heads"):
      total_heads += 1
    else:
      total_tails += 1
 
print("Total Heads: " + str(total_heads))
print("Total Tails: " + str(total_tails))

print("Thank you for playing!")
pass
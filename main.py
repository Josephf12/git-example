import random

def generate_random_number():
  ran_num= random.randint(1,10)
  print(ran_num)
  def difference_from_answer(guess,answer):
    answer=ran_num
    if guess == answer:
      return "correct"
    elif guess > answer:
        print("too High")
    elif guess < answer:
      print("too low")
  difference_from_answer(5,ran_num)    
    
generate_random_number()

#def difference_from_answer(guess,answer):
  
  
def introduction():
  print "Smash Battle\n"
  print "Ruben wants to smash Who?\n"
  print "He can play either Leo, Antonio, or Angel\n"
  peanuts()

def peanuts():
  print "l for Angel and w for the choice of either Antonio or Leo\n"
  answer = raw_input()
  if answer == "l":
    print "New Challenger Approaching\n"
    Angel_Explodes()
  if answer == "w":
    print "Leo or Antonio who will be destroied?\n"
    the_choice()

def the_choice():
  print "Will Ruben fight Antonio or Leo since he is the one with the 3ds and Antonio just borrows them from the other guys around.\n"
  print "a for Antonio and e for Leo"
  answer = raw_input()
  if answer == "a":
    print "New Challenger Approaching\n"
    Antonio_Wins()
  if answer == "e":
    print "New Challenger Approaching\n"
    Leo_Rages()

def Angel_Explodes():
  print "Angel starts to furiously spam villager, but with his lack of training his lack of blood pressure starts to rise tremendously.\n"
  print "His rising blood pressure along with the recent loss he just recieved by losing to Ruben causes his appendix to explode.\nThis makes him realise its not worth it to play against Ruben while he is being shipped off into an ambulance by the paramedics."

def Leo_Rages():
  print "Leo loses to Ruben and throws his 3ds into the office window only to be pulled into the office to get anger mangement."

def Antonio_Wins():
  print "Antonio wins against Ruben by playing Mario."
introduction()

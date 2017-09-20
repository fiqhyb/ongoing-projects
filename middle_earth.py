from threading import Timer
#sequences
seq1=("You realized that you should've hastened your pace as you ride into the beautiful elven city of Rivendell."
      "\nYou walk into a large, circular room that is open to nature and is beyond any beauty that you've seen."
      "\nYou find a seat and you notice that many men, elves, hobbits, dwarves, and wizards are also sitting before Elrond at his council."
      "\nOf which race are you?")
#inputs
input1=("choose perspective\t\n1. first person\t\n2. third person")

print("Defender Of Middle Earth")
def timeout():
    print("please wait...")
t = Timer(1 , timeout)
t.start()
def timeout():
    print("Even the smallest person can change the course of the future...")
t = Timer(10 , timeout)
t.start()
def timeout():
    print(seq1)
t = Timer(15 , timeout)
t.start()
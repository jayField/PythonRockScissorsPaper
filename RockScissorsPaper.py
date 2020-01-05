"""
    RSP game vs A.I user
    A.I user will show for us his random RSP
    You just do win!
"""
import random

rsp = ["rock", "scissors", "paper"]

# for winning rate
cnt_full = 0
cnt_win = 0

# start the game
while (1):

    # It is rsp of A.I
    random.shuffle(rsp)

    # your rsp
    my_rsp = input("rock? scissors? paper?: ")

    # quit point
    if (my_rsp == "quit"):  # quit
        break

    print("you are %s  vs A.I is %s " % (my_rsp, rsp[0]))
    cnt_full += 0

    # drawing condition
    if (my_rsp == rsp[0]):
        print("Draw")
        if (cnt_full != 0):
            print("Now your winning rate is %0.2f%%" % (cnt_win / cnt_full * 100))
            print()
        else:
            print("Now your winning rate is %d" % cnt_full)
            print()

    # User winning condition
    elif ((my_rsp == "rock" and rsp[0] == "scissors") or (my_rsp == "scissors" and rsp[0] == "paper") or (
            my_rsp == "paper" and rsp[0] == "rock")):

        print("YOU WIN")
        cnt_full +=1
        cnt_win += 1
        print("Now your winning rate is %0.2f%%" % (cnt_win / cnt_full * 100))
        print()

    # A.I winning condition
    else:
        cnt_full += 1
        print("A.I WIN")
        print("Now your winning rate is %0.2f%%" % (cnt_win / cnt_full * 100))
        print()


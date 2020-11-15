print(" ")
print("Choose a candidate to vote ")
print("INPUT 1 FOR NARENDRA MODI")
print("INPUT 2 FOR RAHUL GANDHI")
print("INPUT 3 FOR MAMTA BANAERJEE")
print("INPUT 4 FOR NITISH PATEL")
print("INPUT 7 FOR NULL VOTES ")
print("INPUT 8 FOR NEXT LOOP RESERVATION VOTE")
print("INPUT 5 FOR FINISHING VOTING THEN VERIFY VOTES THAT EACH CANDIDATE HAS RECEIVED")
print(" ")

votegeneral = 0
vote1 = 0
vote2 = 0
vote3 = 0
vote4 = 0
vote7 = 0
vote8 = 0

vote = int(input("Input number regarding candidate: "))
print(" ")

while vote !=5:

    print(" ")
    print("Choose a candidate to vote: ")
    print("INPUT 1 FOR NARENDRA MODI:")
    print("INPUT 2 FOR RAHUL GANDHI:")
    print("INPUT 3 FOR MAMTA BANAERJEE:")
    print("INPUT 4 FOR NITISH PATEL:")
    print("INPUT 7 FOR NULL VOTES: ")
    print("INPUT 8 FOR NEXT LOOP RESERVATION VOTE")
    print("INPUT 5 FOR FINISHING VOTING THEN VERIFY VOTES THAT EACH CANDIDATE HAS RECEIVED")
    print(" ")

    vote = int(input("Input number regarding candidate: "))
    print(" ")

    if vote == 1:
        vote1 = vote1+1

    elif vote == 2:

        vote2 = vote2+1

    elif vote == 3:

        vote3 = vote3+1

    elif vote == 4:

        vote4 = vote4+1

    elif vote == 7:

        vote7 = vote7+1

    elif vote == 8:

        vote8 = vote8+1

    else:
     print()

print("ELECTIONS RESULT")
print(" ")
print("NARENDRA MODI: ",vote1)
print(" ")
print("RAHUL GANDHI: ",vote2)
print(" ")
print("MAMTA BANAERJEE: ",vote3)
print(" ")
print("NITISH PATEL: ",vote4)
print(" ")
print("NULL VOTES: ",vote7)
print(" ")
print("NEXT LOOP VOTES: ",vote8)


if vote1>vote2 & vote1>vote3 | vote1>vote4 :
    print(" ")
    print("NARENDRA MODI WON")
    print(" ")

elif vote2>vote1 & vote2>vote3 |vote2>vote4 :
    print(" ")
    print("RAHUL GANDHI WON")
    print(" ")

elif vote3 > vote2 & vote3>vote1 | vote3>vote4:
    print(" ")
    print("MAMTA BANAERJEE WON")
    print(" ")

elif vote4>vote1 & vote4>vote2 | vote4>vote3:
        print(" ")
        print("NITISH PATEL WON")
        print(" ")
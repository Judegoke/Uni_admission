#UNIVERSITY ADMISSION
"""
A university gave a project to create a admission selection programme for them.
The programmer should prompt the user to input his/her name, after that the program will welcome the user and then prompt the user to
input his/her JAMB score, after the post UTME score and the program will calculate the aggregate score ((jamb score / 8) + (post-utme score / 2)).
Now the program should be able to tell the user the course he/she can apply for according to his/her aggregate score.

            Outline
0 - 49           Fail
50 - 60          Agric,Botany,Zoology,Biology,Economics
61 - 70          Computer Sci.,Statictics, Physchology,Theatre Art
71 - 80          Vetenary, CLA, Mathe, Biochemistry
81 - above       Medicine, Law, Nursing.
"""

name = input("Enter your name: ")
print ("Welcome "  + (name))

jamb_score = float (input("Please, enter your Jamb Score: "))
post_score = float (input("Please, enter your Postutme Score: "))

aggregate = ((jamb_score / 8) + (post_score / 2))
print(aggregate)

if aggregate >= 0 and aggregate <= 40:
    print("fail")
elif aggregate >= 50 and aggregate <= 60:
    print("Agric, Botany, Biology, Economics")
elif aggregate >= 61 and aggregate <= 70:
    print("Computer, Statistics, Physchology, Theatre Art")
elif aggregate >= 71 and aggregate <= 80:
    print("Vetenary, CLA, mathematics, Biochemistry")
else:
    print("Medicine, Law, Nursing")


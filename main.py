#Purpose
print("The Purpose of this is to determine acceptance at the University of Fabrizio")
def university_of_fabrizio_admittance():
#1st Input 
    grade_point_avg = float(input("What's your GPA(0-4 scale)?"))
#1st Output of Admittace
    if grade_point_avg > 4:
        gpa_more_4 = "Calibrate to a 0-4 scale"
        return gpa_more_4
    elif grade_point_avg >= 3:
        print(honors_program())
        print(sports_team(grade_point_avg))
    elif grade_point_avg >=2:
        waitlisted = "Your Waitlisted"
        return waitlisted
    else:
        denied = "You're Denied"
        return denied


def sports_team(gpa):
#2nd Input about sports(YES/No)
    sports_involvment = str(input("Do you want to do sports? Yes or No"))
    sports_involvment.strip()
#IF YES leads to an If statement requesting sport lvl, which then leads to a nested if statement regarding the lvl of sport team the user would be able to play at
    if sports_involvment.upper() == "YES":
        sport_choice = str(input("What sport do you play?"))
        sport_choice.strip()
        sport_lvl = int(input("What level are you in this sport? (On a scale of 1-10):"))

        if sport_lvl > 8:
            if gpa >= 3.25:
                school_team = "You made varsity" + sport_choice.lower()
                return school_team
            else:
                school_team = "You made club" + sport_choice.lower()
                return school_team
        if sport_lvl > 5:
            if gpa >= 3.25:
                school_team = "You made club" + sport_choice.lower()
                return school_team
            else:
                school_team = "You made intramural" + sport_choice.lower()
                return school_team
        else:
            if gpa >= 3.25:
                school_team = "You made intramural" + sport_choice.lower()
                return school_team
            else:
                school_team = "You made bench warmer role" + sport_choice.lower()
                return school_team
    else:
        move_on = "Lets move on"
        return move_on

#Functions used to determine outcome of users acceptance in an honors program
def honors_calc(scale):
    if scale > 17:
        SAH = "You have been accepted into Super Awesome Honors Program"
        return SAH
    elif scale > 12:
        AAH = "You have been accepted into Also Awesome Honors Program"
        return AAH
    else:
        print("Sorry you didn't qualify for any honors program")
def honors_program():
    join_honors = str(input("Whould you like to join Honors program?:Yes or no"))
    join_honors.strip()

    if join_honors.upper() == "YES":
        work_exp = int(input("Work experience(Scale of 1-10"))
        community_rating = int(input("Community rating(Scale of 1-10"))
        leadership_rating = int(input("Leadership rating(Scale of 1-10)"))

        maximum_val1 = max(community_rating, work_exp)
        minimum_val1 = min(community_rating, work_exp)

        maximum_val2 = max(leadership_rating, minimum_val1)

        total = maximum_val1 + maximum_val2
        if total > 17:
            print("You will be joining the Super Awesome Honors Program")
        elif total >= 12:
            print("You will be joining the Also Awesome Honors Program")
        else:
            print("You are not eligible for any honors program")
        end_of_program = "You've been admitted to the University, Congrats"
        return end_of_program

    else:
        end_of_program = "You've been admitted to the University, Congrats"
        return end_of_program
def main():
    print(university_of_fabrizio_admittance())


main()

print("Thanks for using this program")

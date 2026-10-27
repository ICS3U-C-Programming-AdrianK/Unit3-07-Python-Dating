# /usr/bin/env python3
# created by : Adrian student 
# Date : 26 OCT 2026
# This programs tells the grandparents if someone is 
# eligible to date their grandchild
import constants 


def main() :
    # get the candidate age as a string 
    candidate_age_str = input("Enter your age : ")
    print("")

    try :
        # cast the candidate age to an integer
        candidate_age_int = int(candidate_age_str )

        # check eligibility
        if candidate_age_int > constants.MIN and candidate_age_int < constants.MAX :
            print("you can date my grandchild")
        elif candidate_age_int <= constants.MIN :
            print("you are too young to date my grandchild")
        elif candidate_age_int >= constants.MAX :
            print("you are too old to date my grandchild")
    except ValueError :
        print("{} is not an integer". format(candidate_age_str))
    finally :
        print("Thank you for you interest")


if __name__ == "__main__":
    main()
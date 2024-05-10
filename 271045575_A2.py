# -------------------USER PART, WITH OBJECTS CREATED IN BUILT IN FUNCTIONS------------------#
import pickle
class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password
    
    def display_info(self):
        print(f"username:{self.name}\npassword:{self.password}")

def signup():
    print("\nWELCOME TO DIGITAL CINEMA, KINDLY SETUP YOUR USERNAME AND PASSWORD\n")
    name = input("Enter your desired User Name:")
    password = input("Enter your desired Password:")
    print("Sign Up completed!")
    print("Please wait for a moment...")
    return User(name, password)


def save_user_info(user_info):
    with open('user_info.py', 'wb') as f:
        pickle.dump(user_info, f)


def load_user_info():
    with open('user_info.py', 'rb') as f:
        return pickle.load(f)

user_info = signup()
save_user_info(user_info)


class Admin:

    def __init__(self,movie_id,title,duration,seats):
        self.movie_id = movie_id
        self.title = title
        self.duration = duration
        self.seats = seats
        
        

    def display_movie_info(self):
        print(f"\nMovie No.{self.movie_id}\nTitle: {self.title}\nDuration: {self.duration}\nAvailable seats: {self.seats}")


def movie_list():
    movie1 = Admin(1,"Inception", "2 hours", 100)
    movie2 = Admin(2,"Interstellar", "2.5 hours", 120)
    movie3 = Admin(3,"Insidious Chapter 2","2.5 hours",80)
    movie4 = Admin(4,"Jumanji","3 hours",110)
    lists = []
    lists.append(movie1)
    lists.append(movie2)
    lists.append(movie3)
    lists.append(movie4)
    for i in lists:
        i.display_movie_info()
        
# ---------------------------------------- Screen and other classes ------------------------------------------------#
class Screen:
    def __init__(self,screen_id):
        self.screen_id = screen_id

    def display_screen_info(self):
        print(f"The number of screens avaialable for this Title are: {self.screen_id}\n")

class Timeslot:
    def __init__(self, t, timeslots):
        self.timeslots = timeslots
        self.t = t

    def display_timeslot_info(self):
        print(f"{self.t}. {self.timeslots}")

class Ticket:
    def __init__(self, seatss, price):
        self.seatss = seatss
        self.price = price

    def display_ticket_info(self, movie_title, time_slot):
        self.movie_title = movie_title
        self.time_slot = time_slot
        total_price = self.seatss * self.price
        
        print(f"\n-----BOOKING DETAILS-----\nMovie: {self.movie_title}\nTime Slot: {self.time_slot}\nNumber of Seats: {self.seatss}\nPrice per Seat: ${self.price}\nTotal Price: ${total_price}")
        


def user_choice():
    
    while True:
        user = int(input("\nEnter the movie number you want tickets for: "))

        if user == 4:
            screen = Screen(2)
            screen.display_screen_info()
            print("Available Timeslots are:")
            timeslot1 = Timeslot("1", "6:00 PM - 9:00 PM")
            timeslot2 = Timeslot("2", "9:30 PM - 12:30 AM")
            movie_title = "Jumanji"
            timeslot1.display_timeslot_info()
            timeslot2.display_timeslot_info()
            confirmation = input("\nAre you sure you want to continue?(y/n):")
            if confirmation == "y":
                    user2 = int(input("\nEnter the desired time slot:"))    
                    seats_no = int(input("\nEnter the number of seats you want to book(7$ each):"))
                    details = Ticket(seats_no,7)
                    if user2 == 1:
                        details.display_ticket_info(movie_title, "6:00 AM - 9:00 AM")
                    elif user2 == 2:
                        details.display_ticket_info(movie_title, "9:30 AM - 12:30 AM")
                    break
            else:
                    movie_list()
        elif user == 3:
            screen = Screen(1)
            screen.display_screen_info()
            print("Available Timeslots are:")
            timeslot1 = Timeslot("1", "6:00 AM - 9:00 AM")
            movie_title = "Insidious Chapter 2"
            timeslot1.display_timeslot_info()
            confirmation = input("\nAre you sure you want to continue?(y/n):")
            if confirmation == "y":
                    user2 = int(input("\nEnter the desired time slot:"))
                    seats_no = int(input("\nEnter the number of seats you want to book(7$ each):"))
                    details = Ticket(seats_no,7)
                    if user2 == 1:
                        details.display_ticket_info(movie_title, "6:00 AM - 9:00 AM")
                    break
            else:
                    movie_list()
        elif user == 2:
            screen = Screen(4)
            screen.display_screen_info()
            print("Available Timeslots are:")
            timeslot1 = Timeslot("1", "6:00 PM - 9:00 PM")
            timeslot2 = Timeslot("2", "9:30 PM - 12:30 AM")
            timeslot3 = Timeslot("3", "1:00 AM - 3:00 AM")
            timeslot4 = Timeslot("4", "3:30 AM - 6:30 AM")
            movie_title = "Interstellar"
            timeslot1.display_timeslot_info()
            timeslot2.display_timeslot_info()
            timeslot3.display_timeslot_info()
            timeslot4.display_timeslot_info()
            confirmation = input("\nAre you sure you want to continue?(y/n):")
            if confirmation == "y":
                    user2 = int(input("\nEnter the desired time slot:"))
                    seats_no = int(input("\nEnter the number of seats you want to book(7$ each):"))
                    details = Ticket(seats_no,7)  
                    if user2 == 1:
                        details.display_ticket_info(movie_title, "6:00 PM - 9:00 PM")
                    elif user2 == 2:
                        details.display_ticket_info(movie_title,"9:30 PM - 12:30 AM")
                    elif user2 == 3:
                        details.display_ticket_info(movie_title,"1:00 AM - 3:00 AM")
                    elif user2 == 4:
                        details.display_ticket_info(movie_title,"3:30 AM - 6:30 AM")
                    break
            else:
                    movie_list()
        elif user == 1:
            screen = Screen(3)
            screen.display_screen_info()
            print("Available Timeslots are:")
            timeslot1 = Timeslot("1", "6:00 PM - 9:00 PM")
            timeslot2 = Timeslot("2", "9:30 PM - 12:30 AM")
            timeslot3 = Timeslot("3", "1:00 AM - 3:00 AM")
            movie_title = "Inception"
            timeslot1.display_timeslot_info()
            timeslot2.display_timeslot_info()
            timeslot3.display_timeslot_info()
            confirmation = input("\nAre you sure you want to continue?(y/n):")
            if confirmation == "y":
                    user2 = int(input("\nEnter the desired time slot:"))
                    seats_no = int(input("\nEnter the number of seats you want to book(7$ each):"))
                    details = Ticket(seats_no,7)
                    if user2 == 1:
                        details.display_ticket_info(movie_title, "6:00 PM - 9:00 PM")
                    elif user2 == 2:
                        details.display_ticket_info(movie_title,"9:30 PM - 12:30 AM")
                    elif user2 == 3:
                        details.display_ticket_info(movie_title,"1:00 AM - 3:00 AM") 
                    elif user2 >= 4:
                        print("Invalid choice was made. please try again later..")
                    break
            else:
                    movie_list()
        if user >= 4:
            print("Invalid choice were made.")
    


def loginpage():
    print("\nWelcome,Kindly enter your user,pass to get access to the movie lists.\n")
    
    count = 0
    
    while count < 3:
        name = input("Please Enter the username:")
        password = input("Please enter the password:")

        if name == user_info.name and password == user_info.password:
            print("\nLogged in Successful!\n")
            movie_list()
            user_choice()
            break
        else:
            count += 1
            print (f"Incorrect password/username!({count}/3)")

        if count >= 3:
            return ("Out of tries, please try again later!")
  
loginpage()
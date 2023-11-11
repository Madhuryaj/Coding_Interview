seats = [0] * 10  # 10 seats available

def menu():
    running = True
    while running:
        print("Welcome to Train Ticket Booking System ")
        print("1. Book a ticket")
        print("2. View available seats")
      
        print("3. Exit")
        choice = input("Enter your choice: ")

        try:
            choice = int(choice)
        except:
            print("Invalid input, please enter a number from the choice below.")
            continue

        if choice == 1:
            book_ticket()
        elif choice == 2:
            view_seats()
        elif choice == 3:
            running = False
            print("Thank you for using Train Ticket Booking System")
        else:
            print("Invalid input, please enter a number from the choice below")


def book_ticket():
    avaliable_seats=view_seats()+1
    #print("Available seats:",avaliable_seats)
    ticket_type = input("Enter the ticket type 'S' for Standard and 'F' for First class : ")
    num_tickets = input("Enter number of tickets to book (max 4 for  Standard and max 4 for first class per transaction ): ")

    num_tickets = int(num_tickets)

    if num_tickets < 1 or num_tickets > 4:
      print("----------------------------------------------------")
      print("Max 4 tickets can be booked for Standard Type and 5 tickets for First Class per session.If you want to book more tickets, please book again.")
      return
    if ticket_type in ("S","s"):
      total_cost = num_tickets * 100  # €100 per ticket
    if ticket_type in ("F","f"):
      total_cost = num_tickets * 150  # €150 per ticket
    else:
      print("Invalid ticket type. Please enter 'S' for Standard and 'F' for First Class. Try Again")
    print("----------------------------------------------------")
    print(f"Total cost is €{total_cost}")
    print("----------------------------------------------------")
    confirm = input("Enter 1 to confirm booking or any other number key to cancel: ")

    try:
        confirm = int(confirm)
        
    except:
        print("----------------------------------------------------")
        print("Oops! Since you entered other than 1, Booking was unsuccessful. Please try again!")
        print("----------------------------------------------------")

        return

    if confirm == 1:#and seats_booked<11:
        seats_booked = 0
        for i in range(len(seats)):
            if seats[i] == 0:
                seats[i] = 1
                print(f"Seat {i+1} booked successfully")
                seats_booked += 1
                avaliable_seats=avaliable_seats-num_tickets
                if seats_booked == num_tickets:
                    break
        print("----------------------------------------------------")
        print("Tickets booked successfully! Enjoy your journey")
        print("----------------------------------------------------")
    else:
        print("----------------------------------------------------")
        print("Oops! Since you entered other than 1, Booking was unsuccessful. Please try again!")
        print("----------------------------------------------------")

def view_seats():
    print("Available Seats:")
    for i in range(len(seats)):
        if seats[i] == 0:
            print(f"Seat {i+1} is available")
    return seats[i];


menu()

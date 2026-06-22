class CinemaHall:
    
    def __init__(self, movie_title: str, total_seats: int, ticket_price: float) -> None:
        self.movie_title = movie_title
        self.total_seats = total_seats
        self.ticket_price = ticket_price
        self.__booked_seats = []
    
    @property
    def income(self) -> int:
        return self.ticket_price * len(self.__booked_seats)
    
    @property
    def booked_seats(self) -> tuple:
        return tuple(self.__booked_seats)
    
    @property
    def available_seats(self) -> int:
        return self.total_seats - len(self.__booked_seats)
        

    def book_seat(self, seat_number: int, ) -> None:
        if seat_number < 1 or seat_number > self.total_seats or seat_number in self.__booked_seats:
            print("This seat cannot be reserved.")
        else:
            self.__booked_seats.append(seat_number)
            print("Your seat has been reserved.")

    def cancel_booking(self, seat_number: int) -> None:
        if seat_number in self.__booked_seats:
            self.__booked_seats.remove(seat_number)
            print("Your reservation has been cancelled.")
        else:
            print("An error occurred")

    def show_hall_info(self,):
        print(f"{"-" * 5}{self.movie_title}{"-" * 5}")
        print(f"Total number of available seats: {self.total_seats}")
        print(f"Total number of reserved seats: {self.booked_seats}")
        print(f"Free seats: {self.available_seats}")
        print(f"Ticket price: {self.ticket_price}")
        print(f"Amount of money earned on tickets: {self.income}")

class VIPCimemaHall(CinemaHall):

    def __init__(self, movie_title: str, total_seats: int, ticket_price: float, service_fee: float) -> None:
        super().__init__(movie_title, total_seats, ticket_price)
        self.service_fee = service_fee

    @property
    def income(self) -> int:
        return len(self.booked_seats) * (self.ticket_price + self.service_fee)



cinema = CinemaHall("Batman", 30, 333.3,)
cinema.show_hall_info()
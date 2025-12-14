
cinema_seats = [
    ['A', 'A', 'B', 'A', 'A'],
    ['A', 'B', 'B', 'A', 'A'],
    ['A', 'A', 'A', 'A', 'B'],
    ['B', 'A', 'A', 'A', 'A'],
    ['A', 'B', 'A', 'A', 'A']
]
def seats_total(seats):
    rows = len(seats)
    columns = len(seats[0])
    return rows * columns
def seats_available(seats):
    count = 0
    for row in seats:
        count += row.count('A')
    return count

def seats_booked(seats):
    count = 0
    for row in seats:
        count += row.count('B')
    return count
def seat_status(seats, row, place):
    status_char = seats[row - 1][place - 1]
    
    if status_char == 'A':
        return "Available"
    elif status_char == 'B':
        return "Booked"
    else:
        return "Invalid Seat Code"
total = seats_total(cinema_seats)
available = seats_available(cinema_seats)
booked = seats_booked(cinema_seats)

print('CINEMA INFORMATION TABLE')
print('------------------------')
print(f"Total Seats: {total}")
print(f"Seats available: {available}")
print(f"Seats booked: {booked}")
print('------------------------')
print(f"Seat in row 1, place 1: {seat_status(cinema_seats, 1, 1)}")
print(f"Seat in row 5, place 5: {seat_status(cinema_seats, 5, 5)}")
print(f"Seat in row 3, place 5: {seat_status(cinema_seats, 3, 5)}")
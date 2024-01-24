"""
Łańcuchy znaków (napisy) to jedne z najważniejszych 
typów danych w języku Python. Pozwalają one na przechowywanie
 i manipulację tekstowymi danymi.
"""

# usuń prefix 'Seat ' dla zmiennej seat_assignment i przypisz do zmiennej clean_seat_assignment
# usuń prefix 'Group ' dla zmiennej boarding_group i przypisz do zmiennej clean_boarding_group
# usuń suffix ' mins' dla zmiennej delay_time i przypisz do zmiennej clean_delay_time
# usuń suffix ' kg' dla zmiennej baggage_weight i przypisz do zmiennej clean_baggage_weight

seat_assignment = 'Seat 24A'
boarding_group = 'Group C'
delay_time = '30 mins'
baggage_weight ='23 kg'

clean_seat_assignment = seat_assignment.removeprefix("Seat ")
clean_boarding_group = boarding_group.removeprefix("Group ")
clean_delay_time = delay_time.removesuffix(' mins')
clean_baggage_weight = baggage_weight.removesuffix(' kg')

print(clean_seat_assignment)
print(clean_boarding_group)
print(clean_delay_time)
print(clean_baggage_weight)

print("---")

gate_number = 'B12'
flight_number = '123'
seat_assignment = '24A'

gate_number_zero = gate_number.zfill(len(gate_number) + 1)
flight_number_zero = flight_number.zfill(len(flight_number) + 3)
seat_assignment_zero = seat_assignment.zfill(len(seat_assignment) + 1)

print(gate_number_zero)
print(flight_number_zero)
print(seat_assignment_zero)

print("---")

"""
1. usuń białe znaki dookoła tekstu
2. zamień słowo 'Boarding' na 'Departing'
3. zamień małe litery w zmiennej seat_assignment na duże 
4. ze zmiennej gate_number wyodrębnij nazwę termiala oraz numer i przypisz do osobnych zmiennych
5. listę cities połącz w jeden łańcuch znaków
"""
seat_assignment = ' 24A '
gate_announcement = 'Boarding for flight UA 123 has begun.'
seat_assignment = '24a'
gate_number = 'B12'
cities = ['New York', 'Los Angeles', 'Chicago']

clean_seat_assignment = seat_assignment.replace(" ", "")
updated_announcement = gate_announcement.replace("Boarding", "Departing")
uppercase_seat = seat_assignment.upper()
terminal = gate_number[0]
gate = gate_number[1:]
cities_string = ", ".join(cities)

print(clean_seat_assignment)
print(updated_announcement)
print(uppercase_seat)
print(terminal)
print(gate)
print(cities_string)

print("---")

# Używając odpowiednich metod tekstowych oraz przekształceń wykorzystując podane zmienne wydrukuj do konsoli schemat rozkładu miejsc w samolocie 
seat_map_header = 'SEAT MAP'
row1 = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1']
row1First = [row1[0], row1[1], row1[2]]
row1Second = [row1[3], row1[4], row1[5]]

row2 = ['A2', 'B2', 'C2', 'D2', 'E2', 'F2']
row2First = [row2[0], row2[1], row2[2]]
row2Second = [row2[3], row2[4], row2[5]]

print(f"{10 * '-'}SEAT MAP{9 * '-'}")
print (f"{' - '.join(row1First)} | {' - '.join(row1Second)}")
print (f"{' - '.join(row2First)} | {' - '.join(row2Second)}")

print("---")
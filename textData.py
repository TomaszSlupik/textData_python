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
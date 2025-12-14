# Prints vehicle registration numbers from Krakow
#
polish_license_plates = [
    'KR5233F', 'PO6987E', 'KR16179', 'BI7192L', 'KK1225S', 
    'WA7930T', 'SK6921I', 'KK6110B', 'KR9053H', 'BI8052Q',
    'KK5498S', 'LU4864U'
]

# Initialize the counter for numbering the Krakow plates
counter = 1

print("--- Krakow License Plates ---")

for car_number in polish_license_plates:
    if car_number.startswith('KR') or car_number.startswith('KK'):
        print(f"{counter}. {car_number}")
        counter += 1
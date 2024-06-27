import csv
import os
import django
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'foodtruck_project.settings')
django.setup()

from foodtrucks.models import FoodTruck


def parse_date(date_str, format1='%m/%d/%Y %I:%M:%S %p', format2='%Y%m%d'):
    """Parse a date string using multiple formats."""
    for fmt in (format1, format2):
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    return None


def get_float(value):
    """Convert a string to a float, or return None if the string is empty."""
    try:
        return float(value)
    except ValueError:
        return None


def get_int(value):
    """Convert a string to an int, or return None if the string is empty."""
    try:
        return int(value)
    except ValueError:
        return None


def load_data():
    with open('food-truck-data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            nois_sent = parse_date(row['NOISent']) if row['NOISent'] else None
            approved = parse_date(row['Approved'])
            received = parse_date(row['Received'])
            expiration_date = parse_date(row['ExpirationDate'])

            FoodTruck.objects.create(
                locationid=get_int(row['locationid']),
                applicant=row['Applicant'],
                facility_type=row['FacilityType'],
                cnn=get_int(row['cnn']),
                location_description=row['LocationDescription'],
                address=row['Address'],
                blocklot=row['blocklot'],
                block=row['block'],
                lot=row['lot'],
                permit=row['permit'],
                status=row['Status'],
                food_items=row['FoodItems'],
                x=get_float(row['X']),
                y=get_float(row['Y']),
                latitude=get_float(row['Latitude']),
                longitude=get_float(row['Longitude']),
                schedule=row['Schedule'],
                dayshours=row['dayshours'] if row['dayshours'] else None,
                nois_sent=nois_sent,
                approved=approved if approved else datetime.now(),  # Default to current date if approved is None
                received=received if received else datetime.now(),  # Default to current date if received is None
                prior_permit=bool(int(row['PriorPermit'])),
                expiration_date=expiration_date,
                location=row['Location'],
                fire_prevention_districts=get_int(row['Fire Prevention Districts']),
                police_districts=get_int(row['Police Districts']),
                supervisor_districts=get_int(row['Supervisor Districts']),
                zip_codes=get_int(row['Zip Codes']),
                neighborhoods_old=row['Neighborhoods (old)'],
            )
    print("Data loaded  ")

if __name__ == '__main__':
    load_data()

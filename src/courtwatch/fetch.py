# src/courtwatch/fetch.py

import requests
from datetime import datetime, timedelta

VENUES = [
    {
        "name": "Vauxhall Park",
        "slug": "VauxhallPark",
        "url": "https://clubspark.lta.org.uk/vauxhallpark/Booking/bookbycourt"
    },
    {
        "name": "Kennington Park",
        "slug": "KenningtonPark",
        "url": "https://clubspark.lta.org.uk/KenningtonPark/Booking/bookbycourt"
    },
    {
        "name": "Clapham Common",
        "slug": "ClaphamCommon",
        "url": "https://clubspark.lta.org.uk/ClaphamCommon/Booking/bookbycourt"
    }
]

def minutes_to_time_string(minutes: int) -> str:
    return (datetime.min + timedelta(minutes=minutes)).strftime('%H:%M')

def fetch_available_slots(start_date: str, end_date: str, venue_slug: str = "VauxhallPark") -> list[dict]:
    """
    Fetch available sessions from start_date to end_date (inclusive).
    Marks sessions outside booking window (typically 7 days ahead).
    """
    today = datetime.today().date()
    max_bookable_date = today + timedelta(days=7)

    url = f"https://clubspark.lta.org.uk/v0/VenueBooking/{venue_slug}/GetVenueSessions"

    results = []

    current = datetime.strptime(start_date, "%Y-%m-%d").date()
    end = datetime.strptime(end_date, "%Y-%m-%d").date()

    while current <= end:
        date_str = current.strftime("%Y-%m-%d")
        params = {
            "resourceID": "",
            "startDate": date_str,
            "endDate": date_str,
            "roleId": "",
        }

        res = requests.get(url, headers={"Accept": "application/json", "User-Agent": "courtwatch-cli"}, params=params)

        if res.status_code != 200:
            print(f"Error fetching {date_str}: {res.status_code}")
            current += timedelta(days=1)
            continue

        data = res.json()

        for resource in data.get("Resources", []):
            court_name = resource.get("Name")
            for day in resource.get("Days", []):
                session_date = datetime.strptime(day["Date"][:10], "%Y-%m-%d").date()
                for session in day.get("Sessions", []):
                    if session.get("Capacity", 0) > 0:
                        results.append({
                            "date": session_date.strftime("%Y-%m-%d"),
                            "court": court_name,
                            "start": minutes_to_time_string(session["StartTime"]),
                            "end": minutes_to_time_string(session["EndTime"]),
                            "cost": session.get("CourtCost", 0.0),
                            "bookable": session_date <= max_bookable_date
                        })

        current += timedelta(days=1)

    return results

from courtwatch.display import show_availability

test_data = [
    {
        "date": "2025-07-22",
        "court": "Court 1",
        "start": "07:00",
        "end": "08:00",
        "cost": 7.70
    },
    {
        "date": "2025-07-22",
        "court": "Court 2",
        "start": "09:00",
        "end": "10:00",
        "cost": 7.70
    }
]

show_availability(test_data)

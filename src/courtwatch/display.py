from rich.console import Console
from rich.table import Table
from rich import box
from datetime import datetime

def is_outside_working_hours(date_str: str, start_time: str) -> bool:
    """Returns True if slot is before 9am / after 6pm on weekdays, or anytime on weekends"""
    date = datetime.strptime(date_str, "%Y-%m-%d")
    hour = int(start_time.split(":")[0])
    weekday = date.weekday()  # 0 = Monday, 6 = Sunday

    if weekday >= 5:
        return True  # Saturday/Sunday = always fine
    return hour < 9 or hour >= 18

def show_availability(data: list[dict], title: str = None):
    console = Console()

    table = Table(
        title=title or "🎾 Available Court Slots",
        box=box.ROUNDED
    )

    table.add_column("Date", style="cyan")
    table.add_column("Court", style="magenta")
    table.add_column("Time", style="green")
    table.add_column("Cost/hour (£)", style="yellow", justify="right")
    table.add_column("Status", style="red")
    table.add_column("Outside Working Hours", style="blue")

    for slot in data:
        time_range = f"{slot['start']}–{slot['end']}"
        cost = f"{slot['cost']:.2f}"
        status = "✅ Bookable" if slot["bookable"] else "⏳ Not Yet Open"
        owh = "✅" if is_outside_working_hours(slot["date"], slot["start"]) else "❌"

        table.add_row(slot["date"], slot["court"], time_range, cost, status, owh)

    console.print(table)



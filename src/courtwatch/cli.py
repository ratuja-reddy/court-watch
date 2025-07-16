# src/courtwatch/cli.py
import typer
from courtwatch.fetch import fetch_available_slots, VENUES
from courtwatch.display import is_outside_working_hours, show_availability
from rich.console import Console
from rich.table import Table
from rich import print


app = typer.Typer(no_args_is_help=True) 

@app.command()
def list_courts():
    """
    List details of all available tennis courts.
    """
    courts = [
        {
            "name": "Vauxhall Park",
            "url": "https://clubspark.lta.org.uk/vauxhallpark/Booking/bookbycourt",
            "location": "Vauxhall, London",
            "postcode": "SW8 1AB"
        },
        {
            "name": "Kennington Park",
            "url": "https://clubspark.lta.org.uk/KenningtonPark/Booking/bookbycourt",
            "location": "Kennington, London",
            "postcode": "SE11 5SS"
        },
        {
            "name": "Clapham Common",
            "url": "https://clubspark.lta.org.uk/ClaphamCommon/Booking/bookbycourt",
            "location": "Clapham, London",
            "postcode": "SW4 6DZ"
        }
    ]

    console = Console()
    table = Table(title="🎾 Available Tennis Courts")

    table.add_column("Court", style="cyan", no_wrap=True)
    table.add_column("Booking URL", style="green")
    table.add_column("Postcode", style="green")

    for court in courts:
        table.add_row(court["name"], court["url"], court["postcode"])

    console.print(table)

from datetime import datetime, timedelta

@app.command()
def check(
    start_date: str,
    end_date: str,
    outside_working_hours: bool = typer.Option(
        False,
        "--outside-working-hours",
        help="Show only slots outside working hours (before 9am or after 6pm on weekdays, all day weekends)"
    ),
):
    """
    Show available tennis slots for all venues between two dates.
    """
    for venue in VENUES:
        name = venue["name"]
        slug = venue["slug"]
        url = venue["url"]

        print(f"\n🔗 [bold underline blue]{name}[/] - [green]{url}[/]\n")

        data = fetch_available_slots(start_date, end_date, venue_slug=slug)

        if outside_working_hours:
            data = [
                slot for slot in data
                if is_outside_working_hours(slot["date"], slot["start"])
            ]

        if data:
            show_availability(data, title=f"🎾 {name} — Available Court Slots")
        else:
            print(f"[italic]No availability for {name}[/italic]")




def main():
    app()

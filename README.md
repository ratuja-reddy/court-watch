# 🎾 CourtWatch CLI

Booking courts in London is a pain. `court-watch` makes it easier! 

A CLI tool which will show you all available and bookable courts. 

No need to have to click through several pages and scan for if a court is available only
to try and checkout and realized it was never available all along.

## ✅ Features

- Multi-day availability checking
- Supports Vauxhall Park, Clapham Common, and Kennington Park (and more coming)
- Displays:
  - Court names and booking links
  - Times and costs
  - Whether slots are within working hours
  - Whether booking is currently open
- Beautiful CLI output using [Rich](https://github.com/Textualize/rich)

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourname/courtwatch.git
cd courtwatch
```

### 2. Install the CLI

Make sure that Poetry is installed. 

```bash
poetry build
pip install dist/courtwatch-0.1.0-py3-none-any.whl
```

## 🥳 Usage

```bash
courtwatch check <start-date> <end-date>
```

## 🔮 Coming up
- More London locations & location filters
- Time-of-day filters (e.g. only after 6 PM or early mornings)
- Web dashbaord

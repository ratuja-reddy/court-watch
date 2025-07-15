# 🎾 CourtWatch CLI

A sleek CLI tool to check real-time availability of public tennis courts in London.

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

### 2. Insteall the CLI

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
- More London locations
- Time-of-day filters (e.g. only after 6 PM or early mornings)
- Web dashbaord
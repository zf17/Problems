months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def outdated():
    while True:
        date = input("Date: ")
        if "/" in date:
            try:
                month, day, year = map(int,date.split("/"))
                if month > 12 or day > 31:
                    continue
                return f"{year}-{int(month):02}-{int(day):02}"
            except ValueError:
                pass
        else:
            try:
                if "," not in date:
                    continue
                date = date.replace(",", "")
                month, day, year = date.split()
                day = int(day)
                if day > 31:
                    continue
                return f"{year}-{(months.index(month)+1):02}-{day:02}"
            except ValueError:
                pass

print(outdated())

# In a file called outdated.py, implement a program that prompts the user for a date, anno Domini, 
# in month-day-year order, formatted like 9/8/1636 or September 8, 1636

# Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either 
# format, prompt the user again. Assume that every month has no more than 31 days; no need to validate 
# whether a month has 28, 29, 30, or 31 days.

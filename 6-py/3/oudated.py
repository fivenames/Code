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

while True:

    try:
        date = input("Date(MM/DD/YYYY): ")

        if '/' in date:
            month, sep, date_and_year = date.partition('/')
            date, sep, year = date_and_year.partition('/')
            month = int(month)
            date = int(date)
            year = int(year)
        else:
            month, sep, date_and_year = date.partition(' ')
            month = int(months.index(month.title())) + 1
            if ',' in date_and_year:
                date, sep, year = date_and_year.partition(',')
                year = int(year.strip())
                date = int(date)
            else:
                date, sep, year = date_and_year.partition(' ')
                year = int(year)
                date = int(date)
    except (ValueError, KeyError):
        pass

    else:
        if(month > 12) or (date > 31):
            pass
        else:
            print(f"{year}-{month}-{date}")
            break

quit()







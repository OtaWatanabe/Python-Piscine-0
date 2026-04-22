from datetime import datetime

now = datetime.now()
seconds = now.timestamp()
month_str = now.strftime("%B")[:3]
day = now.day
year = now.year

print(f"Seconds since January 1, 1970: {seconds} or {seconds:.2e} in scientific notation")
print(f"{month_str} {day} {year}")
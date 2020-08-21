#!/usr/bin/python3
import datetime as dt
    
def main():
    today = dt.datetime.now()
    print(today)
    zeroth_day = today.replace(year=1972, month=9, day=27)
    diff = today - zeroth_day
    diff_secs = diff.days*60*60*24
    print(diff_secs)

if __name__ == "__main__":
    main()

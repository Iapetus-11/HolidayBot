from datetime import datetime
import bs4
import requests
import pydantic
import json
import calendar

class Holiday(pydantic.BaseModel):
    at: datetime
    name: str
    link: pydantic.HttpUrl | None

MONTHS = {month: index for index, month in enumerate(calendar.month_name) if month}
YEAR = 2022

def construct_dt(month_name: str, day: str) -> datetime:
    return datetime(YEAR, MONTHS[month_name], int(day))

def parse_holiday_box(month_name: str, e: bs4.element.Tag) -> Holiday:
    day_no = e.find(class_="holiday-day", recursive=True).string

    name_e = e.find(class_="holiday-name")

    name = name_e.string
    href = ("https://www.calendarr.com" + name_e["href"]) if name_e.has_key("href") else None

    return Holiday(at=construct_dt(month_name, day_no), name=name, link=href)

def parse(soup: bs4.BeautifulSoup) -> list[Holiday]:
    col = soup.find(class_="holidays-box-col2")

    holiday_month = None

    holidays = list[Holiday]()

    for e in col.children:
        if isinstance(e, bs4.NavigableString):
            continue

        if e.has_attr("class") and e["class"][0] == "holiday-month":
            holiday_month = e.string

        if e.has_attr("class") and e["class"][0] == "row":
            holidays.extend([parse_holiday_box(holiday_month, x) for x in e.find_all(class_="list-holiday-box")])

    return holidays

def main():
    html = requests.get("https://www.calendarr.com/united-states/observances-2022/").text

    soup = bs4.BeautifulSoup(html, "html.parser")

    holidays = parse(soup)

    with open("holidays.json", "w+") as f:
        json.dump([json.loads(h.json()) for h in holidays], f)


if __name__ == "__main__":
    main()

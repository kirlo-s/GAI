from GAI import daily_calendar,weekly_calendar,information_card

payload = {"owner":"owner",
    "info":{
        "name" : "servername"
}
}

information_card.generate(payload)
weekly_calendar.generate(payload)
daily_calendar.generate(payload)

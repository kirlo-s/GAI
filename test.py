from GAI import calendar_daily, calendar_weekly, card

payload = {"owner":"owner",
    "info":{
        "name" : "servername"
}
}

card.generate(payload)
calendar_weekly.generate(payload)
calendar_daily.generate(payload)

from GAI import calendar_daily, calendar_weekly, card

payload = {
    "owner":"owner",
    "info":{
        "name" : "aaaaaaaaaaaa"
    },
    "Gen" : False,
    "time":{
        "start" : "19:00",
        "end"   : "22:00"
    }
}

card.generate(payload)
calendar_weekly.generate(payload)
calendar_daily.generate(payload)

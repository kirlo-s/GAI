from GAI import calendar_daily, calendar_weekly, card

payload = {
    "owner":"owner",
    "info":{
        "name_" : "Suspendisse volutpat",
        "name_" : "Nulla non arcu id tellus dignissim morbi",
        "name_" : "Donec faucibus risus volutpat massa nunc",
        "name_" : "Etiam egestas imperdiet orci eu posuere. Nulla sit amet nisi",
        "name" : "[BF3 RUSH] Ground Warfare 2042 & Classic Maps"
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

from datetime import datetime
from GAI import calendar_daily, calendar_weekly, card, events
import pl

payload = pl.payloads[0]
card.card().generate(payload)
calendar_weekly.generate(payload)
events.events().generate(pl.payloads)
calendar_daily.daily().generate(pl.payloads)


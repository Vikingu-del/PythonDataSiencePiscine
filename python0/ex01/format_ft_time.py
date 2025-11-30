import datetime as dt
import pytz as pytz

dt_now = dt.datetime.now(tz=pytz.timezone("Europe/Berlin"))
dfe = dt_now.timestamp()
epoch = dt.datetime(1970, 1, 1, tzinfo=pytz.timezone("Europe/Berlin"))
dfe_sientificformat = f"{dfe:.2e}"


print(f"Seconds since {epoch.strftime('%B %-d, %Y')}: {dfe:,.4f} \
or {dfe_sientificformat} in scientific notation")
print(f"{dt_now.strftime('%B %-d %Y')}")

def get_days_later(days):
    if days == 1:
        return "(next day)"
    elif days > 1:
        return f"({days} days later)"
    return ""


def add_time(time, add, day=False):

    week_days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

    days_later = 0
    one_day = 24
    half_day = 12
    cur_time = time.replace(":", "#").replace(" ", "#").split("#")
    cur_hour, cur_min = int(cur_time[0]), int(cur_time[1])
    additional = add.split(":")
    add_hour, add_min = int(additional[0]), int(additional[1])
    meridian = cur_time[2].lower()

    total_hour = cur_hour + add_hour
    total_min = cur_min + add_min

    if total_min > 60:
        total_hour += int(total_min / 60)
        total_min = int(total_min % 60)

    if add_hour or add_min:
        if meridian == "pm" and total_hour > half_day:
            if total_hour % one_day >= 1.0:
                days_later += 1

        if total_hour >= half_day:
            hour_left = total_hour / one_day
            days_later += int(hour_left)

        tth = total_hour
        while True:
            if tth < half_day:
                break
            if tth >= half_day:
                if meridian == "am":
                    meridian = "pm"
                elif meridian == "pm":
                    meridian = "am"
                tth -= half_day

    remaining_hour = int(total_hour % half_day) or cur_hour + 1
    remaining_min = int(total_min % 60)

    results = f'{remaining_hour}:{remaining_min:02} {meridian.upper()}'
    if day:
        day = day.strip().lower()
        selected_day = int((week_days.index(day) + days_later) % 7)
        current_day = week_days[selected_day]
        results += f', {current_day.title()} {get_days_later(days_later)}'

    else:
        results = " ".join((results, get_days_later(days_later)))

    return results.strip()


print(add_time("11:43 PM", "24:20", "tueSday"))

def clock_angle(hour,  min):
    m_degree = 6 * float(min)
    h_degree = (30 * float(hour)) + ((m_degree / 360) * 30)

    if hour > 12 or hour < 1:
        return "Please input an hour value between 1 and 12."

    elif min > 60 or min < 1:
        return "Please input a minute value between 1 and 60."

    else:
        if h_degree > m_degree:
            return h_degree - m_degree

        else:
            return m_degree - h_degree


print(clock_angle(3, 60))


from utime import localtime, mktime
import ntptime


time_zone_offset = -28800  # 8 hours
time_set_increment = 3600  # seconds
time_last_set = 0
time_on = 0


def set_time():
    try:
        ntptime.settime()
        global time_last_set, time_on
        time_last_set = mktime(localtime())
        if time_on == 0:
            time_on = mktime(localtime())
    except OSError:
        pass


def time_is_expired():
    if time_last_set == 0:
        return True
    else:
        if (mktime(localtime()) - time_last_set) > time_set_increment:
            return True
        else:
            return False


def check_set_time():
    if time_is_expired():
        return set_time()


def local_time():
    return localtime(time_zone_epoch())


def time_zone_epoch():
    return mktime(localtime()) + time_zone_offset


def current_hour():
    return local_time()[3]


def time_alive():
    return mktime(localtime()) - time_on












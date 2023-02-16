from micropython import const
from machine import Timer


# define constants
TIMER_PERIOD_ONE = const(500)
TIMER_PERIOD_TWO = const(1000)

# create virtual timer
timer_a = Timer(-1)
timer_b = Timer(-2)
timer_c = Timer(-3)

# initialize timer
timer_a.init(period=TIMER_PERIOD_ONE, mode=Timer.PERIODIC, callback=lambda t: print('[INFO] Periodic timer A'))
timer_b.init(period=TIMER_PERIOD_ONE, mode=Timer.ONE_SHOT, callback=lambda t: print('[INFO] One shot timer B'))
timer_c.init(period=TIMER_PERIOD_TWO, mode=Timer.PERIODIC, callback=lambda t: print('[INFO] Periodic timer C'))

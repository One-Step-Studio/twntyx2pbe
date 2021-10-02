import time
from typing import Final
from rx import operators as op, interval

# current_session_time updates at the end of the run
from rx.subject import BehaviorSubject


class Clockwork:
    MAX_SESSION_TIME: Final = 900
    DEFAULT_INTERVAL: Final = 1.0

    def __init__(self):
        self.current_session_time: BehaviorSubject = BehaviorSubject(0.0)
        self.ticker = interval(self.DEFAULT_INTERVAL)
        self.start_time = time.time()
        self._reset = False
        self.end_at = time.time() + self.MAX_SESSION_TIME
        self.close_clock()

    def reset_clock(self):
        self._reset = True

    def close_clock(self):

        mini_session_time = self.ticker.pipe(op.take_while(lambda _: time.time() <= self.end_at))

        def mst_fnc(i):
            if self._reset:
                self.end_at = self.end_at + self.MAX_SESSION_TIME
                self._reset = False

        def mst_finish():
            self.current_session_time.on_next(self.end_at - self.start_time)

        mini_session_time.subscribe(
            on_next=mst_fnc,
            on_completed=mst_finish
            )


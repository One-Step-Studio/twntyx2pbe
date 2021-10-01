from rx.subject import BehaviorSubject

from clock import Clockwork


class GlobalScale:
    def __init__(self):
        self.clock: Clockwork = Clockwork()
        self.active = True
        self.sub_clock: BehaviorSubject

        def clock_stop(a):
            if a > 0.0:
                self.sub_clock.dispose()
                self.clock = None
                self.active = False
                print("Game stopped " + str(a))

        self.sub_clock = self.clock.current_session_time.subscribe(
            on_next=clock_stop
        )

        print("Game started")


gs = GlobalScale()
input()

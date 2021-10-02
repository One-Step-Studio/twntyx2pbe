from rx.subject import BehaviorSubject
from twntyx2p.maingame.game_logic.clock import Clockwork


class GlobalScale:
    def __init__(self, player_id : int):
        self.player_id : int = player_id
        self.clock: Clockwork = Clockwork()
        self.active = (True,0.0)
        self.sub_clock: BehaviorSubject

        def clock_stop(a):
            if a > 0.0:
                self.sub_clock.dispose()
                self.clock = None
                self.active = (False,a)
                print("Game stopped " + str(a))

        self.sub_clock = self.clock.current_session_time.subscribe(
            on_next=clock_stop
        )

        print("Game started")

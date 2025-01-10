class CalendarManager:
    def __init__(self):
        self.events = []

    def add_event(self, event):
        if not self.check_conflict(event):
            self.events.append(event)
            return True
        return False

    def remove_event(self, event):
        if event in self.events:
            self.events.remove(event)
            return True
        return False

    def list_events(self):
        return self.events

    def check_conflict(self, new_event):
        for event in self.events:
            if self._events_conflict(event, new_event):
                return True
        return False

    def _events_conflict(self, event1, event2):
        # Assuming event is a tuple (start_time, end_time)
        return not (event1[1] <= event2[0] or event2[1] <= event1[0])
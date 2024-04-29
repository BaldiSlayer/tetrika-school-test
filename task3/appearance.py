def appearance(intervals: dict[str, list[int]]) -> int:
    def construct_event(ind: int, time: int, user_type: str) -> tuple[int, int, str]:
        """
        Creates a tuple representing an event with time, event type, and user type.

        Parameters:
        ind (int): The index of the event.
        time (int): The time of the event.
        user_type (str): The type of user associated with the event.

        Return value:
        Tuple[int, int, str]: A tuple containing the event time, event type (1 or -1), and user type.

        Examples:
        >>> construct_event(0, 30, 'pupil')
        (30, 1, 'pupil')
        >>> construct_event(1, 45, 'tutor')
        (45, -1, 'tutor')
        """
        return min(max(time, lesson_start), lesson_end), 1 - 2 * (ind % 2), user_type

    lesson_start, lesson_end = intervals['lesson']
    pupil = [construct_event(ind, time, 'pupil') for ind, time in enumerate(intervals['pupil'])]
    tutor = [construct_event(ind, time, 'tutor') for ind, time in enumerate(intervals['tutor'])]

    events = sorted(pupil + tutor)
    pupil_count, tutor_count = 0, 0
    current_period_start = -1
    total_time = 0

    for timestamp, event_type, user_type in events:
        if user_type == 'pupil':
            pupil_count += event_type
        else:
            tutor_count += event_type

        # The current gap has started
        if pupil_count > 0 and tutor_count > 0 and current_period_start == -1:
            current_period_start = timestamp

        # the current period is over
        if (pupil_count < 1 or tutor_count < 1) and current_period_start != -1:
            total_time += timestamp - current_period_start
            current_period_start = -1

    return total_time

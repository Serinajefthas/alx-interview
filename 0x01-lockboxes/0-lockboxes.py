#!/usr/bin/python3
"""lockboxes challenge"""


def canUnlockAll(boxes):
    """lockboxes challenges, see if can unlock all boxes"""
    if not boxes:
        return False

    unlocked = set()
    unlocked.add(0)

    key_queue = [0]

    while key_queue:
        key = key_queue.pop(0)

        if key in unlocked:
            continue
        unlocked.add(key)
        key_queue.extend(boxes[key])
    return len(unlocked) == len(boxes)

#!/usr/bin/python3
"""lockboxes challenge"""


def canUnlockAll(boxes):
    """lockboxes challenges, see if can unlock all boxes"""
    if not boxes:
        return False

    unlocked = {0}

    key_queue = [0]

    while key_queue:
        """ breadth first search"""
        box = key_queue.pop(0)
        keys = boxes[box]
        for k in keys:
            if k < len(boxes) and k not in unlocked:
                unlocked.add(k)
                key_queue.append(k)
    return len(unlocked) == len(boxes)

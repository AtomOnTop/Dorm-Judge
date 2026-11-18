from bisect import bisect_right, insort
from datetime import date

# Number of characters at the start of every ticket ID that make up the prefix.
# "TICKET-2026-1118" is exactly 16 characters.
PREFIX_LENGTH = 16

# Highest possible character. Adding it to a prefix gives a string that sorts
# AFTER every string that starts with that prefix (used for the binary search).
MAX_CHAR = "\U0010FFFF"


def build_prefix():
    """
    Build today's 16-character prefix.
    Example for 18 Nov 2026: "TICKET-2026-1118"
    """
    # strftime("%Y-%m%d") -> "2026-1118"  (year, dash, month, day)
    return "TICKET-" + date.today().strftime("%Y-%m%d")


def next_ticket_id(ticket_list, prefix):
    """
    ticket_list: SORTED list of existing ticket IDs
    prefix: the first 16 characters of the new ticket
    returns: a new unique ticket ID like "TICKET-2026-1118-003"

    It continues from the highest number already used for this prefix,
    so IDs are never repeated, even if an older ticket was deleted.
    """
    # Binary search: position just after the last item that could start
    # with this prefix. Fast even for huge lists (about log(n) steps).
    end = bisect_right(ticket_list, prefix + MAX_CHAR)

    # In a sorted list, the item right before `end` is the last ticket of
    # this prefix, if there is one.
    if end > 0 and ticket_list[end - 1].startswith(prefix):
        # "TICKET-2026-1118-002".split("-")[-1] -> "002" -> int -> 2
        last_number = int(ticket_list[end - 1].split("-")[-1])
    else:
        # No ticket with this prefix yet, so we start from 0
        last_number = 0

    # Add 1 and pad with zeros to 3 digits: 1 -> "001", 12 -> "012"
    # (use :04d instead if you may exceed 999 tickets per prefix)
    return f"{prefix}-{last_number + 1:03d}"


def create_ticket(ticket_data, ticket_list):
    """
    Create a new ticket with the provided data.
    Adds the new ID to ticket_list (keeping it sorted)
    and returns the ticket ID as a string.
    """
    # Check every attribute and report the first missing one.
    # Note: this also treats 0, False and "" as missing.
    for attribute in ticket_data:
        if not ticket_data[attribute]:
            raise ValueError(f"Missing required attribute: {attribute}")

    # Build today's prefix and get the next free number for it
    prefix = build_prefix()
    ticket_id = next_ticket_id(ticket_list, prefix)

    # insort inserts the ID in the correct position, so the list stays
    # sorted and the next binary search still works.
    # (append() would break the sorting.)
    insort(ticket_list, ticket_id)

    # create ticket logic here (save ticket_data to a database, etc.)

    return ticket_id



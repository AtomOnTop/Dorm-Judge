**LOGIN INTERFACE**

-> Student login interface will have three options:  (a) `RAISE COMPLAINT`
										(b) `LOOK AT COMPLAINTS`
										(c) `MY COMPLAINTS`


**`RAISE COMPLAINT`:**
The student will be given the option to register a complaint by basically writing an essay into a *text box* and then post the complaint.

The [[special algorithm]] will then parse through the complaint and attach to it the appropriate tags such as `ROOM ISSUE` or `HOSTEL ISSUE` or `PRIORITY:URGENT` or `Water Issue`, `Electricity Issue`.

Issues such as `ROOM ISSUE` or `HOSTEL ISSUE` will be tagged on basis of words such as *`Room Number ___`* or *`Entire Hostel`* etc..

Issues involving priority will be made based on looking at the subject of the issue. So,
1. Issues involving *`water`* or *`electricity`*  or *`Health Hazard/Safety`* will be labelled High Priority
2. Issues labelled as *`insects`* or *`curtain`* will be labelled Medium Priority etc...

Of-course, the student can change these tags or add additional ones, **selecting from a fixed set of pre-built tags**.

**The issue will go on a form and will be given a *UID* which tracks the issue.**

Each issue is tracked entirely by its *UID*, such future comments on the issue and the closure of issue.

**`LOOK AT COMPLAINTS:`**
This will list an issue of all complaints with their UIDs , titles, closed/not closed status, priority and other tags.

Like:

`UID|      TITLE     |STATUS|TAGS`

and any student will be able to open an issue to navigate to all the comments, the status(closed/open) and also the tags.

Students can `subscribe` to an issue. If a student comments on an issue, they automatically get `subscribed`.

**`MY COMPLAINTS:`**
This will just show all the list of complaints the student themselves have written or have `subscribed` to, exactly the same as the **`LOOK AT COMPLAINTS`** section.

This section will get a notification-bell type icon if issues which the student `subscribed` to has any new comments or if the status changes(i.e closed->open or open->closed).

**`SOLUTIONS:`**
A special comment can be tagged with a `solution` tag which will give it a special property of being up-voted or down-voted.

**`CLOSING AN ISSUE:`** *(OPTIONAL FEATURE)*
A student can close an issue if they have authored the issue.


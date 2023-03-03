# Script to merge the boilerplate  with the filter lists at (local-filters.txt) and write it to my-filters.txt

import time

boilerplate = f"""[Adblock Plus 2.0]
! Title: Vishal's personal uBO filter list
! Last modified: {time.ctime()} + {time.tzname[time.daylight]}
! Expires: 7 days (update frequency)
!
! Please report only issues or problems specifically with this filter list via GitHub issues or via e-mail (ubo-filters@vishalnandagopal.com). If you see ads not being blocked, report it on EasyList forums - https://forums.lanik.us/ .
!
! Homepage: https://github.com/vishalnandagopal/ubo-filters
! Licence: https://github.com/vishalnandagopal/ubo-filters/blob/main/LICENSE
! GitHub issues: https://github.com/vishalnandagopal/ubo-filters/issues
! GitHub pull requests: https://github.com/vishalnandagopal/ubo-filters/pulls


! ----------------------------- FILTER LIST BEGINS -----------------------------


"""

lastline = "\n\n\n! ----------------------------- FILTER LIST ENDS -----------------------------"

with open("local-filters.txt", "r") as f:
    content = f.read()

# with open("my-filters.txt", "r") as g:
#     temp = g.read()

with open("my-filters.txt", "w+") as f:
    # with open("temp-local-backup.txt", "w+") as g:
    #     g.write(temp)
    f.write(boilerplate + content + lastline)
    print("Merged")
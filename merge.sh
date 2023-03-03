#!/bin/bash

boilerplate=$"[Adblock Plus 2.0]
! Title: Vishal's personal uBO filter list
! Last modified: `date`
! Expires: 7 days (update frequency)
!
! Please report only issues or problems specifically with this filter list via GitHub issues or via e-mail (ubo-filters@vishalnandagopal.com). If you see ads not being blocked, report it on EasyList forums - https://forums.lanik.us/ .
!
! Homepage: https://github.com/vishalnandagopal/ubo-filters
! Licence: https://github.com/vishalnandagopal/ubo-filters/blob/main/LICENSE\
! GitHub issues: https://github.com/vishalnandagopal/ubo-filters/issues
! GitHub pull requests: https://github.com/vishalnandagopal/ubo-filters/pulls
! ----------------------------- FILTER LIST BEGINS -----------------------------
"

lastline=$"

----------------------------- FILTER LIST ENDS -----------------------------"

if ls | grep -Fq "local-filters.txt"; then
    echo "$boilerplate" > my-filters.txt
    cat local-filters.txt >> my-filters.txt
    echo "$lastline" >> my-filters.txt
    echo "Merged"
else
    echo 'local-filters.txt not found'
fi
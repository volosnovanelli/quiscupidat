for person in response:
    if person["Degree"] is None:
        nodegreecounter = nodegreecounter + 1
    elif person["Degree"] == "Master":
        mastercounter = mastercounter + 1
    elif person["Degree"] == "PhD":
        phdcounter = phdcounter + 1

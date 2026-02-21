durations =  [180,  200,  220,   210]

if any( d <=0 for d in   durations):
    print("invalid playlist")
    print("stopping analysis"  )
else:
    total =sum(  durations)
    songs=len(durations )

    Has_repeat= False
    for x in  durations :
        if durations.count(x) >1:
            Has_repeat =  True
            break

    if total<   300:
        category ="too Short playlist"
        Recommendation =    "add more songs to improve the session."
    elif total >  3600:
        category=     "too long playlist"
        Recommendation ="try reducing the playlist length a bit."
    elif Has_repeat:
        category =   "repetitive playlist"
        Recommendation=    "add variety"
    else :
        Spread=max(   durations ) - min(durations)
        if Spread >  0:
            category=   "balanced playlist"
            Recommendation ="good listening session"
        else:
            category =  "irregular playlist"
            Recommendation =    "reorganize the playlist for a better flow."

    print(  f"total Duration: {total} seconds" )
    print(    f"songs: {songs}")
    print(f"category: {category}"  )
    print(   f"recommendation: {Recommendation}")
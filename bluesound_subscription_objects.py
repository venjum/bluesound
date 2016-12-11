"""
Common subscription objects.
None of these have callback set
"""

from bluesound_subscribe import SubscriptionObject

"""
Title 1 can be a slogan of a radio channel in TuneIn
or a song title in Spotify
"""
title1 = SubscriptionObject(['status', 'title1'])

"""
Title 2 can be artist and song title in TuneIn
or artist in Spotify
"""
title2 = SubscriptionObject(['status', 'title2'])

"""
Title 3 can be radio channel or album title in Spotify
"""
title3 = SubscriptionObject(['status', 'title3'])

"""
Cover image for showing radio station logo or album art
"""
coverImage = SubscriptionObject(['status', 'image'])

"""
Showing current service in use
"""
service = SubscriptionObject(['status', 'service'])

"""
Showing current volume
"""
volume = SubscriptionObject(['status', 'volume'])

"""
Show number of seconds into the track in Spotify.
or number of seconds of listening in TuneIn
"""
secondsInTrack = SubscriptionObject(['status', 'secs'])

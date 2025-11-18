select 
    artist, count(*) as occurrences
from Spotify 
group by 1
order by occurrences desc, artist
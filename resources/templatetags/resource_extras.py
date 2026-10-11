from django import template
from urllib.parse import urlparse, parse_qs
register = template.Library()
@register.filter
def youtube_video(url):
    parsed =urlparse(url)
    if 'youtube.com' not in parsed.netloc:
        return url

    params=parse_qs(parsed.query)
    if params.get('v'):
        return f'https://www.youtube.com/embed/{params["v"][0]}'

    if params.get('list'):
        return f'https://www.youtube.com/embed/videoseries?list={params["list"][0]}'

    return url

@register.simple_tag
def path_total_time(learning_path):
    total_time = sum(r.estimated_minutes for r in learning_path.resources.all())
    hours, minutes = divmod(total_time, 60)
    if hours and minutes:
        return f'Total {hours} hours and  {minutes} mins'
    elif hours:
        return f'Total {hours} hours'
    else:
        return f'Total {minutes} mins'

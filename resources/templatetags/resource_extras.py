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


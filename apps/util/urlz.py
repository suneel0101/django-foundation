import urlparse
from django.utils.http import urlencode


def get_querydict(url):
    parts = urlparse.urlsplit(url)
    return dict(urlparse.parse_qsl(parts[3]))


def add_params(original_url, params):
    """
    Adds new params to a url via the params dict
    and updates existing keys in the url with new values
    """
    querydict = get_querydict(original_url)
    querydict.update(params)
    qs = urlencode(querydict)
    components = urlparse.urlsplit(original_url)
    new_url = urlparse.urlunsplit((components[0], components[1], components[2], qs, components[4]))
    return new_url

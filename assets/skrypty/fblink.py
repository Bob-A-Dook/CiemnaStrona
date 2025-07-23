import re
from urllib.parse import urlparse, unquote

def clean_facebook_link( url ):
    '''Removes known tracking/junk parameters from Facebook links'''

    if 'l.php' in url:
        #It's Facebook's redirect, we have to extract the real link
        parsed_url = urlparse( url )
        nested_url = [p for p in parsed_url.query.split('&')
                      if p.startswith('u=')][0]
        nested_url = nested_url[2:] # Trim "u="
        url = unquote( nested_url ) # Replace %xx escape sequences
    
    u = urlparse( url )
    is_tracking_param = re.compile('^(__cft__|__tn__|fbclid)').match
    good_params = '&'.join(p for p in u.query.split('&')
                           if not is_tracking_param( p ))
    
    if good_params: good_params = '?'+good_params
    else: good_params = ''

    scheme = 'https' if not u.scheme else u.scheme
    netloc = 'www.facebook.com' if not u.netloc else u.netloc
    url = f'{scheme}://{netloc}{u.path}{good_params}'
    return url


def run():
    text = input('FACEBOOK LINK: ')
    if not ('https://' in text and 'facebook.com' in text):
        print('Not a Facebook link')
    else:
        cleaned = clean_facebook_link( text )
        print(cleaned)
        _ = input()

if __name__ == '__main__': run()

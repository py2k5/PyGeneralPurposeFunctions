#!/usr/bin/env python


"""A plugin that provides a Python interface to the Twitter API"""

import json
import sys
import requests
from requests_oauthlib import OAuth1, OAuth2
import io
import warnings
import os

try:
    # python 3
    from urllib.parse import urlparse, urlunparse, urlencode
    from urllib.request import urlopen
    from urllib.request import __version__ as urllib_version
except ImportError:
    from urlparse import urlparse, urlunparse
    from urllib2 import urlopen
    from urllib import urlencode
    from urllib import __version__ as urllib_version

class Api(object):

    def __init__(self,
                 consumer_key=None,
                 consumer_secret=None,
                 access_token_key=None,
                 access_token_secret=None,
                 input_encoding=None,
                 request_headers=None,
                 base_url=None,
                 tweet_mode='compat',
                 timeout=None):

        self.__auth = None
        self._timeout = timeout

        self._InitializeRequestHeaders(request_headers)
        self._InitializeUserAgent()
        self._InitializeDefaultParameters()

        self.tweet_mode = tweet_mode

        if base_url is None:
            self.base_url = 'https://api.twitter.com/1.1'
        else:
            self.base_url = base_url

        self.SetCredentials(consumer_key, consumer_secret, access_token_key, access_token_secret)

    def _InitializeRequestHeaders(self, request_headers):
        if request_headers:
            self._request_headers = request_headers
        else:
            self._request_headers = {}

    def _InitializeUserAgent(self):
        user_agent = 'Python-urllib/%s (python-api/%s)' % \
                     (urllib_version, 1.1)
        self.SetUserAgent(user_agent)

    def _InitializeDefaultParameters(self):
        self._default_params = {}

    def SetUserAgent(self, user_agent):
        """Override the default user agent.
        Args:
          user_agent:
            A string that should be send to the server as the user-agent.
        """
        self._request_headers['User-Agent'] = user_agent


    def SetCredentials(self,
                       consumer_key,
                       consumer_secret,
                       access_token_key=None,
                       access_token_secret=None,
                       application_only_auth=False):

        self._consumer_key = consumer_key
        self._consumer_secret = consumer_secret
        self._access_token_key = access_token_key
        self._access_token_secret = access_token_secret

        auth_list = [consumer_key, consumer_secret,
                    access_token_key, access_token_secret]
        if all(auth_list):
            self.__auth = OAuth1(consumer_key, consumer_secret,
                                access_token_key, access_token_secret)

        self._config = None

    def _RequestUrl(self, url, verb, data=None, json=None, enforce_auth=True):

        if enforce_auth:
            if not self.__auth:
                print("The twitter.Api instance must be authenticated.")


        if not data:
            data = {}

        if verb == 'GET':
            data['tweet_mode'] = self.tweet_mode
            url = self._BuildUrl(url, extra_params=data)
            #print(url)
            resp = requests.get(url, auth=self.__auth, timeout=self._timeout)
            self.response = resp

        else:
            resp = 0  # if not a GET request

        if url:
            limit = resp.headers.get('x-rate-limit-limit', 0)
            remaining = resp.headers.get('x-rate-limit-remaining', 0)
            reset = resp.headers.get('x-rate-limit-reset', 0)

        return resp

    def _BuildUrl(self, url, path_elements=None, extra_params=None):
        # Break url into constituent parts
        (scheme, netloc, path, params, query, fragment) = urlparse(url)

        # Add any additional path elements to the path
        if path_elements:
            # Filter out the path elements that have a value of None
            p = [i for i in path_elements if i]
            if not path.endswith('/'):
                path += '/'
            path += '/'.join(p)

        # Add any additional query parameters to the query string
        if extra_params and len(extra_params) > 0:
            #print(extra_params)
            #extra_query = self._EncodeParameters(extra_params)
            extra_query = urlencode(dict((k, v) for k, v in extra_params.items() if v is not None))

            # Add it to the existing query
            if query:
                query += '&' + extra_query
            else:
                query = extra_query

        # Return the rebuilt URL
        return urlunparse((scheme, netloc, path, params, query, fragment))

    def _EncodeParameters(parameters=None):

        if parameters is None:
            return None
        if not isinstance(parameters, dict):
            raise "`parameters` must be a dict."
        else:
            return urlencode(dict((k, v) for k, v in parameters.items() if v is not None))

    def _ParseAndCheckTwitter(self, json_data):

        try:
            data = json.loads(json_data)
        except ValueError:
            print("Some error occured")
        return data

    def get_rest_quota(self):
        """Quota information in the REST-only response header.
        :returns: Dictionary of 'remaining' (count), 'limit' (count), 'reset' (time)
        """
        remaining, limit, reset = None, None, None
        if self.response:
            if 'x-rate-limit-remaining' in self.response.headers:
                remaining = int(
                    self.response.headers['x-rate-limit-remaining'])
                if remaining == 0:
                    limit = int(self.response.headers['x-rate-limit-limit'])
                    reset = int(self.response.headers['x-rate-limit-reset'])
                    reset = datetime.fromtimestamp(reset)
        return {'remaining': remaining, 'limit': limit, 'reset': reset}

    def search_tweets(self,params=None):
        url = '{}/search/tweets.json'.format(self.base_url)
        resp = self._RequestUrl(url, 'GET', data=params)
        data = self._ParseAndCheckTwitter(resp.content.decode('utf-8'))
        return data

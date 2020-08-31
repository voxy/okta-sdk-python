from __future__ import unicode_literals

from okta.framework.ApiClient import ApiClient
from okta.framework.Utils import Utils
from okta.models.auth.TrustedOrigin import TrustedOriginResponse


class TrustedDomainsClient(ApiClient):
    def __init__(self, *args, **kwargs):
        kwargs['pathname'] = '/api/v1'
        ApiClient.__init__(self, *args, **kwargs)

    def create_trusted_origin(self, trusted_origin_name, trusted_origin_url, trusted_scope='CORS'):

        """Create trusted domain
        :param trusted_origin_name: target origin name
        :type trusted_origin_name: str
        :param trusted_origin_url: target trusted origin url
        :type trusted_origin_url: str
        :param trusted_scope: CORS or REDIRECT
        :type trusted_scope: str
        :rtype: TrustedOriginResponse
        """

        request = {
            'name': trusted_origin_name,
            'origin': trusted_origin_url,
            'scopes': [
                {
                    'type': trusted_scope
                },
            ]
        }

        response = ApiClient.post_path(self, '/trustedOrigins', request)
        return Utils.deserialize(response.text, TrustedOriginResponse)

"""
Copyright start
MIT License
Copyright (c) 2025 Fortinet Inc
Copyright end
"""

import requests
from connectors.core.connector import get_logger, ConnectorError

logger = get_logger('ctm360-hackerview')

error_msg = {
    400: "Bad Request -- Your request is invalid.",
    401: "Unauthorized -- Wrong Credentials provided.",
    403: "Access Denied -- The data requested is hidden for administrators only.",
    404: "Not Found -- The specified data could not be found.",
    405: "Method Not Allowed -- You tried to access a API Endpoint with an invalid method.",
    406: "Not Acceptable -- You requested a format that isn't json.",
    410: "Gone -- The data requested has been removed from our servers.",
    429: "Too Many Requests -- You're requesting too frequently! Slow down!",
    500: "Internal Server Error -- We had a problem with our server. Try again later.",
    503: "Service Unavailable -- We're temporarily offline for maintenance. Please try again later.",
    'time_out': 'The request timed out while trying to connect to the remote server',
    'ssl_error': 'SSL certificate validation failed'
}


class CTM360:
    def __init__(self, config):
        self.base_url = config.get('server').strip('/')
        if not self.base_url.startswith('https://'):
            self.base_url = 'https://{0}'.format(self.base_url)
        self.api_key = config['api_key']
        self.verify_ssl = config['verify_ssl']

    def make_rest_call(self, endpoint, query_params={}, req_params={}, method='GET'):
        service_endpoint = '{0}/api/v2/{1}'.format(self.base_url, endpoint)
        logger.info('Request URL {}'.format(service_endpoint))

        try:
            headers = {'api-key': self.api_key}
            response = requests.request(
                method=method,
                url=service_endpoint,
                headers=headers,
                verify=self.verify_ssl,
                params=query_params,
                data=req_params
            )

            if response.ok:
                if response.status_code == 204:
                    return {"status": "success", "message": "No content returned"}
                return response.json()
            if error_msg[response.status_code]:
                raise ConnectorError('{}'.format(
                    error_msg[response.status_code]))
            response.raise_for_status()
        except requests.exceptions.SSLError as e:
            logger.exception('{}'.format(e))
            raise ConnectorError('{}'.format(error_msg['ssl_error']))
        except requests.exceptions.ConnectionError as e:
            logger.exception('{}'.format(e))
            raise ConnectorError('{}'.format(error_msg['time_out']))
        except Exception as e:
            logger.exception('{}'.format(e))
            raise ConnectorError('{}'.format(e))


def _check_health(config):
    ctm = CTM360(config)
    resp = ctm.make_rest_call(endpoint='issues')
    if resp:
        logger.info('connector available')
        return True
    return False


def get_boolean_string(value):
    return 'true' if value else 'false'


def filter_params(params):
    filtered_params = {k: v for k,
    v in params.items() if v is not None and v != ''}
    return filtered_params


def get_issues(config, params):
    ctm = CTM360(config)
    endpoint = 'issues'
    method = 'GET'
    request_params = {}
    query_params = {
        'first_seen': params.get('first_seen')
    }
    query_params = filter_params(query_params)
    response = ctm.make_rest_call(
        endpoint=endpoint, method=method, query_params=query_params, req_params=request_params)
    return response


def get_domains(config, params):
    ctm = CTM360(config)
    endpoint = 'assets/domain'
    method = 'GET'
    request_params = {}
    query_params = {}
    response = ctm.make_rest_call(
        endpoint=endpoint, method=method, query_params=query_params, req_params=request_params)
    return response


def get_hosts(config, params):
    ctm = CTM360(config)
    endpoint = 'assets/host'
    method = 'GET'
    request_params = {}
    query_params = {}
    response = ctm.make_rest_call(
        endpoint=endpoint, method=method, query_params=query_params, req_params=request_params)
    return response


def get_ip_addresses(config, params):
    ctm = CTM360(config)
    endpoint = 'assets/ip_address'
    method = 'GET'
    request_params = {}
    request_params = filter_params(request_params)
    query_params = {}
    query_params = filter_params(query_params)
    response = ctm.make_rest_call(
        endpoint=endpoint, method=method, query_params=query_params, req_params=request_params)
    return response


def get_resolved_issues(config, params):
    ctm = CTM360(config)
    endpoint = 'resolved_issues'
    method = 'GET'
    request_params = {}
    query_params = {
        'from_date': params.get('from_date'),
        'to_date': params.get('to_date')
    }
    query_params = filter_params(query_params)
    response = ctm.make_rest_call(
        endpoint=endpoint, method=method, query_params=query_params, req_params=request_params)
    return response


operations = {
    'get_issues': get_issues,
    'get_domains': get_domains,
    'get_hosts': get_hosts,
    'get_ip_addresses': get_ip_addresses,
    'get_resolved_issues': get_resolved_issues
}

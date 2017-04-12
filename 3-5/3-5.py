#!/usr/local/bin/python
# -*- coding: utf-8 -*


import requests


class MetrikaAPI(object):
    def __init__(self, counter_id, token, host='https://api-metrika.yandex.ru'):
        self.counter_id = counter_id
        self.token = token
        self.host = host

    def _get_url(self, url='/stat/v1/data', params=None, data=None, method='GET'):
        req = requests.request(
            method=method,
            url=self.host + url,
            params=params,
            data=data,
            headers={'Authorization': 'OAuth ' + self.token},
        )
        try:
            req.raise_for_status()
        except requests.exceptions.HTTPError:
            print(req.content)
            raise
        except Exception:
            print("Unexpected exception")
            raise

        return req

    def get_sources_visits(self):
        req = self._get_url(params=dict(
            metrics='ym:s:visits',
            id=self.counter_id,
        ))
        return req.json()

    def get_sources_users(self):
        req = self._get_url(params=dict(
            metrics='ym:s:users',
            id=self.counter_id,
        ))
        return req.json()

    def get_sources_pageviews(self):
        req = self._get_url(params=dict(
            metrics='ym:s:pageviews',
            id=self.counter_id,
        ))
        return req.json()


def main():
    d = MetrikaAPI(44138734, 'тут мог бы быть токен')
    vis = d.get_sources_visits()
    us = d.get_sources_users()
    view = d.get_sources_pageviews()
    print('Всего визитов: {}'.format(vis['data'][0]['metrics']))
    print('Всего посетителей: {}'.format(us['data'][0]['metrics']))
    print('Всего просмотров: {}'.format(view['data'][0]['metrics']))

if __name__ == '__main__':
    main()

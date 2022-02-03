from ast import Index
from inspect import Attribute
from typing import Union
import requests
import time

def __get_api_data(url: str) -> list[dict[str, str]]:
    response = requests.get(url)

    return response.json()['data']


def __post_api_data(url: str, data: dict[str, Union[str, list[str], dict[str, int]]]):
    response = requests.post(url, json = data)

    # Raise exception if post failed
    response.raise_for_status()


def get_distinct_email_addresses(api_data: list[dict[str, str]]) -> list[str]:
    lookup_dict = {}

    for data_object in api_data:
        try:
            domain = data_object['email'].split('@')[1]

            if domain.count('.') == 0:
                # Domain does not have TLD, ignore it.
                continue

        except (IndexError, AttributeError):
            # No valid domain on provided email, continue processing other entries.
            continue

        if data_object['email'] and lookup_dict.get(data_object['email']) is None:
            lookup_dict[data_object['email']] = True # Value is unused, just need the key part.

    return [x for x in lookup_dict.keys()]


def get_email_domain_counts(api_data: list[dict[str, str]]) -> dict[str, int]:
    lookup_dict = {}
    return_dict = {}

    unique_emails = get_distinct_email_addresses(api_data)

    for email in unique_emails:
        domain = email.split('@')[1]

        if lookup_dict.get(domain) is None:
            lookup_dict[domain] = 1

        else:
            lookup_dict[domain] += 1

    for domain, count in lookup_dict.items():
        if count > 1:
            return_dict[domain] = count

    return return_dict


def get_april_logins(api_data: list[dict[str, str,]]) -> list[str]:
    april_logins = {}

    for data_object in api_data:
        try:
            parsed_time = time.strptime(data_object['login_date'], '%Y-%m-%dT%H:%M:%S%z')

        except (TypeError, ValueError):
            # Time was not valid, continue processing other entries.
            continue

        if parsed_time.tm_mon == 4:
            april_logins[data_object['email']] = True # Value is unused, just need the key part.

    return [x for x in april_logins.keys()]


def __main() -> None:
    response_data = {}

    # TODO: Make url configurable
    api_data = __get_api_data('https://us-central1-marcy-playground.cloudfunctions.net/ordoroCodingTest')

    response_data['your_email_address'] = 'joshuajackson1@protonmail.com'
    response_data['unique_emails'] = get_distinct_email_addresses(api_data)
    response_data['user_domain_counts'] = get_email_domain_counts(api_data)
    response_data['april_emails'] = get_april_logins(api_data)

    # TODO: Make url configurable
    __post_api_data('https://us-central1-marcy-playground.cloudfunctions.net/ordoroCodingTest', response_data)


if __name__ == '__main__':
    __main()

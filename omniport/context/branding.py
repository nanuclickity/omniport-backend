import os

from django.conf import settings
from django.contrib.staticfiles import finders


def singleton_image(name, extension):
    """
    Check if a logo with the given name exists
    :param name: the name of the logo to check for existence
    :param extension: the extension of the logo to check for existence
    :return: the relative path to the logo if found, None otherwise
    """

    logo_relative_path = os.path.join(
        'omniport',
        'branding',
        f'{name}{extension}',
    )
    if finders.find(logo_relative_path) is not None:
        return logo_relative_path
    else:
        return None


def indexed_image(name, extension, preferred_index):
    """
    Check if a logo with the given name, and preferably index, exists
    :param name: the name of the logo to check for existence
    :param extension: the extension of the logo to check for existence
    :param preferred_index: the preferred index of the logo
    :return: the relative path to the logo if found, None otherwise
    """

    logo_relative_path = os.path.join(
        'omniport',
        'branding',
        f'{name}_{preferred_index}{extension}',
    )
    if finders.find(logo_relative_path) is not None:
        return logo_relative_path
    else:
        return singleton_image(name, extension)


def branding_imagery(_=None):
    """
    Add the brand imagery of the institute, maintainer and site to the context
    :param _: the request being served
    :return: the data to add to the context
    """

    data = dict()
    data['INSTITUTE_LOGO'] = singleton_image(
        'institute_logo', '.png'
    )
    data['MAINTAINERS_LOGO'] = singleton_image(
        'maintainers_logo', '.png'
    )
    data['SITE_LOGO'] = indexed_image(
        'site_logo', '.png',
        settings.SITE_ID
    )
    data['SITE_FAVICON'] = indexed_image(
        'site_favicon', '.ico',
        settings.SITE_ID
    )
    return data


def branding_text(_=None):
    """
    Add the brand text of the institute, maintainer and project to the context
    :param _: the request being served
    :return: the data to add to the context
    """

    data = dict()
    data['INSTITUTE'] = settings.INSTITUTE
    data['INSTITUTE_HOME_PAGE'] = settings.INSTITUTE_HOME_PAGE
    data['MAINTAINERS'] = settings.MAINTAINERS
    data['MAINTAINERS_HOME_PAGE'] = settings.MAINTAINERS_HOME_PAGE
    return data
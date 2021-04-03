from django.core.exceptions import ValidationError
import os
from uuid import uuid4
from random import randint


def validate_max_image_size(image):
    '''
    Check image for maximum size
    :param image:
    :return:
    '''

    file_size = image.file.size
    limit_mb = 8
    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError("Max size of file is %s MB" % limit_mb)


def agent_logo(instance, file_name):
    '''
    Upload agent logo, uploading folder will be created, if not exist
    :param instance:
    :param file_name:
    :return:
    '''

    upload_to = 'agent/logo'
    ext = file_name.split('.')[-1]
    if instance.pk:
        file_name = '{}.{}.{}'.format(instance.id, uuid4().hex, ext)
    else:
        file_name = '{}.{}.{}'.format(instance.id, uuid4().hex, ext)
    return os.path.join(upload_to, file_name)


def customer_image(instance, file_name):
    '''
    Upload customer image, uploading folder will be created, if not exist
    :param instance:
    :param file_name:
    :return:
    '''

    upload_to = 'customer/image'
    ext = file_name.split('.')[-1]
    if instance.pk:
        file_name = '{}.{}.{}'.format(instance.id, uuid4().hex, ext)
    else:
        file_name = '{}.{}.{}'.format(instance.id, uuid4().hex, ext)
    return os.path.join(upload_to, file_name)


def upload_visa(instance, file_name):
    '''
    Upload customer visa, uploading folder will be created, if not exist
    :param instance:
    :param file_name:
    :return:
    '''

    upload_to = 'customer/visa'
    ext = file_name.split('.')[-1]
    if instance.pk:
        file_name = '{}.{}.{}'.format(instance.id, uuid4().hex, ext)
    else:
        file_name = '{}.{}.{}'.format(instance.id, uuid4().hex, ext)
    return os.path.join(upload_to, file_name)

def upload_passport(instance, file_name):
    '''
    Upload customer passport, uploading folder will be created, if not exist
    :param instance:
    :param file_name:
    :return:
    '''

    upload_to = 'customer/passport'
    ext = file_name.split('.')[-1]
    if instance.pk:
        file_name = '{}.{}.{}'.format(instance.id, uuid4().hex, ext)
    else:
        file_name = '{}.{}.{}'.format(instance.id, uuid4().hex, ext)
    return os.path.join(upload_to, file_name)
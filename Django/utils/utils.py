import os
from datetime import datetime
import random
from django.core.exceptions import ObjectDoesNotExist

def get_order_generate():
    return ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(3))


# def update_paginate():
#     return int(get_config_value("paginado", int(os.environ.get('PAGINATE'))))

# !/usr/bin/env python
# -*- coding: utf-8 -*-
# DateTime: 2019/3/16 9:37
from flask import Blueprint

bp=Blueprint('errors',__name__)

from app.errors import handlers

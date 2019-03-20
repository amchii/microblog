# !/usr/bin/env python
# -*- coding: utf-8 -*-
# DateTime: 2019/3/16 9:54
from flask import Blueprint

bp=Blueprint('auth',__name__)

from app.auth import routes
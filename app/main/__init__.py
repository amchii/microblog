# !/usr/bin/env python
# -*- coding: utf-8 -*-
# DateTime: 2019/3/16 10:20
from flask import Blueprint

bp=Blueprint('main',__name__)

from app.main import routes
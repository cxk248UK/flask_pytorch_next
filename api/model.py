import torch
from flask import (Blueprint, request)

bp = Blueprint('model', __name__, url_prefix='/model')

@bp.get('/create')
def create():
    return [10,20,30,50,60]


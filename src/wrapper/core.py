# -*- coding: utf-8 -*-
from . import wrapper

def get_hmm():
    """Get a thought."""
    return 'hmmm...'


def hmm():
    """Contemplation..."""
    if wrapper.get_answer():
        print(get_hmm())

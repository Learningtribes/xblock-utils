# -*- coding: utf-8 -*-

from xblock.fields import String


class File(String):
    def __init__(self, accept='*/*', *args, **kwargs):
        super(File, self).__init__(*args, **kwargs)
        self.accept = accept

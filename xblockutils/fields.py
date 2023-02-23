# -*- coding: utf-8 -*-

from xblock.fields import String


class File(String):
    def __init__(self, accept='*/*', extra_description="", optional_values=None, *args, **kwargs):
        super(File, self).__init__(*args, **kwargs)
        self.accept = accept
        self.extra_description = extra_description
        self.optional_values = optional_values or []

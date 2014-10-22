import os

import pyblish.api


@pyblish.api.log
class SelectCurrentFile(pyblish.api.Selector):
    """Inject the current working file into context

    .. note:: This is mandatory for the supplied extractors
    or else they will fail.

    """

    hosts = ['modo']
    version = (0, 1, 0)

    def process_context(self, context):
        """Todo, inject the current working file"""
        pass

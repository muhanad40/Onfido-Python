class OnfidoObjectBase(object):

    def __init__(self, *args, **kwargs):
        if len(args):
            data = args[0]
            self._add_to_object(data)

    def _add_to_object(self, data):
        for item in data.items():
            setattr(self, item[0], item[1])
class OnfidoObjectBase(object):

    def __init__(self, *args, **kwargs):
        if len(args):
            data = args[0]
            self._add_to_object(data)

    def __str__(self):
    	cls_name = type(self).__name__
    	return '<{0} id="{1}">'.format(cls_name, self.id)

    def _add_to_object(self, data):
        for item in data.items():
            setattr(self, item[0], item[1])
from lense.engine.api.handlers import RequestHandler

class Example_Get(RequestHandler):
    """
    Example request handler.
    """
    def launch(self):
        """
        Required worker method for request handler.
        """
        return self.ok()
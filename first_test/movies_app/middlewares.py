import time


class XRequestTimingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        initial_time = time.monotonic_ns()

        response = self.get_response(request)

        duration = time.monotonic_ns() - initial_time

        response.headers["X-Request-Timing"] = int(duration / 1000000)
        return response

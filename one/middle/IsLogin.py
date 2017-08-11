from django.utils.deprecation import MiddlewareMixin

class M1(MiddlewareMixin):
    def process_request(self, request):
        print('m1.request')
        pass

    def process_response(self, request, response):
        print('m1.response')
        return response
        pass

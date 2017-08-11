from django.utils.deprecation import MiddlewareMixin

class Row1(MiddlewareMixin):
    def process_request(self,request):
        print "6666666666666"

    def process_response(self,request,response):
        print "2222222222222222"
        return response

class Row2(MiddlewareMixin):
    def process_request(self,request):
        print "88888888888888888888"

    def process_response(self,request,response):
        print "33333333333333333"
        return response

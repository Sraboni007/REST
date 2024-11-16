from rest_framework.views import exception_handler

def mycustomexceptionhandler(exc, context):
    # Call the default exception handler
    response = exception_handler(exc, context)

    if response is not None:
        # Add a custom field to the response
        response.data['status_code'] = response.status_code

    return response

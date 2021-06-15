# swagger_client.IVRApi

All URIs are relative to *https://rest.paycomet.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_session**](IVRApi.md#check_session) | **POST** /v1/ivr/session-state | Checks an IVR session
[**get_session**](IVRApi.md#get_session) | **POST** /v1/ivr/get-session | Creates an IVR session
[**session_cancel**](IVRApi.md#session_cancel) | **POST** /v1/ivr/session-cancel | Cancel an IVR session

# **check_session**
> InlineResponse20030 check_session(paycomet_api_token, body=body)

Checks an IVR session

check_session

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IVRApi()
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Authorization privilege required)
body = swagger_client.IvrSessionstateBody() # IvrSessionstateBody |  (optional)

try:
    # Checks an IVR session
    api_response = api_instance.check_session(paycomet_api_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IVRApi->check_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paycomet_api_token** | **str**| PAYCOMET API key (Authorization privilege required) | 
 **body** | [**IvrSessionstateBody**](IvrSessionstateBody.md)|  | [optional] 

### Return type

[**InlineResponse20030**](InlineResponse20030.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_session**
> InlineResponse20029 get_session(paycomet_api_token, body=body)

Creates an IVR session

get_session

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IVRApi()
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Authorization privilege required)
body = swagger_client.IvrGetsessionBody() # IvrGetsessionBody |  (optional)

try:
    # Creates an IVR session
    api_response = api_instance.get_session(paycomet_api_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IVRApi->get_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paycomet_api_token** | **str**| PAYCOMET API key (Authorization privilege required) | 
 **body** | [**IvrGetsessionBody**](IvrGetsessionBody.md)|  | [optional] 

### Return type

[**InlineResponse20029**](InlineResponse20029.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **session_cancel**
> InlineResponse20031 session_cancel(paycomet_api_token, body=body)

Cancel an IVR session

session_cancell

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IVRApi()
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Authorization privilege required)
body = swagger_client.IvrSessioncancelBody() # IvrSessioncancelBody |  (optional)

try:
    # Cancel an IVR session
    api_response = api_instance.session_cancel(paycomet_api_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IVRApi->session_cancel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paycomet_api_token** | **str**| PAYCOMET API key (Authorization privilege required) | 
 **body** | [**IvrSessioncancelBody**](IvrSessioncancelBody.md)|  | [optional] 

### Return type

[**InlineResponse20031**](InlineResponse20031.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


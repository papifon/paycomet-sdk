# swagger_client.HeartbeatApi

All URIs are relative to *https://rest.paycomet.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**heartbeat**](HeartbeatApi.md#heartbeat) | **POST** /v1/heartbeat | Check the system

# **heartbeat**
> InlineResponse2007 heartbeat(body=body, paycomet_api_token=paycomet_api_token)

Check the system

Get heartbeat of API

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HeartbeatApi()
body = swagger_client.V1HeartbeatBody() # V1HeartbeatBody |  (optional)
paycomet_api_token = 'paycomet_api_token_example' # str | PAYCOMET API key (Query privilege required) (optional)

try:
    # Check the system
    api_response = api_instance.heartbeat(body=body, paycomet_api_token=paycomet_api_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HeartbeatApi->heartbeat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1HeartbeatBody**](V1HeartbeatBody.md)|  | [optional] 
 **paycomet_api_token** | **str**| PAYCOMET API key (Query privilege required) | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


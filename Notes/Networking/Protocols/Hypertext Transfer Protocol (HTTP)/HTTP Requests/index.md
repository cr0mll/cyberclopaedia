# Format
An HTTP request tells the server what the client wants it to do. The format of an HTTP request is as follows:

```
METHOD RESOURCE_PATH HTTP_VERSION
HEADERS

OPTIONAL BODY
```

The first line is called the **request line**. The `METHOD` field is a single word, known as an [HTTP action verb](HTTP%20Methods.md) and it specifies what operation the server should carry out. The `RESOURCE_PATH` is the path to the resources on the server which the action is to be performed on and corresponds to the path of the URL following the host. Finally, the `HTTP_VERSION` specifies which version of the HTTP protocol the client wants to use when communicating with the server. 

Next are the [HTTP headers](HTTP%20Headers.md). These provide metadata to the server and can contain information such as who the client is, how the resource is to be encoded and more. The HTTP standard defines numerous headers for different purposes, but one may also expand on them by implementing custom headers.

```admonish note
The request line and each header line must be terminated via a CRLF character sequence.
```

The headers are followed by a blank line. Depending on the request method, there may also be an optional request body, such as in the case of uploading a file to the server.
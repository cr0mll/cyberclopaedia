# Introduction
The HTTP method of an HTTP request tells the server which action the client wants it to perform and as such, a single request is only allowed to have a single method. The method is of an HTTP request is specified by an **action verb**, which is the first thing in the request line of the header.

There are 7 methods specified by the HTTP standard, but they may also be extended via the implementation of custom ones. Some of these methods require a request body, while others do not.

| Method | Description|Has Request Body? |
| :----: | :---------------: |:---:|
|`GET`|Retrieve a resource from the server.|No|
|`HEAD`|Retrieve only the headers for a resource from the server.|No|
|`POST`|Send data to the server for processing.|Yes|
|`PUT`|Upload the request body to the server.|Yes|
|`TRACE`|Trace the messages.|No|
|`OPTIONS`|Retrieve from the server what HTTP methods can be used on it.|No.|
|`DELETE`|Remove a document from the server.|No.|

```admonish note
Due to security reasons, HTTP servers rarely implement all of the above methods and even if they do, there are usually heavy restrictions on who is allowed to use them and how.
```


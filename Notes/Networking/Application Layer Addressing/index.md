# Uniform Resources Identifiers (URIs)
The TCP/IP suite provides functionality for locating and accessing resources at the application layer. This is achieved through the use of *Uniform Resource Identifiers (URIs)*.

The premise behind URIs is to serve as an extension to the [Domain Name System](Protocols/Domain%20Name%20System%20(DNS)/index.md). DNS assigns high-level identifiers to hosts which can store resources such as various files. In essence, a URI is a way to refer to a specific file on a specific host.

## Types of URIs
There are two types of Uniform Resource Identifiers: 
- **Uniform Resource Name (URN)** - this is an identifier which uniquely identifies a resource, but specifies no location or way to access it. One can think it of it as merely a number which gets assigned to a given resource.
- **Uniform Resource Locator (URL)** - this is a uniform resource identifier which identifies a resource by specifying its location as well as an application layer protocol to access it. You have most likely seen URLs with only HTTP(s) as their protocol, but they can actually employ a wide array of protocols such as FTP or Telnet.
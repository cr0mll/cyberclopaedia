# The Rich Header

This chunk of data is NOT part of a typical PE file. It is an undocumented structure which is only found in files built with the Visual Studio Toolset. It is located immediately after the DOS stub and before the NT headers and serves the purpose of outlining the Visual Studio tools and versions that were used to build the PE file. It is possible to completely zero out this part of the PE file without affecting it.

The Rich Header comprises a chunk of XOR-encrypted data. It begins with a signature, `DanS`, followed by three zero-ed DWORDs used for padding. Next are entries containing information about the Visual Studio tools used in the build process of the PE file. The entries are represented by DWORD pairs, where the high word of the first DWORD stores the product or type ID and the low word contains the build ID. The second DWORD is used for storing the use count for each tool.

At the end of the header is another signature, `Rich`, followed by a checksum. The checksum field is what serves as the XOR key.

The Rich Header is automatically parsed by PE-Bear and can be easily inspected:

![](<../../../Reverse Engineering/Binary Formats/PE/Resources/Images/PE\_Rich\_Header.png>)

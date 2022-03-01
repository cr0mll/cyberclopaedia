# The Heap
The heap is a memory region which allows for dynamic allocation. Memory on the heap is alloted at runtime and programs are permitted to freely request additional heap memory whenever it is required.

It is the program's job to request and relieve any heap memory *only once*. Failure to do so can result in undefined behaviour. In C, heap memory is usually allocated through the use of `malloc` and whenever the program is finished with this data, the `free` function must be envoked in order to mark the area as available for use by the operating system and/or other programs.

Heap memory can also be allocated by using malloc-compatible heap functions like `calloc`, `realloc` and `memalign` or in C++ using the corresponding `new` and `new[]` operators as well as their deallocation counterparts `delete` and `delete[]`.


## Heap Rules

1. *Do not* read or write to a pointer returned by `malloc` after that pointer has been passed to `free`. -> Can lead to use after free vulnerabilities. 
2. *Do not* use or leak uninitialised information in a heap allocation. -> Can lead to information leaks or uninitialised data vulnerabilities.
3. *Do not* read or write bytes after the end of an allocation. -> Can lead to heap overflow and read beyond bounds vulnerabilities.
4. *Do not* pass a pointer that originated from `malloc` to `free` more than once. -> Can lead to double delete vulnerabilities.
5. *Do not* write bytes before the beginning of the allocation. -> Can lead to heap underflow vulnerabilities.
6. *Do not* pass a pointer that did not originate from `malloc` to `free`.  -> Can lead to invalid free vulnerabilities.
7. *Do not* use a pointer returned by `malloc` before checking if the function returned `NULL`. -> Can lead to null-dereference bugs and sometimes arbitrary write vulnerabilities.
 
The implementation of the heap is platform specific.

# The GLIBC Heap
The heap grows from lower to higher address. 

## Chunks
The heap manager allocates resources in the so-called *chunks*. These chunks are stored adjacent to each other and must be 8-byte aligned or 16-byte aligned on 32-bit and 64-bit systems respectively. In addition to this padding, each chunks contains metadata which provides information about the chunk itself. Consequently, issuing a request for memory allocation on the heap actually allocates more bytes than originally requested.

It is important to distinguish between in-use chunks and free (or previously allocated) chunks, since they have disparate memory layouts.

The following diagram outlines a chunk that is in use:

![[Resources/Images/In_use_chunk.png]]

The `size` field contains the chunk size in bytes. The following three bits carry specific meaning:
- **A (0x04)** - Allocated arena. If this bit is 0, the chunk comes from the main arena and the main heap. If this bit is 1, the chunk comes from mmap'd memory and the location of the heap can be computed from the chunk's address.
- **M (0x02)** - If this bit is set, then the chunk was `mmap`-ed and isn't part of a heap.
- **P (0x01)** - If this bit is set, then the previous chunk should not be considered for coalescing and the `mchunkptr` points to a previous chunk still in use

A free chunk looks a bit different:

![[Resources/Images/Free_chunk.png]]

The size and AMP fields carry on the same meaning as those in chunks that are in use. Free chunks are organised in linked or doubly linked lists called *bins*. The `fwd` and `bck` pointers are utilised in the implementation of those linked lists. Different types of bins exist for different purposes.

The top of the heap is by convention called *the top chunk*.

## Memory Allocation on the Heap
### Allocating from Free Chunks
When an application requests heap memory, the heap manager traverses the bins in search of a free chunk that is large enough to service the request. If such a chunk is found, it is removed from the bin, turned into an in-use chunk and then a pointer is returned to the user data section of the chunk.

### Allocating from the Top Chunk
If no free chunk is found that can service the request, the heap manager must construct an entirely new chunk at the top of heap. To achieve this, it first needs to ascertain whether there is enough space at the top of the heap to hold the new chunk.

### Requesting Additional Memory at the Top of the Heap from the Kernel
Once the free space at the top of the heap is used up, the heap manager will have to ask the kernel for additional memory.

On the initial heap, the heap manager asks the kernel to allocate more memory at the end of the heap by calling `sbrk`.On most Linux-based systems this function internally uses a system call called `brk`. 

Eventuall, the heap will grow to its maximum size, since expanding it any further would cause it to intrude on other sections of the process' address space. In this case, the heap manager will resort to using `mmap` to map new memory for heap expansions.

If `mmap` also fails, then the process is unable to allocate more memory and `malloc` returns `NULL`.

### Allocating Large Chunks
Large chunks get treated differently in their allocation. These are allocated off-heap through the direct use of `mmap` calls and this is reflected in the chunk's metadata by setting the `M` bit to 1. When such allocations are later returned to the heap manager via a call to `free`, the heap manager releases the entire `mmap`-ed region back to the system via `munmap`.

Different platforms have different default thresholds for what counts as a large chunk and what doesn't.

## Arenas

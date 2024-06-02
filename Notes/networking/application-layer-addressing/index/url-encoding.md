# Introduction
Normally, URLs are comprised of the so-called *safe* characters which include the lower-  and uppercase alphanumerics `a-zA-Z` and the digits 0 through 9 as well as the characters: dollar-sign (`$`), hyphen (`-`), underscore (`_`), period (`.`), plus sign (`+`), exclamation point (`!`), asterisk (`*`), apostrophe (`'`), left parenthesis (`(`),
and right parenthesis (`)`).

### URL Encoding
Any other characters are considered *unsafe* either due to their reserved meaning or because they are outside the ASCII range. Any such characters must be URL-encoded. This is achieved by representing each unsafe character via a `%` symbol followed by a hexadecimal sequence of digits which uniquely identifies it:

|Character|URL Encoding|Character|URL Encoding|Character|URL Encoding|
|:--:|:--:|:--:|:--:|:--:|:--:|
|`<space>`|`%20`|`<`|`%3C`|`>`|`%3E`|
|`#`|`%23`|`%%`|`%25`|`{`|`%7B`|
|`}`|`%7D`|<code>&#124;</code>|`%7C`|`\`|`%5C`|
|`^`|`%5E`|`~`|`%7E`|`[`|`%5B`|
|`]`|`%5D`|<code>&#96;</code>|`%60`|`;`|`%3B`|
|`/`|`%2F`|`?`|`%3F`|`:`|`%3A`|
|`@`|`%40`|`=`|`%3D`|`&`|`%26`|

```admonish note
Every character has a URL-encoding, including safe ones.
```

Whenever the above sequences are encountered in a URL, they are interpreted as the literal character they represent. 
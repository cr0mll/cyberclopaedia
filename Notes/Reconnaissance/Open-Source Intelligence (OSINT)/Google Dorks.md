# Introduction
Goolge can be a very powerful tool in your OSINT toolkit. *Google dorking* or *Google hacking* is the art of using specially crafted Google queries to expose sensitive information on the Internet. Such a query is called a *Google dork*.

You may find all sorts of data and information, including exposed *passwd* files, lists with usernames, software versions, and so on.

```admonish warning
If you find such an exposed web server, do NOT click on the links from the search results. Such an act may be considered illegal! Only do this if you have written permission from the target system's owner.
```


A good resource for finding Google dorks is the Google Hacking Database located at https://www.exploit-db.com/google-hacking-database.

*You shouldn't enter any spaces between the advanced search operator and the query*.

# Common operators
**site:** - restricts the search results to those only on the specified domain or site

**inurl:** - restricts results to pages containing the specified word in the URL

**allinurl:** - restricts results to pages containing all the specified words in the URL

**intitle:** - restricts results to pages containing the specified word in the title

**allintitle:** - restricts results to pages containing all the specified words in the title

**inanchor:** - restricts results to pages containing the specified word in the anchor text of links located on that page
- an anchor text is the text displayed for links instead of the URL

**allinanchor:** - restricts results to pages containing all the specified terms in the anchor text of links located on that page

**cache:** - displays Google's cached version of the webpage instead of the current version

**link:** - searches for pages that contain links pointing to the specified site or page
- you can't combine a link operator with a regular keyword query
- combining link: with other advanced search operators may not yield all the matching results

**related:** - displays websites similar or related to the one specified

**info:** - finds information about a specific page

**location:** - finds location information about a specific query

**filetype:** - restricts results to the specified filetype
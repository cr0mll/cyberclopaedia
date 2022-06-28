
# Welcome
The Cyberclopaedia is welcome to all and the community's contributions are much appreciated.

# Getting Started
You would first need to create a Pull Request. 

In your pull request it is important that you only alter files located in the `Notes` directory. Do NOT use mdbook to build the book yourself in the PR, since that may generate unnecessary merge conflicts and will also mingle with the book publishing cycle (sections of the book may not be made available on https://cr0mll.github.io/cyberclopaedia immediately after they are written). Moreover, do not touch the `SUMMARY.md` file, since it is auto-generated.

You are advised to use Obsidian as your markdown editor, although really anything is possible as long as it uses the `![]()` syntax for images and the `[]()` syntax for links.

Once you are finished with adding new or improving old content, you should submit your pull request and await its merge.

*Note, case sensitives applies throughout.*

## Project Structure
Any content should be classifiable in one of the main categories: Cryptography, Reconnaissance, Exploitation, Post Exploitation, Reverse Engineering, Web (preferably not since this section will be deprecated), or Malware Analysis. If your content does not conform to such classification, you should create a new such category, but that's only for extreme cases. Once again, however, do NOT mess with the `summarise.py` script.

Each folder should be equipped with a `README.md` file which should serve as an introduction to the contents inside. 

Resources are split at every directory into the `Resources` folder, with images specifically being placed under the `Resource/Images` folder. From there on, you are free to create new subdirectories inside for each article, which should be eponymous with the article's name. Your other option is to just prefix every resource with the article name that it pertains to. Resource names should be written in `Camel_Snake_Case`.
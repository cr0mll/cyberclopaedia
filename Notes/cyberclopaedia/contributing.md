# Contributing

## Overview

The Cyberclopaedia is open to contribution from everyone via pull requests on the [Cyberclopaedia GitHub repository](https://github.com/cr0mll/cyberclopaedia). When contributing new content, please ensure that it is as relevant as possible, contains detailed (and yet tractable) explanations and is accompanied by diagrams where appropriate.

#### In-Scope

You should only make changes inside the [eight category folders](contributing.md#structure) under the `Notes/` directory. Minor edits to already existing content outside of the aforementioned allowed directories are permitted as long as they do not bring any semantic change - for example fixing typos.

#### Out-of-Scope

Any major changes outside of the eight category folders in the `Notes/` directory are not permitted and will be rejected.

## Structure

Cyberclopaedia content is organised in the following eight categories: [Reconnaissance](../reconnaissance/), [Exploitation](../exploitation/), [Post Exploitation](../post-exploitation/), [System Internals](../system-internals/), [Reverse Engineering](../reverse-engineering/), [Hardware Hacking](../hardware-hacking/), [Cryptography](../cryptography/) and [Networking](../networking/). You should organise your content within them. If you feel like it is completely unable to fit in one of these categories (highly unlikely), you are still encouraged to submit your pull request. It will be reviewed and you will be either instructed to move your content to an already existing category which was deemed appropriate, or your new category will be implemented. Note that the name of the new category may not be the same as the one suggested by you if a different name is more pertinent.

Inside the eight category directories, you are free to create as many new folders and go as many layers deep as you like. Nevertheless, you should still strive to abide by the already existing structure.

#### Naming

All file and directory names should follow Title Case.

#### Folder Organisation

Each folder you create must have the following structure:

![](<../Cyberclopaedia/Resources/Images/Folder Structure.svg>)

Images, such as diagrams, are respectively placed in the `Resources/Images` subdirectory. Every page in your main folder should be reflected in this subdirectory by means of an eponymous folder within `Resource/Images`. Any images used in this page would then go in `Resource/Images/Page Name`.

The `index.md` file is required by mdBook. This is the file which gets rendered when someone clicks on the folder name in the website's table of contents. Ideally, it should contain an overview of or introduction to the content inside the directory, but you may also leave it empty.

#### Page Structure

Ideally, pages should begin with an introduction or overview section - for example, with an `# Introduction` or `# Overview` heading.

The name of any new major topic in a page should be indicated with a Heading 1 style. From then on, subtopics should be introduced with Heading 2, 3 and so on.

For links and images, do NOT use wiki-links style. Instead, use the standard `(text)[link]` or `!()[path]` paradigms. Note that images should be isolated by an empty line both above and below.

LaTeX is done using the `$` delimiters for inline equations and the `$$` delimiters for blocks. The latter should be isolated by an empty line both above and below, just like images. If you want to insert a dollar sign, prepend it with a backslash or put it in a code block.

## Toolchain

* Website building: The Cyberclopaedia website is built using [mdBook](https://github.com/rust-lang/mdBook). The summary file is automatically created with the `summarise.py` script in the Scripts directory. Do NOT run this script or build the book yourself when contributing content to the Cyberclopaedia. This is done only by reviewers in order to avoid unnecessary merge conflicts. An mdBook installation is NOT necessary for contributions.
* Markdown: Feel free to use your favourite markdown editor. [Obsidian](https://obsidian.md/) is an excellent free option.
* Diagrams: These should be in the form of vector `.svg` images. Diagrams should have a completely opaque, white background and appropriate padding. As a suggestion, you can use [diagrams.net](https://app.diagrams.net/) with the following export settings:

![](<../Cyberclopaedia/Resources/Images/Diagram.net Export Settings.png>)

## Licensing

All content inside the Cyberclopaedia, including contributions, is subject to the [MIT licence](license.md). By contributing, you guarantee that any content you submit is compatible with this licence.

Knowledge should be free.

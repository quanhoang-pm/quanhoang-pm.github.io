---
title: "Ubuntu installation in dual boot mode"
permalink: /ubuntu-installation/
date: 2020-05-10
last_modified_at: 2020-06-06 21:30:00
categories:
  - ubuntu
tags:
  - installation
  - ubuntu
---

Ubuntu 20.04 LTS has been released since April 2020. The post is about what should be taken into account during installation process. This is mostly written for my own reference in the future.

#### Things to backup

Personally, I prefer a new fresh operating system for a new start. Therefore I backup only four directories Documents, Musics, Pictures, and Templates. Softwares can be installed after the installation has finished.

My custom setting worth noticing is shown in the table below. Neglect Atom settings if you are not a fan of Atom like me.

| Setting                              | Directory                                                                 |
|:-------------------------------------|:--------------------------------------------------------------------------|
| Bookmark folders                     | ~/.config/gtk-3.0/bookmarks (pointed out [here][link:nautilus-bookmarks]) |
| Custom keywords in Atom              | ~/.atom/packages/language-todo-extra-words/grammars/todo-extra-words.cson |
| Custom shortcuts in Jupyter notebook | None                                                                      |
| Git global configuration             | ~/.gitconfig                                                              |
| Configuration in Atom                | ~/.atom/config.cson                                                       |
| Keyboards remapping in Atom          | ~/.atom/keymap.cson                                                       |
| Code snippets in Atom                | ~/.atom/snippets.cson                                                     |
| Startup Applications                 | None                                                                      |

[link:nautilus-bookmarks]: https://askubuntu.com/questions/503162/where-does-nautilus-store-its-bookmarks

#### Installation process

The overall process might be as follows:
- [Create a live USB stick][link:create-live-usb] by Startup Disk Creator.
- [Remove / resize the obsolete operating systems][link:GParted] (e.g., Windows OS) by GParted.
- Install the new Ubuntu OS by following [the instruction][link:install-OS].

[link:create-live-usb]: https://ubuntu.com/tutorials/tutorial-create-a-usb-stick-on-ubuntu
[link:GParted]: https://www.howtogeek.com/114503/how-to-resize-your-ubuntu-partitions/
[link:install-OS]: https://itsfoss.com/install-ubuntu-dual-boot-mode-windows/

#### Side notes

Before installation, it's best to know which partitions are mounted to which directories (`/`, `/boot`, `/home`, etc). You can acquire that kind of information via File Systems panel in System Monitor.

If you're not sure about the guide provided in English, here is [an article written in Vietnamese][link:installation-in-vnm] presenting how to install Ubuntu OS alongside Windows OS.

You might want to name your USB with something like `Ubuntu20.04LTS`. It is relatively easy to rename a USB in Windows OS. As for this action in Ubuntu OS, you can use Disks application as mentioned in [this question][link:rename-USB] in askubuntu forum.

After rebooting, your computer may go directly to Windows OS instead of prompting you to choose between Ubuntu OS and Windows OS. You need to get into the BIOS and make sure that the *ubuntu* device is above the *Windows* device in the OS boot manager. The detailed steps are in [an answer][link:OS-boot-manager] in askubuntu forum.

As for the layout on the desktop, software icons on the left side bar are taken from `Show Applications` (the button in the bottom left corner of the screen), you just need to drag and drop them to appropriate locations. Moreover, for a clean desktop, the trash icon can be hidden by an option in GNOME Tweaks.

Finally, just in case you break something while creating new partitions, the guide in [Ubuntu documentation][link:ubuntu-documentation] might be helpful.

[link:installation-in-vnm]: https://thuthuat.taimienphi.vn/cach-cai-ubuntu-song-song-voi-windows-10-8-7-uefi-va-gpt-31617n.aspx
[link:rename-USB]: https://askubuntu.com/a/233681/1073641
[link:ubuntu-documentation]: https://help.ubuntu.com/community/Grub2/Installing#Fixing_a_Broken_System
[link:OS-boot-manager]: https://askubuntu.com/questions/789016/how-do-i-access-ubuntu-after-installing-alongside-windows-10-non-eufi

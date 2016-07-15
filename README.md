BatchUTF-8 for Notepad++
========================

This file is for use with the *Python Script* plugin for *Notepad++*.

Copyright
---------
Copyright © 2016 TNG Consulting Inc. - <http://www.tngconsulting.ca>

Unless otherwise noted, computer program source code and documentation
for BatchUTF-8 for Notepad++ is covered under TNG Consulting Inc.
copyrighgt, and is distributed under the MIT License.

You should have received a copy of the MIT License (see LICENSE.md)
along with BatchUTF-8.  If not, see <https://mit-license.org/>.

Authors
-------
Michael Milette - Lead Developer - <http://www.tngconsulting.ca>

Description
-----------
The BatchUTF-8 Python script for Notepad++ allows you to crawl a local
directory tree, converting text files to UTF-8 character set, replacing
all occurrences of strings iso-8859-1 and windows-1252 to utf-8 and
changing end-of-lines to CR/LF (Dos/Windows Format).

The script will only process files with the following file type
extensions:

    .htm, .css, .xml, .txt, .php, .sql, .js, .py, .md, .html, .json

A trace of the scripts progress will appear in the Python Script console,
if visible.

Requirements
------------
This script requires:
* Windows 7, 8, 8.1 and 10
* Notepad++
* Python 2.7 (32-bit version)

Changes
-------
2016-07-16 - Initial version.

Installation
------------
Installing Python 2.7.x

* You can download the installer for Python from:
  https://www.python.org/downloads/windows/
* Double click on the downloaded file to complete the installation process.

Installing the Python Script plugin for Notepad++:

* Launch Notepad++.
* In the menu, click *Plugins* > *Plugin manager*.
* Search for *Python Scripts* in the list of available plugins,
  check its box and click the Install button.
* You may need to re-start Notepad++.

Installing BatchUTF-8

* Go to C:\Users\<your user name>\AppData\Roaming\Notepad++\plugins\config\PythonScript\scripts
* Copy the BatchUTF8.py into this folder.

Unininstallation
----------------
Uninstalling the script by deleting the following file:
C:\Users\<your user name>\AppData\Roaming\Notepad++\plugins\config\PythonScript\scripts\BatchUTF8.py

Usage & Settings
----------------
There are no settings for this script.

Important: It is highly recommended that you only run this script on a
copy of your files or make a backup before you proceed.

Note: This script will also replace any occurrence of the following strings
found in the file content:

* *iso-8859-1* will be replaced with *utf-8*.
* *windows-1252* will be replaced with *utf-8*.

To begin batch converting files to UTF-8:

* In the Notepad++ menu, click *Plugins* > Python Scripts > Scripts > BatchUTF8
* Enter the root directory where the files ready for conversion are located
  and click OK.
* Click *Yes* again to confirm that you want to proceed. Once you've clicked
  this button, there is no turning back.

Troubleshooting
---------------
If the script doesn't seem to be converting the character encoding for the files,
ensure that the following "Autodetect character encoding" setting is checked in
Notepad++'s Settings > Preferences > MISC.

Limitations
-----------
Although it will convert all character sets recognized by Notepad++, it will
only search/replace *iso-8859-1* and *windows-1252* strings with *utf-8*. You
will need to modify the source

code in order to have it replace strings for other character sets.

Security considerations
-----------------------
We are not currently aware of any security concerns.

Motivation for this script
--------------------------
The development of this plugin was motivated by the web development
efforts of TNG Consulting Inc.

Further information
-------------------
For further information regarding the local_BatchUTF-8 plugin, support or to
report a bug, please visit the project page at:

    <http://github.com/michael-milette/npp-BatchUTF-8>

Future
------
* Automate search/replace for other character sets recognized by Notepad++.
* Fixing situations where every second line in the source code is blank.
* Giving user the ability to choose the type of end-of-line to be apply.
* Preserve the original date/time stamp of each file.
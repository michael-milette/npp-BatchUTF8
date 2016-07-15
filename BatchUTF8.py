# Batch UTF-8 Converter for Notepad++
# Copyright (c) 2016 TNG Consulting Inc.
# http://www.tngconsulting.ca
# Batch UTF-8 is released under the MIT License.
# Version 1.0 by: Michael Milette, www.tngconsulting.ca
# Date: 2016-07-16
# See README for details.
*/

#***   IMPORTS   ***
import os
from Npp import *

def main():
    #*** DEFINITIONS ***
    appName = 'Batch UTF-8 Converter for Notepad++'

    #*** Get Windows My Documents folder. ***
    try:
        import ctypes.wintypes;
    except ImportError: # Happens if you installed 64-bit Python but Notepad++'s version is 32-bit.
        filePathSrc = "c:\\"
    else:
        CSIDL_PERSONAL = 5       # My Documents
        SHGFP_TYPE_CURRENT = 0   # Get current, not default value
        buf= ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
        ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_PERSONAL, None, SHGFP_TYPE_CURRENT, buf)
        filePathSrc = buf.value

    #*** Prompt for Root folder to be processed ***
    filePathSrc = notepad.prompt("Specify the root folder of files to be converted to UTF-8:\rSupported file formats: .htm, .html, .css, .js, .xml, .txt, .php, .py, .json, .sql and .md", appName, filePathSrc)
    if filePathSrc == None:
        return

    #*** Confirm action ***
    action = notepad.messageBox('Ready to convert files in ' + filePathSrc + ' to UTF-8?', appName, MESSAGEBOXFLAGS.YESNO | MESSAGEBOXFLAGS.DEFBUTTON2)
    if action != MESSAGEBOXFLAGS.RESULTYES:
        return

    #*** Do the deed... ***
    for root, dirs, files in os.walk(filePathSrc):
        for fn in files:
           if fn[-4:] in ['.htm', '.css', '.xml', '.txt', '.php', '.sql'] or fn[-3:] in ['.js', '.py', '.md'] or fn[-5:] in ['.html', '.json']:
                notepad.open(root + "\\" + fn)
                console.write(root + "\\" + fn + "\r\n")
                if (notepad.getEncoding() != BUFFERENCODING.UTF8):
                    notepad.runMenuCommand("Encoding", "Convert to UTF-8")
                if (editor.findText(0, 0, editor.getLength(), "iso-8859-1") != None):
                    editor.replace('iso-8859-1', 'utf-8')
                if (editor.findText(0, 0, editor.getLength(), "windows-1252") != None):
                    editor.replace('windows-1252', 'utf-8')
                if (notepad.getFormatType() != FORMATTYPE.WIN):
                    notepad.runMenuCommand("EOL Conversion", "Windows Format")
                notepad.save()
                notepad.close()

main()
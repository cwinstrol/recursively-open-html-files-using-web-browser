import os,webbrowser
#webbrowser.register('chromium',None,webbrowser.BackgroundBrowser("C:\\ProgramFiles\\chrome-win\\chrome.exe"),preferred=True)
#dn=''
def oc(dn):
    for p,ds,fs in os.walk(dn):
        for f in fs:
            if f.endswith('.html'):
                webbrowser.get('chromium').open_new_tab(os.path.join(p,f))
                #change default .html app and open with code?

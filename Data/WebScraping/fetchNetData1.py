import urllib.request

def testRequest():
    # TODO: the process is similar with local file open and read,
    webUrl = urllib.request.urlopen("http://www.baidu.com")
    # getcode 200 means everything ok
    # 404 not found 
    returnCode = webUrl.getcode()
    print(f"Result Code: {returnCode}")
    if returnCode == 200:
        data = webUrl.read()
        print(data)

if __name__ == "__main__":
    testRequest()   
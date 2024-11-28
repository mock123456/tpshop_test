import urllib
from urllib import parse
import requests
import base64
API_KEY = "x3kLGmvH9gNgh3Sea0SITDPV"
SECRET_KEY = "do2cqpjfI3vkrkBAnrOhUEtfFl5N0Xfj"


def verification_code(picture_url):
    '''输入文件url,返回信息包含验证码和status_code'''
    url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic?access_token=" + get_access_token()
    content = get_file_content_as_base64(path=picture_url, urlencoded=True)
    # image 可以通过 get_file_content_as_base64("C:\fakepath\4.jpg",True) 方法获取
    payload = f'image={content}&detect_direction=false&paragraph=false&probability=false&multidirectional_recognize=false'
    # payload = 'image=iVBORw0KGgoAAAANSUhEUgAAAGQAAAAlCAIAAAA7hNvKAAAID0lEQVR4nO2Za1BT2R3A%2F%2FeVdwgECJAEEogQUKqCurgK2nV0dkGn4059Te063dZOfbRupx07rdsP7cxO1%2F3SzrirU3e7raNTd9WK2i7i%2BGBVtFWo0l0kIJKg5MEjQN65yU3uOf1wLYugmFSKdia%2FT7kn5%2Fzzv7977zn%2Fe0IEYghSJAb5vBP4fyIlKwlSspIgJSsJUrKSgJ7h3%2BNiXIgN8QjRFCUWiaViqdCOMQ6yQYSQUqYkyRf0EhIzVjqEIuFrbc3BcLC4oFgpVzIUE%2BfjGGMgACF8q%2BuWzWHjET%2BnaM6amtU0NdNXMRFmLqcPTx6kKHr7um0TRHT2du07ti%2FEhoRDq8M6t%2FhrRbqiRGIGwoH6plPzzfPnFc%2Bd%2FownMUOybA6bpbfzvR%2FtZWhmfPullkuHzx5B6Ku7GyHk8XtB9%2FSYXfe73j%2F2gT%2Fkv%2FvgbqnBLBaJE0zGG%2FDefdDd4%2BihSKp63lJ9jj7BgTMkK8iGSJKkHzXVcqflxMUTCCGzwVxTUdNqabXarRtWbchKzwqEAkq5coqAYTZ8uOGwP%2BQHgCHPUISLJijL5uw9eu6ozWmLxWMA0D%2Fs2rVxF0VRiYydIVklBcWxeKxv4EG5qVxoGfWPfvzXP4Yj4VJj6U83%2F0QilszSmyJcxKQ3AYAv6BscGdSoNQRBjI%2BDMeYRf6P9xtW2ZseQk6GZWDwW5aLOIYdKMXvqHDDG%2FcP9ew%2FtZaPsWNhRnyeO4gnKmqF1RyKW1C557XDDEW%2FQJ7Rcvd0cjoSzM7Lf2rRLIpYAgE6jE0wBgEqhkkvlLrcrEo2MjxPlor8%2FefBg%2FYedvZ2LZi98d%2BdvJCIJAHT2dj41hxAb2n%2FiABtlTXrTxlUbM1WZVeVVr7%2BylqGYp44VmH5ZFpvF7XFPbl%2F50kqMcX1TPQBwMe5iywUAqJlfrZApHhtHIVOoVZlWp42NskKLy%2B1qbmtutbQKh2XGMpVSpVapAaDbfu%2BpiV28edE%2BaE9Xpn%2F3G29qs7XVFdVv1H27srQy8UplOh9Dnucv%2FbPpSMMRANBpdC%2BXL64sq1SnqUWMiKGZjLSMX3zn57%2F66NfHLxzX5%2Bh9QT8AjD2VAMBGWbfH7XL3l5vmCAalYklJQfEX976cVzz37oO7Hxzfz%2FO8RCRhoyzGmKIohmbUaWqX22V1WDHGE57Z8fhD%2FtNXz2CMlTLlb%2F%2F8uxHfCAD0u%2Ft%2FuGHnFKMmMG13VpyPn%2FvHuaONR4VD55DzL00n9%2Bx%2F%2B52P37n%2Bxd%2BFRrVKvXP9jg6b5fiFE0KLLvvhsocQ2n%2FiwNsHfvnJ%2BU%2FGZ8%2FQTF5WXsO1s%2FuOvR9iQwRB7HlzT6G2EAC8AS9FUvk5%2BQAQ5aLeoHeK9O5YO3ieBwD7oF0wBQCtllZPwJP4OU6PLITQ6cun6z8%2FxSPemGeoXVKbl5UnfMVGI%2FNL5o31NBvM29dtY%2BiHd7RU8rCCH%2FWP3uu7BwArFrwik8jGB9dlawFjYfLKzsjOz9XPLiwDALdnGADGKjI28sjsNgEhOABkqjK3ffMHs%2FJnAQDGODLlqAlMw2MYi8eu%2Fev6Z80NPOIBQC6VZ6Rl%2FGzLbi7GtXW1aTXadGX6%2BP4ZygyGFgmfr9y%2BuqC0UiqWttxpCUfCGcqMuuq6yc9Fob4IMAAAj3gCCKPWCACDowMAUFwwS52m3rr2e9rsvCmS7Bt4AAAEEFvXbi03zemwWXrsPRKRRJOpSfxMp0HWlz3th%2F52COGHhWWHzdJhs1y5dXn7uu2ra1ZP7o8BMMbC50%2FPf9rc1mzMM1y%2BfQUA6qrrJlStAl6%2FBwMGgEAowMU4lSKdIqkhjxsAMlWZO9fvKC4onjrJYd8IAKhV6rLCUgCwD9oBoKq8Kqn3qmmQVWYs3b1ld1vX7YI8QyAcaLze6A%2F5nW7X%2BRsXvv%2F61sn9KZIcKyDZKNvd193d1w0AFEkpZYpYPDbBV3ffvZOf1wslVZyPhyIhhVROU7Qv4BNq1xJDyVOT9P2nZInH4403G%2Fv6%2Bxia%2BfqC5Umd6TPJ6rH31Dedys%2FNN%2BmLNtduFtZgm8MmrO5PWmVoijbpiqwOKwAILzoMzZQZy3Kzcj9rbjjZVK%2FX6HLUuXKZPMpF77vu99h7NGrNsoplZ66cifPxEBuSSxVSsbSmombqKn88BBAAMOIb2fHeTi7G0RS9vHJ5gm%2BgX2WeVO8JWHot7db2dmu7XqOvLK3EPL7Z0WKxWQBALBIvr1z2%2BLwJonZprWPI2dnbSZCEMc9YU1GzuLxKIVP4gv6Bkf6BkQG3Z9gX8MbiMb1Gt7i8ymw0B8JBQVYwHNSoNZte3bRo9sLEU83NzHEMOQGAi3EkQa6qWrl%2B5fpk94KeSRZGD6ee%2FuH%2Bd%2F%2B0FwDuu%2B5zcY4giA0r15vyTU8amJWe9eNvveUNeBmakUlkErGEJEgAUCnSVIo0s8GMEEIYCaUTRVIEQaQrIyRBIoR8QZ%2BIFi2Z%2B3Li9REArKlZ89HpP%2FA8X6gt3FL3hkFreOzkODXPJOul8qoWS6tzyMkjXph3SILMzcxZVrF8xaIVwvk%2FCalYOrbzNxmSJMlHyxqJSKJSqlQKlT5Hn5QmgaXzli4sWxjhIiqFKtmxYzzr5t%2FAyIDF1mlz2cJsWC6VFWoLSwxmvSaBHZbkOXu9cdGcRdnpWf%2BL4IkwDTulGGOEEWAAAkiC%2FC8ue4IghJ7vjvM0lA4EQVBEQlscz8hz35t%2FQf8aeDFJyUqClKwkSMlKgpSsJEjJSoKUrCRIyUqClKwkSMlKgn8DSIdVVHCi9isAAAAASUVORK5CYII%3D&detect_direction=false&paragraph=false&probability=false&multidirectional_recognize=false'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


def get_file_content_as_base64(path, urlencoded=False):
    """
    获取文件base64编码
    :param path: 文件路径
    :param urlencoded: 是否对结果进行urlencoded
    :return: base64编码信息
    """
    with open(path, "rb") as f:
        content = base64.b64encode(f.read()).decode("utf8")
        if urlencoded:
            content = urllib.parse.quote_plus(content)
    return content


def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))

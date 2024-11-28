import base64
import urllib
import requests
"""
这个文件定义了验证码处理的方法
"""

API_KEY = "x3kLGmvH9gNgh3Sea0SITDPV"
SECRET_KEY = "do2cqpjfI3vkrkBAnrOhUEtfFl5N0Xfj"


def main():
    url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic?access_token=" + get_access_token()

    # image 可以通过 get_file_content_as_base64("C:\fakepath\4.jpg",True) 方法获取
    payload = 'image=%2F9j%2F4AAQSkZJRgABAQEAYABgAAD%2F2wBDAAMCAgMCAgMDAwMEAwMEBQgFBQQEBQoHBwYIDAoMDAsKCwsNDhIQDQ4RDgsLEBYQERMUFRUVDA8XGBYUGBIUFRT%2F2wBDAQMEBAUEBQkFBQkUDQsNFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBT%2FwAARCAAtAIEDASIAAhEBAxEB%2F8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL%2F8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4%2BTl5ufo6erx8vP09fb3%2BPn6%2F8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL%2F8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3%2BPn6%2F9oADAMBAAIRAxEAPwD9Q6KKK6DkCioby7jsLOe5lOIoY2kc%2FwCyBk%2FyrxrwP%2B1x4C8X%2FCef4i3dzP4Z8NQ6idMe41hBHibKj%2BEkEEsOfr6VvCjUqJyhG6ul83sB7XRWV4g15dF8L6lrUVtNqKWlnJeJbWozJOEQuEQd2bGB7kV%2BaviX9q74%2B%2BPtJh%2BNWkxJoHwy8O6xBC2h6fMrNdAsBJHcnG5gQygkgKN4KjPNduCy%2BrjbuDSS01fV7L1YH6f0VleFfElj4x8N6Xrmmyiaw1G2juoHBzlHUMP50%2FxLqEmleHNVvYiBLbWksyE9AVQkfyrzeV83K9wNKivin%2FgnH%2B0lrPxbt%2FGPhzxfr0%2BueIrW5Gp2t1dYDS20nDKgGAFjYLwAAPMAAr7WrqxmFngq0qFTdAFFeJ%2FG79oib4N%2FFD4Y%2BHLjREuNE8XX7WFxrDzlfsj%2FACrGAmMHLOvJPADcVxf7PvxP8XSftRfGb4ceMtbm1Z7CSLU9FWSJY1isWxtRdoAOFliBOMk5yc1pHBVZUXW6W5vVX5X9z3A%2BoKKKK88Aq5b%2FAOpX%2FPeqdXLf%2FUr%2FAJ71EtjSG5JRRRWRuZ9FFFdByHm%2F7SHioeCfgJ4%2F1reEe10a5MZZguZGQqgyemWZR%2BNfltovjrUfEnwf%2BE3wGuvCWpaJFdeJbXUm1W8BZNVhmZ3%2BVSi%2FKBOuGBYEIpr9K%2F2u%2FhX4k%2BNnwK1vwb4Xns4NQ1KW38xr5isZijlWRlyBwSUX9a8o8afBfxLf%2FtRfASCDRLj%2FAIQjwfpBWXUonHkRzRxNtQjOescYGR3r6zKsRQoUGp25rylva3LH3fW7bVhM%2Bu0UJGqjoBivz40nTfD3wF%2FaE%2BLfwg8aXVtpXww8f6XNrNm103l29vuV%2FMYOeFIxIBjvEnoM%2FoTXkHx9%2FZf8HftGT%2BG5PFK3Q%2FsSd5Y%2FskmwzI4G6Jzj7pKj9fWvIy%2FEwoSlCs3ySWtt01qmvNMZ81%2F8E4f2gNT1VZfhJJp82taRoJums%2FE9rFJ9nEG9TDE2V%2BXOZCGYjsuOM19ofEi4%2By%2FDvxRMcER6VdP83TiFjUngfwD4e%2BG%2Fh%2B30TwzpFro2lwABbe1jCg8Yyx6seOpya2rq2hvLeW3uIkngmQxyRSKGV1IwQQeoI7VGMxNLEYp16cOVN39e7%2BYH4ifD3UvGfgW68HeOfD9te%2BCtIjuY9Bk8Y3ED%2BTc%2BdK8o3KOCAoIYKTxH1ycV%2B3sZYxoWKlsDJXoT7Vm33hXRtU0610%2B80myurC1dJLe1mt0aKJk%2B4VUjAK9sdK1a6czzJZi4y5OVq%2Fnvt%2FW3YSVj5T%2F4KSeCJ%2FEP7O8viKwAXU%2FCeoW%2BqxSgEsibxG5XHpvDfRK%2Bafh9oOv%2FAAN%2BOXwL%2BKms%2BNZvGFr8Q42gvNQusx%2BXHPGoSI5YlipkQ%2FVOgr9J%2FG3ha18ceDtc8O3vFpq1lNZSkDkLIhQke4zXm3gH9l3wp4Z%2BFvgvwX4gQ%2BMofCdy15p95qa%2FPHMWdg2Aei%2BYQAcjAHoK6cHmUKGE9hU1V2mrfZlHv0s7MLHslFJS182MKuW%2F%2BpX%2FAD3qnVy3%2FwBSv%2Be9RLY0huSUUUVkbmfRRRXQcgUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAVct%2F8AUr%2FnvVOrlv8A6lf896iWxpDckooorI3P%2F9k%3D&detect_direction=false&paragraph=false&probability=false&multidirectional_recognize=false'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


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


def base64_img(url):
    '''输入图片的url，返回base64编码格式，建议传jpg格式图片'''
    with open(url, 'rb') as f:
        data = f.read()
        base64_data = base64.b64encode(data)
        return base64_data


if __name__ == '__main__':
    main()




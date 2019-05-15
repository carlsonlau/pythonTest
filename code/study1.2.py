import requests
import pandas
from lxml import etree


### 数据抓取 ####

headers = {
   'cookie':'session-id=134-5170006-8913216; ubid-main=133-2832378-3311352; x-wl-uid=1Gs6IaSrjGSO6YIQDYsl+ahTILqK06XRkYFWiUR4RgfRNAzZBEKcVl4NGey0XPViIFKk7RkA22ZUOEmfzUVrLYA==; s_vnum=1983338183799%26vn%3D2; session-id-time=2082787201l; aws-priv=eyJ2IjoxLCJldSI6MCwic3QiOjB9; aws-target-static-id=1555990304116-822299; aws-target-data=%7B%22support%22%3A%221%22%7D; s_fid=2AF4FC56925C3CB6-30D128D056A24EEF; s_vn=1587526304792%26vn%3D1; regStatus=pre-register; aws-target-visitor-id=1555990304120-141745.22_7; s_dslv=1555990957097; s_nr=1555990957100-Repeat; s_pers=%20s_fid%3D014609014C310F6F-1EEB2C2365AB8DA6%7C1708935634479%3B%20s_dl%3D1%7C1557478493344%3B%20gpv_page%3DUS%253ASC%253A%2520SellerCentralLogin%7C1557478493353%3B%20s_ev15%3D%255B%255B%2527www.amz123.com%2527%252C%25271557476693358%2527%255D%255D%7C1715329493358%3B; x-main=2ZIa0I79EFcwFSdVeXVuuvaLV6uwgytGHcx1n5H9hHGJ49CzoFXP3d08sNEx2eiv; at-main=Atza|IwEBIOG1RYwR3vkJZ_xX7TQH3Mt2cI6X6hPBdyVFyGAUjHNv6U-Sg33tqySAtUD5_bmIp8RErdhdye2HPZBuY79h0pEHzB-ODGZMNaBHn2XsUkjhWb3pqgc0WOA2HJhzvFJNkhSdulvPAbDZ3tQTtCD0e77V_hseJUC37bjDuKmzBjsFvr_Qe_hQgcgdjT1Fhzs38__HsxTuPvK55do2oUVaGopQT_zMFaNScsHzeudvfasWwxJMB6j9zKXgItq8RVGJAcGL9iHbPSWwgkyIzKgxjvR6jy9EKMotkuoFNn5UYhOQgDFHnjDQaGnsCAinIAGg8XhKBh5bew0lyXk68sdj8IB4Wlv6FHX-0tSrlhvSkR1mXorJDjnV2YnRLbfSlPJAZzG7ot11qVAe46AZco6Vm0mJ; sess-at-main="GF2XWIAuNtyKNrKbatWplqjSaGWt7UWSoYzVUvuBDc4="; sst-main=Sst1|PQFq7c7AtT7WfWTvDuaK-6ixCxO2ElULEsF59QUmStCk9m5zSF8aCYrQoaLjk1AqahRbV3X6fQ7qFqolemRvehwjdQg2NLl6la422GA116tA7T6V0mObJvcBzqfQdvcHozDjs9WOha-V9v7q0kXWyG1gNsrMtUaIeZzyBvCc69v7AJR6dQwtonwHPxkZVcC6DJZWg8zoU8dbyC4swGIvVdbXLnUK_x8PbbIxEI8UjtZkU7NhX1FZHPr1z0LYaT6Swh1jeGsTVmiRDO6vu7HF1jWe4qSmxKPY0jRmzheBeU4QveuYOlNMUqJvkabVVUct9GoVGgevx26Pf0uRHAlEnnattQ; lc-main=en_US; i18n-prefs=USD; x-amz-captcha-1=1557824909935999; x-amz-captcha-2=b41ESKCUSQ7uniPaQvjgQw==; skin=noskin; session-token=YoRiUnMPx+v5Q4Kmd0l1y9FCVsV5gFBc+xLNxSBD5D6X+ePB9nT9IneJmonjS7r46QrGLp2FWBHyg/y6SnhMj1TlHbvBlYJBuDD1S3MVM/ssGnO/OO9GPQtWs1Ik6N1OZ92rqc9om5iHDPAhn/LyUYTP+4rowuXUzXUArwL0gh+yXSFRPHiUeGVtBuEvjovsKckebaLaPHcWQxkJUhFMTFt1goT5BdSmc/IhALKoOARdeUUqndSiRPbsEQPMRK6sz/oZjxpzaQAuvEWc19MWjQ==; csm-hit=tb:4ZW9H8PNZ28RS5VYF814+s-7NX5H3RY5N1H24AHXH67|1557817741454&t:1557817741454&adb:adblk_yes', #括号中填上你的cookie
   'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36 ', #括号中填上你的User-Agent
}

r = requests.get('https://www.amazon.com/s?k=baseball+cap',headers = headers).text

#print(r)

s = etree.HTML(r)
print(s.xpath('//*[@id="search"]/div[1]/div[2]/div/span[3]/div[1]/div[5]/div/div/div/div[2]/div[2]/div/div[1]/h2/a/@href'))


### 数据抓取 ####

### 数据整理 ####



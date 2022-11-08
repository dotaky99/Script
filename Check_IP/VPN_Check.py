import json
import requests

hostName = "localhost"
serverPort = 8080

class IPQS:
    country_all = {'AD':'안도라', 'AE':'아랍에미리트', 'AF':'아프가니스탄', 'AG':'앤티가바부다', 'AI':'앵귈라', 'AL':'알바니아', 'AM':'아르메니아', 'AO':'앙골라', 'AQ':'남극', 'AR':'아르헨티나', 'AS':'아메리칸사모아', 'AT':'오스트리아', 'AU':'오스트레일리아', 'AW':'아루바', 'AX':'올란드제도', 'AZ':'아제르바이잔', 'BA':'보스니아헤르체고비나', 'BB':'바베이도스', 'BD':'방글라데시', 'BE':'에의', 'BF':'부르키나파소', 'BG':'불가리아', 'BH':'바레인', 'BI':'부룬디', 'BJ':'베냉', 'BL':'생바르텔레미', 'BM':'버뮤다', 'BN':'브루나이', 'BO':'볼리비아', 'BQ':'보네르섬', 'BR':'브라질', 'BS':'바하마', 'BT':'부탄', 'BV':'부베섬', 'BW':'보츠와나', 'BY':'벨라루스', 'BZ':'벨리즈', 'CA':'캐나다', 'CC':'코코스제도', 'CD':'콩고민주공화국', 'CF':'중앙아프리카공화국', 'CG':'콩고공화국', 'CH':'스위스', 'CI':'코트디부아르', 'CK':'쿡제도', 'CL':'칠레', 'CM':'카메룬', 'CN':'중국', 'CO':'콜롬비아', 'CR':'코스타리카', 'CU':'쿠바', 'CV':'카보베르데', 'CW':'퀴라소', 'CX':'크리스마스섬', 'CY':'키프로스', 'CZ':'체코', 'DE':'독일', 'DJ':'지부티', 'DK':'덴마크', 'DM':'도미니카연방', 'DO':'도미니카공화국', 'DZ':'알제리', 'EC':'에콰도르', 'EE':'에스토니아', 'EG':'이집트', 'EH':'서사하라', 'ER':'에리트레아', 'ES':'스페인', 'ET':'에티오피아', 'FI':'핀란드', 'FJ':'피지', 'FK':'포클랜드제도', 'FM':'미크로네시아연방', 'FO':'페로제도', 'FR':'프랑스', 'GA':'가봉', 'GB':'영국', 'GD':'그레나다', 'GE':'조지아', 'GF':'아나의', 'GG':'건지섬', 'GH':'가나', 'GI':'지브롤터', 'GL':'그린란드', 'GM':'감비아', 'GN':'니의', 'GP':'과들루프', 'GQ':'니의', 'GR':'그리스', 'GS':'사우스조지아사우스샌드위치제도', 'GT':'과테말라', 'GU':'괌', 'GW':'니비사우의', 'GY':'가이아나', 'HK':'홍콩', 'HM':'허드맥도널드제도', 'HN':'온두라스', 'HR':'크로아티아', 'HT':'아이티', 'HU':'헝가리', 'ID':'인도네시아', 'IE':'아일랜드', 'IL':'이스라엘', 'IM':'맨섬', 'IN':'인도', 'IO':'영국령인도양지역', 'IQ':'이라크', 'IR':'이란', 'IS':'아이슬란드', 'IT':'이탈리아', 'JE':'저지섬', 'JM':'자메이카', 'JO':'요르단', 'JP':'일본', 'KE':'케냐', 'KG':'스스탄의', 'KH':'캄보디아', 'KI':'키리바시', 'KM':'코모로', 'KN':'세인트키츠네비스', 'KP':'조선민주주의인민공화국', 'KR':'대한민국', 'KW':'쿠웨이트', 'KY':'케이맨제도', 'KZ':'카자흐스탄', 'LA':'라오스', 'LB':'레바논', 'LC':'세인트루시아', 'LK':'스리랑카', 'LI':'리히텐슈타인', 'LR':'라이베리아', 'LS':'레소토', 'LT':'리투아니아', 'LU':'룩셈부르크', 'LV':'라트비아', 'LY':'리비아', 'MA':'모로코', 'MC':'모나코', 'MD':'몰도바', 'ME':'몬테네그로', 'MF':'생마르탱', 'MG':'마다가스카르', 'MH':'마셜제도', 'MK':'북마케도니아', 'ML':'말리', 'MM':'미얀마', 'MN':'몽골', 'MO':'마카오', 'MP':'북마리아나제도', 'MQ':'마르티니크', 'MR':'모리타니', 'MS':'몬트세랫', 'MT':'몰타', 'MU':'모리셔스', 'MV':'몰디브', 'MW':'말라위', 'MX':'멕시코', 'MY':'말레이시아', 'MZ':'모잠비크', 'NA':'나미비아', 'NC':'누벨칼레도니', 'NE':'니제르', 'NF':'노퍽섬', 'NG':'나이지리아', 'NI':'니카라과', 'NL':'네덜란드', 'NO':'노르웨이', 'NP':'네팔', 'NR':'나우루', 'NU':'니우에', 'NZ':'뉴질랜드', 'OM':'오만', 'PA':'파나마', 'PE':'페루', 'PF':'프랑스령폴리네시아', 'PG':'니의', 'PH':'필리핀', 'PK':'파키스탄', 'PL':'폴란드', 'PM':'생피에르미클롱', 'PN':'핏케언제도', 'PR':'푸에르토리코', 'PS':'팔레스타인', 'PT':'포르투갈', 'PW':'팔라우', 'PY':'파라과이', 'QA':'카타르', 'RE':'레위니옹', 'RO':'루마니아', 'RS':'세르비아', 'RU':'러시아', 'RW':'르완다', 'SA':'사우디아라비아', 'SB':'솔로몬제도', 'SC':'세이셸', 'SD':'수단', 'SE':'스웨덴', 'SG':'싱가포르', 'SH':'세인트헬레나', 'SI':'슬로베니아', 'SJ':'스발바르얀마옌', 'SK':'슬로바키아', 'SL':'시에라리온', 'SM':'산마리노', 'SN':'세네갈', 'SO':'소말리아', 'SR':'수리남', 'SS':'남수단', 'ST':'상투메프린시페', 'SV':'엘살바도르', 'SX':'신트마르턴', 'SY':'시리아', 'SZ':'에스와티니', 'TC':'터크스케이커스제도', 'TD':'차드', 'TF':'프랑스령남방및남극지역', 'TG':'토고', 'TH':'태국', 'TJ':'타지키스탄', 'TK':'토켈라우', 'TL':'동티모르', 'TM':'투르크메니스탄', 'TN':'튀니지', 'TO':'통가', 'TR':'튀르키예', 'TT':'트리니다드토바고', 'TV':'투발루', 'TW':'중화민국', 'TZ':'탄자니아', 'UA':'우크라이나', 'UG':'우간다', 'UM':'미국령군소제도', 'US':'미국', 'UY':'우루과이', 'UZ':'우즈베키스탄', 'VA':'바티칸시국', 'VC':'세인트빈센트그레나딘', 'VE':'베네수엘라', 'VG':'영국령버진아일랜드', 'VI':'미국령버진아일랜드', 'VN':'베트남', 'VU':'바누아투', 'WF':'왈리스푸투나', 'WS':'사모아', 'YE':'예멘', 'YT':'마요트', 'ZA':'남아프리카공화국', 'ZM':'잠비아', 'ZW':'짐바브웨'}
    key = ""
    with open("API_KEY", "r") as f:
        key = str(f.readline().strip())

    def check_vpn(self):
        ip_list = []
        with open("IP_LIST", "r") as f:
            for line in f:
                ip_list.append(str(line.strip()))

        print("host\tfraud_score\tcountry_code\torganization\tproxy\tvpn\trecent_abuse")
        for ip in ip_list:
            url = "https://ipqualityscore.com/api/json/ip/%s/%s" %(self.key, ip)
            x = requests.get(url)
            parse_json = json.loads(x.text)
            print(parse_json["host"], end="\t")
            print(parse_json["fraud_score"], end="\t")
            country_tr = parse_json["country_code"]
            print(country_tr, end="\t")
            print(parse_json["organization"], end="\t")
            print(parse_json["proxy"], end="\t")
            print(parse_json["vpn"], end="\t")
            print(parse_json["recent_abuse"])
            

if __name__ == "__main__":
    imple = IPQS()
    imple.check_vpn()
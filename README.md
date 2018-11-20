# tfrss

**이 프로그램은 python 3 기준으로 테스트 되었습니다.**

# 실행 환경 구성
## PhantomJS 설치
1. docker/레지스트리 에서 "wernight/phantomjs" 검색 후 다운로드

2. 이미지 생성 및 실행

   root 권한으로 NAS 접속
   root@myID:~# <B>docker run -d -p 8910:8910 wernight/phantomjs phantomjs --webdriver=8910</B> 실행

3. 웹브라우저(IE,CHROME)에서 nas IP:8910 으로 접속하여 아래와 같은 메세지가 나와야 함.

>"Unknown Command - {"headers":{"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","Accept-Encoding":"gzip, deflate","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7","Connection":"keep-alive","Cookie":"stay_login=0; .......}


## Phyton
1. 패키지 센터에서 Phyton3을 설치합니다.
2. putty 로 나스에 접속하여 관리자 권한으로 전환 합니다 
  'sudo -i'
> * 적당한 위치에 폴더를 하나 만듭니다.
>
>   cd /volume1/web/
>   /volume1/web/# mkdir makerss
>   /volume1/web/# cd makerss
>
> * pip 설치
>
>   /volume1/web/makerss# wget https://bootstrap.pypa.io/get-pip.py
>   python3 -m install get-pup.py
>
> * selenium 패키지 설치
>
>   /volume1/web/makerss# python3 -m pip install selenium
>
> * codecs 패키지 설치
>
>   /volume1/web/makerss# python3 -m pip install codecs
>
> * 권한설정
>
>   /volume1/web/makerss# chmod 777 *
>

## 실행

/volume1/web/makerss# phython3 tfrss.py

......



정상적으로 실행되었다면 tdrama_rss.xml 파일이 생성되어 있어야 합니다.

/volume2/web/makerss# cat tdrama_rss.xml


## 다운로드 스테이션 rss 등록

http://localhost/makerss/tdrama_rss.xml 를 등록합니다.





#### RD와 PhantomJS 설치 방법은 소주6잔님 글을 참조했습니다. 감사합니다.
>  https://github.com/soju6jan
>  https://www.clien.net/service/board/cm_nas/12534455







######################  Setting  ########################################################

LOCAL_URL = 'http://127.0.0.1:8910/'            #PHANTOMJS 로컬 주소

TORRENT_SITE_URL = 'http://www.tfreeca22.com'   #티프리카 주소

BO_TABLE_NAME = 'tdrama'                        #대상게시판ID

BO_TABLE_NAME_Xpath = './/div[@class="list_subject"]/a[2]'  #대상게시판 첫 게시글 Xpath

INIT_START_NUM = 100                            #첫 실행시 가져올 목록 수

#########################################################################################


# 프로그램 설명

1. 최초 실행 시 지정된 게시판 최종 게시글 id='xxxxxx' num을 가져와 endNum에 저장한다.
2. endNum - INIT_START_NUM 만큼 게시글을 크롤링해 xml을 생성한다.
3. endNum - 1 을 BO_TABLE_NAME+rss.txt로 저장한다.
4. 다음 실행시부터 BO_TABLE_NAME+rss.txt에 저장되어 있는 게시글 id num 부터 실행 당시 최종 게시글까지 크롤링해 xml을 생성한다.
5. 실행시 최종 게시글 id num -1을 BO_TABLE_NAME+rss.txt에 저장한다.
6. 다음 실행시부터 4~6를 반복한다.

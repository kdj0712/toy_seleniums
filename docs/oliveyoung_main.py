import oliveyoung_move as move
import oliveyoung_item as item
# oliveyoung_move.py에 있는 function들을 인용하고 이를 move이라는 이름으로 치환한다.
# oliveyoung_item.py에 있는 function들을 인용하고 이를 item이라는 이름으로 치환한다.


# 기본 function 형식 - stand-bying. 호출되었을 때만 기능.
def main(): 
    try :
        uri="https://www.oliveyoung.co.kr/store/main/main.do?oy=0"
        browser = move.getOliveYoung(uri) 
        #매개 변수인 uri를 사용할 move 파일의 get_OliveYoung 펑션을 실행시킨 것을 browser라는 변수로 담는다.
        browser = move.go_nail_care(browser)
        #매개 변수인 browser를 사용할 move 파일의 go_nail_care 펑션을 실행시킨 것을 browser라는 변수로 담는다.
        browser = move.roof(browser=browser)
        #매개 변수인 browser를 사용할 move 파일의 roof 펑션을 실행시킨 것을 browser라는 변수로 담는다.
    except:
        pass
    finally:
        move.quitBrowser(browser)  
        #매개 변수인 browser를 사용할 move 파일의 quitBrowser function을 호출해서 프로그램을 종료시킨다..
    return 0

if __name__ == "__main__":
    try :
        main()   # main function을 실행시킨다.
    except:
        pass  
    finally:
        pass  
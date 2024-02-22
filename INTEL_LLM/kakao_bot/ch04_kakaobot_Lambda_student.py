###### 기본 정보 설정 단계 #######







# OpenAI API KEY
client = openai.OpenAI(api_key = os.environ['OPENAI_API'])

###### 메인 함수 단계 #######

# 메인 함수




    # 카카오 정보 저장

    # 응답 결과를 저장하기 위한 텍스트 파일 생성








    # 답변 생성 함수 실행





    # 답변 생성 시간 체크



            # 3.5초 안에 답변이 완성되면 바로 값 리턴



        # 안정적인 구동을 위한 딜레이 타임 설정


    # 3.5초 내 답변이 생성되지 않을 경우










# 답변/사진 요청 및 응답 확인 함수

    # 사용자다 버튼을 클릭하여 답변 완성 여부를 다시 봤을 시

        # 텍스트 파일 열기


        # 텍스트 파일 내 저장된 정보가 있을 경우










    # 이미지 생성을 요청한 경우









    # ChatGPT 답변을 요청한 경우









            
    #아무 답변 요청이 없는 채팅일 경우

        # 기본 response 값



###### 기능 구현 단계 #######

# 메세지 전송





# 사진 전송






# 응답 초과시 답변
def timeover():
    response = {"version":"2.0","template":{
      "outputs":[
         {
            "simpleText":{
               "text":"아직 제가 생각이 끝나지 않았어요??\n잠시후 아래 말풍선을 눌러주세요?"
            }
         }
      ],
      "quickReplies":[
         {
            "action":"message",
            "label":"생각 다 끝났나요??",
            "messageText":"생각 다 끝났나요?"
         }]}}
    return response

# ChatGPT에게 질문/답변 받기








# DALLE 에게 질문/그림 URL 받기










# 텍스트파일 초기화
def dbReset(filename):
    with open(filename, 'w') as f:
        f.write("")


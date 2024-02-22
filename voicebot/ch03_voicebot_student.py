##### 기본 정보 입력 #####

# audiorecorder 패키지 추가

# OpenAI 패키지 추가

# 파일 삭제를 위한 패키지 추가

# 시간 정보를 위한 패키지 추가S

# TTS 패키기 추가

# 음원 파일 재생을 위한 패키지 추가


##### 기능 구현 함수 #####
def STT(audio):
    # 파일 저장


    # 음원 파일 열기

    # Whisper 모델을 활용해 텍스트 얻기


    # 파일 삭제



def ask_gpt(prompt, model):




def TTS(response):
    # gTTS 를 활용하여 음성 파일 생성





    # 음원 파일 자동 재생









    # 파일 삭제



##### 메인 함수 #####
def main():
    # 기본 설정
    



    # session state 초기화










    # 제목 

    # 구분선


    # 기본 설명











    # 사이드바 생성


        # Open AI API 키 입력받기


        st.markdown("---")

        # GPT 모델을 선택하기 위한 라디오 버튼 생성


        st.markdown("---")

        # 리셋 버튼 생성

            # 리셋 코드 




            
    # 기능 구현 공간
    col1, col2 =  st.columns(2)
    with col1:
        # 왼쪽 영역 작성

        # 음성 녹음 아이콘 추가


            # 음성 재생 

            # 음원 파일에서 텍스트 추출


            # 채팅을 시각화하기 위해 질문 내용 저장


            # GPT 모델에 넣을 프롬프트를 위해 질문 내용 저장
 

    with col2:
        # 오른쪽 영역 작성
        st.subheader("질문/답변")

            # ChatGPT에게 답변 얻기


            # GPT 모델에 넣을 프롬프트를 위해 답변 내용 저장


            # 채팅 시각화를 위한 답변 내용 저장



            # 채팅 형식으로 시각화 하기


                    st.write(f'<div style="display:flex;align-items:center;"> \
                             <div style="background-color:#007AFF;color:white;border-radius:12px;padding:8px 12px;margin-right:8px;">\
                             {message}</div><div style="font-size:0.8rem;color:gray;">{time}</div></div>', unsafe_allow_html=True)
                    st.write("")

                    st.write(f'<div style="display:flex;align-items:center;justify-content:flex-end;">\
                             <div style="background-color:lightgray;border-radius:12px;padding:8px 12px;margin-left:8px;">\
                             {message}</div><div style="font-size:0.8rem;color:gray;">{time}</div></div>', unsafe_allow_html=True)
                    st.write("")
            
            # gTTS 를 활용하여 음성 파일 생성 및 재생
            TTS(response)
        else:
            st.session_state["check_reset"] = False

if __name__=="__main__":
    main()

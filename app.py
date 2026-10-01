import streamlit as st
from datetime import datetime, timedelta

# 페이지 기본 설정
st.set_page_config(page_title="법률사무소 더안 - 송무 컨택 비서", page_icon="⚖️", layout="wide")

# 타이틀 및 브랜딩
st.title("⚖️ 법률사무소 더안 - 송무 컨택 비서")
st.markdown("---")

# 사이드바 - 대분류 카테고리 선택
st.sidebar.header("📁 업무 단계 선택")
category = st.sidebar.radio(
    "송무 단계를 선택하세요",
    [
        "0. 상담 및 초기 안내",
        "1. 사건 시작 & 접수", 
        "2. 재판 진행 (서면/송달)", 
        "3. 기일 안내", 
        "4. 재판 결과 & 선고 안내", 
        "5. 소송 종결 & 확정"
    ]
)

# 공통 입력 사항 (의뢰인 이름)
st.sidebar.markdown("---")
st.sidebar.subheader("👤 기본 정보 입력")
client_name = st.sidebar.text_input("의뢰인/고객 성함", placeholder="홍길동")
if not client_name:
    client_name = "OOO"

# 10분 단위 시간 선택지 생성 (08:00 ~ 19:50)
time_options = [f"{h:02d}:{m:02d}" for h in range(8, 20) for m in range(0, 60, 10)]

# -------------------------------------------------------------
# 📂 0. 상담 및 초기 안내 단계
# -------------------------------------------------------------
if category == "0. 상담 및 초기 안내":
    st.subheader("📂 상담 및 초기 안내 단계")
    sub_category = st.selectbox(
        "안내 유형 선택",
        [
            "방문 상담 접수 안내",
            "예약금 안내 (이혼·가사 전문)",
            "예약금 입금 확인 안내",
            "유선 상담 접수 안내",
            "상담 종료 인사",
            "약정 후 착수금 안내",
            "이혼 기본서류 안내"
        ]
    )
    
    if sub_category == "방문 상담 접수 안내":
        col1, col2, col3 = st.columns([3, 3, 4])
        with col1:
            consult_date = st.date_input("상담 날짜")
        with col2:
            selected_time = st.selectbox("시간 선택", options=time_options, index=36)
        with col3:
            custom_time = st.text_input("✍️ 시간 직접 입력 (예외적인 경우)", placeholder="예: 14:05")
            
        final_time = custom_time if custom_time else selected_time
        date_str = consult_date.strftime('%Y년 %m월 %d일')
        
        weekday_dict = {0: '월', 1: '화', 2: '수', 3: '목', 4: '금', 5: '토', 6: '일'}
        formatted_weekday = weekday_dict[consult_date.weekday()]
        
        text_output = f"""법률사무소 더안입니다.
방문상담 예약이 접수되었습니다.

일시: {date_str}({formatted_weekday}) {final_time}
장소: 청주시 서원구 원흥로 102(산남동), 4층

고객님의 이야기에 귀 기울이고, 현실적이고 명확한 해결방안을 찾아드리겠습니다.
편안한 마음으로 방문해 주시기 바랍니다.
(상담 시 관련 서류나 자료가 있으시면 함께 준비해 주시면 더욱 도움이 됩니다.)

[예약금 안내]
원활한 예약 관리를 위해 예약금 제도를 운영하고 있습니다. 아래 계좌로 20,000원을 입금해 주시면 상담 예약이 최종 확정됩니다.
[신한은행 110-590-715260 (정상의)]
입금하신 예약금은 상담료에서 공제됩니다.

[주차 안내]
건물 주차공간이 협소하여 주차가 어려울 수 있습니다. 여유 있게 오셔서 법원 또는 인근 자동차학원 주차장을 이용해 주시기 바랍니다.

부득이하게 늦으시거나 일정 조정이 필요하신 경우 언제든 연락 주시기 바랍니다. 감사합니다."""

    elif sub_category == "예약금 안내 (이혼·가사 전문)":
        text_output = f"""안녕하세요, 법률사무소 더안입니다.

문의해 주셔서 감사드립니다.
저희 더안은 이혼·가사 분야 전문 변호사가 상담부터 사건 종결까지 직접 담당합니다. 처음 털어놓기 어려운 이야기도 편안하게 말씀해 주세요. 의뢰인의 상황에 맞는 현실적인 방향을 함께 찾아드리겠습니다.

저희 사무소는 안전하고 체계적인 예약 관리를 위해 예약금 제도를 운영하고 있습니다. 예약금 입금 후 예약이 최종 확정되며, 입금하신 금액은 상담료에서 공제됩니다.

[ 예약 안내 ]
예약금 : 20,000원
입금 계좌 : 신한은행 110-590-715260 (정상의)
기본 상담료 : 100,000원 (50분 기준)

※ 예약금은 상담료에서 차감되며, 취소 시 환불되지 않습니다.

입금 확인 즉시 예약을 확정해 드리겠습니다.
감사합니다."""

    elif sub_category == "예약금 입금 확인 안내":
        col1, col2, col3 = st.columns([3, 3, 4])
        with col1:
            consult_date = st.date_input("상담 날짜")
        with col2:
            selected_time = st.selectbox("시간 선택", options=time_options, index=36)
        with col3:
            custom_time = st.text_input("✍️ 시간 직접 입력", placeholder="예: 11:30")
            
        final_time = custom_time if custom_time else selected_time
        date_str = consult_date.strftime('%Y.%m.%d.')
        
        text_output = f"""안녕하세요, 법률사무소 더안입니다.
예약금 입금 확인하였습니다.

상담 일시 : [{date_str} / {final_time}]

예약하신 일정에 뵙겠습니다. 
오시는 길 조심히 오시기 바랍니다. 고객의 목소리에 귀기울여 최선의 해결책을 찾아가겠습니다."""

    elif sub_category == "유선 상담 접수 안내":
        text_output = f"""법률사무소 더안입니다.
유선상담 일정이 확정되었습니다.

힘든 상황에서도 용기를 내어 상담을 신청해 주셔서 감사합니다.
의뢰인 님의 상황을 꼼꼼히 듣고, 최선의 도움을 드리겠습니다.

※ 유선상담은 선불 결제로 진행됩니다.
상담료: 70,000원 [신한 110-590-715260 (정상의)]

리뷰 작성 시 할인혜택이 제공됩니다. 입금 확인 후 예정된 시간에 연락드리겠습니다. 편안한 마음으로 기다려주시기 바랍니다.
※ 더욱 효율적인 상담을 위해 아래 내용을 미리 정리해 주시면 도움이 됩니다. 감사합니다.

- 상담하고 싶은 핵심 질문 2~3가지
- 현재 상황과 관련된 주요 사실 관계
- 보유하고 계신 문서나 증거"""

    elif sub_category == "상담 종료 인사":
        text_output = f"""안녕하세요, 법률사무소 더안입니다. 
오늘 귀한 시간 내어 상담 진행해 주셔서 감사합니다.

상담 드린 내용이 의뢰인님의 고민을 해결하시는 데 조금이나마 실질적인 도움이 되었기를 진심으로 바랍니다.

혹시 상담 이후 추가로 궁금하신 점이 생기거나, 도움이 필요한 부분이 있으시면 언제든 편하게 연락 주시기 바랍니다. 저희는 항상 의뢰인님의 곁에서 함께 고민하겠습니다.
감사합니다."""

    elif sub_category == "약정 후 착수금 안내":
        text_output = f"""안녕하세요, 법률사무소 더안입니다. 
저희 사무소를 믿고 소중한 사건을 맡겨주셔서 깊이 감사드립니다.

보내주신 믿음에 보답할 수 있도록, 착수금 입금이 확인되는 즉시 사건 검토와 절차 진행을 위한 준비에 착수하도록 하겠습니다. 

입금 확인이나 향후 일정 등에 대해 궁금하신 점은 언제든 편하게 문의해 주시기 바랍니다. 의뢰인 님의 가장 어려운 순간에 든든한 힘이 될 수 있도록 최선을 다하겠습니다.
감사합니다."""

    elif sub_category == "이혼 기본서류 안내":
        text_output = f"""법률사무소 더안입니다.
이혼 기본서류 안내드립니다.

<이혼 기본서류>
-모든 서류 '상세' 표시-

-본인, 배우자 각 1부
1. 기본증명서 
2. 가족관계증명서
3. 혼인관계증명서
4. 주민등록등본
5. 주민등록초본 (주소변동사항 포함)

-미성년자녀 있는 경우
(자녀 각1부)
1. 기본증명서
2. 가족관계증명서
3. 주민등록등본
4. 주민등록초본 (주소변동사항 포함)

-그 외
주장 사실을 보충하는 증거자료"""

# -------------------------------------------------------------
# 📂 1. 사건 시작 & 접수 단계
# -------------------------------------------------------------
elif category == "1. 사건 시작 & 접수":
    st.subheader("📂 사건 시작 & 접수 단계")
    sub_category = st.selectbox(
        "안내 유형 선택",
        ["최초 개설 인사", "소장 등 접수 안내", "가압류신청 접수 안내"]
    )
    
    if sub_category == "최초 개설 인사":
        text_output = f"""법률사무소 더안입니다.
{client_name} 고객님의 소중한 신뢰에 보답할 수 있도록 최선을 다해 법률서비스를 제공하겠습니다.
앞으로 이 대화창을 통해 진행상황을 안내해 드리며, 궁금한 점이나 전달사항이 있으시면 언제든 이곳에 말씀해 주시기 바랍니다.

어려운 시간을 함께 극복하고 좋은 결과를 만들어 갈 수 있도록 끝까지 최선을 다하겠습니다. 감사합니다."""

    elif sub_category == "소장 등 접수 안내":
        case_num = st.text_input("사건번호", placeholder="예: 청주지방법원 2026가합00000호")
        fee = st.text_input("납부할 인지대/송달료 금액", placeholder="예: 150,000원")
        bank_account = st.text_input("입금 계좌", value="[농협 000-0000-0000-00 법률사무소 더안]")
        
        text_output = f"""법률사무소 더안입니다. 

{client_name} 님께서 의뢰하신 사건의 소장이 법원에 정상적으로 접수되었습니다. 
[사건번호: {case_num}]

소송 절차 진행을 위해 아래와 같이 법원 인지대 및 송달료 납부가 필요합니다.

총 납부액 : {fee}
입금계좌: {bank_account}"""

    elif sub_category == "가압류신청 접수 안내":
        case_num = st.text_input("사건번호", placeholder="예: 청주지방법원 2026카단00000호")
        fee = st.text_input("납부할 인지대/송달료 금액", placeholder="예: 80,000원")
        bank_account = st.text_input("입금 계좌", value="[농협 000-0000-0000-00 법률사무소 더안]")
        
        text_output = f"""법률사무소 더안입니다. 

{client_name} 님의 사건의 가압류신청이 법원에 접수되어 안내드립니다. 사건번호는 {case_num}입니다.

가압류 절차가 진행되기 위해서는 법원에 인지액 및 송달료를 납부해주셔야 합니다. 아래 계좌로 {fee}을 입금해 주시기 바랍니다.

입금계좌: {bank_account}"""

# -------------------------------------------------------------
# 📂 2. 재판 진행 (서면/송달) 단계 (분리됨)
# -------------------------------------------------------------
elif category == "2. 재판 진행 (서면/송달)":
    st.subheader("📂 재판 진행 (서면 송달 & 제출)")
    sub_category = st.selectbox(
        "안내 유형 선택",
        [
            "작성 서면 초안 확인 요청 (의뢰인 검토)",
            "소송 진행 중 상대방 서면 송달 안내",
            "가압류신청 담보제공명령 안내"
        ]
    )
    
    if sub_category == "작성 서면 초안 확인 요청 (의뢰인 검토)":
        doc_type_option = st.radio(
            "서면 종류 선택",
            ["준비서면", "소장", "답변서", "의견서", "참고서면", "기타"],
            horizontal=True
        )
        if doc_type_option == "기타":
            custom_doc_type = st.text_input("✍️ 서면 종류 직접 입력", placeholder="예: 탄원서, 고소장 등")
            final_doc_type = custom_doc_type if custom_doc_type else "서면"
        else:
            final_doc_type = doc_type_option

        text_output = f"""법률사무소 더안입니다.

{client_name} 님, 제출 예정인 {final_doc_type} 초안을 보내드립니다.

사실관계 중 잘못 기재된 부분이나 추가·수정할 내용이 있는지 확인 부탁드립니다. 

수정사항이 있으시면 표시하여 말씀해 주시고, 별도 의견이 없이 제출을 원하시면 "제출해 주세요."라고 회신 부탁드립니다."""

    elif sub_category == "소송 진행 중 상대방 서면 송달 안내":
        text_output = f"""법률사무소 더안입니다.
진행중인 사건과 관련하여 상대방이 제출한 서면이 송달되어 전달드립니다.

검토 요청사항
• 위 서면 내용을 확인해 주시고, 반박이 필요한 부분이나 추가 제출할 근거자료가 있으시면 보내주시기 바랍니다.
• 원활한 검토 및 서면 작성을 위해 관련 의견과 자료는 늦어도 재판기일 2주 전까지 보내주시기 바랍니다. 이후 전달되는 자료는 해당 기일까지 서면에 반영하기 어려울 수 있습니다.
• 그 밖에 의견이나 문의사항이 있으시면 말씀해 주십시오.

변호사님이 전달해 주신 내용과 서면을 면밀히 검토한 후 구체적인 대응방안을 함께 논의드리겠습니다."""

    elif sub_category == "가압류신청 담보제공명령 안내":
        st.warning("⚠️ 담보제공명령은 기한 준수가 매우 중요합니다.")
        due_date = st.date_input("담보제공 마감 기한")
        due_date_str = due_date.strftime('%Y. %m. %d.')
        
        text_output = f"""🚨 [중요] 법원 담보제공명령 안내 (제출 마감일: {due_date_str}까지)

법률사무소 더안입니다.
{client_name} 님의 부동산가압류 신청과 관련하여 법원으로부터 담보제공명령이 내려졌습니다. (담보제공명령은 가압류 결정에 필요한 절차로, 법원이 정한 담보를 제공하면 가압류 결정을 하겠다는 취지입니다.)

현금 공탁 대신 보증보험 증권 발급 방식으로 진행하실 수 있으므로, 아래 안내에 따라 보증보험을 발급받아 주시면 됩니다.

🔹 진행 방법
1. 아래 안내드리는 보증보험 담당자에게 연락
2. 담당자 안내에 따라 보증보험 발급 진행
(컴퓨터 공인인증서를 통한 온라인 발급 또는 휴대폰 앱 발급 가능)
3. 증권 발급 후 보증보험사에서 전자소송으로 바로 제출되어 담보 제공 절차가 완료됩니다.

🔹 보증보험 담당자
• SGI서울보증 대왕법조대리점
• 담당자: 대표 전익태
• 연락처: 010-2830-9796

🔹 보험료 안내
• 보험료는 보증금액의 약 0.1%~0.3% 정도이며, 정확한 금액은 발급 과정에서 안내받으실 수 있습니다.

🔹 유의사항
• 법원에서 정한 기한({due_date_str}) 내에 증권 발급이 완료되어야 가압류 절차가 진행될 수 있으니, 가급적 빠른 연락 부탁드립니다."""

# -------------------------------------------------------------
# 📂 3. 기일 안내 단계 (분리됨)
# -------------------------------------------------------------
elif category == "3. 기일 안내":
    st.subheader("📂 기일 안내 (재판/공판/조정/선고기일)")
    sub_category = st.selectbox(
        "안내 유형 선택",
        [
            "(민사, 가사 등) 재판 기일 안내", 
            "(형사) 공판기일 안내",
            "(민사, 가사 등) 조정기일 안내", 
            "기일 변경 안내 (민사, 가사 등 - 본인 출석 X)", 
            "기일 변경 안내 (형사 공판기일 - 본인 출석 필수!)", 
            "(형사 사건) 선고기일 안내 - 피고인 출석 필요!",
            "(형사 외 사건) 선고기일 안내 - 출석 불필요"
        ]
    )
    
    col1, col2, col3, col4 = st.columns([2, 2, 2, 3])
    with col1:
        date_input = st.date_input("날짜 선택")
    with col2:
        selected_time = st.selectbox("시간 선택 (10분 단위)", options=time_options, index=37)
    with col3:
        custom_time = st.text_input("✍️ 시간 직접 입력 (선택지에 없는 경우만)", placeholder="예: 14:15")
    with col4:
        court_room = st.text_input("법정 호수", placeholder="제229호 법정")
        
    final_time = custom_time if custom_time else selected_time
    date_str = date_input.strftime('%Y.%m.%d.')

    if sub_category == "(민사, 가사 등) 재판 기일 안내":
        text_output = f"""법률사무소 더안입니다. 
{client_name} 님 사건의 변론기일이 지정되어 안내드립니다. 
{date_str} 변론기일({court_room} {final_time})

변론기일에는 변호사님이 출석하여 진행될 예정이니, 의뢰인께서는 편하신 대로 참석 여부를 정하시면 됩니다. 출석을 원하시는 경우 미리 말씀해 주시면 감사하겠습니다."""

    elif sub_category == "(형사) 공판기일 안내":
        st.warning("⚠️ 형사 사건 공판기일입니다. 피고인 본인 출석 필수 안내가 포함됩니다.")
        text_output = f"""법률사무소 더안입니다. {client_name} 님 사건의 공판기일이 지정되어 안내드립니다. 
{date_str} 공판기일({court_room} {final_time})
  
형사 사건의 공판기일에는 변호사님과 함께, 피고인 본인도 직접 출석하셔야 합니다."""

    elif sub_category == "(민사, 가사 등) 조정기일 안내":
        text_output = f"""법률사무소 더안입니다. 
{client_name} 님 사건의 조정기일이 지정되어 안내드립니다. 
{date_str} 조정기일({court_room} {final_time})

조정기일에는 변호사님이 출석하여 진행되며, 의뢰인께서 함께 참석하시면 보다 신속하고 원활한 의사결정을 할 수 있어 조정 진행에 큰 도움이 됩니다. 

부득이하게 참석이 어려우신 경우에는 당일 조정 진행을 위하여 상시 연락 가능한 상태를 유지해 주시기 바랍니다. (통상 1시간 정도 소요됩니다.)

참석 여부를 알려주시면 그에 맞춰 준비하도록 하겠습니다.
궁금하신 사항이 있으시면 언제든지 연락주시기 바랍니다."""

    elif sub_category == "기일 변경 안내 (민사, 가사 등 - 본인 출석 X)":
        text_output = f"""법률사무소 더안입니다. 
{client_name} 님 사건의 변론기일이 변경되어 안내드립니다. 
{date_str} 변론기일({court_room} {final_time})
  
변론기일에는 변호사님이 출석하시니 당사자 본인은 별도로 출석하지 않으셔도 무방합니다. 출석을 희망하시는 경우 미리 말씀해주시면 감사하겠습니다."""

    elif sub_category == "기일 변경 안내 (형사 공판기일 - 본인 출석 필수!)":
        st.error("🚨 형사 공판기일 변경입니다. 피고인 본인이 반드시 직접 출석해야 함을 안내합니다.")
        text_output = f"""법률사무소 더안입니다. 
{client_name} 님 사건의 공판기일이 변경되어 안내드립니다. 
{date_str} 공판기일({court_room} {final_time})
  
형사 사건의 공판기일에는 변호사님과 함께, 피고인 본인도 직접 출석하셔야 합니다."""

    elif sub_category == "(형사 사건) 선고기일 안내 - 피고인 출석 필요!":
        st.warning("⚠️ 형사사건 선고입니다. 피고인 본인의 직접 출석이 필요함을 명시합니다.")
        text_output = f"""법률사무소 더안입니다. 
{client_name} 님 사건의 선고기일이 지정되어 안내드립니다. 
{date_str} 선고기일({court_room} {final_time})

형사 사건의 선고기일에는 피고인 본인이 직접 출석하셔야 합니다. 선고기일에는 변론이 진행되지 않아 변호사님은 출석하지 않으니 참고해 주시기 바랍니다."""

    elif sub_category == "(형사 외 사건) 선고기일 안내 - 출석 불필요":
        text_output = f"""법률사무소 더안입니다. 
{client_name} 님 사건의 선고기일이 지정되어 안내드립니다. 
{date_str} 판결선고기일({court_room} {final_time})

선고기일에는 출석하지 않으셔도 됩니다. 선고 내용 확인 후 안내드리겠습니다."""

# -------------------------------------------------------------
# 📂 4. 재판 결과 & 선고 안내 단계
# -------------------------------------------------------------
elif category == "4. 재판 결과 & 선고 안내":
    st.subheader("📂 재판 결과 & 선고 안내")
    sub_category = st.selectbox(
        "안내 유형 선택",
        [
            "선고 결과 안내",
            "선고결과 안내(전부 승소 경우)",
            "판결문 등 열람의사 사전 확인",
            "판결문 등 전달 및 항소/이의기한 안내"
        ]
    )
    
    if sub_category == "선고 결과 안내":
        result_text = st.text_area("구두 선고 결과 내용", placeholder="예: 원고 청구 기각, 소송비용 원고 부담")
        text_output = f"""법률사무소 더안입니다. 금일 {client_name} 님 사건의 판결선고 결과를 안내드립니다.
“ {result_text} ”

※ 위 내용은 법정에서 구두 선고내용을 정리한 것으로, 일부 정확하지 않을 수 있습니다. 판결문 송달 후 정확한 내용을 전달드리겠습니다. 판결문 송달은 선고일로부터 통상 2일 내외로 소요되니 참고해 주시기 바랍니다."""

    elif sub_category == "선고결과 안내(전부 승소 경우)":
        doc_choice = st.radio("문서 종류 선택", ["판결문", "결정문"], horizontal=True)
        appeal_word = "항소" if doc_choice == "판결문" else "항고"

        text_output = f"""법률사무소 더안입니다.

{client_name} 님, {doc_choice} 전달드립니다.
이번 사건은 전부 승소로 판결되었습니다.

첨부된 {doc_choice}을 확인해 주시기 바라며,
상대방의 {appeal_word} 등 추가 진행사항이 있는 경우 별도로 안내드리겠습니다.
추가 설명이 필요하시면 언제든지 연락 주시기 바랍니다. 감사합니다."""

    elif sub_category == "판결문 등 열람의사 사전 확인":
        case_num = st.text_input("사건번호", placeholder="2026가단50000")
        doc_type = st.selectbox("송달 문서 종류", ["판결문", "조정갈음결정", "화해권고결정", "결정문"], key="check_doc_type")
        
        if doc_type in ["조정갈음결정", "화해권고결정"]:
            st.info(f"💡 안내: 송달 완료 전, 상대방의 열람 시점을 탐색하고 조율하는 단계입니다. PDF를 아직 단톡방에 송부하지 마세요.")
            limit_word = "이의신청 기한은"
            info_word = "내용을"
        elif doc_type == "결정문":
            st.error("⚠️ [직원 필독] 일반 결정문은 불복 기한이 14일이 아닐 수 있습니다(예: 즉시항고 7일 등). 반드시 재판부 명령서상의 기한을 별도로 재확인하세요!")
            limit_word = "불복 기한은"
            info_word = "내용을"
        else:
            st.info(f"💡 안내: 송달 완료 전, 상대방의 열람 시점을 탐색하고 조율하는 단계입니다. PDF를 아직 단톡방에 송부하지 마세요.")
            limit_word = "항소 기한은"
            info_word = "판결 내용을"
            
        text_output = f"""법률사무소 더안입니다.

{client_name} 님 {case_num} 사건의 {doc_type}이 발송되었습니다. {limit_word} {doc_type}을 실제로 열람한 날부터 각자 14일이 기산되므로, 열람 시점에 따라 양측의 마감일이 달라질 수 있습니다.

현재 우리 측과 상대방 모두 미확인 상태입니다. 아래 두 방안 중 원하시는 방향을 말씀해 주시면 그에 맞춰 진행하겠습니다.

1. 즉시 확인: {info_word} 즉시 파악하여 전달받길 원하시는 경우

2. 상대방 확인 후 확인: 상대방의 열람 시점 및 항소(이의) 여부를 지켜본 뒤 대응하길 원하시는 경우 (※ 단, 양측 모두 장기간 확인하지 않을 경우 법원에서 같은 시점에 송달 처리할 수 있습니다.)

의견 주시면 그에 맞춰 진행하도록 하겠습니다."""

    elif sub_category == "판결문 등 전달 및 항소/이의기한 안내":
        st.error("🚨 중요: 마감일 도과 방지 및 기한 고지가 필수인 대화입니다.")
        doc_type = st.selectbox("송달 문서 종류 선택", ["판결문", "조정갈음결정", "화해권고결정", "결정문"], key="send_doc_type")
        view_date = st.date_input("실제 문서 열람일(송달일)")
        
        limit_date = view_date + timedelta(days=14)
        notice_date = limit_date - timedelta(days=2)
        
        limit_date_str = limit_date.strftime('%Y. %m. %d.')
        notice_date_str = notice_date.strftime('%Y. %m. %d.')
        
        if doc_type in ["조정갈음결정", "화해권고결정"]:
            action_word = "결정에"
            form_word = "이의신청서를"
            limit_word = "이의신청기한은"
            intent_word = "이의신청 의사가"
        elif doc_type == "결정문":
            st.error("⚠️ [직원 필독] 일반 결정문은 불복 기한이 14일이 아닐 수 있습니다(예: 즉시항고 7일 등). 반드시 확인 후 필요시 수동 편집하세요!")
            action_word = "결정에"
            form_word = "불복(항고 등) 신청서를"
            limit_word = "불복기한은"
            intent_word = "불복 의사가"
        else:
            action_word = "판결에"
            form_word = "항소장을"
            limit_word = "항소기한은"
            intent_word = "항소 의사가"
            
        text_output = f"""법률사무소 더안입니다.

{client_name} 님, {doc_type} 열람하여 전달드립니다.
첨부된 문서를 꼭 확인해 주시기 바랍니다.

{action_word} 불복하시는 경우, {doc_type}을 받은 날로부터 14일 이내에 {form_word} 제출해야 합니다. 

{limit_word} {limit_date_str}까지입니다. 

{intent_word} 있으신 경우, 기한 2일 전인 {notice_date_str}까지 미리 알려주셔야 차질 없이 {form_word} 제출할 수 있습니다. 추가 설명이나 상담이 필요하시면 연락 주시기 바랍니다."""

# -------------------------------------------------------------
# 📂 5. 소송 종결 & 확정 단계
# -------------------------------------------------------------
elif category == "5. 소송 종결 & 확정":
    st.subheader("📂 소송 종결 & 확정 단계")
    sub_category = st.selectbox(
        "안내 유형 선택",
        ["조정조서 전달", "이혼신고 안내"]
    )
    
    if sub_category == "조정조서 전달":
        text_output = f"""안녕하세요, 법률사무소 더안입니다.

금일 법원으로부터 귀하 사건의 조정조서가 송달되어 전달드립니다.
첨부된 문서를 꼭 확인해 주시기 바랍니다.

조정조서는 송달과 함께 효력이 발생하고 양 당사자의 송달로서 확정됩니다. 
감사합니다."""

    elif sub_category == "이혼신고 안내":
        text_output = f"""법률사무소 더안입니다.
진행하신 이혼 사건이 확정, 종결되었습니다. 이혼신고를 완료하셔야 모든 절차가 마무리되오니, 아래 안내사항을 확인해 주시기 바랍니다.
  
🔹이혼신고 기한 : 재판 확정일로부터 1개월 이내
 - 원고 또는 신청인이 기한 내에 신고하지 않을 경우 5만원 이하 과태료가 부과될 수 있으며, 피고 또는 피신청인도 단독으로 이혼신고가 가능합니다.
  
🔹신고 장소 : 주소지 관할 구청, 시청 또는 읍·면사무소
  
🔹필요서류 : 판결 등본(또는 조정조서 등), 확정증명원, 신분증
  
※ 위 서류는 사무실 방문 또는 등기우편으로 수령 가능합니다. 우편 수령을 원하시는 경우 송달 가능 주소를 남겨 주시기 바랍니다. 
   
(우편 발송 후 부재 등으로 수령이 어려우신 경우 반송되어 절차가 지연될 수 있으니 유의해 주시기 바랍니다.)"""

# -------------------------------------------------------------
# 📋 출력 화면 및 클릭 복사 버튼
# -------------------------------------------------------------
st.markdown("---")
st.subheader("📋 생성된 카카오톡 안내 문구")

final_text = st.text_area("카카오톡으로 복사하여 전송할 메시지 내용", value=text_output, height=350)

escaped_text = final_text.replace("\\", "\\\\").replace("`", "\\`").replace("\n", "\\n").replace("\r", "\\r")

copy_button_html = f"""
    <button onclick="copyToClipboard()" style="
        background-color: #f44336; 
        color: white; 
        padding: 12px 24px; 
        border: none; 
        border-radius: 6px; 
        cursor: pointer; 
        font-size: 16px;
        font-weight: bold;
        width: 100%;
        margin-top: 10px;
    ">📋 단톡방 문구 복사하기 (클릭)</button>

    <script>
    function copyToClipboard() {{
        const text = `{escaped_text}`;
        
        const textarea = document.createElement("textarea");
        textarea.value = text;
        document.body.appendChild(textarea);
        textarea.select();
        
        try {{
            document.execCommand('copy');
            alert("✅ 문구가 클립보드에 성공적으로 복사되었습니다!\\n카톡방에 붙여넣기(Ctrl+V) 하세요.");
        }} catch (err) {{
            alert("❌ 복사에 실패했습니다. 문구를 드래그하여 직접 복사해 주세요.");
        }}
        
        document.body.removeChild(textarea);
    }}
    </script>
"""

st.components.v1.html(copy_button_html, height=70)

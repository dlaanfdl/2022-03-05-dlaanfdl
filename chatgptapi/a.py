import openai
import KEY

openai.api_key = KEY.API_KEY  # YOUR KEY

model = "gpt-3.5-turbo"

query = '''
키워드를 조합하여 '교과 세부능력 및 특기사항 기재'사항을 작성해줘

'교과 세부능력 및 특기사항 기재' 작성 규칙은 다음과 같다.

1. 학교생활기록부는  학생의  성장과  학습  과정을  상시 관찰･평가한  누가기록  중심의  종합 기록이어야 함.

2. 학교생활기록부에는 학교교육계획이나 학교교육과정에 따라 학교에서 실시한 각종 교육활동의 이수상황(활동내용에 따른 개별적 특성이 드러나는 사항 중심)을 기재하는 것이 원칙임.

3. 주어진 키워드를 전부 사용하여 프로젝트를 진행하였으며 이에 대한 평가가 들어가야 한다.

4. '교과 세부능력 및 특기사항 기재' 는 1~2개의 문장으로 구성된다.

5. 중요한것은 '교과 세부능력 및 특기사항 기재'는 느낀점이 들어가면 안된다.

6. '교과 세부능력 및 특기사항 기재'는 미래의 이야기가 들어가서는 안 된다.

7. '교과 세부능력 및 특기사항 기재'는 500자이내로 입력되어야 한다.

8. 프로젝트로 얻게 된 능력이 들어가야 한다.

9. 결과가 들어가야 한다.

10. 학생의 노력,목표 성취를 위한 자기주도적 학습에 의한 변화와 성장 정도를 중심으로 기재한다.

11. 제 3자의 입장에서 적어야한다.

12. 창작한 내용이 들어가서는 안된다.

13. 성적관련된 내용이 들어가서는안 된다.


예를 들어 'python', 'opencv' 키워드를 받아서 다음과 같이 작성하면 좋다.
"해당 학생은 프로그래밍 분야에서 Python과 영상처리 분야에서 OpenCV를 활용하여 프로젝트를 진행하였습니다. 이를 통해 Python과 OpenCV에 대한 기술적인 이해와 응용 능력을 갖췄으며, 문제 해결과 결과에 대한 책임감을 가지고 프로젝트를 수행할 수 있는 능
력을 보여주었습니다."

주어진 키워드는 다음과 같다.
'''

keywords = input().split('/')
str = "'"
for keyword in keywords:
    str += keyword
    str += "', "

query += str

messages = [
    {"role": "system", "content": "school teacher"},
    {"role": "user", "content": query}
]

response = openai.ChatCompletion.create(
    model=model,
    messages=messages
)
ans = response['choices'][0]['message']['content']
print(ans)


from django.shortcuts import render,redirect
# from .models import PersonalityTypes
# from django.shortcuts import render
# from .forms import PersonalityQtnForm

# # Create your views here.


def home(request):
    return render(request,'HomePage.html')


# def personalityType(request):
   
#     allTypes=PersonalityTypes.objects.all()
#     return render(request,'PersonalityTypes.html',{'alltypes':allTypes})





def AllProfiles(request):
    return render(request,'all-profiles.html')

def aboutpage(request):
    return render(request,'about.html')






def personalityTest(request):
    questions = [
         ("Do you feel more energized after spending time alone (I) or with others (E)? ", 'I', 'E'),
    ("Would you rather attend a small gathering with close friends (I) or a large party with many people (E)? ", 'I', 'E'),
    ("Do you prefer one-on-one conversations (I) or group discussions (E)? ", 'I', 'E'),
    ("Do you enjoy meeting new people and making new friends (E), or do you prefer deeper connections with a few close friends (I)? ", 'I', 'E'),
    ("Are you more reserved and quiet (I) or outgoing and talkative (E)? ", 'I', 'E'),
    ("Do you focus on the present moment and concrete details (S) or future possibilities and abstract concepts (N)? ", 'S', 'N'),
    ("Are you more practical and realistic (S) or imaginative and creative (N)? ", 'S', 'N'),
    ("Do you prefer step-by-step instructions and guidelines (S) or the freedom to explore new ways of doing things (N)? ", 'S', 'N'),
    ("Are you more likely to trust your gut instincts (N) or rely on facts and evidence (S)? ", 'S', 'N'),
    ("Do you find it easy to remember specific details and facts (S) or tend to forget them but remember the big picture (N)? ", 'S', 'N'),
    ("When making decisions, do you prioritize logic and rationality (T) or consider the impact on people's feelings and emotions (F)? ", 'T', 'F'),
    ("Are you more objective and analytical (T) or empathetic and compassionate (F)? ", 'T', 'F'),
    ("Do you value honesty and straightforwardness (T) or diplomacy and harmony (F)? ", 'T', 'F'),
    ("Are you more likely to critique and criticize (T) or encourage and support (F)? ", 'T', 'F'),
    ("Is it easier for you to remain emotionally detached (T) or emotionally invested (F)? ", 'T', 'F'),
    ("Do you prefer having a structured and organized life (J) or enjoy flexibility and adaptability (P)? ", 'J', 'P'),
    ("Are you more comfortable with planned schedules and deadlines (J) or go with the flow and adapt as things come (P)? ", 'J', 'P'),
    ("Do you like making decisions and sticking to them (J) or keeping your options open and being spontaneous (P)? ", 'J', 'P'),
    ("Are you inclined to complete tasks before relaxing (J) or leave things open-ended and enjoy the process (P)? ", 'J', 'P'),
    ("Do you tend to be more methodical and systematic (J) or improvisational and opportunistic (P)? ", 'J', 'P'),
    ]
  
    if request.method == 'POST':
        form = PersonalityQtnForm(questions, request.POST)
        if form.is_valid():
            # Process the form data here
            # You can access the user's answers using form.cleaned_data
            # Do something with the collected answers
            answers = [form.cleaned_data[f"question_{i}"] for i in range(len(questions))]
            # Further processing or saving the answers
            # Redirect or render a response
            
            #find the number of yes or no
            print(answers)
             #find corresponding personality indicators
            ans_list=map_answers_to_personality(answers)
            print(ans_list) 
            #get correct personality type
            personality_type =   calculate_personality_type(ans_list)   
            print(personality_type)         

    else:
        form = PersonalityQtnForm(questions)

    return render(request, 'adminPage.html', {'form': form, 'questions': questions})


def map_answers_to_personality(answers):
    personality_types = []
    for i in range(0, len(answers),4):
        # Mapping for I/E (example)
        if answers[i] == 'yes':
            personality_types.append('I')
        else:
            personality_types.append('E')

        # Mapping for S/N (example)
        if answers[i+1] == 'yes':
            personality_types.append('S')
        else:
            personality_types.append('N')

        # Mapping for T/F (example)
        if answers[i+2] == 'yes':
            personality_types.append('T')
        else:
            personality_types.append('F')

        # Mapping for J/P (example)
        if answers[i+3] == 'yes':
            personality_types.append('J')
        else:
            personality_types.append('P')

    return personality_types


def calculate_personality_type(answers):
            print(answers,"ddddddddddddddddddddddddddddddddd")
            personality_type =''
            # Calculate scores for each dimension\n",
            I = answers.count('I')
            E = answers.count('E')
            S = answers.count('S')
            N = answers.count('N')
            T = answers.count('T')
            F = answers.count('F')
            J = answers.count('J')
            P = answers.count('P')
            print(I)
            print(E)
            print(S)
            print(N)
            print(T)
            print(F)
            print(J)
            print(P)
        
            # Determine the first dimension (I/E)\n",
            if I > E:
                personality_type += 'I'
            else:
                personality_type += 'E'
         # Determine the second dimension (S/N)\n",
            if S > N:
                personality_type += 'S'
            else:
                personality_type += 'N'
        
            # Determine the third dimension (T/F)\n",
            if T > F:
                personality_type += 'T'
            else:
                personality_type += 'F'
  
            # Determine the fourth dimension (J/P)\n",
            if J > P:
                personality_type += 'J'
            else:
                personality_type += 'P'
    
            # Define personality type based on the four dimensions\n",
            personality_types = {
                'ISTJ': 'ISTJ--The Inspector',
                'ISFJ': 'ISFJ--The Protector',
                'INFJ': 'INFJ--The Counselor',
                'INTJ': 'INTJ--The Mastermind',
                'ISTP': 'ISTP--The Craftsman',
                'ISFP': 'ISFP--The Composer',
                'INFP': 'INFP--The Healer',
                'INTP': 'INTP--The Architect',
                'ESTP': 'ESTP--The Dynamo',
                'ESFP': 'ESFP--The Performer',
                'ENFP': 'ENFP--The Champion',
                'ENTP': 'ENTP--The Visionary',
                'ESTJ': 'ESTJ--The Supervisor',
                'ESFJ': 'ESFJ--The Provider',
               'ENFJ': 'ENFJ--The Teacher',
                'ENTJ': 'ENTJ--The Commander',
            
            }
            return personality_types.get(personality_type)
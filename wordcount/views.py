from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    full_text = request.GET['fulltext']
    word_list = full_text.split() #문자열을 공백을 기준으로 분리한 후, 리스트로 저장하는 함수
    word_dict = {}
    
    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    sorted_dict = sorted(word_dict.items(), key=lambda t : t[1], reverse=True)

    return render(request, 'count.html', {'fulltext' : full_text, 'total' : len(word_list), 'dictionary' : sorted_dict})


from django.shortcuts import render
from django.http import HttpResponse
import dill

ifile = open("./savedModels/knn_model.dill", "rb")
model = dill.load(ifile)
ifile.close()
files_names = ['KNeighborsClassifier_v1.dill','MultinomialNB_v1.dill','RandomForestClassifier_v1.dill','SVC_v1.dill']
models = list()
for file in files_names:
    ifile = open(f'./savedModels/{file}', "rb")
    model = dill.load(ifile)
    models.append(model)
    ifile.close()


def index(request):
    mail = request.POST.get('mail', "")
    result = ""
    if(mail):
        result = model.msg_predict(mail)[0]
    return render(request, 'Index.html', {'result': result, 'mail': mail})

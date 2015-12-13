from django.shortcuts import render

# Create your views here.


# def home(request):
#     """
#     Evaluation of tweets
#     :param request:
#     :return:
#     """
    #config_train, train = home.models.Configuration.objects.get_or_create(name=common.TRAIN_CONFIG_NAME)
    #if request.method == 'POST':
    #    evaluation_form = EvaluationForm(request.POST)
    #    if evaluation_form.is_valid():
    #        evaluation_form.save()
    #        min_next_eval_tweet_id = get_next_tweet_to_evaluate()
    #        evaluation_form = EvaluationForm(initial={'tweet': min_next_eval_tweet_id})
    #    else:
    #        pass
    #else:
    #    evaluation_form = None
    #    if not config_train.enable:
    #        min_next_eval_tweet_id = get_next_tweet_to_evaluate()
    #        evaluation_form = EvaluationForm(initial={'tweet': min_next_eval_tweet_id})

    #data_dictionary = {
    #    "config_train_enable" : config_train.enable,
    #    'evaluation_form': evaluation_form
    #}

    # return render(request, 'polls/home.html', data_dictionary)

def home(request):
    data_dictionary = {
        'data' : None,
    }
    return render(request, 'polls/twitter_home.html', data_dictionary)

def about(request):
    return render(request, 'polls/twitter_about.html', {})


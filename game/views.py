from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

def show_game_sjm(request):

     return render_to_response('game/game_sjm.html')

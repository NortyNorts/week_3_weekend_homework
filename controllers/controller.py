from crypt import methods
from unittest import result
from flask import render_template, request, redirect
from app import app
from models.player import *
from models.game import *

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/game')
def game():
    return render_template('index.html', title=game,)

@app.route('/game', methods=['Post'])
def game_result():
    player1=request.form['player1']
    player2=request.form['player2']
    game = Game()
    game.play_new_game(player1,player2)
    result = game.winner
    
    
    return render_template('index.html', result=result)
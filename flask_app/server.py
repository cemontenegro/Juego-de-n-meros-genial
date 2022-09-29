from flask import Flask, render_template, redirect, session, request
import random


app = Flask(__name__)
app.secret_key = "secreto"

@app.route('/')
def elegir():
	if not 'numero_aleatorio' in session:
		session['numero_aleatorio'] = random.randint(1, 100)
	print(session['numero_aleatorio'], "/*?"*20)
	return render_template("adivinar.html")

@app.route('/adivina', methods=['POST'])
def adivina():
	if session ['numero_aleatorio'] > int(request.form['numero_integrado_por_usuario']):
		print ("Demasiado bajo!")
		return render_template ("bajo.html")
	elif session ['numero_aleatorio'] < int(request.form['numero_integrado_por_usuario']):
		print ("Demasiado alto!")
		return render_template ("alto.html")
	else:
		print ("Adivinaste! Juega otra vez")
		session.clear()
		return render_template ("adivinaste.html")

	return redirect('/')


if __name__ == "__main__":
	app.run(debug=True)
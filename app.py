from flask import Flask, url_for, render_template, redirect, request, session, flash
import mysql.connector
from flask_wtf import CSRFProtect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from config import config

app = Flask(__name__)
app.config.from_object(config['development'])

# LINKS


def links():

    programs = [
        ('Administración de Empresas', url_for(
            'administracion'), 'class="fa-solid fa-briefcase"'),
        ('Computación e Informática', url_for(
            'computacion'), 'class="fa-solid fa-computer"'),
        ('Contabilidad', url_for('contabilidad'), 'class="fa-solid fa-calculator"'),
        ('Electrónica', url_for('electronica'),
         'class="fa-solid fa-network-wired"'),
        ('Electrotecnia', url_for('electrotecnia'), 'class="fa-solid fa-lightbulb"'),
        ('Laboratorio', url_for('laboratorio'), 'class="fa-solid fa-flask"'),
        ('Mecánica Automotriz', url_for(
            'mecanicaAutomotriz'), 'class="fa-solid fa-car"'),
        ('Mecánica de Producción', url_for(
            'mecanicaProduccion'), 'class="fa-solid fa-industry"'),
        ('Metalurgia', url_for('metalurgia'), 'class="fa-solid fa-screwdriver-wrench"')]

    admission = [
        ('Examen De Admisión', url_for('admision'),
         'class="fa-solid fa-pen-to-square"'),
        ('Pre Cueto', url_for('preCueto'), 'class="fa-solid fa-graduation-cap"')]

    institutional = [
        ('Secretaría Académica', url_for('secretariaAcademica'),
         'class="fa-solid fa-address-book"'),
        ('Mesa De Partes', url_for('mesaDePartes'),
         'class="fa-solid fa-folder-open"'),
        ('Tesorería', url_for('tesoreria'),
         'class="fa-solid fa-hand-holding-dollar"'),
        ('Nosotros', url_for('nosotros'), 'class="fa-solid fa-users"'),
        ('Documentos', url_for('documentos'), 'class="fa-solid fa-file"')]

    data = {
        'programs': programs,
        'admission': admission,
        'institutional': institutional
    }
    return data

# ROUTE MAIN


@app.route('/')
def main():
    return render_template('/CarlosCueto/index.html', data=links())


@app.route('/administracion')
def administracion():
    return render_template('/CarlosCueto/administracion.html', data=links())


@app.route('/computacion')
def computacion():
    return render_template('/CarlosCueto/computacion.html', data=links())


@app.route('/contabilidad')
def contabilidad():
    return render_template('/CarlosCueto/contabilidad.html', data=links())


@app.route('/electronica')
def electronica():
    return render_template('/CarlosCueto/electronica.html', data=links())


@app.route('/electrotecnia')
def electrotecnia():
    return render_template('/CarlosCueto/electrotecnia.html', data=links())


@app.route('/laboratorio')
def laboratorio():
    return render_template('/CarlosCueto/laboratorio.html', data=links())


@app.route('/mecanica-Automotriz')
def mecanicaAutomotriz():
    return render_template('/CarlosCueto/mecanicaAutomotriz.html', data=links())


@app.route('/mecanica-Produccion')
def mecanicaProduccion():
    return render_template('/CarlosCueto/mecanicaProduccion.html', data=links())


@app.route('/metalurgia')
def metalurgia():
    return render_template('/CarlosCueto/metalurgia.html', data=links())


@app.route('/admision')
def admision():
    return render_template('/CarlosCueto/admision.html', data=links())


@app.route('/preCueto')
def preCueto():
    return render_template('/CarlosCueto/preCueto.html', data=links())


@app.route('/secretaria-Academica')
def secretariaAcademica():
    return render_template('/CarlosCueto/secretariaAcademica.html', data=links())


@app.route('/mesa-De-Partes')
def mesaDePartes():
    return render_template('/CarlosCueto/mesaDePartes.html', data=links())


@app.route('/tesoreria')
def tesoreria():
    return render_template('/CarlosCueto/tesoreria.html', data=links())


@app.route('/nosotros')
def nosotros():
    return render_template('/CarlosCueto/nosotros.html', data=links())


@app.route('/documentos')
def documentos():
    return render_template('/CarlosCueto/documentos.html', data=links())


# ! ROUTES INTRANET
# Configuración de la conexión a la base de datos
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="estudiantes"
)


@app.route('/login', methods=["GET", "POST"])
def login_page():
    form = UserForm()  # Crear una instancia del formulario

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        cursor = db.cursor()
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        user = cursor.fetchone()

        if user:
            session['user_info'] = {
                'name': user[1],
                'user_id': user[2],
                'username': user[3]
            }
            return redirect(url_for('intranet'))

    return render_template('/CuetoIntranet/login.html', form=form)


@app.route('/intranet')
def intranet():
    if 'user_info' in session:
        user_info = session['user_info']
        return render_template('/CuetoIntranet/index.html', name=user_info['name'])
    else:
        return "Acceso no autorizado"


class UserForm(FlaskForm):
    name = StringField('Nombre')
    username = StringField('Nombre de usuario')
    password = PasswordField('Contraseña')
    submit = SubmitField('Agregar Usuario')


@app.route('/admin/users', methods=["GET", "POST"])
def admin_users():
    form = UserForm()

    if form.validate_on_submit():
        name = form.name.data
        username = form.username.data
        password = form.password.data

        cursor = db.cursor()
        # Consulta si ya existe un usuario con el mismo nombre de usuario
        query = "SELECT * FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            # Mostrar mensaje de error o realizar alguna acción en caso de duplicado
            flash('El usuario ya existe', 'error')
        else:
            # Insertar el nuevo usuario si no existe duplicado
            insert_query = "INSERT INTO users (name, username, password) VALUES (%s,%s, %s)"
            cursor.execute(insert_query, (name, username, password))
            db.commit()
            flash('Usuario agregado exitosamente', 'success')

    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    return render_template('/CuetoIntranet/admin_users.html', users=users, form=form)


@app.route('/admin/users/delete/<int:user_id>', methods=["POST", "GET"])
def admin_delete_user(user_id):
    if request.method == "POST":
        cursor = db.cursor()
        query = "DELETE FROM users WHERE id = %s"
        cursor.execute(query, (user_id,))
        db.commit()

        return redirect(url_for('admin_users'))

    return redirect(url_for('admin_users'))


@app.route('/logout')
def logout():
    # Eliminar información de la sesión
    session.clear()
    # Redirigir a la página de inicio de sesión (o a otra página)
    return redirect(url_for('login_page'))


csrf = CSRFProtect(app)


if __name__ == '__main__':
    with app.app_context():
        app.run()

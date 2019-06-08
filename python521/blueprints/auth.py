
import flask
import ldap3

blueprint = flask.Blueprint('auth', __name__)

@blueprint.route('/sign-in', methods=[ 'GET', 'POST' ])
def get_sign_in():    

    if flask.request.method == 'POST':
        server = ldap3.Server('ldap://127.0.0.1:389')
        connection = ldap3.Connection(
            server,
            'cn=admin,dc=dexter,dc=com,dc=br',
            '4linux'
        )
        try:
            connection.bind()
        except:
            flask.flash('Sem conexão como LDAP', 'danger')
            return flask.redirect('/sign-in')

        email = flask.request.form['email']
        password = flask.request.form['password']

        connection.search(
            'uid={},dc=dexter,dc=com,dc=br'.format(email), 
            '(objectClass=person)', 
            attributes=['userPassword',]
        )
        try:
            saved_password = connection.entries[0].\
                userPassword.value.decode()

            if saved_password == password:
                flask.flash('Seja Bem-vindo', 'success')
                return flask.redirect('/')

            raise Exception('')
        except:
            flask.flash('Usuário não encontrado no LDAP', 'danger')

    context = {
        'page': 'sign-in',
        'route': {
            'is_public': True
        },
    }

    return flask.render_template('sign-in.html', context=context)


@blueprint.route('/sign-up', methods=[ 'GET', 'POST' ])
def get_sign_up():    

    if flask.request.method == 'POST':
        server = ldap3.Server('ldap://127.0.0.1:389')
        connection = ldap3.Connection(
            server,
            'cn=admin,dc=dexter,dc=com,dc=br',
            '4linux'
        )
        try:
            connection.bind()
        except:
            flask.flash('Sem conexão como LDAP', 'danger')
            return flask.redirect('/sign-up')
        
        first_name = flask.request.form['first_name']
        last_name = flask.request.form['last_name']
        email = flask.request.form['email']
        password = flask.request.form['password']
        object_class = [
            'top',
            'person',
            'organizationalPerson',
            'inetOrgPerson'
        ]
        user = {
            'cn': first_name,
            'sn': last_name,
            'mail': email,
            'uid': email,
            'userPassword': password
        }
        cn = 'uid={},dc=dexter,dc=com,dc=br'.format(email)
        if connection.add(cn, object_class, user):
            flask.flash('Usuário Cadastrado com sucesso', 'success')
            return flask.redirect('/sign-in')
                    
        flask.flash('Erro ao cadastrar usuário', 'danger')

    context = {
        'page': 'sign-up',
        'route': {
            'is_public': True
        },
    }

    return flask.render_template('sign-up.html', context=context)


@blueprint.route('/sign-in', methods=[ 'POST' ])
def post_sign_in():
    return ''

@blueprint.route('/sign-out', methods=[ 'POST' ])
def post_sign_out():
    return ''
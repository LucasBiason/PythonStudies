
import flask

blueprint = flask.Blueprint('auth', __name__)

@blueprint.route('/sign-in', methods=[ 'GET' ])
def get_sign_in():    

    context = {
        'page': 'sign-in',
        'route': {
            'is_public': True
        },
    }

    return flask.render_template('sign-in.html', context=context)


@blueprint.route('/sign-up', methods=[ 'GET', 'POST' ])
def get_sign_up():    

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
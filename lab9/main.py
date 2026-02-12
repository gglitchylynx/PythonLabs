from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask('Work Experience Tracker')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class WorkPlace(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(300), nullable=False)
    term = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f'WorkPlace: {self.company} - {self.term} мес.'


@app.route('/')
def main():
    workplaces = WorkPlace.query.all()
    total_term = sum(work.term for work in workplaces)
    return render_template('index.html', workplaces=workplaces, total_term=total_term)


@app.route('/add', methods=['POST'])
def add_workplace():
    try:
        data = request.json
        workplace = WorkPlace(
            company=data['company'],
            term=int(data['term'])
        )
        db.session.add(workplace)
        db.session.commit()
        
        workplaces = WorkPlace.query.all()
        total_term = sum(work.term for work in workplaces)
        
        return jsonify({
            'success': True,
            'total_term': total_term,
            'workplaces': [{'id': w.id, 'company': w.company, 'term': w.term} for w in workplaces]
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400


@app.route('/clear', methods=['DELETE'])
def clear_all():
    try:
        WorkPlace.query.delete()
        db.session.commit()
        return jsonify({'success': True, 'total_term': 0})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
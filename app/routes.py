from flask import Blueprint, jsonify, request
from app.models import Task
from app.extensions import db
import logging

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/tasks', methods=['GET'])
def get_tasks():
    try:
        tasks = Task.query.all()
        return jsonify([task.as_dict() for task in tasks])
    except Exception as e:
        logging.error(f"Error retrieving tasks: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500

@api_blueprint.route('/tasks', methods=['POST'])
def create_task():
    try:
        data = request.get_json()
        new_task = Task(title=data['title'], description=data.get('description'))
        db.session.add(new_task)
        db.session.commit()
        return jsonify(new_task.as_dict()), 201
    except Exception as e:
        logging.error(f"Error creating task: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500

@api_blueprint.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    try:
        data = request.get_json()
        task = Task.query.get_or_404(id)
        task.title = data['title']
        task.description = data.get('description', task.description)
        task.done = data.get('done', task.done)
        db.session.commit()
        return jsonify(task.as_dict())
    except Exception as e:
        logging.error(f"Error updating task {id}: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500

@api_blueprint.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    try:
        task = Task.query.get_or_404(id)
        db.session.delete(task)
        db.session.commit()
        return '', 204
    except Exception as e:
        logging.error(f"Error deleting task {id}: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500

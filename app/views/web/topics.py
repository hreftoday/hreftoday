# -*- coding: utf-8 -*-

from flask import url_for, redirect, render_template
from flask_login import current_user
from app.utils.forms import form_required, populate_obj
from app.models import Topic
from app.forms import TopicForm
from .core import bp

@bp.route('/topics', defaults={'page': 1})
def get_topics(page):
    pagination = Topic.query.filter_by(user_id=current_user.id).paginate(page)
    return render_template('web/topic/list.html', pagination=pagination)

@bp.route('/topics/add')
def add_topic_page():
    return render_template('web/topic/add.html', form=TopicForm())

@bp.route('/topics/add', methods=['POST'])
@form_required(TopicForm)
def add_topic():
    topic = Topic(user_id=current_user.id)
    return _save_topic(topic)

@bp.route('/topics/<int:id>/update')
def update_topic_page(id):
    topic = Topic.query.get_or_404(id)
    return render_template('web/topic/update.html', topic=topic, form=TopicForm(obj=topic))

@bp.route('/topics/<int:id>/update', methods=['POST'])
@form_required(TopicForm)
def update_topic(id):
    topic = Topic.query.get_or_404(id)
    return _save_topic(topic)

def _save_topic(topic):
    populate_obj(topic)
    return redirect(url_for('web.get_topic_issues', id=topic.id))
from datetime import datetime
from app import db


class Task(db.Model):
      __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, default='')
    status = db.Column(db.String(20), default='pending')
    priority = db.Column(db.String(10), default='medium')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
              return {
                            'id': self.id,
                            'title': self.title,
                            'description': self.description,
                            'status': self.status,
                            'priority': self.priority,
                            'user_id': self.user_id,
                            'created_at': self.created_at.isoformat(),
                            'updated_at': self.updated_at.isoformat(),
              }

    def __repr__(self):
              return f'<Task {self.title}>'

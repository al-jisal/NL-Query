from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from datetime import datetime


class Student(db.Model):
    __tablename__ = 'student'
    student_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    initial = db.Column(db.String(3), nullable=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(30), nullable=False)
    mentor = db.Column(db.Integer, db.ForeignKey("alum.alum_id"), nullable=True)

    def set_password(self, password):
        """Create hashed password and store it in the database"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check password_hash with the password provided by the user"""
        return check_password_hash(self.password_hash, password)
    
    def check_username(self, username):
        """Check username with the username provided by the user"""
        return self.username == username
    
    def set_username(self, username):
        """Set username to a new value"""
        self.username = username

    def set_mentor(self, mentor):
        """Set mentor to a new value"""
        self.mentor = mentor

    def get_mentor(self):
        """Returns the mentor of the student"""
        return self.mentor
    
    def get_id(self):
        return self.student_id


class Alum(db.Model):
    __tablename__ = 'alum'
    alum_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    initial = db.Column(db.String(3), nullable=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(30), nullable=False)

    def set_password(self, password):
        """Create hashed password and store it in the database"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check password_hash with the password provided by the user"""
        return check_password_hash(self.password_hash, password)
    
    def check_username(self, username):
        """Check username with the username provided by the user"""
        return self.username == username
    
    def set_username(self, username):
        """Set username to a new value"""
        self.username = username

    def get_id(self):
        return self.alum_id
    


# class Post(db.Model):
#     __tablename__ = 'posts'

#     post_id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     content = db.Column(db.Text, nullable=False)
#     timestamp = db.Column(db.DateTime, default=datetime.utcnow)

#     image_data = db.Column(db.LargeBinary, nullable=True)
#     image_content_type = db.Column(db.String(50), nullable=True)
#     video_data = db.Column(db.LargeBinary, nullable=True)
#     video_content_type = db.Column(db.String(50), nullable=True)

#     event_name = db.Column(db.String(100), nullable=True)
#     event_date = db.Column(db.Date, nullable=True)
#     event_description = db.Column(db.Text, nullable=True)
    
#     user_id = db.Column(db.Integer, db.ForeignKey('alum.alum_id'), nullable=False)
#     author = db.relationship('Alum', backref='posts', lazy=True)

#     def __repr__(self):
#         return f"<Post {self.title}>"
    
    
# class Project(db.Model):
#     __tablename__ = 'projects'
    
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     subtitle = db.Column(db.String(200))
#     description = db.Column(db.Text)
#     start_date = db.Column(db.Date, nullable=False)
#     end_date = db.Column(db.Date)
#     is_current = db.Column(db.Boolean, default=False)
    
#     # Foreign keys
#     student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'))
#     alum_id = db.Column(db.Integer, db.ForeignKey('alum.alum_id'))
    
#     # For student or alum
#     student = db.relationship('Student', backref=db.backref('projects', lazy=True))
#     alum = db.relationship('Alum', backref=db.backref('projects', lazy=True))
    
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)
#     updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


# class Experience(db.Model):
#     __tablename__ = 'experiences'
    
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     subtitle = db.Column(db.String(200))  # Company/Organization name
#     description = db.Column(db.Text)
#     start_date = db.Column(db.Date, nullable=False)
#     end_date = db.Column(db.Date)
#     is_current = db.Column(db.Boolean, default=False)
    
#     # Foreign keys
#     student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'))
#     alum_id = db.Column(db.Integer, db.ForeignKey('alum.alum_id'))
    
#     # For student or alum
#     student = db.relationship('Student', backref=db.backref('experiences', lazy=True))
#     alum = db.relationship('Alum', backref=db.backref('experiences', lazy=True))
    
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)
#     updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


# class Achievement(db.Model):
#     __tablename__ = 'achievements'
    
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     subtitle = db.Column(db.String(200))
#     description = db.Column(db.Text)
#     start_date = db.Column(db.Date, nullable=False)
#     end_date = db.Column(db.Date)
#     is_current = db.Column(db.Boolean, default=False)
    
#     student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'))
#     alum_id = db.Column(db.Integer, db.ForeignKey('alum.alum_id'))
    
#     # Relationship to either student or alum
#     student = db.relationship('Student', backref=db.backref('achievements', lazy=True))
#     alum = db.relationship('Alum', backref=db.backref('achievements', lazy=True))
    
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)
#     updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


# class Connection(db.Model):
#     __tablename__ = 'connections'
    
#     id = db.Column(db.Integer, primary_key=True)
#     # The user who initiated the connection
#     initiator_student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'))
#     initiator_alum_id = db.Column(db.Integer, db.ForeignKey('alum.alum_id'))
#     # The user who received/accepted the connection
#     receiver_student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'))
#     receiver_alum_id = db.Column(db.Integer, db.ForeignKey('alum.alum_id'))
    
#     status = db.Column(db.String(20), default='pending')  # pending, accepted, rejected
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)
#     updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
#     initiator_student = db.relationship('Student', foreign_keys=[initiator_student_id],
#                                       backref=db.backref('initiated_connections', lazy=True))
#     initiator_alum = db.relationship('Alum', foreign_keys=[initiator_alum_id],
#                                    backref=db.backref('initiated_connections', lazy=True))
#     receiver_student = db.relationship('Student', foreign_keys=[receiver_student_id],
#                                      backref=db.backref('received_connections', lazy=True))
#     receiver_alum = db.relationship('Alum', foreign_keys=[receiver_alum_id],
#                                   backref=db.backref('received_connections', lazy=True))
    
    
#     @staticmethod
#     def are_connected(user1, user2):
#         """Check if two users are connected"""
#         if isinstance(user1, Student):
#             user1_type = 'student'
#             user1_id = user1.student_id
#         else:
#             user1_type = 'alum'
#             user1_id = user1.alum_id
            
#         if isinstance(user2, Student):
#             user2_type = 'student'
#             user2_id = user2.student_id
#         else:
#             user2_type = 'alum'
#             user2_id = user2.alum_id
            
#         connection = Connection.query.filter(
#             (
#                 (Connection.initiator_student_id == user1_id if user1_type == 'student' else Connection.initiator_alum_id == user1_id) &
#                 (Connection.receiver_student_id == user2_id if user2_type == 'student' else Connection.receiver_alum_id == user2_id)
#             ) |
#             (
#                 (Connection.initiator_student_id == user2_id if user2_type == 'student' else Connection.initiator_alum_id == user2_id) &
#                 (Connection.receiver_student_id == user1_id if user1_type == 'student' else Connection.receiver_alum_id == user1_id)
#             )
#         ).filter_by(status='accepted').first()
        
#         return connection is not None

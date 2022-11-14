from app import db

class Manager(db.Model):
    __tablename__ = 'manager'

    manager_id = db.Column(db.Integer, primary_key=True)
    manager_name = db.Column(db.VARCHAR(length=50))


class Team(db.Model):
    __tablename__ = 'team'

    team_id = db.Column(db.Integer, primary_key=True)
    venue_id = db.Column(db.Integer)
    team_name = db.Column(db.VARCHAR(length=50))


class ManagerTeam(db.Model):
    __tablename__ = 'managerteam'
    
    contract_id = db.Column(db.Integer, primary_key=True)
    manager_id = db.Column('Manager', db.ForeignKey('manager.manager_id'))
    team_id = db.Column('Team', db.ForeignKey('team.team_id'))
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=True)
    
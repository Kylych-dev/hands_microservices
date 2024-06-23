from main import app, db
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()




'''
rabbit mq 

amqps://kxxkwlpk:5rd83BkFV2ln5F7gXCVVsCG927DZ41TN@puffin.rmq2.cloudamqp.com/kxxkwlpk

'''
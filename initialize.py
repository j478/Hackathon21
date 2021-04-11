from app import db, providers, drugsInStock, drugsPerscribed
from random import randint

def createProviders():
	db.drop_all()
	db.create_all()
	provider1 = providers(username="compName1", password="compPass1", compName="fizzer", salesRep="Tommy John", isAdmin=False)
	db.session.add(provider1)
	provider2 = providers(username="compName2", password="compPass2", compName="astrozinika", salesRep="Johnny Tom", isAdmin=False)
	db.session.add(provider2)
	provider3 = providers(username="compName3", password="compPass3", compName="modurna", salesRep="Timmy Jim", isAdmin=False)
	db.session.add(provider3)
	Admin = providers(username="HospitalAdmin", password="admin", compName="So&So Hospital", salesRep="N/A", isAdmin=True)
	db.session.add(Admin)
	db.session.commit()

def createDrugs():
	Sdrug1 = drugsInStock(name="adalimumab", stock=randint(0,20))
	db.session.add(Sdrug1)
	Pdrug1 = drugsPerscribed(name="adalimumab", numGiven=randint(0,20))
	db.session.add(Pdrug1)
	Sdrug2 = drugsInStock(name="apixaban", stock=randint(0,20))
	db.session.add(Sdrug2)
	Pdrug2 = drugsPerscribed(name="apixaban", numGiven=randint(0,20))
	db.session.add(Pdrug2)
	Sdrug3 = drugsInStock(name="lenalidomide", stock=randint(0,20))
	db.session.add(Sdrug3)
	Pdrug3 = drugsPerscribed(name="lenalidomide", numGiven=randint(0,20))
	db.session.add(Pdrug3)
	Sdrug4 = drugsInStock(name="nivolumab", stock=randint(0,20))
	db.session.add(Sdrug4)
	Pdrug4 = drugsPerscribed(name="nivolumab", numGiven=randint(0,20))
	db.session.add(Pdrug4)
	Sdrug5 = drugsInStock(name="pembrolizumab", stock=randint(0,20))
	db.session.add(Sdrug5)
	Pdrug5 = drugsPerscribed(name="pembrolizumab", numGiven=randint(0,20))
	db.session.add(Pdrug5)
	Sdrug6 = drugsInStock(name="etanercept", stock=randint(0,20))
	db.session.add(Sdrug6)
	Pdrug6 = drugsPerscribed(name="etanercept", numGiven=randint(0,20))
	db.session.add(Pdrug6)
	Sdrug7 = drugsInStock(name="trastuzumab", stock=randint(0,20))
	db.session.add(Sdrug7)
	Pdrug7 = drugsPerscribed(name="trastuzumab", numGiven=randint(0,20))
	db.session.add(Pdrug7)
	Sdrug8 = drugsInStock(name="rituximab", stock=randint(0,20))
	db.session.add(Sdrug8)
	Pdrug8 = drugsPerscribed(name="rituximab", numGiven=randint(0,20))
	db.session.add(Pdrug8)
	Sdrug9 = drugsInStock(name="rivaroxaban", stock=randint(0,20))
	db.session.add(Sdrug9)
	Pdrug9 = drugsPerscribed(name="rivaroxaban", numGiven=randint(0,20))
	db.session.add(Pdrug9)
	Sdrug10 = drugsInStock(name="aflibercept", stock=randint(0,20))
	db.session.add(Sdrug10)
	Pdrug10 = drugsPerscribed(name="aflibercept", numGiven=randint(0,20))
	db.session.add(Pdrug10)
	db.session.commit()


	
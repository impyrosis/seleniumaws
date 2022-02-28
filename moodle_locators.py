from faker import Faker

fake = Faker(locale='en_CA')

#-----------Locaters Section-------------------------------
#----------------------------------------------------------

app = 'Moodle'
moodle_url = 'http://52.39.5.126/'
moodle_home_page_title = 'Software Quality Assurance Testing'
moodle_login_page_url = 'http://52.39.5.126/login/index.php'
moodle_login_page_title = 'Software Quality Assurance Testing: Log in to the site'
moodle_dashborad_url = 'http://52.39.5.126/my/'
moodle_dashboard_page_title = 'Dashboard'
admin_username = 'raogohar'
admin_password = '@Moodle123'
add_new_user_page_title = 'SQA: Administration: Users: Accounts: Add a new user'
browse_list_of_users_title = 'SQA: Administration: Users: Accounts: Browse list of users'
moodle_users_main_page = 'http://52.39.5.126/admin/user.php'
moodle_users_main_page_title = 'SQA: Administration: Users: Accounts: Browse list of users'

#----------------------------------------------------------


#------------------------------------------------------------------------------------
# fake data section


first_name = fake.first_name()
last_name = fake.last_name()
middle_name = fake.first_name()
full_name = first_name + " " + last_name
new_username = f'{first_name}{last_name}'.lower()
new_password = fake.password()
email = f'{new_username}@{fake.free_email_domain()}'
moodle_net_profile = f'https://moodle.net/{new_username}'
city = fake.city()
#alternate_name = fake.first_name()
country = fake.current_country()
description = fake.sentence(5)
list_of_interest = [fake.job(),fake.job(),fake.job(),fake.job(),fake.job()]
#description = f'user added ny {admin_userename} via python-selenium automated script'
pic_desc = f'pic submitted by {full_name}'
web_page = fake.url()
icq_number = fake.pyint(111111,999999)
skype_id = new_username
aim_id = f'{last_name.lower()} {fake.pyint(111,999)}'
yahoo_id = new_username
msn_id = f'{last_name.lower()}{fake.pyint(111,999)}{city}'
id_number = fake.pyint(1111111,9999899)
institution = fake.company()
department = fake.catch_phrase()
phone = fake.phone_number()
mobile_phone = fake.phone_number()
address = fake.address().replace("\n"," ")

list_opt = ['Web page', 'ICQ number', 'Skype ID', 'AIM ID', 'Yahoo ID', 'MSN ID','ID number', 'Institution', 'Department','Phone', 'Mobile phone', 'Address']
list_ids = ['id_url', 'id_icq', 'id_skype', 'id_aim','id_yahoo','id_msn', 'id_idnumber', 'id_institution','id_department','id_phone1', 'id_phone2', 'id_address' ]
list_val = [web_page,icq_number, skype_id, aim_id,yahoo_id,msn_id,id_number,institution,department,phone,mobile_phone,address]

print(list_val)

print(first_name,last_name,middle_name,new_username,new_password,email)


#------------------------------------------------------------------------------------

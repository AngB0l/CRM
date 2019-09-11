from django.shortcuts import render

companies = [
    {
        'company': 'kallimarmaro',
        'field': 'Marble',
        'remarks': 'Excellent',
        'address': '7o xlm thessalonikis thermis',
        'area': 'thermi',
        'city': 'thessaloniki',
        'epitheto': 'bolaris',
        'onoma': 'markos',
        'stathero': '2310461611',
        'kinito': '6973203410',
        'email': 'info@kallimarmaro.gr',
        'website': 'www.kallimarmaro.gr',
        'qowners': 'yes',
        'todo': 'send samples',
    },
    {
            'company': 'sachanas',
            'field': 'Marble',
            'remarks': 'have thassos blocks',
            'address': 'kalohori',
            'area': 'ditika',
            'city': 'thessaloniki',
            'epitheto': 'sachanas',
            'onoma': 'ilias',
            'stathero': '2310111611',
            'kinito': '6974630351',
            'email': 'info@ms.gr',
            'website': 'www.sachanas.gr',
            'qowners': 'no',
            'todo': 'visit factory',
        },
]
contacts = [
    {
        'date' : '11/7/2019',
        'user' : 'chrys',
        'company': 'sachanas',
        'project' : 'general',
        'comment' : 'zitisan prosfora gia 10000m2 thasou gia ergo sti ksanthi',
    },
    {
        'date': '18/8/2019',
        'user': 'chrys',
        'company': 'sachanas',
        'project': 'general',
        'comment': 'zitisan prosfora gia 10000m2 thasou gia ergo sti kavala',
    },
    {
        'date': '19/9/2019',
        'user': 'chrys',
        'company': 'petra',
        'project': 'general',
        'comment': 'piga apo to latomeio gia na doume ogkous',
    },
]
persons = [
    {
        'lname':'bolaris',
        'fname':'markos' ,
        'company':'kallimarmaro',
        'possition':'CEO',
        'mphone' : '6973203401',
    },
    {
        'lname': 'sachanas',
        'fname': 'ilias',
        'company': 'sachanas Marble',
        'possition': 'CEO',
        'mphone' : '6952207806',
    },
    {
        'lname': 'bolari',
        'fname': 'chrysavgi',
        'company': 'kallimarmaro',
        'possition': 'sales',
        'mphone' : '6973203409',
    },

]

def home(request):
    return render(request, 'crm/home.html')

def company(request):
    context = {
        'companies' : companies
    }
    return render(request, 'crm/company.html', context)

def quarry(request):
    return render(request, 'crm/quarry.html')

def contact(request):
    context = {
        'contacts': contacts
    }
    return  render(request, 'crm/contact.html', context)

def person(request):
    context = {
        'persons' : persons
    }
    return  render(request, 'crm/person.html', context)
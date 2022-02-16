from django.shortcuts import render
from .models import  Product

def index(request):
   
    product = Product.objects.all()
    product_no = Product.objects.all().count()     
    mylist = []
    context = {
        'products':product,
        'product_no':product_no,
        'mylist':mylist
    }

    return render(request, "addeditems.html", context)

def cal_amount(request):
    amount = 0.0
    count_of_items = {}
    products = Product.objects.all()
    result = {'CH1':[],'AP1':[],"CF1":[],"MK1":[],"OM1":[]}
    #retrieving the data stored in Product table
    for p in products:
        id = p.product_id
        q = request.POST.get('q_id_' + str(id))
        count_of_items[p.product_id] = q
        if q is not None and q != '' and int(q):
            q = int(q)
            amount += (float)(q * (p.product_price))
            result[p.product_id].append(p.product_name)
            result[p.product_id].append(q)
            result[p.product_id].append(range(q))
            result[p.product_id].append(p.product_price)
    apple_flag = 0
    discount ={}
    discount = {'BOGO': [], 'APPL':[], 'CHMK':[],'APOM':[]}
    #storing the counts in variable for easy calculations
    coffee = 0 if count_of_items['CF1']=="" else (int)(count_of_items['CF1'])
    apples = 0 if count_of_items['AP1']=="" else(int)(count_of_items['AP1'])
    milk = 0 if count_of_items['MK1']=="" else(int)(count_of_items['MK1'])
    chai = 0 if count_of_items['CH1']=="" else(int)(count_of_items['CH1'])
    oatmeal = 0 if count_of_items['OM1']=="" else(int)(count_of_items['OM1'])
    #BOGO discount
    if coffee>1:
        l1 = [(int)(coffee/2),-11.23,range((int)(coffee/2))]
        discount["BOGO"] = l1
        amount += (float)(l1[0]*l1[1])
    #CHMK discount
    if chai>0 and milk>0:
        l2 = [chai if chai < milk else milk, -4.75,range(chai if chai < milk else milk)]
        discount["CHMK"] = l2
        amount += (float)(l2[0]*l2[1])
    #APPL discount
    if apples>2:
        apple_flag = 1
        l3 = [apples, -1.50]
        l3.append(range(l3[0]))
        discount["APPL"] = l3
        amount += (float)(l3[0]*l3[1])
    #APOM discount
    if oatmeal>0 and apples>0:
        l = []
        l.append(apples)
        if apple_flag == 0:
            l.append(-3.00)
        else:
            l.append(-2.25)
            discount['APPL'] = []
        l.append(range(l[0]))
        discount["APOM"] = l
        amount += (float)(l[0]*l[1])
    result["total_amount"]="%.2f" % amount
    #storing the all the required results in result dict
    for p in products:
        if p.product_id == 'CF1':
            result['CF1'].append(discount["BOGO"])
        if p.product_id == 'MK1':
            result['MK1'].append(discount["CHMK"])
        if p.product_id == 'AP1':
            result['AP1'].append(discount["APPL"])
        if p.product_id == 'OM1':
            result['OM1'].append(discount["APOM"])
    return render(request, "finalBill.html",result)               
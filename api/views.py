from django.http import HttpRequest, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
import json
from .models import SmartPhone


def add_product(reqeust: HttpRequest) -> JsonResponse:
    """add new product to database"""
    if reqeust.method == 'POST':
        # get body from request
        body = reqeust.body
        # get body data
        decoded = body.decode()
        # data to dict
        data = json.loads(decoded)
        # get all properties
        price = data.get('price', False)
        img_url = data.get('img_url', False)
        color = data.get('color', False)
        ram = data.get('ram', False)
        memory = data.get('memory', False)
        name = data.get('name', False)
        model = data.get('model', False)

        # check all properties is valid
        if price == False or type(price) != float:
            return JsonResponse({"status": "price field is required. or float"})
        if img_url == False:
            return JsonResponse({"status": "img_url field is required."})
        if color == False:
            return JsonResponse({"status": "color field is required."})
        if ram == False:
            return JsonResponse({"status": "ram field is required."})
        if memory == False:
            return JsonResponse({"status": "memory field is required."})
        if name == False:
            return JsonResponse({"status": "name field is required."})
        if model == False:
            return JsonResponse({"status": "model field is required."})

        # create a inctance of SmartPhone 
        smartphone = SmartPhone.objects.create(
            price=price,
            img_url=img_url,
            color=color,
            ram=ram,
            memory=memory,
            name=name,
            model=model
        )
        # save data
        smartphone.save()

        # return data
        returned = smartphone.to_dict()
        return JsonResponse(returned)
    

def get_all_product(request: HttpRequest) -> JsonResponse:
    """get products to database"""
    if request.method == "GET":
        # get all priduct from database
        products = SmartPhone.objects.all()
        data = request.GET
        ram = data.get('ram', 0)
        memory = data.get('memory', 0)
        model = data.get('model', '')
        mx = data.get('max', -1)
        print(ram)
        # results data
        result = []
        for product in products:
            # add smartphone data as dict
            if ram:
                if product.ram == int(ram):
                    result.append(product.to_dict())
            elif memory:
                if product.memory == int(memory):
                    result.append(product.to_dict())
            elif model != '':
                if product.model == model:
                    result.append(product.to_dict())
            elif mx != -1:
                if float(product.price) <= float(mx):
                    result.append(product.to_dict())
            else:
                result.append(product.to_dict())
        
        return JsonResponse(result, safe=False)
    

def get_product(request: HttpRequest, pk: int) -> JsonResponse:
    """get product from database by id"""
    if request.method == "GET":
        try:
            # get product from database by id
            product = SmartPhone.objects.get(id=pk)
            return JsonResponse(product.to_dict())
        except ObjectDoesNotExist:
            return JsonResponse({"status": "object doesn't exist"})
    

def delete_product(request: HttpRequest, pk: int) -> JsonResponse:
    """delete product from database by id"""
    if request.method == "POST":
        try:
            # get product from database by id
            product = SmartPhone.objects.get(id=pk)
            product.delete()
            return JsonResponse(product.to_dict())
        except ObjectDoesNotExist:
            return JsonResponse({"status": "object doesn't exist"})
        
    

def update_product(request: HttpRequest, pk: int) -> JsonResponse:
    """delete product from database by id"""
    if request.method == "POST":
        try:
            # get body from request
            body = request.body
            # get body data
            decoded = body.decode()
            # data to dict
            data = json.loads(decoded)
            # get all properties
            price = data.get('price', False)
            img_url = data.get('img_url', False)
            color = data.get('color', False)
            ram = data.get('ram', False)
            memory = data.get('memory', False)
            name = data.get('name', False)
            model = data.get('model', False)

            # get product from database by id
            product = SmartPhone.objects.get(id=pk)

            # check all properties is valid
            if price is not False:
                product.price = price
            if img_url:
                product.img_url = img_url
            if color:
                product.color = color
            if ram:
                product.ram = ram
            if memory:
                product.memory = memory
            if name:
                product.name = name
            if model:
                product.model = model

            # save product
            product.save()

            return JsonResponse(product.to_dict())
            
        except ObjectDoesNotExist:
            return JsonResponse({"status": "object doesn't exist"})

def get_products_in_range(request: HttpRequest) -> JsonResponse:
    if request.method == "GET":
        body = request.GET
        products = SmartPhone.objects.filter(price__gte=float(body['min']), price__lte=float(body['max']))
        result = []
        for product in products:
            result.append(product.to_dict())
        return JsonResponse(result, safe=False)

def get_products_in_models(request: HttpRequest) -> JsonResponse:
    if request.method == "GET":
        args = request.GET.getlist('model')
        models = SmartPhone.objects.filter(model__in=args['model'])
        result = []
        for model in models:
            result.append(model.to_dict())
        return JsonResponse(result, safe=False)
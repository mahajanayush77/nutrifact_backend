
from django.shortcuts import render, get_object_or_404, get_list_or_404
from . import models, serializers
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.decorators import api_view, schema
from core.hello import return_string

# Create your views here.
class View(APIView):
    def post(self, request, *args, **kwargs):
        content = request.data.get('content', None)
        data = {
            "Content": content,
        }
        print("HI")
        print("HI")
        print("HI")
        print("HI")

        # string = """###~~CARBONATED WATER~SWEETENED CARBONATED BEVERAGE~NGREDIENTS: CARBONATED WATER,~SUGAR, ACIDITY REGULATOR (338).~CAFFEINE. CONTAINS PERMITTED NATURAL~COLOUR (1504) AND ADDED FLAVOURS (NATURAL~ATURE- DENTICAL AND ARTIFICIAL FLAVOURING~SUBSTANCES).~CONTAINS NO FRUIT.###~CONTAINS CAFFEINE"|###~NUTRITION FACTS (Typical Values Per 100m~ENERGY: 40 kcal~SUGAR: 10~RANUFACTURED BY~OUSTAN COCA-COLA BEVERAGES PVT. LTD,~15/74/33 PIRANGUT, TAL. MULSHI,~IST. PUNE 412111, MAHARASHTRA.~CONSUMER HELPLINE: 1800-180-2653###~CARBOHYDRATE: 1Og###~PROTEIN: 0###~FAT: 09###~RAIL: Indiahelpline@coca-cola.com~NDER AUTHORITY OF THE COCA-COLA COMPANT~1 COCA-COLA PLAZA, ATLANTA, GA 30313, USA~FOR DATE OF MANUFACTURE, BATCH NO. &~MR.P. INCL OF ALL TAXES):~SEE BOTTOM OF CAN.###~EST BEFORE SIX MONTHS FROM~MANUFACTURE WHEN STORED~NA COOL AND DRY PLACE.~OTHE COCA-COLA~COMPANY~PSSA LICENSE NO:~10012022000287###~please~recycle###~MET QUANTITY:###~330 ml###~AGUAUTY PROOUST OF~The CocaCola Gompany###~Coce Ce###~~LIVE POSIVELY""".upper()

        string = str(content).upper()
        print(content)
        data = return_string(string)
        print(data)
        return Response(data, status = HTTP_200_OK)

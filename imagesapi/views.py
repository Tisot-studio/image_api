from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Images
from .serializers import AllImagesSerializer, ImageSerializer
from PIL import Image
from urllib.parse import urlparse
import requests
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import os


# Получение списка доступных изображений и добавление изображений
@api_view(['GET', 'POST'])
def getImages(request):
    if request.method == 'GET':
        image = Images.objects.all()
        serializer = AllImagesSerializer(
            image, many=True, context={'request': request})
        return Response(serializer.data)

    if request.method == 'POST':
        try:
            if request.FILES:
                file = request.FILES.get('file')
                im = Image.open(file)
                width, height = im.size
                image = Images.objects.create(
                    name=file,
                    picture=file,
                    width=width,
                    height=height
                )
            else:
                img_url = request.data['url']
                name = urlparse(img_url).path.split('/')[-1]
                # Получаем изображение по ссылке
                r = requests.get(img_url)
                im = Image.open(BytesIO(r.content))
                width, height = im.size
                # Сохраняем изображение в кэш
                byte_file = BytesIO()
                im.save(byte_file, format='JPEG')
                # Сохраняем изображение в файл
                downloaded_file = InMemoryUploadedFile(
                    byte_file, None, name, 'image/jpeg',  None, None)

                image = Images.objects.create(
                    name=name,
                    url=img_url,
                    picture=downloaded_file,
                    width=width,
                    height=height
                )

            serializer = AllImagesSerializer(
                image, many=False, context={'request': request})
            return Response(serializer.data)
        except:
            message = {'oops': f' что-то не то'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)


# Получение детальной информации о изображении
@api_view(['GET', 'DELETE'])
def getImage(request, pk):
    if request.method == 'GET':
        try:
            image = Images.objects.get(id=pk)
            serializer = ImageSerializer(
                image, many=False, context={'request': request})
            return Response(serializer.data)
        except:
            message = {'oops': f' Изображение под номером {pk} не найдено'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        try:
            image = Images.objects.get(id=pk)
            # Удаляем запись в БД
            image.delete()
            # Удаляем само изображение
            os.remove(f'./static/images/{image.name}')
            return Response()
        except:
            message = {'oops': f' Изображение под номером {pk} не найдено'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)


# Изменение размера изображения
@api_view(['POST'])
def resizeImage(request, pk):
    # try:
        image = Images.objects.get(id=pk)

        r_width = request.data.get('width', 0)
        r_height = request.data.get('height', 0)

        if r_width == 0:
            new_width = image.width
        else:
            new_width = request.data['width']
        if r_height == 0:
            new_height = image.height
        else:
            new_height = request.data['height']

        im = Image.open(f'./static/images/{image.name}')
        new_img = im.resize((int(new_width), int(new_height)))
        width, height = new_img.size
        # После изменения размера изображения сохраняем его в кэш, а затем сохраняем его в новый файл,
        # который записывается в БД
        byte_file = BytesIO()
        new_img.save(byte_file, format='JPEG')
        resized_file = InMemoryUploadedFile(
            byte_file, None, f'{image.name}_{r_width}_{r_height}.jpg', 'image/jpeg',  None, None)
        # В parent_picture указан просто id родительского изображения,
        # т.к. по ТЗ не совсем понятно, нужно ли делать взаимосвязь
        # #parent_picture = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True).
        # Здесь создается независимая запись в БД где указывается лишь то, из какой первоначальной
        # записи она была создана.
        resized_image = Images.objects.create(
            name=f'{image.name}_{r_width}_{r_height}',
            picture=resized_file,
            width=width,
            height=height,
            parent_picture= int(image.id)
        )
        serializer = ImageSerializer(
            resized_image, many=False, context={'request': request})
        return Response(serializer.data)
    # except:
    #     message = {'oops': f' что-то не то'}
    #     return Response(message, status=status.HTTP_400_BAD_REQUEST)

from django.http import HttpResponse, JsonResponse


# def list_post(request):
#     recetas = pd.read_csv(path_recetas)
#     post = recetas.head(10)
#     posts = post.to_dict('records')
    
#     content = []
#     for post in posts:
#         content.append("""
#                        <p><strong>{nombre}<strong></p>
#                        <p><small>{categoria}</small></p>
#                        <figure><img src="{img}"/></figure>
#                        """.format(**post))
#     return HttpResponse('<br>'.join(content))
#     # print(type(posts))
#     # return HttpResponse(str(posts))